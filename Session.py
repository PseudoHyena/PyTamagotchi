import pygame
import time
import random
from Window import Window
from Colors import Color
from Pets import Pet
from GameObjects import Food
from GameObjects import Poop
from Button import Button

def gameLoop(user, displayWidth, displayHeight, isFullscreen, title, font):

    #Загрузка спрайтов еды
    food_images = []

    foodSizeX = int(displayWidth / 12.2)
    foodSizeY = int(displayHeight / 9.6)

    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\BarryPie.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Brownie.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Dounut.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Flan.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\FrenchFries.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\IceCream.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Pancake.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Pie.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Pizza.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))
    food_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Food\\Roll.png").convert_alpha(),
                                              (foodSizeX, foodSizeY)))

    food_count_list = user.getFoodCount()
    food_saturation_list = user.getFoodSaturation()
    food_price_list = user.getFoodPrice()

    ########################################

    #Загрузка спрайтов poop

    poop_images = []

    poopSizeX = int(displayWidth // 14.233333333)
    poopSizeY = int(displayHeight // 8.571428571)

    poop_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Poops\\Poop1.png").convert_alpha(),
                                              (poopSizeX, poopSizeY)))
    poop_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Poops\\Poop2.png").convert_alpha(),
                                              (poopSizeX, poopSizeY)))
    poop_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Poops\\Poop3.png").convert_alpha(),
                                              (poopSizeX, poopSizeY)))
    poop_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Poops\\Poop4.png").convert_alpha(),
                                              (poopSizeX, poopSizeY)))
    poop_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Poops\\Poop5.png").convert_alpha(),
                                              (poopSizeX, poopSizeY)))

    timeToPoop_heap = []
    if (user.poopHeap != None):
        for i in user.poopHeap.split():
            timeToPoop_heap.append(int(i))

    poops_heap = []
    poops_heap.extend(user.getPoopsObjects())
    for poop in poops_heap:
        poop.setImage(poop_images[poop.number])

    timeTo_Poop = 180

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

    work_background_image = pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\WorkBG.png").convert(),
                                (displayWidth, displayHeight))

    shop_board_image = pygame.transform.scale(pygame.image.load_extended("Sprites\\Backgrounds\\ShopB.png").convert(),
                                (int(displayWidth * 0.25), int(displayHeight * 0.75)))

    background = None
    background_stage = 0
    isMain_active = True


    ########################################

    #coin

    coinSizeX = int(displayWidth // 17.42857143)
    coinSizeY = int(displayHeight // 10)

    coin_image = pygame.transform.scale(pygame.image.load_extended("Sprites\\Coin.png").convert_alpha(), (coinSizeX, coinSizeY))

    coin_triggerX, coin_triggerY = (random.randrange(5, displayWidth - coinSizeX - 5),
                                            random.randrange(5, displayHeight - coinSizeY - 5))

    isCoin_active = False

    ########################################

    #Board

    board_image = pygame.image.load_extended("Sprites\\Board.png").convert()
    boardSizeX = board_image.get_width()
    boardSizeY = board_image.get_height()

    work_triggerX1 = (displayWidth - boardSizeX) + 90
    work_triggerY1 = 38
    work_triggerX2 = (displayWidth - boardSizeX) + 135
    work_triggerY2 = 85

    shop_triggerX1 = (displayWidth - boardSizeX) + 35
    shop_triggerY1 = 82
    shop_triggerX2 = (displayWidth - boardSizeX) + 85
    shop_triggerY2 = 123

    stock_triggerX1 = (displayWidth - boardSizeX) + 110
    stock_triggerY1 = 131
    stock_triggerX2 = (displayWidth - boardSizeX) + 181
    stock_triggerY2 = 182

    menu_triggerX1 = (displayWidth - boardSizeX) + 40
    menu_triggerY1 = 215
    menu_triggerX2 = (displayWidth - boardSizeX) + 83
    menu_triggerY2 = 270

    isBoard_active = False
    isWork_active = False
    isShop_active = False

    ########################################

    #Инициализация окна
    window = Window(displayWidth, displayHeight, Color().black)
    display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

    #########################################

    #Инициализация питомца и синхронизация
    pet = Pet(user.images)
    pet.x = (displayWidth - pet.width) // 2
    pet.y = (displayHeight - pet.height) // 2 + 60

    pet.hungerLevel = user.hungerLevel
    pet.moodLevel = user.moodLevel
    currentTime = user.time
    currentDay = user.day
    coin_sum = user.coin if user.coin != None else 0

    #########################################

    #Временные константы и дельты
    oneGameTimeUnitPerRealTimeUnit = 0.5
    timeTo_hunger = 1.8
    timeTo_mood = 1.5
    timeTo_autoSave = 60
    timeOf_coin = 0.5

    time_timer = time.time()
    time_hunger = time.time()
    time_mood = time.time()
    time_autoSave = time.time()
    time_coin = time.time()

    wait_time = random.randrange(0, 3)
    wait_currentTime = time.time()

    hour = currentTime // 60
    min = currentTime - hour * 60

    #####

    hunger_stage = pet.hungerLevel // 10 - 4 if (pet.hungerLevel // 10 - 4) > 0 else 0
    tikToDeath_number = 1080 - (hunger_stage - 1) * 180
    tikToDeath_currentNumber = user.hungerDeathTik

    #####

    ##########################################

    #Инициализация стат. баров
    timer = font.render((("0" if hour // 10 == 0 else "") + str(hour) + ":" + ("0" if min // 10 == 0 else "") + str(min)), False, (0, 0, 0)).convert()
    day_timer = font.render("Day: " + (str(currentDay)), False, (0, 0, 0)).convert()
    hungerLevel = font.render(("Hunger: " + str(pet.hungerLevel) + "%"), False, (0, 0, 0)).convert()
    moodLevel = font.render(("Mood: " + str(pet.moodLevel) + "%"), False, (0, 0, 0)).convert()

    ##########################################

    def save():
        user.moodLevel = pet.moodLevel
        user.hungerLevel = pet.hungerLevel
        user.time = currentTime
        user.day = currentDay
        user.hungerDeathTik = tikToDeath_currentNumber
        _timeToPoop_heap = ""
        if (len(timeToPoop_heap) != 0):
            for poop in timeToPoop_heap:
                _timeToPoop_heap += (str(poop) + " ")
        user.poopHeap = _timeToPoop_heap
        user.setPoopsObject(poops_heap)
        user.coin = coin_sum
        user.setFoodCount(food_count_list)

    ##########################################

    #Игровой цикл
    while True:
        #Обработка событий
        for e in pygame.event.get():
            #Обработка события выхода и синхронизация
            if (e.type == pygame.QUIT):
                save()
                exit()

            if (e.type == pygame.KEYDOWN):
                if (e.key == pygame.K_b):
                    if (isBoard_active == True):
                        isBoard_active = False
                    else:
                        isBoard_active = True

                if (e.key == pygame.K_ESCAPE):
                    isMain_active = True
                    isWork_active = False
                    isShop_active = False

            #Обработка событий по нажатию ЛКМ
            if (e.type == pygame.MOUSEBUTTONDOWN and e.button == 1):
                if (isMain_active):
                    if (pygame.mouse.get_pos()[0] >= pet.x and pygame.mouse.get_pos()[0] <= pet.x + pet.width):
                        if (pygame.mouse.get_pos()[1] >= pet.y and pygame.mouse.get_pos()[1] <= pet.y + pet.height):
                            pet.moodLevel += 1

                    #if (isChickenLeg_food_target_active == False):
                        #if (pygame.mouse.get_pos()[0] >= chickenLeg_food.x and pygame.mouse.get_pos()[0] <= chickenLeg_food.x + chickenLeg_food.width):
                            #if (pygame.mouse.get_pos()[1] >= chickenLeg_food.y and pygame.mouse.get_pos()[1] <= chickenLeg_food.y + chickenLeg_food.height):
                                #isChickenLeg_food_target_active = True

                    else:
                        if (pygame.mouse.get_pos()[0] >= pet.x and pygame.mouse.get_pos()[0] <= pet.x + pet.width):
                            if (pygame.mouse.get_pos()[1] >= pet.y and pygame.mouse.get_pos()[1] <= pet.y + pet.height):
                                #pet.hungerLevel -= chickenLeg_food.saturation
                                poop_time = (currentTime + timeTo_Poop) % 1440
                                timeToPoop_heap.append( poop_time if (poop_time / 360) >= 1 else (360 + random.randrange(0, 30)))
                                isChickenLeg_food_target_active = False

                            else:
                                isChickenLeg_food_target_active = False
                        else:
                            isChickenLeg_food_target_active = False

                    if (len(poops_heap) != 0):
                        for poop in poops_heap:
                            if (pygame.mouse.get_pos()[0] >= poop.x and pygame.mouse.get_pos()[0] <= poop.x + poop.width):
                                if (pygame.mouse.get_pos()[1] >= poop.y and pygame.mouse.get_pos()[1] <= poop.y + poop.height):
                                    poops_heap.remove(poop)

                if (isWork_active):
                    if (isCoin_active):
                        if (pygame.mouse.get_pos()[0] >= coin_triggerX and pygame.mouse.get_pos()[0] <= coin_triggerX + coinSizeX):
                            if (pygame.mouse.get_pos()[1] >= coin_triggerY and pygame.mouse.get_pos()[1] <= coin_triggerY + coinSizeY):
                                isCoin_active = False
                                wait_time = random.randrange(2, 4)
                                wait_currentTime = time.time()
                                time_coin = 0

                                coin_sum += 1
                                print(str(coin_sum))

                if (isShop_active):
                    startX = -1 * int(shop_board_image.get_width() // 4)
                    stepX = int(shop_board_image.get_width() // 2)
                    startY = -1 * int(shop_board_image.get_height() // 12)
                    stepY = int(shop_board_image.get_height() // 6)
                    foodN = 0

                    break_flag = False
                    for i in range(5):
                        for j in range(2):
                            posX = (displayWidth - shop_board_image.get_width()) + startX + stepX - foodSizeX // 2 - foodSizeX // 5
                            posY = startY + stepY

                            if (pygame.mouse.get_pos()[0] >= posX and pygame.mouse.get_pos()[0] <= posX + foodSizeX):
                                if (pygame.mouse.get_pos()[1] >= posY and pygame.mouse.get_pos()[1] <= posY + foodSizeY):
                                    if (coin_sum >= food_price_list[foodN]):
                                        coin_sum -= food_price_list[foodN]

                                    break_flag = True
                                    break

                            if (break_flag):
                                break

                            foodN += 1
                            startX += stepX
                        startX = -1 * int(shop_board_image.get_width() // 4)
                        startY += stepY

                if (isBoard_active):
                    if (pygame.mouse.get_pos()[0] >= work_triggerX1 and pygame.mouse.get_pos()[0] <= work_triggerX2):
                        if (pygame.mouse.get_pos()[1] >= work_triggerY1 and pygame.mouse.get_pos()[1] <= work_triggerY2):
                            isWork_active = True
                            isMain_active = False
                            isBoard_active = False

                            wait_time = random.randrange(1, 4)
                            wait_currentTime = time.time()

                    if (pygame.mouse.get_pos()[0] >= shop_triggerX1 and pygame.mouse.get_pos()[0] <= shop_triggerX2):
                        if (pygame.mouse.get_pos()[1] >= shop_triggerY1 and pygame.mouse.get_pos()[1] <= shop_triggerY2):
                            isBoard_active = False
                            isShop_active = True

                    if (pygame.mouse.get_pos()[0] >= stock_triggerX1 and pygame.mouse.get_pos()[0] <= stock_triggerX2):
                        if (pygame.mouse.get_pos()[1] >= stock_triggerY1 and pygame.mouse.get_pos()[1] <= stock_triggerY2):
                            print("Stock")

                    if (pygame.mouse.get_pos()[0] >= menu_triggerX1 and pygame.mouse.get_pos()[0] <= menu_triggerX2):
                        if (pygame.mouse.get_pos()[1] >= menu_triggerY1 and pygame.mouse.get_pos()[1] <= menu_triggerY2):
                            save()
                            return



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


        if (isMain_active):
            background = background_images[background_stage].copy()

            if (hour > 21 or hour <= 5):
                background.blit(pet.object[1], (pet.x, pet.y))
            else:
                background.blit(pet.object[0], (pet.x, pet.y))

            #background.blit(chickenLeg_food.object, (chickenLeg_food.x, chickenLeg_food.y))

            #if (isChickenLeg_food_target_active):
                #background.blit(chickenLeg_food_target.object, (pygame.mouse.get_pos()[0] - chickenLeg_food_target.width // 2,
                       #                                         pygame.mouse.get_pos()[1] - chickenLeg_food_target.height // 2))

            if (len(poops_heap) != 0):
                for poop in poops_heap:
                    background.blit(poop.object, (poop.x, poop.y))

            if (isBoard_active):
                background.blit(board_image.copy(), (displayWidth - boardSizeX, 0))

            background.blit(timer, (10, 10))
            background.blit(day_timer, (10, 40))
            background.blit(hungerLevel, (10, 70))
            background.blit(moodLevel, (10, 100))

        if (isWork_active):
            background = work_background_image.copy()
            coin = coin_image.copy()
            coin_sum_text = font.render(str(coin_sum), False, (0, 0, 0)).convert()

            if (time.time() - wait_currentTime >= wait_time):
                if (time_coin == 0):
                    time_coin = time.time()

                if (time.time() - time_coin <= timeOf_coin):
                    isCoin_active = True
                else:
                    coin_triggerX, coin_triggerY = (random.randrange(5, displayWidth - coinSizeX - 5),
                                           random.randrange(5, displayHeight - coinSizeY - 5))

                    wait_time = random.randrange(2, 4)
                    wait_currentTime = time.time()
                    time_coin = 0
                    isCoin_active = False

            if (isCoin_active):
                background.blit(coin, (coin_triggerX, coin_triggerY))

            background.blit(coin, (10, 10))
            background.blit(coin_sum_text, (15 + coinSizeX, (10 + coin_sum_text.get_height()) // 2))

        if (isShop_active):
            shopBoard = shop_board_image.copy()

            startX = -1 * int(shopBoard.get_width() // 4)
            stepX = int(shopBoard.get_width() // 2)
            startY = -1 * int(shopBoard.get_height() // 12)
            stepY = int(shopBoard.get_height() // 6)
            foodN = 0

            for i in range(5):
                for j in range(2):
                    posX = startX + stepX - foodSizeX // 2 - foodSizeX // 5
                    posY = startY + stepY

                    shopBoard.blit(food_images[foodN].copy(), (posX, posY))

                    price_text = font.render((str(food_price_list[foodN]) + "$"), False, (0, 0 , 0)).convert()
                    shopBoard.blit(price_text, (posX + foodSizeX + 5, posY + foodSizeY - price_text.get_height()))

                    foodN += 1
                    startX += stepX
                startX = -1 * int(shopBoard.get_width() // 4)
                startY += stepY

            background.blit(shopBoard, (displayWidth - shopBoard.get_width(), 0))

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

            if (hour >= 6 and hour < 22):
                if (hunger_stage > 0):
                    tikToDeath_currentNumber += 1
                else:
                    tikToDeath_currentNumber = 0

            if (currentTime == 360):
                currentDay += 1
                day_timer = font.render(("Day: " + str(currentDay)), False, (0, 0, 0)).convert()

            hour = (currentTime // 60) % 24
            min = currentTime - hour * 60
            timer = font.render((("0" if hour // 10 == 0 else "") + str(hour) + ":" + ("0" if min // 10 == 0 else "") + str(min)), False, (0, 0, 0)).convert()
            time_timer = time.time()

        #########################################

        if (len(timeToPoop_heap) != 0 and currentTime >= timeToPoop_heap[0]):
            poopX = random.randrange(10, displayWidth - poopSizeX - 10)
            poopY = random.randrange(displayHeight - int(displayHeight // 6.857142857), displayHeight - poopSizeY - 5)

            poop_number = random.randrange(0, len(poop_images))
            poop = Poop(poop_number)
            poop.setImage(poop_images[poop_number])
            poop.x = poopX
            poop.y = poopY
            poops_heap.append(poop)

            timeToPoop_heap.pop(0)

        #########################################

        hunger_stage = (pet.hungerLevel // 10 - 4) if (pet.hungerLevel // 10 - 4) > 0 else 0
        tikToDeath_number = (1080 - (hunger_stage - 1) * 180) if (hunger_stage - 1) >= 0 else 0
        if (hunger_stage == 0):
            tikToDeath_currentNumber = 0

        #print((str(pet.hungerLevel) + " " + str(tikToDeath_currentNumber) + " of " + str(tikToDeath_number)))

        if (hunger_stage >= 1 and tikToDeath_currentNumber >= tikToDeath_number):
            print("Pet is dead")
            return

        #########################################

        """if (time.time() - time_autoSave >= timeTo_autoSave):
            save()
            """
