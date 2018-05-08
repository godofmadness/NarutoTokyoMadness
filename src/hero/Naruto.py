from ..sprite.PoweredSprite import PoweredSprite
import pygame
from ..logger.LoggerFactory import LoggerFactory
from ..constants.DamageType import *
from ..skill.SkillSprite import SkillSprite
from ..constants.Contstants import *
from ..music.SoundEffectService import SoundEffectService
from ..skill.RasenganFactory import RasenganFactory
from ..animation.skill.RasenganAnimation import RasenganAnimation

"""Instantiate this class usign Factory """
class Naruto(PoweredSprite):


    # load sprites
    def __init__(self):
        super().__init__()
        self.name = "Player1"
        self.log = LoggerFactory.getStreamLogger(__name__)
        self.damage = 2
        self.health = 100
        self.hud = None
        self.icon = None
        self.skill1AnimationCallback = self.onSpecialMove1AnimationFrame
        self.dead = False

    def takeDamage(self, damage, damageSide, damageType, time):
        # health decrement
        if self.health > 0:
            print("DAMAGE TAKEN BY NARUTO " + str(damage))
            self.health -= damage
        else:
            self.dead = True

        if damageType == SKILL:
            self.log.debug("STRoG DAMAGE TO NARUTO")
            # self.stun(1)
            self.animateStrongDamage(damage, damageSide, time)

        elif damageType == BASIC_ATTACK:
            self.log.debug("LIGHT DAMAGE TO NARUTO")
            self.animateBasicDamage(damage, damageSide)

    def specialMove1(self, time):
        sfs = SoundEffectService(pygame.mixer)
        sfs.play("naruto/rasengan1.mp3")

        rasengan = RasenganFactory.getInstance(self)
        self.currentSkill = rasengan
        self.animation = RasenganAnimation(rasengan, RASENGAN_SKILL_FRAMERATE, time)
        self.animateSpecialMove1(self.animation)

    def onSpecialMove1AnimationFrame(self, time):

        for el in self.context.activeSpriteList:
            print("ACTIVE SPRITE LIST EL " + str(el))
            print("ACTIVE SPRITE LIST EL RECT " + str(el.rect))

        collideList = pygame.sprite.spritecollide(self, self.context.activeSpriteList, False)
        collideList.remove(self)
        collideList.remove(self.currentSkillObject)
        for target in collideList:

            #  if collide target was another skill
            if isinstance(target, SkillSprite):
                # todo break all active skills
                self.log.debug("NARTCOMBO BREAK")
                pass
                # comboBreak()

            elif not self.currentSkillObject.isHitted():
                self.inSM1 = False
                self.inSM1Hit = True
                self.animation.setHitStartTime(time)
                target.takeDamage(self.getActiveSkill().getDamage(), self.getDirection(), SKILL, time)

    def update(self, updateTime):

        # if self.currentSkillObject != None:
            # print("RASENGAN RECT " + str(self.currentSkillObject.rect))
        if self.hud != None:
            self.hud.update(updateTime, self.health, self.icon)

        super().update(updateTime)


    def getDamage(self):
        return self.damage

    def getHealth(self):
        return self.health


    def getActiveSkill(self):
        return self.currentSkill

    def isDead(self):
        return self.dead

    def setHUD(self, hud):
        self.hud = hud

    def getName(self):
        return self.name

    def setIcon(self, icon):
        self.icon = icon