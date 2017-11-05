import pygame
import time
from Window import Window
from Colors import Color
from Pets import Pet
from GameObjects import Food
from Button import Button
from Save import User

def gameLoop(user, displayWidth, displayHeight, isFullscreen, title, font):
    #Загрузка спрайтов питомцев
    pet_images = []

    petsSizeX = int(displayWidth / 7.112962963)
    petsSizeY = int(displayHeight / 4)

    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\BlueBird.png").convert_alpha(), (petsSizeX, petsSizeY)))
    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Chicken.png").convert_alpha(), (petsSizeX, petsSizeY)))
    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Eagle.png").convert_alpha(), (petsSizeX, petsSizeY)))
    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Owl.png").convert_alpha(), (petsSizeX, petsSizeY)))
    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\YellowBird.png").convert_alpha(), (petsSizeX, petsSizeY)))

    ######################################

    #Загрузка спрайтов еды
    food_images = []

    foodSizeX = int(displayWidth / 14.23333333)
    foodSizeY = int(displayHeight / 16)

    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\ChickenLeg.png").convert_alpha(), (foodSizeX, foodSizeY)))

    chickenLeg_food = Food(food_images[0])
    chickenLeg_food.saturation = 10
    chickenLeg_food.x = displayWidth - 2 * chickenLeg_food.width
    chickenLeg_food.y = 3 * chickenLeg_food.height + int(displayHeight / 24)

    chickenLeg_food_target = Food(food_images[0])
    chickenLeg_food_target.saturation = 10
    isChickenLeg_food_target_active = False

    ########################################

    #Загрузка фоновых спрайтов
    background_images = []

    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\0-3.png").convert(),
                                 (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\3-5.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\5-6.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\6-8.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\8-12.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\12-15.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\15-17.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\17-19.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\19-21.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\21-23.png").convert(),
                               (displayWidth, displayHeight)))
    background_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\23-0.png").convert(),
                               (displayWidth, displayHeight)))
    background = None
    background_stage = 0

    ########################################

    #Инициализация окна
    window = Window(displayWidth, displayHeight, Color().black)
    display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

    #########################################

    #Инициализация питомца и синхронизация
    pet = Pet(pet_images[0])
    pet.x = (displayWidth - pet.width) // 2
    pet.y = (displayHeight - pet.height) // 2 + 60

    pet.hungerLevel = user.hungerLevel
    pet.moodLevel = user.moodLevel
    currentTime = user.time

    #########################################

    #Временные константы и дельты
    oneGameTimeUnitPerRealTimeUnit = 0.5
    timeTo_hunger = 1.8
    timeTo_mood = 1.5
    timeTo_autoSave = 60

    time_timer = time.time()
    time_hunger = time.time()
    time_mood = time.time()
    time_autoSave = time.time()

    hour = currentTime // 60
    min = currentTime - hour * 60

    ##########################################

    #Инициализация стат. баров
    timer = font.render((("0" if hour // 10 == 0 else "") + str(hour) + ":" + ("0" if min // 10 == 0 else "") + str(min)), False, (0, 0, 0)).convert()
    hungerLevel = font.render(("Hunger: " + str(pet.hungerLevel) + "%"), False, (0, 0, 0)).convert()
    moodLevel = font.render(("Mood: " + str(pet.moodLevel) + "%"), False, (0, 0, 0)).convert()

    #Игровой цикл
    while True:
        #Обработка событий
        for e in pygame.event.get():
            #Обработка события выхода и синхронизация
            if (e.type == pygame.QUIT):
                user.moodLevel = pet.moodLevel
                user.hungerLevel = pet.hungerLevel
                user.time = currentTime
                exit()

            if (e.type == pygame.KEYDOWN):
                if (e.key == pygame.K_ESCAPE):
                    user.moodLevel = pet.moodLevel
                    user.hungerLevel = pet.hungerLevel
                    user.time = currentTime
                    return

            #Обработка события кормежки
            if (e.type == pygame.MOUSEBUTTONDOWN):
                if (pygame.mouse.get_pos()[0] >= pet.x and pygame.mouse.get_pos()[0] <= pet.x + pet.width):
                    if (pygame.mouse.get_pos()[1] >= pet.y and pygame.mouse.get_pos()[1] <= pet.y + pet.height):
                        pet.moodLevel += 1
                        display.blit(hungerLevel, (10, 40))
                        pygame.display.update()

                if (isChickenLeg_food_target_active == False):
                    if (pygame.mouse.get_pos()[0] >= chickenLeg_food.x and pygame.mouse.get_pos()[0] <= chickenLeg_food.x + chickenLeg_food.width):
                        if (pygame.mouse.get_pos()[1] >= chickenLeg_food.y and pygame.mouse.get_pos()[1] <= chickenLeg_food.y + chickenLeg_food.height):
                            isChickenLeg_food_target_active = True

                else:
                    if (pygame.mouse.get_pos()[0] >= pet.x and pygame.mouse.get_pos()[0] <= pet.x + pet.width):
                        if (pygame.mouse.get_pos()[1] >= pet.y and pygame.mouse.get_pos()[1] <= pet.y + pet.height):
                            pet.hungerLevel -= chickenLeg_food.saturation
                            display.blit(hungerLevel, (10, 40))
                            pygame.display.update()

                    isChickenLeg_food_target_active = False

        #Отрисовка и обновление

        if (hour >= 0 and hour <= 3):
            background_stage = 0
        elif (hour <= 5):
            background_stage = 1
        elif (hour <= 6):
            background_stage = 2
        elif (hour <= 8):
            background_stage = 3
        elif (hour <= 12):
            background_stage = 4
        elif (hour <= 15):
            background_stage = 5
        elif (hour <= 17):
            background_stage = 6
        elif (hour <= 19):
            background_stage = 7
        elif (hour <= 21):
            background_stage = 8
        elif (hour <= 23):
            background_stage = 9
        elif (hour <= 0):
            background_stage = 10

        background = background_images[background_stage].copy()
        display.blit(background, (0, 0))
        background.blit(pet.object, (pet.x, pet.y))

        background.blit(chickenLeg_food.object, (chickenLeg_food.x, chickenLeg_food.y))

        if (isChickenLeg_food_target_active):
            background.blit(chickenLeg_food_target.object, (pygame.mouse.get_pos()[0] - chickenLeg_food_target.width // 2,
                                                            pygame.mouse.get_pos()[1] - chickenLeg_food_target.height // 2))

        background.blit(timer, (10, 10))
        background.blit(hungerLevel, (10, 40))
        background.blit(moodLevel, (10, 70))

        display.blit(background, (0, 0))
        pygame.display.update()

        #########################################

        #Временные расчеты разностей, изменение статов
        if (time.time() - time_hunger >= timeTo_hunger):
            pet.hungerLevel += 1

            if (pet.hungerLevel < 0):
                pet.hungerLevel = 0
            elif (pet.hungerLevel > 100):
                pet.hungerLevel = 100

            hungerLevel = font.render(("Hunger: " + str(pet.hungerLevel) + "%"), False, (0, 0, 0)).convert()
            time_hunger = time.time()

        if (time.time() - time_mood >= timeTo_mood):
            pet.moodLevel -= 1

            if (pet.moodLevel < 0):
                pet.moodLevel = 0
            elif (pet.moodLevel > 100):
                pet.moodLevel = 100

            moodLevel = font.render(("Mood: " + str(pet.moodLevel) + "%"), False, (0, 0, 0)).convert()
            time_mood = time.time()

        if (time.time() - time_timer >= oneGameTimeUnitPerRealTimeUnit):
            currentTime = (currentTime + 1) % 1440

            hour = (currentTime // 60) % 24
            min = currentTime - hour * 60
            timer = font.render((("0" if hour // 10 == 0 else "") + str(hour) + ":" + ("0" if min // 10 == 0 else "") + str(min)), False, (0, 0, 0)).convert()
            time_timer = time.time()

        if (time.time() - time_autoSave >= timeTo_autoSave):
            user.moodLevel = pet.moodLevel
            user.hungerLevel = pet.hungerLevel
            user.time = currentTime
