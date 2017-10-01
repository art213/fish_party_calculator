import numpy as np
#np.random
from pylab import *
import time

lang = str (input ('Choose languages - EN/RU'))

if (lang == 'EN') or (lang=='En') or (lang=='en'):
    j=1
    while j > 0:
        kolvo = int (input('Count of fish parties'))
        buyin = int (input ('Buyin'))
        jackpot = int (input ('How much jackpot in euros'))
        jackbi = jackpot/buyin
        rake = 0.05
        evchips = int (input('Your EVchips per tournament'))
        rakeback = 0.3


        i=1
        prize=0
        profitg = 0 #профит для графика
        profitgg = []
        profitgrb = 0 #профит для графика с рейкбеком
        profitggrb = []

        while i <=kolvo:
            a = [2, 4, 6, 10, 25, 50, 100, jackbi]
            b = [1, 0, 0]
            jack = [0.5, 0.3, 0.2]
            d = np.random.choice(a, p=[0.699745, 0.25, 0.04, 0.007, 0.003, 0.0002, 0.00005, 0.000005])
            cj = np.random.choice(jack, p=[(500 + evchips) / 1500, (1 - (500 + evchips) / 1500) / 2, (1 - (500 + evchips) / 1500) / 2])
            c = np.random.choice(b, p=[(500 + evchips) / 1500, 0.5 * (1000 - evchips) / 1500, 0.5 * (1000 - evchips) / 1500])
            if d > 49:
                print('On', i, 'tournament x', d)
                if d <51:
                    print('Profit -', c*d*buyin, 'euro')
                if d >50:
                    print('Profit -', cj*d*buyin, 'euro')
            if d <51:
                prize += c*d*buyin
                profitg +=c*d*buyin-buyin
                profitgg +=[profitg]
                profitgrb += c * d*buyin - buyin +buyin*rake*rakeback
                profitggrb += [profitgrb]

    #        print ('Множитель -', d)
#        print ('Выигрыш -', c*d)

            if d>50:
                prize +=cj*d*buyin
                profitg += cj * d*buyin - 1
                profitgg += [profitg]
                profitgrb += cj * d*buyin - buyin + buyin*rake * rakeback
                profitggrb += [profitgrb]
#        print (d)
#        print (cj*d)

            i += 1


#print (prize)
        profit = prize-kolvo*buyin

        print ('For', kolvo, 'tournaments:')
#print ('Максимальный множитель -', max (d))
#print ('Максимальный выигрыш -', max (c*d), 'бай-инов')
        print ('Profit -', profit, 'euro')
        print ('With rakebacks - ', profit+0.3*kolvo*0.05*buyin, 'euro')
        print ('ROI', (profit/(kolvo*buyin))*100, '%')
        print ('ROI with rakeback', ((profit+0.3*kolvo*buyin*0.05)/(kolvo*buyin))*100, '%')

        kolvog = linspace (1, kolvo, kolvo)


        figure()
        plot (kolvog, profitgg, kolvog, profitggrb)
        xlabel ('Count tournaments')
        ylabel('Profit (with rakeback), euro')
        title('Fish Party')
        show()

        q = str (input('Simulation again? yes/no'))

        if (q=='Yes') or (q=='yes') or (q=='YES'):
            print ('Good Luck!')
            j+=1
        else:
            print ('Buy! And good luck!')
            print('Developed by Artur Yarovoy, 2017 год')
            time.sleep(5)
            break


if (lang == 'RU') or (lang=='Ru') or (lang=='ru'):
    j=1
    while j > 0:
        kolvo = int (input('Введите кол-во турниров'))
        buyin = int (input ('Введите бай-ин турнира'))
        jackpot = int (input ('Введите размер джекпота в евро'))
        jackbi = jackpot/buyin
        rake = 0.05
        evchips = int (input('Введите кол-во ев-фишек'))
        rakeback = 0.3


        i=1
        prize=0
        profitg = 0 #профит для графика
        profitgg = []
        profitgrb = 0 #профит для графика с рейкбеком
        profitggrb = []

        while i <=kolvo:
            a = [2, 4, 6, 10, 25, 50, 100, jackbi]
            b = [1, 0, 0]
            jack = [0.5, 0.3, 0.2]
            d = np.random.choice(a, p=[0.699745, 0.25, 0.04, 0.007, 0.003, 0.0002, 0.00005, 0.000005])
            cj = np.random.choice(jack, p=[(500 + evchips) / 1500, (1 - (500 + evchips) / 1500) / 2, (1 - (500 + evchips) / 1500) / 2])
            c = np.random.choice(b, p=[(500 + evchips) / 1500, 0.5 * (1000 - evchips) / 1500, 0.5 * (1000 - evchips) / 1500])
            if d > 49:
                print('На', i, 'турнире выпал множитель x', d)
                if d <51:
                    print('Выигрыш -', c*d*buyin, 'евро')
                if d >50:
                    print('Выигрыш -', cj*d*buyin, 'евро')
            if d <51:
                prize += c*d*buyin
                profitg +=c*d*buyin-buyin
                profitgg +=[profitg]
                profitgrb += c * d*buyin - buyin +buyin*rake*rakeback
                profitggrb += [profitgrb]

    #        print ('Множитель -', d)
#        print ('Выигрыш -', c*d)

            if d>50:
                prize +=cj*d*buyin
                profitg += cj * d*buyin - 1
                profitgg += [profitg]
                profitgrb += cj * d*buyin - buyin + buyin*rake * rakeback
                profitggrb += [profitgrb]
#        print (d)
#        print (cj*d)

            i += 1


#print (prize)
        profit = prize-kolvo*buyin

        print ('За', kolvo, 'турниров:')
#print ('Максимальный множитель -', max (d))
#print ('Максимальный выигрыш -', max (c*d), 'бай-инов')
        print ('Итоговый профит -', profit, 'евро')
        print ('С учетом рейкбека - ', profit+0.3*kolvo*0.05*buyin, 'евро')
        print ('ROI', (profit/(kolvo*buyin))*100, '%')
        print ('ROI с учетом рейкбека', ((profit+0.3*kolvo*buyin*0.05)/(kolvo*buyin))*100, '%')

        kolvog = linspace (1, kolvo, kolvo)


        figure()
        plot (kolvog, profitgg, kolvog, profitggrb)
        xlabel ('Кол-во турниров')
        ylabel('Профит (с рейкбеком) в евро')
        title('Fish Party')
        show()

        q = str (input('Хотите провести симуляцию еще раз? Да/Нет'))

        if (q=='Да') or (q=='да'):

            print ('Удачи!')

            j+=1
        else:

            print ('Наверно, хватит симулировать. Пора катать. Удачи!')
            print('Разработка - Артур Яровой, 2017 год')
            time.sleep(5)
            break
