# From Learn Python the Hard Way

from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck as this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent('''
            The Google AI robot army is taking over the world and destroying all humankind.
            You are the only member left of the secret Duck Duck Go rebels with access to the
            main server room that is controlling the Google AI army.  Your last mission is to 
            get the neutron destruct bomb from the Weapons Armory, put it in the server room, 
            and blow it up after getting into your escape hovercraft.
            
            You're running down the central corridor to the Weapons Armory when a robot
            jumps out.  It's blocking the door to the Armory and about to blast you with its
            ray gun.
            
            Options: shoot, dodge, tell a joke
                     
                     '''))

        action = input('> ')

        if action == 'shoot':
            print(dedent('''
                Quick on the draw you yank out your blaster and fire it at the robot.  You're
                laser hits the robot's reflective shield and bounces back at you, striking you
                dead.  There is no beating the Google AI robot's taking over the world.
            '''))
            return 'death'
        elif action == 'dodge':
            print(dedent('''
                Lise a world class boxer you dodge, weave, slip and slide right as
                the robot's blaster cranks a laser past your head.  In the middle of your
                artful dodge your foot slips and you bang your head on the metal wall and
                pass out.  You wake up shortly after only to die as the robot blasts you
                with it's laser.
            '''))
        elif action == 'tell a joke':
            print(dedent('''
                Lucky for you were able to ask Siri on your iPhone for help on how to dodge robots.
                Siri distracts the robot by insulting Google's AI, while Siri and the Google AI
                robot exchange insults, you shot the robot in its glass eyes and jump through
                the Amory door.
            '''))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent('''
            You do a dive roll into the Weapon Armory, crunch and scan the room for more robots
            that might be hiding.  It's dead quiet, too quiet.  You stand up and run to the far
            side of the room and find the neutron bomb in its container.  There's a keypad
            lock on the box and you need the code to get the bomb out.  If you get the code wrong
            10 times then the lock closes forever and you can't get the bomb.  The code is
            3 digits.
        '''))

        # code = f'{randint(1,9)}{randint(1,9)}{randint(1,9)}'
        code = '{randint(1,9)}{randint(1,9)}{randint(1,9)}'
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDDO!!!")
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(dedent('''
                The container clicks open and the seal breaks, letting gas out.
                You grab the neutron bomb and run as fast as you can into the center
                of the server room where you must place it in the right spot.
            '''))
            return 'the_server_room'
        else:
            print(dedent('''
                The lock buzzes one last time and then you hear a sickening
                melting sound as teh mechanism is fused together.  You decide to sit there,
                where the Google AI robots find you and blow you up with their laser guns.
            '''))
            return 'death'


class TheServerRoom(Scene):

    def enter(self):
        print(dedent('''
            You burst into the server room with the neutron destruct bomb under your arm
            and surprise 5 Google AI robots guarding the room.  They haven't pulled their
            weapons out yet, as they see the active omb under your arm and don't want to
            set it off.
        '''))
        action = input('> ')

        if action == 'throw the bomb':
            print(dedent('''
                In a panic you throw the bomb at the group of robots and make a leap for the
                door.  Right as you drop it, a robot shoots you in the back killing you.  As
                you die you see another robot frantically try to disarm the bomb.  You die
                knowing they wil probably blow up when it goes off.
            '''))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent('''
                You point your blaster at the bomb under your arm and the robots put their
                hands up and start to back away.  You inch backward to the door, open it,
                and then carefully place the bomb on the floor, pointing you blaster
                at it.  You then jump back through the door, punch the close button and
                blast the lock so the robots can't get out.  Now that the bomb is placed 
                you run to the your escape hovercraft to get out of their.
            '''))
            return 'escape_hovercraft'
        else:
            print("DOES NOT COMPUTE")
            return 'the_server_room'


class EscapeHovercraft(Scene):

    def enter(self):
        print(dedent('''
            You rush outside desperately trying to make it to the escape Duck Duck Go hovercrafts 
            before the whole building explodes.  It seem like hardly any robots are in the area,
            so your run is clear of interference.  You get to the parking lot and need to
            pick one.  Some have been damaged by robots but you don't have time to check
             them all.  There are five hovercraft, pick one to take.
        '''))

        good_craft = randint(1, 5)
        guess = input('[hovercraft #]> ')

        if int(guess) != good_craft:
            print(dedent('''
                You jump into the pod {guess} and hit Go button.  The hovercraft takes off but
                then implodes as the engine ruptures, crushing your body into jam jelly.
            '''))
            return 'death'
        else:
            print(dedent('''
                You jump into the hovercraft {guess} and hit the go button.  The hovercraft
                easily takes off in the air.  As it flies into the sky, you see the server building
                explode...taking out the Google Robot AI army control.  You won!
            '''))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good Job.")
        print("Wait...what's that buzzing sound?  Sounds like your phone. You take your"
              "phone out of your pocket.  Siri thanks you for helping take out Google,"
              " now the Apple AI robot army can"
              "take over the world (*evil Siri laugh*)")


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_server_room': TheServerRoom(),
        'escape_hovercraft': EscapeHovercraft(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


# a variable a_game is declared
# a_game is set to an instance object of the class Game() with the attribute" central_corridor"
#  but central_corridor itself is a name of a function
# the function play() is called on the instance object a_game
# this is where the game really begins

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
