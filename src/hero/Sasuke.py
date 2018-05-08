from ..sprite.PoweredSprite import PoweredSprite
import pygame
from ..logger.LoggerFactory import LoggerFactory
from ..skill.ChidoryFactory import ChidoryFactory
from ..constants.Contstants import *
from ..animation.skill.ChidoriAnimation import ChidoriAnimation
from ..music.SoundEffectService import SoundEffectService
from ..constants.DamageType import *
from ..skill.SkillSprite import SkillSprite

class Sasuke(PoweredSprite):


    # load sprites
    def __init__(self):
        super().__init__()
        self.name = "Player 2"
        self.log = LoggerFactory.getStreamLogger(__name__)
        self.damage = 2
        self.health = 100
        self.hud = None
        self.icon = None
        self.currentSkill = None
        self.skill1AnimationCallback = self.onSpecialMove1AnimationFrame
        self.animation = None
        self.dead = False

    def takeDamage(self, damage, damageSide, damageType, time):
        # health decrement

        if self.health > 0:
            print("DAMAGE TAKEN BY SASUKE " + str(damage))
            self.health -= damage
        else:
            self.dead = True


        if damageType == SKILL:
            self.log.debug("STRoG DAMAGE TO SASUKE")
            # self.stun(1)
            self.animateStrongDamage(damage, damageSide, time)

        elif damageType == BASIC_ATTACK:
            self.log.debug("LIGHT DAMAGE TO SASUKE")
            self.animateBasicDamage(damage, damageSide)

        # self.animateBasicDamage(damage, damageSide)


    def update(self, updateTime):

        if self.hud != None:
            self.hud.update(updateTime, self.health, self.icon)

        super().update(updateTime)



    def specialMove1(self, time):
        sfs = SoundEffectService(pygame.mixer)
        sfs.play("sasuke/chidory.mp3")

        chidory = ChidoryFactory.getInstance(self)
        self.currentSkill = chidory
        self.animation = ChidoriAnimation(chidory, CHIDORY_SKILL_FRAMERATE, time)
        self.animateSpecialMove1(self.animation)


    # called with every frame while skill is in animation
    def onSpecialMove1AnimationFrame(self, time):

        for el in self.context.activeSpriteList:
            print("ACTIVE SPRITE LIST EL " + str(el))
            print("ACTIVE SPRITE LIST EL RECT " + str(el.rect))


        collideList = pygame.sprite.spritecollide(self, self.context.activeSpriteList, False)

        collideList.remove(self)
        collideList.remove(self.currentSkillObject)

        # todo remove all skills from collide list
        for target in collideList:
            #  if collide target was another skill
            if isinstance(target, SkillSprite):
                # todo brea all active skills
                self.log.debug("COMBO BREAK")
                pass
                # comboBreak()


            elif not self.currentSkillObject.isHitted():
                self.inSM1 = False
                self.inSM1Hit = True
                self.animation.setHitStartTime(time)
                target.takeDamage(self.getActiveSkill().getDamage(), self.getDirection(), SKILL, time)

        #
        # pass


    def getDamage(self):
        return self.damage

    def getHealth(self):
        return self.health

    def getActiveSkill(self):
        return self.currentSkill

    def isDead(self):
        return self.dead

    def getName(self):
        return self.name


    def setHUD(self, hud):
        self.hud = hud

    def setIcon(self, icon):
        self.icon = icon