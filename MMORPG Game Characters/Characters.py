#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 7 Project
# Purpose: MMORPG Game Characters' Classes Implementation
#
# Author: Ahmad M. Osman
# Date: March 27, 2017
#
# Filename: Characters.py
#
##########################################################################

from abc import ABC, abstractmethod


class Character(ABC):
    '''Base Character Type'''

    @abstractmethod
    def __init__(self, agility_, attack_, defense_, health_, level_, stamina_, type_):
        '''Constructing base character'''
        self._agility = agility_
        self._attack = attack_
        self._defense = defense_
        self._health = health_
        self._level = level_
        self._stamina = stamina_
        self._type = type_

    @abstractmethod
    def level_up(self):
        '''Character level up'''
        self._agility += 15
        self._attack += 25
        self._defense += 18
        self._health += 60
        self._level += 1
        self._stamina += 10

    @property
    def agility(self):
        return self._agility

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def stamina(self):
        return self._stamina

    @property
    def type(self):
        return self._type

    def __str__(self):
        '''Base character output'''
        return "LVL: " + str(self._level) + " | ATT: " + str(self._attack) + " | DEF: " + str(self._defense) + " | AGI: " + str(self._agility) + " | HP: " + str(self._health) + " | STM: " + str(self._stamina)


class Archer(Character):
    '''Archer Character Type Class'''

    def __init__(self, flying_):
        '''Constructing an Archer'''
        super().__init__(40, 15, 20, 240, 1, 10, "Archer")
        self._flying = flying_
        self._flying_interval = 10

    def level_up(self):
        '''Leveling an Archer up'''
        super().level_up()
        if self._flying:
            self._flying_interval += 15

    @property
    def flying(self):
        return self._flying

    @property
    def flying_interval(self):
        return self._flying_interval

    def __str__(self):
        '''Archer character output'''
        if self._flying:
            return "Flying Archer of " + super().__str__() + " | FLYINT: " + str(self._flying_interval) + '.'
        else:
            return "Non-Flying Archer of " + super().__str__() + '.'


class Trojan(Character):
    '''Trojan Character Type Class'''

    def __init__(self, is_sane_):
        '''Constructing a Trojan'''
        super().__init__(10, 50, 35, 520, 1, 25, "Trojan")
        self._is_sane = is_sane_
        self._running_interval = 25

    def level_up(self):
        '''Leveling a Trojan up'''
        super().level_up()
        self._running_interval += 10

    @property
    def is_sane(self):
        return self._is_sane

    @property
    def running_interval(self):
        return self._running_interval

    def __str__(self):
        '''Trojan character output'''
        if self._is_sane:
            return "Sane Trojan of " + super().__str__() + " | RUNINT: " + str(self._running_interval) + '.'
        else:
            return "Insane Trojan of " + super().__str__() + " | RUNINT: " + str(self._running_interval) + '.'


class Wizard(Character):
    '''Wizard Character Type Class'''

    def __init__(self, is_evil):
        '''Constructing a Wizard'''
        super().__init__(15, 10, 12, 700, 1, 100, "Wizard")
        self._is_evil = is_evil
        self._mana = 150

    def level_up(self):
        '''Leveling a Trojan up'''
        super().level_up()
        if self._is_evil:
            self._mana += 47
        else:
            self._mana += 74

    @property
    def is_evil(self):
        return self._is_evil

    @property
    def mana(self):
        return self._mana

    def __str__(self):
        '''Wizard character output'''
        if self._is_evil:
            return "Fire Wizard " + super().__str__() + " | MANA: " + str(self._mana) + '.'
        else:
            return "Water Wizard " + super().__str__() + " | MANA: " + str(self._mana) + '.'
