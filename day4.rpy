init:
    $ day4_map_necessary_done = 0
    $ day4_mi_accept = 0
    $ day4_un_compl = 0
    $ day4_us_compl = 0
    $ day4_sl_compl = 0
    $ day4_dv_compl = 0
    $ day4_uv_apple = False
    $ day4_uv_mine = 0
    $ mr1 = 0
    $ mr2 = 0
    $ mr3 = 0

label day4_std_morning:

    $ backdrop = "days"

    $ new_chapter(4, u"День четвертый")

    $ day_time()

    scene bg int_house_of_mt_day onlayer master with fade:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat

    play sound sfx_hell_alarm_clock fadein 2

    window show
    "Я проснулся оттого, что в моей голове что-то звенело."
    "Казалось, что этот звук идет откуда-то из глубин мозга, поэтому установить его источник сразу не удалось."
    window hide

    $ renpy.pause(2)

    window show
    "Однако через некоторое время после тщательного изучения комнаты стало понятно, что это будильник."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_int_cabin_day fadein 2

    window show
    th "Странно, откуда он здесь взялся и почему стоит рядом с моей кроватью?"
    "Я посмотрел на время – было полвосьмого утра."
    "Ольги Дмитриевны в комнате обнаружить не удалось, значит, на линейку меня идти никто не заставит."
    th "Следовательно, можно еще поспать."
    "Я закрыл глаза, но мое сознание, похоже, уже переключилось в дневной режим…"
    th "Стоит распланировать день – в конце концов, хоть сегодня необходимо что-то выяснить!"
    "Однако в голову мне решительно ничего не приходило."
    "Было просто необходимо проветриться, а заодно и заняться утренним туалетом."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    play music music_list["everyday_theme"] fadein 3

    show mz normal glasses pioneer at center onlayer master with dissolve
    window show
    "По дороге к умывальникам я встретил Женю."
    me "Чего это ты в такую рань?"
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "А что такого?"
    "Она посмотрела на меня так, как будто я ее чем-то обидел."
    me "Ничего, просто спросил."
    mz "Вот и иди куда шел!"
    hide mz onlayer master with dissolve
    "Конечно, Женя не отличалась особой приветливостью, но сегодня она казалась какой-то совсем озлобленной."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    window show
    "Холодная вода немного взбодрила меня, и разум прояснился…"
    "Хотя почему-то мои мысли были сосредоточены не на поиске ответов, а на том, как бы за завтраком занять место получше…"

    play sound sfx_bush_leaves

    "Я почистил зубы и уже собирался уходить, как вдруг услышал какой-то шорох в кустах."
    "Наверное, белка или еще какой зверек."
    "Шорох раздался вновь, но уже чуть дальше."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path2_day onlayer master
    with dissolve

    window show
    "Я прошел с десяток метров по лесной тропинке, пытаясь установить источник звука."

    stop music fadeout 4

    "Но никого и ничего рядом со мной не было, лишь утренний лес вокруг, такой, каким он и должен быть."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 3

    show mi normal pioneer far at center onlayer master with dissolve
    window show
    "Я вернулся назад и около умывальников увидел Мику, которая что-то высматривала в траве."
    show mi normal pioneer at center onlayer master with dissolve
    "Заметив меня, она подошла ближе."
    mi "Ой, привет, доброе утро! А я тут, знаешь, зубной порошок рассыпала, вот теперь собрать пытаюсь."
    "Я посмотрел на покрытую росой траву."
    me "А ты уверена, что это хорошая идея?"
    show mi upset pioneer at center onlayer master with dspr
    mi "Ну, как же! Как же! У меня ведь больше нет! Это был последний!"
    "Мику надула губки, как ребенок, у которого отняли любимую игрушку."
    me "Возьми мой."
    "Сказал я и полез в пакет, который лежал рядом с умывальником."
    "Но порошка там не оказалось."
    th "Странно, ведь я только что его туда положил!{w} Отошел буквально на минутку, а он исчез…"
    me "Слушай, похоже, я его забыл…"
    "Не хотелось ей говорить о том, что он просто пропал."
    "Зная впечатлительность этой девочки, можно было предположить, что исчезающие средства гигиены могут вызвать у нее такую бурю эмоций, что мой мозг уйдет на перезагрузку во избежание перегрева."
    me "Ладно, я пойду тогда…"
    show mi smile pioneer at center onlayer master with dspr
    mi "Да, конечно! Ты заходи к нам… Ну, то есть ко мне, я же пока одна в музыкальном клубе. Но мы… То есть я… Будем тебе всегда…"
    hide mi onlayer master with dissolve

    stop music fadeout 4

    "Конца фразы я не расслышал, так как был уже далеко."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    play music music_list["sweet_darkness"] fadein 5

    window show
    "Вернувшись в домик вожатой, я достал мобильник и посмотрел на индикатор батареи."
    "Судя по всему, жить ему оставалось не более суток."
    th "Конечно, здесь он мне особо не поможет, но все же…"
    "А найти в восьмидесятых годах зарядку от сотового телефона – почти то же самое, что изобрести его."

    if day3_sl_evening == 1:

        play sound sfx_knock_door7_polite

        "Я уже собирался идти на завтрак, как в дверь постучали."
        show sl normal pioneer at center onlayer master with dissolve
        "На пороге стояла Славя."
        sl "Доброе утро!{w} А Ольга Дмитриевна?.."
        "Я уставился на ее грудь и не мог отвести взгляда – слишком уж сильно она мне врезалась в память вчера."
        show sl surprise pioneer at center onlayer master with dspr
        sl "Семен?"
        "Она посмотрела на меня встревожено, а я никак не мог посмотреть ей в глаза."
        sl "Что-то не так?"
        me "Да нет, все как раз так…"
        sl "Ольга Дмитриевна?.."
        me "Не знаю, когда проснулся, ее уже не было…"
        "Я все-таки смог оторвать взгляд от славиной груди."
        show sl smile pioneer at center onlayer master with dspr
        sl "Ладно, мне еще в одно место надо заскочить, так что увидимся на завтраке."
        hide sl onlayer master with dissolve
        "Она улыбнулась, помахала мне рукой и убежала."

    if day3_un_evening == 1:

        play sound sfx_knock_door7_polite

        "Я уже собирался идти на завтрак, как в дверь постучали."
        show un normal pioneer at center onlayer master with dissolve
        "На пороге стояла Лена."
        un "Доброе утро…"
        me "Доброе…"
        "Я несколько смутился."
        "События вчерашней ночи еще стояли у меня перед глазами, но упоминать о них не стоило…"
        me "Ольгу Дмитриевну ищешь, наверное?"
        show un shy pioneer at center onlayer master with dspr
        un "Да нет…{w} То есть да…"
        "Лена была такой же, как и всегда, скромной и стеснительной."
        "Казалось, что тот танец на пристани – всего лишь сон."
        me "А ее нет."
        un "А, ну, ладно тогда…{w} Я пойду."
        me "Угу…"
        hide un onlayer master with dissolve
        "Когда она ушла, я подумал, что все же был слишком холоден, и при следующей встрече решил обязательно быть поприветливее."

    "Несмотря ни на что утро было прекрасным."
    "Яркое солнце освещало затерянный где-то во времени и пространстве пионерлагерь «Совёнок», согревало его обитателей и придавало им силы провести этот день с пользой."
    "Или в моем случае – угробить его на тщетные попытки найти разгадку всего происходящего."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 4

    window show
    "У столовой было необычайно многолюдно."
    "Конечно, на завтрак, обед и ужин местные обитатели спешили как на пожар, но зачем же толпиться в дверях…"
    "Я подошел поближе и попытался узнать, что происходит."
    window hide

    stop music fadeout 3

    jump day4_main1

label day4_fail_morning:

    $ backdrop = "days"

    $ new_chapter(4, u"День четвертый")

    $ day_time()

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with fade

    play sound sfx_hell_alarm_clock fadein 2

    window show
    "Меня разбудил адский треск в голове.{w} Казалось, что она разрывается изнутри."
    window hide

    $ renpy.pause(2)

    window show
    "Я кое-как продрал глаза, увидел на тумбочке перед собой будильник, выключил его и моментально отключился."
    window hide

    scene bg black onlayer master
    with fade

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with fade

    play ambience ambience_int_cabin_day fadein 2

    window show
    "Когда я проснулся вновь, на часах было уже без пятнадцати девять."
    "Похоже, что пора вставать, иначе был риск пропустить завтрак."
    "Я поднялся с кровати, почесался и…{w} вспомнил, что было вчера!"
    "Под подушкой лежал клочок бумаги:"



    "«Ты здесь не просто так»."
    th "Что же это может означать…"
    th "Как я отправил сам себе послание?"
    th "Почему я этого не помню?"
    "Вопросов было куда больше, чем ответов.{w} Точнее, ответа не было ни одного."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я вышел на улицу и щурясь оглядел лагерь."
    th "Нет, на мираж не похоже…"
    "Но из-за этой записки все стало куда более запутанным."
    th "Чему же можно верить, а чему нет?"
    "В животе предательски заурчало."
    "Я решил, что даже агент Малдер не вел свои секретные материалы на голодный желудок, и направился к столовой."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    "Там было необычайно многолюдно."
    "Конечно, на завтрак, обед и ужин местные обитатели спешили как на пожар, но зачем же толпиться в дверях…"
    "Я подошел поближе и попытался узнать, что происходит."
    window hide

    jump day4_main1

label day4_us_morning:

    $ new_chapter(4, u"День четвёртый")

    $ day_time()

    scene bg black onlayer master

    window show
    "Во сне я ощутил тепло."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    "Такое часто бывает – мозг еще не включился, но ты все равно чувствуешь, как солнце бьет в глаза, и когда просыпаешься, некоторое время щуришься, чтобы привыкнуть к яркому свету."
    "Прекрасное утро.{w} На улице ворковали птички, воздух был свеж и прян, и весь мир купался в лучах наступающего дня."
    "Я бы с удовольствием еще полежал, но что-то было не так…"
    "Все события минувшего вечера за секунду пролетели у меня перед глазами."
    "Страшные и не очень истории, Ульяна…"
    window hide

    stop ambience fadeout 2

    scene cg d4_us_morning onlayer master
    with fade

    play music music_list["i_want_to_play"] fadein 3

    window show
    "Которая крепко обнимала меня и совсем не по-детски храпела."
    "Тогда я ничуть не волновался."
    th "В конце концов, время еще раннее – вряд ли больше семи или восьми утра."
    th "Ну, кому понадобится идти в библиотеку в такой час?"
    "Я откинулся назад и посмотрел в окно."
    th "Судя по всему, буквально через пару минут солнце займет такое положение, что будет бить Ульянке в глаза."
    me "Вот тогда ты и проснешься…"
    th "Интересно, как же она так крепко смогла меня обнять?"
    th "Ведь действительно, вырваться никак не получается…"

    "В принципе, я был готов пролежать так еще час или два, но вдруг послышались шаги."

    stop music fadeout 3

    play ambience ambience_music_club_day fadein 3

    "Стало ясно, что дело пахнет керосином."
    me "Вставай! Слышишь?! Просыпайся!"
    "Я аккуратно, но в то же время настойчиво начал трясти Ульяну за плечи, попытался ослабить захват, но ничего не вышло."
    "А в это время шаги все приближались."
    "Надо было спасаться любыми возможными способами!"
    "Встать не получится – это я выяснил еще вчера, – поэтому решил ползти."
    "Все это очень напоминало какие-то военные сборы, на которых я никогда не был – солдат тащит за собой раненого командира под минометным обстрелом."
    "Командир без сознания, солдат измотан, а кругом – колючая проволока…"
    window hide

    scene cg day4_us_morning onlayer master
    with dissolve

    window show
    "Я только и успел, что заползти за шкаф и перевернуть Ульяну так, чтобы ее не было видно, как дверь в библиотеку открылась."
    "На пороге стояла Женя."
    th "Похоже, она слишком уж трепетно относится к своей работе, раз приходит сюда с первыми петухами."
    el "… подожди!"
    "Я услышал знакомый голос."
    th "Вот, собственно, наверное, и первые петухи пожаловали…"
    mz "Почему это нельзя было сделать вчера? Или сегодня, но попозже?"
    el "Потому что наука не терпит промедлений!"
    mz "Наука…"
    "Это был Электроник."
    mz "Сейчас, подожди, я поищу."

    "Она направилась в нашу сторону."
    "Я из последних сил перевернул Ульянку так, чтобы она оказалась у меня на спине, кое-как встал на четвереньки и пополз к соседнему шкафу, где упал и попытался отдышаться."
    mz "Как ты говорил? Кибернетическая математика?..{w} Или математическая кибернетика?.."
    th "Похоже, она нас не заметила."
    el "Мне бы что-нибудь про «Теорию автоматов»…"
    mz "Откуда у нас тут про оружие? Ты что, сдурел?!"
    el "Так это не про оружие совсем…"
    "Какое-то время они оба молчали."
    el "Жень…"
    mz "Чего еще?"
    el "А пойдем сегодня вечером на речку…"
    mz "Это зачем?"
    el "Ну…{w} Просто…"
    mz "У меня здесь дел много…{w} А ты иди давай, робот твой тебя ждет."
    el "Ладно…"

    play sound sfx_close_door_1

    "Я услышал звук закрывающейся двери."

    stop ambience fadeout 2

    play music music_list["i_want_to_play"] fadein 3

    th "А Электронику-то тоже не чуждо ничто человеческое."
    "Я тихо усмехнулся."
    "Впрочем, сейчас было не до веселья – предстояло как-то выбраться отсюда незамеченными."
    "Самым простым решением мне тогда показалось дождаться, пока Женя пойдет завтракать."
    "Все же она была ударницей коммунистического труда, а не одним из мифических роботов Электроника, поэтому потребность в пище для нее никто не отменял."
    "Ульяна тем временем и не думала просыпаться."
    th "Хорошо хоть храпеть перестала."
    "В библиотеке было тихо."
    "Что делала Женя, я не видел, но такое положение вещей до определенной степени меня устраивало."
    "Я уже было успокоился, как со стороны ее стола донеслись какие-то звуки: щелканье, шипение и…{w} заиграла музыка."
    "Точнее, гимн!"
    th "Приехали."
    "И все бы ничего, если бы Женя не начала подпевать!"
    mz "Союз нерушимый…"
    "Ее чувству патриотизма оставалось только позавидовать."
    "Хотя с голосом у нее были явные проблемы – советская эстрада в ее лице уж точно не потеряла талантливую певицу."
    "После гимна какой-то голос рассказал о перевыполнении плана по уборке зерновых."
    "Очевидно, Женя включила радио."
    "Я начал внимательно вслушиваться – возможно, удастся что-нибудь узнать."
    "Однако после сводок с полей голос диктора начал пропадать, а через некоторое время исчез вовсе."
    th "Может быть, помехи…"
    "Женя встала и направилась в нашу сторону."
    "Ситуация становилась критической."
    "Титаническим усилием воли мне все же удалось разжать захват Ульянки."
    "Теперь я был свободен, но настолько измотан всеми этими поползновениями, что не чувствовал в себе сил даже встать."
    "Надо было готовиться к худшему и придумывать оправдания…"
    "Но внезапно шаги затихли."
    "Судя по всему, Женя остановилась с другой стороны шкафа, за которым лежали мы."
    "Послышалось шуршание книг."
    th "Наверное, что-то ищет."
    "Взяв книгу, она вернулась к столу."

    play sound sfx_open_door_strong

    "В этот момент с грохотом распахнулась дверь."
    mt "Семен?!{w} Не видела?"
    "Ольга Дмитриевна явно сильно запыхалась."
    mt "Ульяна?!"
    mz "Нет…"
    "Удивленно ответила Женя."

    play sound sfx_open_door_strong

    "Послышался такой же звук, но в этот раз дверь, видимо, захлопнули."
    "Похоже, нас уже ищут, и сейчас Женя начнет обход библиотеки…"

    play sound sfx_dinner_jingle_normal

    "Однако, к счастью, в этот момент где-то вдалеке заиграла музыка, призывающая пионеров на завтрак."
    "Женя, как и подобает пунктуальному человеку, не стала задерживаться, и через минуту в библиотеке нас вновь осталось двое – я и Ульяна."
    "Теперь предстояло решить, что делать с ней…"
    "Уже не надо было бояться, что меня кто-то услышит, поэтому я наклонился над ней и заорал ей в ухо:"
    me "Проснись и пой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    show us fear pioneer at center onlayer master with dissolve
    window show
    "Ульяна мгновенно вскочила и начала спросонья озираться по сторонам."
    show us normal pioneer at center onlayer master with dspr
    "Заметив меня, она некоторое время непонимающе смотрела мне в глаза."
    show us surp3 pioneer at center onlayer master with dspr
    us "А что ты здесь делаешь?"
    me "Играю в разведчиков."
    us "А?"
    me "Неважно… Выспалась?"
    show us surp1 pioneer at center onlayer master with dspr
    us "Да…"
    "Кажется, она еще не совсем пришла в себя."
    me "Завтракать?"

    stop music fadeout 3

    us "Да…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_library_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Мы вышли из библиотеки."
    "Я был несказанно рад сему факту."
    th "Теперь уж точно не придется никому объяснять, что, как и почему я делал с Ульяной там всю ночь…"
    show us shy pioneer at center onlayer master with dissolve
    us "Ты прости, что я так вот заснула…"
    me "Да ничего."
    "Наверное, в моем голосе было слишком много скептицизма, потому что она посмотрела на меня с недоверием."
    show us normal pioneer at center onlayer master with dspr
    us "Подожди-ка…{w} А что ты все время там делал?"
    me "Ты не поверишь…"
    show us surp1 pioneer at center onlayer master with dspr
    us "Подожди-ка…{w} То есть…"
    show us laugh pioneer at center onlayer master with dspr
    "Она хихикнула, отбежала от меня на пару метров и звонко прокричала:"
    show us laugh pioneer far at center  onlayer master with dissolve
    us "А я первая на завтрак!"
    hide us onlayer master with dissolve
    me "После такого-то пит-стопа немудрено…"
    "Сказал я, но Ульяна уже не могла меня слышать, так как была далеко."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    "У столовой было необычайно многолюдно."
    "Конечно, на завтрак, обед и ужин местные обитатели спешили как на пожар, но зачем же толпиться в дверях…"
    "Я подошел поближе и попытался узнать, что происходит."
    window hide

    jump day4_main1

label day4_main1:

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    window show
    "На пороге, казалось, собрался весь лагерь."
    "Здесь были и все знакомые мне девочки, и Ольга Дмитриевна, и Электроник."
    "Они что-то оживленно обсуждали."
    "Я подошел поближе."
    show mt normal pioneer onlayer master at right
    show el normal pioneer onlayer master at left
    with dissolve

    stop ambience fadeout 2

    play music music_list["silhouette_in_sunset"] fadein 3

    mt "О, Семен!"

    if day3_us_evening == 1:
        show mt angry pioneer at right onlayer master with dspr
        mt "И где же ты был?!{w} Я тебя всю ночь ждала! И с самого раннего утра ищу!{w} Ульяна сказала, что вы вчера вместе уходили вечером из библиотеки."
        show us surp1 pioneer at center onlayer master with dissolve
        "Я посмотрел на Ульянку.{w} Она ехидно улыбалась."
        me "Я…"
        mt "Ладно, с тобой позже!"
        hide us onlayer master with dissolve
        show mt normal pioneer at right onlayer master with dspr

    mt "Ты не видел сегодня Шурика?"
    me "Нет, а что такое?"
    mt "Мы его с утра не можем найти!"
    th "Исчезновение пионеров – это что-то новенькое."
    mt "Но вчера же он был с тобой в палатке?"
    "Она обращалась к Электронику."
    el "Был…"
    mt "А утром ты проснулся, а его нет?"
    el "Нет…"
    mt "И почему ты сразу не пошел ко мне?"
    show el upset pioneer at left onlayer master with dspr
    el "Ну, я подумал, что, может, он раньше проснулся и умываться пошел или еще куда…"
    show sl normal pioneer at center onlayer master with dissolve
    sl "А он вчера ничего такого не говорил?"
    "В разговор вмешалась Славя."
    el "Например?"
    sl "Ну, что собирается куда-то?"
    el "Нет…"
    me "А что такого страшного-то произошло?{w} Время только девять утра. Может, он прогуляться решил."
    show sl serious pioneer at center onlayer master with dspr
    sl "Ты не знаешь Шурика."
    "Она серьезно посмотрела на меня."
    me "Не знаю, да…"
    "Но в то же время ничего подозрительного в этой ситуации я не находил."
    mt "Ладно, не будем паниковать. Наверняка найдется!"
    show us grin pioneer at right onlayer master with dissolve:
        xpos 1.2
        linear 0.5 xpos 0.65
    us "Чтобы он пропустил завтрак…"
    "Усмехнулась Ульянка."
    show dv normal pioneer at left onlayer master with dissolve:
        xpos -0.2
        linear 0.5 xpos -0.1
    dv "Точно! Пора уже и есть идти."
    hide us onlayer master
    hide dv onlayer master
    hide sl onlayer master
    hide el onlayer master
    if day3_us_evening != 1:
        hide mt onlayer master
    with dissolve
    "Все собравшиеся начали заходить в столовую."

    if day3_us_evening == 1:
        show mt normal pioneer at right onlayer master with dspr
        "Меня остановила Ольга Дмитриевна."
        mt "Семен, а ты постой-ка."
        me "Да?"
        show mt angry pioneer at right onlayer master with dspr:
            linear 1.0 xalign 0.5
        mt "Изволишь объясниться, где ты был ночью?"
        me "Я…"
        "Вот об этом я как-то не подумал…"
        "Действительно, подобное не могло остаться незамеченным, и мне стоило бы придумать годное объяснение."
        "Но я не придумал…"
        me "А я…{w} А мы с Ульяной в библиотеке книги расставляли, а потом она убежала и меня закрыла! И я сидел там до утра!"
        mt "Я была с утра в библиотеке!{w} А вот тебя там не видела."
        th "Да я в курсе…"
        me "Ну…{w} Я незаметно ушел…"
        mt "А почему Ульяна говорит совсем другое?"
        th "И что же, интересно, она говорит?"
        me "Ну, вы же ее знаете…"
        show mt normal pioneer at center onlayer master with dspr
        mt "Да, пожалуй…"
        "Она задумалась."
        show mt angry pioneer at center onlayer master with dspr
        mt "Но ты не думай, что я тебе поверю!"
        "Я и не думал…"
        show mt normal pioneer at center onlayer master with dspr
        mt "Разберемся с этим позже, я не забуду!{w} А сейчас есть дела поважнее – найти Шурика."
        me "Да…"
        mt "Иди уж есть…"
        hide mt onlayer master with dissolve

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Выбирать, куда приткнуться, мне опять не пришлось – единственные свободные места оказались рядом с Алисой и Ульяной."
    show us laugh pioneer onlayer master at cright
    show dv normal pioneer onlayer master at cleft
    with dissolve
    us "Садись."
    "Она показала на стул рядом с собой."
    "Я сел."
    if day3_dv_dumped:
        "Алиса выглядела как обычно и даже не думала устраивать мне разнос за то, что я обещал вчера вечером прийти на сцену, но не пришел."
        "Я решил, что раз она не хочет об этом говорить, то и мне не стоит."
    us "Может, все же возьмешь еду?"
    th "Точно!{w} Об этом я и не подумал как-то…"
    "Завтрак вроде бы был такой же, как и вчера, но сегодня он как будто выглядел аппетитнее."
    "Может быть, просто очень хотелось есть…"
    "А может, я пытался побыстрее покончить с ним, чтобы не нарваться на очередную ульянкину выходку."
    us "Пойдешь сегодня с нами на пляж?"
    me "Когда?"
    us "Поедим и пойдем."
    "Вообще говоря, развлечения сегодня не входили в мои планы, но в то же время час-два вполне можно было поваляться на солнышке и подумать."
    me "Пойду, почему нет…"
    show us laugh2 pioneer at cright onlayer master with dspr
    us "Вот и отлично!"
    "Она мило улыбнулась."
    me "Опять небось что-нибудь замышляешь?"
    show us surp2 pioneer at cright onlayer master with dspr
    us "Нет, ты что!"
    "Ульяна замахала руками."
    show dv smile pioneer at cleft onlayer master with dspr
    dv "Наверняка!"
    "Ухмыльнулась Алиса."
    dv "Она такая!"

    if day3_dv_evening == 1:
        "Я внимательно посмотрел на Алису и тут же вспомнил вчерашний вечер."
        "Ее странное поведение, нашу ссору."
        "Но сейчас она казалась такой же, как и всегда."
        th "Может, и не стоит тогда ничего говорить?"
        "Хотя, наверное, я и не собирался."
        "В конце концов, за ночь произошедшее перестало казаться чем-то действительно необычным, даже стали появляться мысли, что мне все лишь показалось."

    show us surp3 pioneer at cright onlayer master with dspr
    us "А вот и нет!"
    me "Я склонен с ней согласиться."
    show us grin pioneer at cright onlayer master with dspr
    us "Да никто и не сомневался!"
    "Ульянка взяла поднос с грязной посудой и встала."
    us "Приятного аппетита!"
    hide us onlayer master with dissolve
    "Она сказала это так, что я полностью уверился в том, что ничего хорошего сегодня на пляже меня не ждет…"
    show dv normal pioneer at cleft onlayer master with dspr:
        linear 0.5 xalign 0.5
    "Мы остались вдвоем с Алисой."
    me "Знаешь, я все же, наверное, с вами не пойду…"
    show dv normal pioneer at center onlayer master with dspr
    dv "А что так?"
    me "Ну, дела кое-какие…"
    show dv surprise pioneer at center onlayer master with dspr
    dv "И что же у тебя за дела?"
    "Она заглянула мне в глаза так, что я не нашелся, что соврать."
    me "Ну, у меня и плавок даже нет…"
    show dv normal pioneer at center onlayer master with dspr
    dv "Надень мои."
    me "Думаешь, они на меня налезут?"
    show dv grin pioneer at center onlayer master with dspr
    dv "А ты попробуй!"
    me "Думаю, не стоит…"
    show dv smile pioneer at center onlayer master with dspr
    dv "Да ты не бойся!{w} Найдем мы тебе плавки!"
    "От этой фразы страх мой только усилился."
    dv "Подожди меня возле столовой, я вернусь через пару минут."
    me "Ладно…"

    stop ambience fadeout 2

    th "В конце концов, ничего такого в том, чтобы просто ее дождаться, нет…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Закончив завтрак, я вышел на улицу и сел на ступеньки."
    "Мимо меня один за другим проходили пионеры, спешащие по своим делам."
    "Никто не останавливался.{w} Никто даже не смотрел на меня."
    "Кажется, они совсем не считали меня чужаком, а напротив – обычным подростком их возраста, можно сказать, своим товарищем."
    "Я поймал себя на мысли, что и сам начал воспринимать этот лагерь и всех его обитателей уже не с такой обостренной настороженностью, как в первый день."
    window hide

    with fade

    window show
    "Алиса действительно вернулась через пару минут."
    show dv normal pioneer at center onlayer master with dissolve
    dv "Готов?"
    me "К чему?"

    play music music_list["i_want_to_play"] fadein 1

    "Она протянула мне плавки…{w} Хотя плавками это назвать было сложно…"
    "Больше они походили на розовые семейные трусы, украшенные бабочками и цветочками.{w} Точнее, ими и являлись."
    me "Боюсь спросить, откуда ты это взяла?"
    show dv grin pioneer at center onlayer master with dspr
    dv "А что, боишься их надеть?"
    me "Да как-то, знаешь…{w} Не имею никакого желания."
    "Ее прикол я оценил, но совершенно не собирался выставлять себя на посмешище."
    show dv angry pioneer at center onlayer master with dspr
    dv "Надевай!"
    "Грубо сказала она."
    me "Почему бы тебе их не примерить вместо меня?{w} Мне кажется, цвет этого бикини прекрасно оттеняет твои глаза!"
    show dv smile pioneer at center onlayer master with dspr
    dv "Давай на спор!"
    "Спорить с ней у меня не было ни малейшего желания."
    me "Нет, спасибо."
    show dv angry pioneer at center onlayer master with dspr
    dv "Короче, либо ты идешь на пляж в этом, либо плаваешь голым!"
    th "Если все тщательно взвесить, то второй вариант будет даже лучше первого."
    me "Я вообще уже не планирую туда идти…"
    show dv grin pioneer at center onlayer master with dspr
    dv "Тогда я всем расскажу, что ты подбросил мне эти трусы!"
    me "И зачем мне это делать?"
    show dv laugh pioneer at center onlayer master with dspr
    dv "А мне откуда знать?"
    "Она расхохоталась."
    "Дальше спорить с Алисой мне совсем не хотелось, поэтому я решил все же пойти на пляж."
    "Конечно, не в этих гламурных плавках."
    me "Ладно, приду минут через десять."
    show dv smile pioneer at center onlayer master with dspr
    dv "Вот и славно!"

    stop music fadeout 3

    "Сказав это, она убежала."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    stop ambience fadeout 2

    window show
    "Я поплелся к домику вожатой, чтобы взять полотенце и заодно попытаться из чего-нибудь соорудить плавки."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_int_cabin_day fadein 3

    show mt normal pioneer at center onlayer master with dissolve
    window show
    "В комнате меня ждала Ольга Дмитриевна."
    mt "Семен, о Шурике ничего не слышно?"
    me "Ровно столько же, сколько и полчаса назад…"
    "Я подошел к своей кровати и взял полотенце."
    mt "Куда-то собираешься?"
    me "Да, на пляж…"
    mt "Подожди, а у тебя есть плавки?{w} А то ты же вроде без вещей приехал…"
    "Странно, что этот факт не удивил ее при первой встрече."
    me "Нет…"
    show mt surprise pioneer at center onlayer master with dspr
    mt "А в чем пойдешь?"
    th "Действительно, а в чем?"
    me "Не знаю…"
    show mt normal pioneer at center onlayer master with dspr
    mt "Сейчас, подожди…"

    play sound sfx_key_drawer

    "Она подошла к шкафу и открыла ключом запертый ящик."
    "Через мгновение у вожатой в руках были обычные мужские плавки черного цвета."
    th "И откуда они у нее взялись?{w} А главное, зачем?"
    "Хотя, может, кто-то из прошлой смены забыл, мало ли…"
    "Учитывая все странности этого лагеря, найти мужские плавки в комнате Ольги Дмитриевны – это еще не самое удивительное."
    me "Спасибо."

    stop ambience fadeout 2

    "Плавки были как раз моего размера."
    window hide

    scene bg black onlayer master
    with dissolve

    window show
    "..."
    "Я переоделся за домиком и пошел на пляж."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_beach_day onlayer master
    with dissolve

    play ambience ambience_lake_shore_day fadein 3

    window show
    "Там уже собралось много пионеров, но из знакомых – только Алиса и Ульяна."
    show us laugh swim at cright onlayer master with dissolve
    us "Иди к нам!"
    "Я подошел и сел рядом с ними на песок."
    show dv smile swim at cleft onlayer master with dissolve
    dv "Смотрю, ты нашел получше…"
    "Она уставилась на мои плавки и ехидно улыбнулась."
    me "Как видишь…"
    us "Пойдем плавать!"
    me "Не хочется что-то…{w} Может, попозже…"
    "Я не был большим любителям купаться."
    dv "Ну, как знаешь…"
    hide us onlayer master
    hide dv onlayer master
    with dissolve
    "Девочки убежали к воде."
    th "Зачем я вообще сюда пришел?{w} Почему не ищу ответы, разгадки?.."
    th "Но волнует ли это меня сейчас?"
    "Хоть лагерь и казался нормальным, за все время пребывания здесь со мной произошло много всяких странных событий, но ни одно из них не дало мне даже малейшего намека на суть того, что тут творится."
    "Напротив, все, что случалось, только больше запутывало ситуацию."
    th "Да и какие у меня альтернативы?"
    th "От местных обитателей правды не добиться…{w} Если они вообще ее знают."
    th "Попытаться уйти отсюда?"
    th "Но далеко ли я дойду пешком при том, что даже не знаю, где точно нахожусь…"
    th "Получается, что мне остается только ждать."
    show us laugh swim onlayer master at cright
    show dv normal swim onlayer master at cleft
    with dissolve
    "Через некоторое время девочки вернулись.{w} Ульяна что-то держала в руках."
    us "Смотри!"
    "Я поднял глаза и увидел рака.{w} Обычного речного рака."
    window hide

    scene cg d4_us_cancer onlayer master
    with dissolve

    window show
    "Ульянка легла рядом и принялась его мучить."
    me "Оставь бедное животное в покое!"
    us "Ты что!{w} Это же рак!"
    me "Ну и что, что рак?{w} Он тоже имеет право на жизнь!"
    us "Вот сейчас я ему клешни поотрываю, а потом попрошу повариху его сварить на ужин!"
    me "Как будто больше есть нечего…"
    "Я посмотрел на Алису.{w} Похоже, ульянкины забавы с бедным ракообразным ее совсем не интересовали."
    me "Хоть ты ей скажи!"
    dv "А что такого?{w} Он же рак – так ему и надо!"
    "Похоже, эти девочки прогуливали уроки природоведения в начальных классах, и бережное отношение к окружающей среде им было чуждо…"
    me "Отдай!"
    "Я выхватил рака у Ульянки."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_beach_day onlayer master
    with dissolve

    show us shy2 swim at center onlayer master with dissolve
    window show
    us "Да ради Бога…"
    "Меня немного удивило, что она не стала сопротивляться."
    "Я посмотрел в глаза бедному животному."
    "Они совершенно ничего не выражали, но, думаю, если бы он умел разговаривать, то обязательно возмутился, возможно, даже сослался на конвенцию ООН о правах человека."
    "Правда, не уверен, что это бы помогло..."
    window hide

    with fade

    window show
    "Я отнес рака к реке и отпустил на волю."
    show us surp1 swim at center onlayer master with dspr
    us "Ничего, еще наловлю – тут их много."
    "Сказала Ульянка."
    me "Кто бы сомневался…"
    "Пробормотал я себе под нос."
    hide us onlayer master with dissolve
    window hide

    with fade2

    stop ambience fadeout 2

    window show
    "Время шло, и незаметно меня разморило…"
    window hide

    scene bg black onlayer master
    with fade

    window show
    "Я задремал."
    "Не помню, что мне снилось, если снилось вообще, но проснулся я от того, что кто-то тряс меня за плечо."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_beach_day onlayer master
    with fade

    play ambience ambience_lake_shore_day fadein 3

    show mt normal swim at center onlayer master with dissolve
    window show
    "Надо мной стояла Ольга Дмитриевна."
    me "Тоже поплавать пришли?"
    "Спросил я спросонья."
    mt "Нет.{w} Уже обед скоро, а мы Шурика все еще не можем найти."
    "Сказала вожатая, стоящая передо мной в мокром купальнике..."
    me "И?"
    mt "Хочу, чтобы ты поискал его."
    me "А что, кроме меня, в лагере больше пионеров нет?"
    "Я искренне возмутился."
    "С каждым разом становилось все понятнее, что Ольга Дмитриевна держит меня за посыльного с функциями раба.{w} Или наоборот..."
    show mt angry swim at center onlayer master with dspr
    mt "Раз я пришла к тебе, значит, хочу, чтобы ты мне помог."
    "И почему же именно ко мне?"
    "Однако, подумав, я решил согласиться."
    "В конце концов, похоже, плечи и вся спина сильно обгорели на солнце во время сна, а поиски Шурика, возможно, позволят получше познакомиться с теми местами лагеря, где бывать мне еще не доводилось."
    me "Ладно…"
    "В плавках идти не комильфо, поэтому сначала надо было переодеться."
    window hide

    stop ambience fadeout 2

    scene black onlayer master
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "И вот спустя десять минут я стоял на пороге домика Ольги Дмитриевны и думал, куда пойти…"
    window hide

    $ disable_all_zones()

    $ set_zone("camp_entrance","day4_busstop")
    $ set_zone("boat_station","day4_boathouse")
    $ set_zone("me_mt_house","day4_house_of_mt")
    $ set_zone("forest","day4_forest")

    jump day4_map

label day4_map:
    if day4_map_necessary_done == 2:
        jump day4_main2
    $ show_map()

label day4_busstop:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    "Хорошим вариантом была автобусная остановка."
    "У меня в голове промелькнула шальная мысль, что Шурик, как и я, решил сбежать из этого лагеря и стоит ждет автобус номер 410…"
    "Это вполне могло оказаться правдой, если он тоже попал сюда случайно."
    "Хотя вероятность этого крайне мала."
    th "Но чем черт не шутит!"
    th "Тем более вдруг автобус и правда приедет…"

    stop ambience fadeout 2

    "Впрочем, в это верилось с трудом."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_camp_entrance_day onlayer master
    with dissolve

    play ambience ambience_camp_entrance_day fadein 3

    window show
    "В итоге, постояв на остановке пару минут, я убедился, что ни Шурика, ни кого другого здесь не встречу, и пошел назад в лагерь."

    play sound sfx_body_bump

    with vpunch
    "Однако из ворот кто-то выскочил и мгновенно врезался в меня.{w} Удар был не сильный, так что я всего лишь немного отшатнулся."
    show mi shocked pioneer close at center  onlayer master with dissolve   
    "Передо мной стояла Мику.{w} Она потирала ушибленный лоб."
    me "Ой, извини…"
    show mi normal pioneer at center onlayer master with dissolve
    mi "Да ничего! Это я во всем виновата! Понимаешь, я в музыкальный кружок шла, но задумалась над новой песней… Знаешь, текст придумывала, музыку… И сама не заметила, как здесь оказалась."
    mi "Так что ты не извиняйся!"
    "Количество слов в минуту превышало лимит восприятия моего мозга."
    "Я попытался в спешном порядке ретироваться."
    me "Да, да… Мне идти пора… Такие дела…"
    show mi shy pioneer at center onlayer master with dspr
    mi "Подожди!"
    "Хотелось, как обычно, уйти, не дослушав ее, но Мику схватила меня за руку."
    "От ее прикосновения у меня мурашки по коже побежали, а перед глазами пронеслись картины мучительной казни через риторику."
    show mi serious pioneer at center onlayer master with dspr
    mi "Можешь мне помочь немного, пожалуйста? Совсем чуть-чуть?"
    "Подобное в мои планы никак не входило."
    me "Да я бы с радостью, но мне…"
    mi "Ну пожалуйста…"
    "Она посмотрела на меня такими щенячьими глазами, что мое сердце начало таять…"
    "Руку при этом она и не думала отпускать."
    me "А в чем, собственно, помощь заключается?"
    show mi normal pioneer at center onlayer master with dspr
    mi "Подыграешь мне! А то у меня так совсем не получается сочинять! Я могу петь… Или играть… Или петь… А вместе почему-то не получается…"
    th "Даже у человека-оркестра есть свои слабости."
    me "Да ты знаешь, я и играть-то ни на чем толком не умею…"
    mi "Не страшно! Я тебе покажу! Пойдем!"
    window hide

    menu:
        "Согласиться":
            $ day4_mi_accept = 1
            window show
            th "С другой стороны, я же ничего не теряю!"
            "Хотя..."
        "Отказаться":
            window show
            me "Знаешь, мне Шурика надо искать и все такое..."
            show mi upset pioneer at center onlayer master with dspr
            "Мику разочарованно посмотрела на меня."
            mi "Ну, совсем чуть-чуть!"
            "Я не нашелся, что ответить..."

    show mi happy pioneer at center onlayer master with dspr
    "Она потащила меня за собой."
    th "Скорее всего, ничего хорошего из этого не выйдет, но единственный вариант вырваться – грубо выхватить руку."
    "Но это было бы неучтиво..."

    stop ambience fadeout 2

    th "Ну, в конце концов, ничего страшного не происходит…{w} Наверное…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    play ambience ambience_music_club_day fadein 3

    show mi normal pioneer at center onlayer master with dissolve
    window show
    "Через минуту мы уже стояли в здании музыкального кружка."
    "Мику взяла гитару."
    mi "Вот, смотри!"
    window hide

    scene cg d4_mi_guitar onlayer master
    with dissolve

    play sound sfx_miku_song_learn1

    window show
    "Она села и начала играть."
    "Я следил за ее руками.{w} Мелодия была довольно простой."
    "Да и с виду повторить ее было несложно."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    show mi normal pioneer at center onlayer master with dissolve
    window show
    mi "Запомнил?"
    me "Вроде да."
    mi "Ну, давай тогда попробуем!"

    play sound sfx_miku_song_learn2

    "Я взял гитару и начал играть."
    "Получилось не очень…"
    mi "Давай еще раз покажу."
    window hide

    scene cg d4_mi_guitar onlayer master
    with dissolve

    play sound sfx_miku_song_learn1

    window show
    "Она играла куда лучше меня."
    "Глядя на Мику, я задумался…"
    th "Конечно, она не в меру разговорчивая, рассеянная и слишком наивная…{w} Но при этом к музыке у нее есть явный талант."
    "Это было видно!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    show mi normal pioneer at center onlayer master with dissolve
    window show
    mi "Попробуй еще раз."
    "Во второй раз у меня получилось куда лучше."
    show mi smile pioneer at center onlayer master with dspr
    mi "Вот! Это уже похоже!"
    "Она улыбнулась."
    "На самом деле, ничего сложного – надо было просто повторять одни и те же ноты."
    th "Главное – не сбиться!"
    show mi normal pioneer at center onlayer master with dspr
    mi "Давай! На счет три!"
    me "Давай…"
    mi "Раз! Два! Три!"
    window hide

    scene cg d4_mi_sing onlayer master
    with dissolve

    play music music_list["miku_song_voice"] fadein 1

    window show
    "Это была песня на японском."
    "Честно говоря, я ничего не понял, но пела Мику хорошо.{w} Даже отлично!"
    "Видно было, что она всю душу вкладывает в каждую ноту, в каждое слово."
    th "Да, пожалуй, музыка – это именно то, чем ей стоит заниматься в жизни."
    "Казалось, не она выбрала музыку, а музыка – ее…"
    "За последние полчаса я взглянул на Мику совсем по-другому."

    stop music fadeout 2

    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    show mi smile pioneer at center onlayer master with dissolve
    window show
    mi "Ой, спасибо тебе! Понравилось? У меня наконец-то получилось, а то одной как-то не очень… Я либо с текста сбивалась, либо мимо струн попадала… А с тобой все отлично вышло! Спасибо тебе!"
    mi "Знаешь, у тебя талант определенно!{w} Так вот сразу взять и сыграть…"
    th "Нет, похоже, мнение о ней я изменил рановато…"
    me "Спасибо тебе за песню!{w} Мне пора, увидимся!"
    mi "И тебе…"
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day onlayer master
    with dissolve

    window show
    "Остаток фразы остался за дверью."
    "Я оперся о стену музыкального кружка и облегченно вздохнул."
    "Но песенка Мику все равно все еще вертелась у меня в голове…"
    window hide

    $ disable_current_zone()
    $ day4_map_necessary_done +=1
    jump day4_map

label day4_forest:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    "Конечно, было понятно, что Ольга Дмитриевна с пионерами уже осмотрела весь лагерь."
    "Можно сказать, прочесала вдоль и поперек…"
    "Поэтому искать Шурика, например, в столовой или на пляже смысла никакого не было."
    "Тем более в кружке кибернетики! Там был его второй дом.{w} А может, даже и первый."
    "Поэтому стоило осмотреть окрестный лес."
    "Естественно, далеко заходить желания не возникало, иначе пришлось бы искать и меня."
    "Вообще, я за свою жизнь не так часто бывал на природе."
    "Разве что в детстве и юношестве ездил каждое лето на дачу."
    "Но все равно она была рядом с городом…"

    stop ambience fadeout 2

    "А тут можно найти все, чего я так долго не видел – кромешная зелень, пение птиц и свежий воздух."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    play ambience ambience_forest_day fadein 3

    window show
    "Я вышел на лесную полянку и сел на пенек."
    th "Как же здесь спокойно…"
    th "И куда пошел Шурик?.."
    "Хотя, с другой стороны, он мог исчезнуть и не по своей воле."
    "Сам этот лагерь был далеко не нормальным местом, так что ничего удивительного, если здесь пропадают пионеры."
    th "Интересно только, всему виной та сила, которая забросила меня сюда, или вмешалась какая-то местечковая чертовщина?"
    "Погруженный в свои мысли, я не заметил, как трава передо мной начала шевелиться."
    "Я присмотрелся внимательнее и увидел белку."
    "Она осторожно подошла ко мне и уставилась мне на руки."
    "Наверное, она привыкла, что ее здесь кормят."
    me "Прости, животное, у меня ничего с собой нет…"
    "Конечно, белка меня понять не могла и продолжала просто сидеть, ожидая угощения."
    "Мне стало даже несколько обидно, что в кармане не завалялось даже крошки хлеба."
    "Я поймал себя не мысли, что стыжусь смотреть ей в глаза и пошел дальше."

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "После нескольких минут плутаний я вышел к умывальникам."
    th "Получается, что и в лесу его нет.{w} По крайней мере в ближайших окрестностях."
    "А дальше идти было попросту страшно."
    "Я подошел к умывальникам, снял рубашку и решил немного ополоснуться, так как довольно сильно вспотел."
    "Однако это оказалось не так просто."
    th "В раковину залезть явно не получится, а тут нет даже ковшика…"
    "Вдруг сзади послышались шаги.{w} Я обернулся."
    show el normal pioneer far at center  onlayer master with dissolve   
    "По дорожке в мою сторону шел Электроник."
    show el normal pioneer at center onlayer master with dissolve
    el "Шурика искал?"
    me "Да…{w} А ты?"
    el "И я…"
    me "Слушай, ты же его лучше знаешь, куда он мог пойти?"
    show el upset pioneer at center onlayer master with dspr
    el "Не имею ни малейшего понятия."
    "Он развел руками."
    me "Да уж…{w} Просто я не очень понимаю, зачем разводить такую панику? Ночью же он был в палатке? То есть его нет совсем недолго…{w} Может, погулять пошел…"
    show el angry pioneer at center onlayer master with dspr
    el "Ты просто не знаешь Шурика!"
    "Его голос казался взволнованным."
    el "Он фанатик своего дела!{w} Робототехника и кибернетика – это его жизнь. Таких людей – один на миллион! Нет, на миллиард! Его талант не знает границ! Я восхищаюсь им! Это стальной человек!"
    el "Нет, даже победитовый!"
    "В эту минуту он был похож на Гитлера, читающего речь перед многотысячной толпой."
    "Да и жестикуляция соответствовала."
    me "Ладно…{w} И что с того?"
    show el shocked pioneer at center onlayer master with dspr
    el "Как это что? Ты не понимаешь?"
    me "Нет…"
    el "Он все! Понимаешь, – ВСЕ! – свободное время проводит в нашем клубе!"
    me "То есть вот так пропасть для него странно?"
    el "Конечно!"
    show el normal pioneer at center onlayer master with dspr
    "Электроник, кажется, немного успокоился."
    me "Ладно…"
    "Он пристально посмотрел на меня."
    el "Мыться собираешься?"
    me "Да не то чтобы…{w} Просто ополоснуться, а то жарко."
    el "Я вот тоже…"
    "Он огляделся."
    el "Эх, жаль ни ведра, ни ковшика нет… Не из чего облиться…"
    "Это я уже заметил."
    show el smile pioneer at center onlayer master with dspr
    el "Тогда сделаем так…"
    "Он обошел умывальники и потянул один из кранов."
    "К моему удивлению, его носик поднялся, и вода лилась уже не в раковину, а почти под прямым углом."
    "Так можно было вполне помыться."
    window hide

    scene cg d4_el_wash onlayer master
    with dissolve

    stop ambience fadeout 2

    play music music_list["eternal_longing"] fadein 3

    window show
    "Электроник же тем временем снял рубашку, а затем присел и, кажется, спустил шорты."
    "Точно я сказать не мог, так как он по пояс был скрыт за умывальниками."
    "Он направил струю на себя и начал напевать себе под нос:"
    el "Чисто-чисто моем трубочиста…"
    "Я стоял в полнейшем шоке, не зная, что и думать."
    "Похоже, он это заметил."
    el "Сейчас помоюсь и тебе место уступлю."
    "Меня аж передернуло…"
    me "Да нет, знаешь…{w} Я вспомнил, что у меня дела! Мне пора!"
    "При всех странностях Электроника таких наклонностей я за ним не замечал."
    el "Ты чего?{w} В такой жаркий день помыться под холодной водой – самое лучшее удовольствие!"
    me "Не-не-не!{w} Так не пойдет!{w} И вообще, мне пора уже."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    window show
    "Я быстро надел рубашку и убежал обратно в лес."
    th "Интересно, что это на него нашло?.."
    window hide

    $ disable_current_zone()
    $ day4_map_necessary_done +=1
    jump day4_map

label day4_house_of_mt:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    th "Но все же это глупая затея."
    "Если бы Шурик был где-то в лагере, его давно нашли (если, конечно, он сам бы того захотел)."

    stop ambience fadeout 2

    th "Так что вряд ли мне удастся чем-то им помочь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_int_cabin_day fadein 3

    window show
    "С этими мыслями я зашел в домик и развалился на кровати."
    th "Если меня здесь найдет Ольга Дмитриевна, ничего хорошего не будет..."
    th "Впрочем, это уже чересчур."
    "Тем не менее делать мне ничего не хотелось."
    "День сегодня, как и все прошлые, был жаркий, так что оставалось только лежать и ждать обеда."
    "Я уже было задремал, как в дверь постучали."

    play sound sfx_knocking_door_outside

    me "Войдите."

    play sound sfx_open_door_2

    "На пороге стояла Славя."
    show sl normal pioneer at center onlayer master with dissolve
    sl "А Ольги Дмитриевны нет?"
    me "Нет."
    sl "А ты что делаешь?"
    "Спросила она с некоторым недоверием."
    "Я оглядел кровать и себя и ответил:"
    me "Лежу…"
    sl "Это я вижу.{w} Но я слышала, что тебе Ольга Дмитриевна поручила искать Шурика."
    me "Ну, да…"
    sl "И?"
    me "Какой смысл?{w} Она уже наверняка весь лагерь обыскала."
    me "Да и прошло не так много времени.{w} Зачем панику разводить?"
    show sl serious pioneer at center onlayer master with dspr
    sl "Всякое бывает…"
    "Славя глубокомысленно посмотрела на меня."
    sl "Вставай."
    me "А это обязательно?"
    "Меня настолько разморило, что даже мысль о том, что сейчас придется куда-то идти, пугала."
    show sl smile pioneer at center onlayer master with dspr
    sl "Да!"
    "Она улыбнулась."

    stop ambience fadeout 2

    "Как бы то ни было, Славе отказывать нельзя."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show sl normal pioneer at center onlayer master with dissolve
    window show
    "Я нехотя встал и вместе с ней вышел на улицу."
    "Некоторое время мы просто стояли на пороге, и грелись в лучах летнего солнца.{w} Хотя я скорее жарился…"
    me "Куда пойдем?"
    sl "Надо проверить везде."
    th "Отличная идея…"
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    play ambience ambience_library_day fadein 3

    play music music_list["take_me_beautifully"] fadein 3

    "Первым пунктом нашего маршрута была библиотека."
    "Славя подошла к Жене, сидевшей за столом, и о чем-то с ней заговорила."
    "Я же просто стоял в дверях и ждал – лишний раз общаться с местной библиотекаршей у меня не было никакого желания."
    "Через пару минут Славя вернулась ко мне."
    show sl normal pioneer at center onlayer master with dissolve
    me "И как?"
    sl "Нет…"
    "Она покачала головой."
    th "А чего, собственно, можно было ожидать?"

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    window show
    "Столовая.{w} До обеда оставалось еще порядком времени, так что не стоило ждать здесь привычной толпы пионеров."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Внутри было так же пусто, как и снаружи."
    "Пока Славя разговаривала с поварихами, я сидел и крутил в руках солонку."
    "Немного соли высыпалось на стол."
    "Если бы я верил в приметы, то наверняка бы расстроился…"
    show sl normal pioneer at center onlayer master with dissolve
    "Вернувшись, Славя сообщила, что и здесь его нет."
    "Было бы удивительно, если бы она нашла его, скажем, в холодильнике…"

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Далее по плану шел медпункт."
    "Внутрь я решил не заходить и подождал Славю снаружи."
    "Результатов никаких."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_playground_day onlayer master
    with dissolve

    window show
    "На спортивной площадке пионеры играли в футбол."
    "Шурику затеряться среди них было бы проблематично."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    show sl normal pioneer at center onlayer master with dissolve
    window show
    "Наконец, мы подошли к зданию кружков."
    me "Ты считаешь, что он может быть тут? Мне кажется, это первое место, где его стоит искать…"
    sl "Зайдем."
    window hide

    stop ambience fadeout 3

    play sound sfx_open_door_clubs_2

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day onlayer master
    with dissolve

    show sl normal pioneer at center onlayer master with dissolve
    window show
    "Внутри никого не было."
    hide sl onlayer master with dissolve
    "Славя открыла дверь в соседнюю комнату и зашла."
    "Я последовал за ней."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_clubs_male2_night onlayer master
    with dissolve

    window show
    "Все это мне казалось очень глупой затеей."
    "Тем более странным было то, что придумала все это Славя."
    th "Нет, я понимаю, ответственность там, все дела…{w} Но очевидно же, что его нет в лагере."
    th "В конце концов, не играет же он с нами в прятки."
    show sl normal pioneer at center onlayer master with dissolve
    sl "И здесь нет…"
    me "А чего ты ожидала?{w} Что он в шкафу сидит?"
    show sl angry pioneer at center onlayer master with dspr
    sl "Ну!"
    "Кажется, я ее обидел."
    me "Извини, извини…{w} Просто, серьезно!"
    show sl serious pioneer at center onlayer master with dspr
    sl "Я понимаю…{w} Но надо ведь проверить все варианты."
    me "Слушай, а ты-то что думаешь?"
    show sl normal pioneer at center onlayer master with dspr
    sl "Насчет исчезновения Шурика?"
    me "Да."
    show sl smile pioneer at center onlayer master with dspr
    sl "Может быть, он гулял в лесу и его там поймал Леший."
    "Она рассмеялась."
    me "Неправдоподобно как-то…"
    th "Впрочем, в этом лагере что угодно может быть правдой."
    show sl normal pioneer at center onlayer master with dspr
    sl "Да, наверное…{w} Сейчас не время для шуток…"
    me "Не грусти!{w} Найдется он!"
    show sl smile pioneer at center onlayer master with dspr
    sl "Надеюсь…"
    "Она улыбнулась."
    sl "Ладно, у меня еще кое-какие дела."
    me "Увидимся."
    hide sl onlayer master with dissolve
    "Она ушла, а я еще некоторое время стоял и разглядывал кладовку кружка кибернетиков."

    stop music fadeout 3

    "..."

    if day4_map_necessary_done < 2:
        "Однако активность Слави меня так вдохновила, что я решил поискать еще где-нибудь."
        window hide
    else:
        window hide

    $ disable_current_zone()
    $ day4_map_necessary_done +=1
    jump day4_map

label day4_boathouse:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    th "Может, Шурику захотелось пособирать камни у воды."
    th "В крайнем случае я найду там его хладный труп…"

    stop ambience fadeout 2

    th "Впрочем, до такого дойти не должно!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я проходил по площади, как вдруг услышал, что меня кто-то окликнул."
    show dv smile pioneer2 far at center  onlayer master with dissolve   
    dv "Подожди!"
    show dv smile pioneer2 at center onlayer master with dissolve
    "Она подошла ко мне и улыбнулась.{w} Я сразу почуял подвох."
    dv "Куда путь держишь?"
    me "Шурика ищу…{w} Ольга Дмитриевна попросила."
    show dv normal pioneer2 at center onlayer master with dspr
    dv "И как, интересно?"
    "Алиса пристально посмотрела мне в глаза, из-за чего я смутился и отвел взгляд."
    me "Да не то чтобы очень…{w} Но человек все-таки пропал!"
    dv "Ну, ты же не будешь впадать в панику из-за такой мелочи?"
    me "Ты о чем?"
    dv "Прошло всего несколько часов.{w} Может, загулял…"
    "Конечно, я был согласен с ней, но вида не подал."
    me "Да, верно…{w} Но всякое может быть…"
    show dv smile pioneer2 at center onlayer master with dspr
    dv "Давай я тебе помогу!"
    me "Эээ… Чем это?"
    "Я насторожился."
    dv "Шурика искать!"
    me "Да я и сам бы…"
    show dv grin pioneer2 at center onlayer master with dspr
    dv "Да брось ты!"
    "Она опять как-то недобро улыбнулась."
    "Нет, улыбка ее была вполне милой, но мне почему-то упорно казалось, что ничего хорошего за ней не скрывается."
    me "Ну, если ты настаиваешь…"
    "Пока что я не мог понять, что она замышляет, а веской причины для отказа не находилось…"
    show dv smile pioneer2 at center onlayer master with dspr
    dv "Только сначала мне надо домой забежать взять кое-что."
    me "Хорошо, я подожду…"
    dv "Да что ты стоять будешь!{w} Пойдем со мной!"

    stop ambience fadeout 2

    me "Ладно…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_dv_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show dv normal pioneer2 at center onlayer master with dissolve
    window show
    "Мы подошли к домику Алисы."
    "Оно бы походило на все остальные домики пионеров, если бы не Веселый Роджер на двери…"
    dv "Кстати, моя соседка – Ульянка."
    me "Окей.."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_dooor_campus_2

    pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_dv_day onlayer master
    with dissolve

    play ambience ambience_int_cabin_day fadein 2

    show dv normal pioneer2 at center onlayer master with dissolve
    window show
    "Мы зашли."
    "Внутри царил полнейший беспорядок, и мне сразу вспомнилась моя старая квартира."
    th "Впрочем, почему «старая»…"
    "Вообще, я совсем по-другому себе представлял девчачьи комнаты – белоснежные простыни на кроватях; стены, пол и полоток сверкают; нигде ни пылинки…"
    th "Но если учесть, что здесь живут две самые «образцовые» пионерки…"
    "Я поймал себя на мысли, что мы уже некоторое время просто стоим здесь."
    me "И что ты хотела взять?"
    show dv surprise pioneer2 at center onlayer master with dspr
    dv "А?"
    "Кажется, я вывел Алису из задумчивости."
    show dv smile pioneer2 at center onlayer master with dspr
    dv "Да…{w} На самом деле это не здесь…{w} Подожди, я быстро!"
    hide dv onlayer master with dissolve
    "Она улыбнулась и убежала."
    th "Что-то она какая-то рассеянная сегодня."
    "Я принялся разглядывать комнату."
    "Нельзя сказать, что создавалось впечатление того, что здесь недавно случился погром, но беспорядок был порядочный…"
    th "Получается, я еще не самый ленивый и неаккуратный человек в мире – раз уж за недолгое пребывание в лагере можно развести такой бардак."
    "Убранство моей квартиры все же создавалось годами…"
    "Я не думал ни о чем конкретно, а просто осматривал домик Алисы."
    "Плакаты советских артистов, какие-то книжки на полках, всякая бытовая мелочевка…"

    stop ambience fadeout 2

    play music music_list["always_ready"] fadein 1

    "И тут я понял, что что-то не так!"
    th "В ближайшее время должно что-то случиться!{w} Что-то плохое!"
    th "Почему Алиса меня оставила здесь?"
    "Ответ на этот вопрос таил в себе разгадку.{w} Но я его не знал…"
    "Однако шестое чувство подсказывало мне, что здесь оставаться опасно."
    "Я подошел к двери и дернул за ручку."

    play sound sfx_campus_door_rattle

    "Заперто!"
    th "Вот так номер!{w} Как она успела закрыть меня так, что я даже не услышал?"
    th "Неизвестно, что она затевает, но выбираться отсюда необходимо!"

    play sound sfx_open_window

    "Я подошел к окну, с трудом открыл его и вылез."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_dv_day onlayer master
    with dissolve

    window show
    th "Теперь можно спокойно идти по своим делам или…"
    "Я выбрал второй вариант и принялся ждать."
    th "Не просто же так она меня здесь заперла."
    "Хотелось выяснить это, и к тому же мне было просто интересно посмотреть на выражение ее лица, когда она увидит, что меня нет."
    "Я спрятался за кустами рядом с домиком и принялся ждать."
    window hide

    with fade

    window show
    "Через некоторое время послышались шаги."
    "К домику подошли Алиса и Ольга Дмитриевна."
    show dv normal pioneer far onlayer master at cleft
    show mt normal panama pioneer far onlayer master at cright
    with dissolve  
    dv "Сейчас все сами увидите!"
    hide dv onlayer master with dissolve
    "Она открыла дверь и вошла…"
    "Но буквально спустя минуту выскочила из домика."
    window hide

    scene cg d4_dv_mt onlayer master
    with dissolve

    window show
    dv "Знаете, я это…"
    "На лице Алисы было такое выражение, как будто она выиграла на соревнованиях по ловле ежей, пришла всем хвастаться медалью, но в последний момент узнала, что это совсем не олимпийский вид спорта."
    mt "Он испарился, получается?"
    "Скептически спросила Ольга Дмитриевна."
    th "Как хорошо, что я закрыл окно после того, как вылез!"
    dv "Да нет…{w} Тут, понимаете…"
    mt "Я все понимаю, Двачевская!"
    mt "Что ты, что соседка твоя – постоянно одно и то же, одно и тоже! Сколько можно уже?!"
    dv "Но ведь правда..."
    mt "Что правда, что? У тебя один рассказ лучше другого. Про Семена в твоем домике, про приставания. Что ты придумываешь постоянно? Вообще ужас."
    "Алиса казалась действительно расстроенной и, что более удивительно, не находила, что сказать."
    "С одной стороны, меня такая ситуация забавляла, но с другой – ее все же было немного жалко."
    "Хотя сама заслужила..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_dv_day onlayer master
    with dissolve

    show dv rage pioneer far at center  onlayer master with dissolve
    window show
    "Наконец вожатая закончила отчитывать ее и ушла."
    "Алиса была вне себя от злости.{w} Она сжала кулаки и вся тряслась, а ее лицо так покраснело, что, казалось, она сейчас лопнет."
    "Я сидел в кустах и тихо посмеивался."
    "Однако мне все же было интересно, что же она замышляла, и, наплевав на страх быть поколоченным, я вышел из своего укрытия."
    me "И что же ты хотела показать вожатой?{w} Меня?"
    show dv surprise pioneer at center onlayer master with dissolve
    "Алиса обернулась и недоуменно уставилась в мою сторону."
    "Впрочем, через секунду недоумение сменилось негодованием."
    show dv rage pioneer at center onlayer master with dspr
    dv "Ты! Ты!"

    stop music fadeout 3

    me "А что я?"

    play ambience ambience_camp_center_day fadein 3

    "Она немного смягчилась."

    if day2_dv_bet == 1:

        if day2_card_result < 3:
            show dv smile pioneer at center onlayer master with dspr
            dv "Хотела тебе вернуть должок."
            "Она ухмыльнулась."
            me "Какой это?"
            dv "Ну, ты же мне проспорил.{w} Вот я и хотела показать вожатой, как ты до меня домогаешься."
            th "Интересно, что такого криминального могла бы найти Ольга Дмитриевна в данной ситуации, но речь не о том…"
            me "Ясно…"

        if day2_card_result == 3:
            show dv angry pioneer at center onlayer master with dspr
            dv "Хотела тебе отомстить!"
            me "За что это?"
            th "Действительно, что я такого сделал этой девочке, чтобы мне еще и мстить…"
            dv "За то, что обыграл меня в карты!"
            th "Важный повод!{w} Без сомнения…"
            me "Ясно…"
    else:

        dv "Потому что ты слабак!"
        me "Это почему же?"
        dv "Потому что побоялся со мной тогда поспорить!"
        me "Когда это?"
        dv "Когда в карты играли!"
        "Серьезная причина…"
        me "Да уж…"

    me "Может быть, мне стоит перед тобой извиниться?"
    "Ехидно спросил я."
    show dv sad pioneer at center onlayer master with dspr
    dv "Да иди ты!"

    play sound sfx_slam_door_campus

    hide dv onlayer master with dissolve
    "Она, хлопнув дверью, вошла в свой домик."
    "Я совсем не обижался на Алису."
    "В конце концов, от нее вполне можно было ожидать чего-нибудь подобного."
    "Тем более все обошлось в общем-то без последствий."
    "И даже более того – удача была на моей стороне, – ее растерянный и смущенный вид доставил мне массу удовольствия."
    "Посмеиваясь, я удалялся от домика Алисы, который чуть не стал для меня смертельной ловушкой."
    window hide

    $ disable_current_zone()
    $ day4_map_necessary_done +=1
    jump day4_map

label day4_main2:

    scene bg black onlayer master
    with dissolve

    window show
    "..."

    stop ambience fadeout 2

    "На обед я шел со смешанными чувствами – выполненного долга и бесцельно потраченных нескольких часов."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "В столовой было, как всегда, многолюдно."
    "Остаться незамеченным не получилось – меня окликнула Ольга Дмитриевна."
    show mt normal pioneer onlayer master at center
    show sl normal pioneer onlayer master at right
    show el normal pioneer onlayer master at left
    with dissolve
    mt "Семен, иди к нам."
    "За четырехместным столом сидели вожатая, Славя и Электроник."
    hide mt onlayer master
    hide sl onlayer master
    hide el onlayer master
    with dissolve
    "Я кивнул головой и отправился за обедом."
    "В этот раз мне пришлось несколько минут постоять в очереди."
    "Сегодняшнее меню мало чем отличалось от предыдущих дней.{w} По крайней мере по внешнему виду блюд."
    show mt normal pioneer onlayer master at center
    show sl normal pioneer onlayer master at right
    show el normal pioneer onlayer master at left
    with dissolve
    "Когда я сел за стол и пожелал всем приятного аппетита, Ольга Дмитриевна сказала:"
    mt "Ну, и что вы думаете?"
    me "О чем?"
    mt "О Шурике же!{w} Уже обед, а его все нет."
    "Я подметил пушкинскую рифму, но не стал акцентировать на этом внимание."
    show sl sad pioneer at right onlayer master with dspr
    sl "Мы обыскали весь лагерь."
    show el upset pioneer at left onlayer master with dspr
    el "Я обошел весь лес поблизости."
    "Ольга Дмитриевна посмотрела на меня."
    me "И я…{w} помогал."
    show mt surprise pioneer at center onlayer master with dspr
    mt "Надо звонить в милицию!"
    me "Может, хотя бы до вечера подождем?"
    "Лениво заметил я."
    me "Домой он поехал, например…"
    mt "Не может быть!{w} Шурик живет отсюда в тысячах километрах."
    me "Ну, так на поезде…"
    mt "До ближайшей станции…"
    "Она замолчала."
    show mt normal pioneer at center onlayer master with dspr
    mt "Далеко…"
    "А вот это было уже интереснее."
    th "Как только разговор заходит о том, как выбраться из «Совёнка», все местные обитатели сразу же пытаются сменить тему."
    me "Далеко – это сколько?"
    mt "Это много."
    "Она посмотрела на меня так, что по ее виду можно было понять, что дальнейшие расспросы неуместны."
    sl "Значит, надо идти глубже в лес… Может, он заблудился!"
    el "У него всегда с собой компас."
    "Вмешался в разговор Электроник."
    "Интересно, что еще можно найти в его чудо-жилетке (если она у него вообще есть)?"
    "Мне бы компас вряд ли помог, заплутай я в лесу…"
    show mt surprise pioneer at center onlayer master with dspr
    mt "И в милицию!{w} В милицию вечером!"
    th "Хотя бы не немедленно."
    me "Ну, до вечера…"
    "Все замолчали."
    me "Еще далеко до вечера, я в этом смысле."
    show mt sad pioneer at center onlayer master with dspr
    mt "Если он правда пропал, то нельзя медлить!"
    show sl serious pioneer at right onlayer master with dspr
    sl "Мы не можем пока этого знать."
    mt "Ну а где он тогда, где он?"
    "В словах вожатой была доля истины – довольно странно вот так «прятаться» целый день."
    "Да и зачем ему это?{w} Все-таки Шурик показался мне вполне серьезным пионером, а такое поведение больше подошло бы Ульянке."
    "Значит, действительно были основания полагать, что он пропал."
    me "В любом случае мы сделали все от нас зависящее, теперь остается только ждать."
    "Славя, Электроник и Ольга Дмитриевна грустно посмотрели на меня, но ничего не сказали."
    "..."
    hide el onlayer master
    hide sl onlayer master
    hide mt onlayer master
    with dissolve

    stop ambience fadeout 2

    "Закончив обедать, я отнес поднос на стол с грязной посудой и вышел из столовой."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    window show
    th "Еще даже не вторая половина дня…"
    th "Чем бы заняться…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Лагерь словно отходил к послеобеденному сну."
    "Только Генда пристально смотрел на меня из-под очков."
    "Конечно, взгляд его был направлен на что-то другое, но мне почему-то казалось, что он следит именно за мной."
    th "Наверняка он знает, куда пропал Шурик.{w} Только вот рассказать не сможет…"
    "Я задумался над исчезновением руководителя кибернетического кружка."
    th "Может быть, оно тоже как-то связано с моей ситуацией?"
    show cs normal at center onlayer master with dissolve
    cs "О, пионер!"
    "Передо мной стояла медсестра."
    "Я вопросительно посмотрел на нее."
    cs "Посиди в медпункте за меня.{w} Мне нужно срочно отойти. Травма у кого-то."
    me "Я?"
    cs "Да, ты!{w} Вот ключи!"

    play sound sfx_keys_rattle

    pause(1)

    hide cs onlayer master with dissolve
    "Медсестра кинула мне ключи и убежала."
    th "Почему именно я?{w} Что, больше никого не нашлось? И что именно я должен делать? А если что-то случится?.."
    th "Но раз уж отказаться не успел, то ничего не поделаешь…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    window show
    "Я стоял перед дверью в нерешительности."
    "Вроде как у меня нет другого выбора, но в то же время эта ситуация была далека от нормальной."
    th "С одной стороны, ничего страшного – посижу здесь полчасика, она вернется…"
    th "Ну, а если кто-то действительно придет за помощью?{w} Со сломанной ногой?{w} Или пробитой головой?"
    "Меня охватило нешуточное волнение."
    "С одной cтороны, в этом лагере, кроме ссадин и синяков, никаких серьезных травм не бывает."

    stop ambience fadeout 2

    "Но в то же время не давала покоя мысль о том, что, случись что, и я окажусь беспомощным."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    "Я даже первую помощь оказывать не умел…"
    "Мое внимание привлек журнал, лежащий у медсестры на столе."
    th "Хороший способ отвлечься.{w} Наверное..."
    "Он назывался «Советская модница»."
    "Год и месяц издания нигде указаны не были."
    "Впрочем, ничего удивительного – здесь случаются и более странные вещи, а про советские журналы я знал всего лишь чуть более, чем ничего, может, на них и не печатали дату выпуска…"

    play sound sfx_open_journal

    "С глянцевых страниц на меня смотрели модели, разряженные в старомодные платья."
    th "Сейчас бы так точно не стали ходить."
    "Я усмехнулся."
    th "Интересно, Славя, например, считает это модным?"
    th "Представляю, что было, если бы она надела нечто подобное и появилась в моем времени…"
    th "Вот иду я с ней под ручку в своем пальто и с капюшоном на голове, а она в пышном платье с рюшечками…"
    "Получается, я уже представляю Славю в моем мире…{w} Вместе со мной…{w} И не только Славю."
    th "Вот это платье больше подойдет Ульяне, вот этот сарафанчик – Алисе, а вот эта юбочка и кофточка – Лене."
    "Действительно, если бы эти девочки были реальными…"
    "Нет, я видел их, слышал их голос, мог даже прикоснуться."
    th "Но они все равно здесь, а я…{w} я просто не принадлежу этому месту."
    th "Оно для меня не реально.{w} Я просто жду возможности выбраться отсюда."
    th "Жду, потому что от меня уже ничего не зависит…"
    "Я вздохнул, положил голову на стол и задремал."
    window hide

    scene bg black onlayer master
    with fade

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with fade

    play sound sfx_open_door_clubs

    window show
    "Меня разбудил шум открывающейся двери."

    play music music_list["everyday_theme"] fadein 3

    show un normal pioneer at center onlayer master with dissolve
    "На пороге стояла Лена."
    if day3_un_dumped:
        th "Ведь я вчера обещал помочь ей в медпункте..."
        "Кровь резко прилила к лицу, и я отвернулся, делая вид, что чем-то занят."
    un "А медсестры нет?{w} Тогда попозже зайду…"
    me "Я за нее!"
    th "Раз на меня возложена обязанность по лечению пионеров, то к делу надо подойти со всей ответственностью."
    "Хотя, на самом деле, я, наверное, просто боялся, что из-за меня что-то случится…"
    me "На что жалуетесь?"
    "Я постарался как можно аккуратнее улыбнуться, чтобы не смутить Лену."
    un "Да ничего такого…{w} Голова немного болит просто."
    me "Сейчас исправим!"
    th "Что-нибудь обезболивающее..."
    "Где какие лекарства лежат, я, конечно же, не знал, поэтому процесс поиска занял порядком времени."
    me "Нашел!"
    "Я протянул Лене таблетку анальгина."
    show un smile pioneer at center onlayer master with dspr
    un "Спасибо…"
    "Она улыбнулась."
    "Это стало для меня неожиданностью, и я несколько выпал из реальности, уставившись на нее."
    show un surprise pioneer at center onlayer master with dspr
    un "Что?"
    "Лена моментально смутилась."
    me "Слушай, а вот интересно, тебе понравилось бы такое?"
    "Не знаю, что на меня нашло, но я схватил со стола журнал и показал ту картинку, где были нарисованы юбка и кофта, которые, как мне показалось, больше всего подошли бы ей."
    "Может быть, из-за мыслей об этих девочках и моем реальном мире у меня окончательно помутился рассудок…"
    "Может быть, я хотел развлечься вместо того, чтобы просто ждать возвращения медсестры…"
    "Лена посмотрела на рисунок."
    show un normal pioneer at center onlayer master with dspr
    un "Да, наверное…"
    me "А сейчас это… модно?"
    show un shy pioneer at center onlayer master with dspr
    un "Наверное…"
    "Она смутилась и покраснела."
    un "А почему ты спрашиваешь?"
    th "Действительно, почему…"
    window hide

    menu:
        "Мне кажется, на тебе это бы смотрелось прекрасно":
            $ day4_un_compl = 1
            $ lp_un = lp_un + 1
            window show
            un "Спасибо…"
            me "Да не за что, я же правду говорю!"
        "Да просто так":
            window show
            un "Ясно…"

    "Некоторое время мы молчали."
    me "Как голова?"
    show un smile pioneer at center onlayer master with dspr
    un "Лучше, спасибо."
    "Она улыбнулась."
    un "Я пойду."
    me "Удачи!"
    hide un onlayer master with dissolve

    stop music fadeout 3

    "Лена вышла, а я сел и принялся дальше листать журнал."
    "..."
    window hide

    with fade

    play sound sfx_knock_door7_polite

    window show
    "Через некоторое время в дверь постучали."
    th "Похоже, все будет не так просто, как казалось."
    "Я внезапно представил себя медсестрой…{w} хотя скорее медбратом…{w} и сказал:"
    me "Войдите!"

    play sound sfx_open_door_clubs

    play music music_list["eat_some_trouble"] fadein 3

    show us normal pioneer at center onlayer master with dissolve
    "Дверь открылась, и я увидел Ульянку."
    me "С каких это пор ты стучишься?"
    show us sad pioneer at center onlayer master with dspr
    us "А что, нельзя?"
    "Она насупилась."
    me "Болит что-то?"
    show us dontlike pioneer at center onlayer master with dspr
    us "А тебе я с какой стати рассказывать должна?{w} Где медсестра?"
    me "Перед тобой."
    "Я вальяжно закинул ногу на ногу и вопросительно посмотрел на Ульяну."
    show us surp1 pioneer at center onlayer master with dspr
    us "Тогда я, пожалуй, пойду.{w} Лучше уж умереть, чем лечиться у тебя."
    "Она ехидно улыбнулась."
    me "Ты даже не пробовала ведь!"
    show us normal pioneer at center onlayer master with dspr
    "Ульяна на мгновение задумалась."
    us "Хотя таблетки можешь и ты мне дать."
    me "А что вас беспокоит?"
    "Она ответила не сразу."
    show us dontlike pioneer at center onlayer master with dspr
    us "Тяжесть в животе…"
    me "А не пустота в голове?"
    "Пробурчал я себе под нос."
    show us surp3 pioneer at center onlayer master with dspr
    us "Чего?"
    me "Ничего, сейчас поищу."
    show us normal pioneer at center onlayer master with dspr
    "В первом же ящике нашлась упаковка но-шпы."
    show us laugh2 pioneer at center onlayer master with dspr
    us "Спасибо вам, доктор!"
    "Она весело улыбнулась."
    "Смотря на Ульянку, я никак не мог понять, как такой жизнерадостный и активный ребенок может испытывать проблемы со здоровьем…"
    window hide

    menu:
        "Небось ворованных конфет объелась?":
            show us dontlike pioneer at center onlayer master with dspr
            window show
            "Она недобро посмотрела на меня."
            us "Нет, все тебе оставила!"
            window hide

            pause(1)

            play sound sfx_slam_door_campus

            hide us onlayer master with dissolve
            window show
            "Ульянка убежала, хлопнув дверью."
            "Наверное, задать такой вопрос было не лучшим решением."
        "В столовой отравилась?":
            $ day4_us_compl = 1
            $ lp_us = lp_us + 1
            window show
            me "Учитывая местную стряпню, это не удивительно."
            show us surp1 pioneer at center onlayer master with dspr
            us "Может быть…"
            "Она ухмыльнулась."
            show us grin pioneer at center onlayer master with dspr
            us "А ты, я погляжу, здоровенький!"
            me "Не жалуюсь…"
            us "Ну, бывай!"
            window hide

            pause(1)

            play sound sfx_slam_door_campus

            hide us onlayer master with dissolve
            window show
            "Ульянка убежала, хлопнув дверью."

    stop music fadeout 3

    "..."
    window hide

    with fade

    window show
    "Я вновь углубился в изучение советских модных тенденций."
    "Время шло, а медсестра так и не возвращалась."
    "В поисках Шурика я не участвовал, разгадок своего положения не искал…{w} Просто сидел и листал журнал."
    "В какой-то момент даже показалось, что такая ситуация меня вполне устраивает…"
    th "В конце концов, пока что все происходящее можно считать чем-то вроде отдыха в летнем лагере, а если ничего не изменится в ближайшее время, тогда уж стоит и волноваться начинать."

    play sound sfx_knock_door2

    "В дверь опять постучали."
    th "Сегодня эпидемия, что ли, какая-то?"

    play sound sfx_open_door_clubs

    play music music_list["my_daily_life"] fadein 3

    show sl normal pioneer at center onlayer master with dissolve
    "На пороге стояла Славя."
    show sl smile pioneer at center onlayer master with dspr
    sl "Ой, привет! А медсестры нет?"
    me "Привет. Нет. Я за нее."
    show sl shy pioneer at center onlayer master with dspr
    sl "Ясно.{w} А мне бы…"
    "Она замялась."
    me "Что?"
    if d1_keys and not d2_gave_keys:
        show sl normal pioneer at center onlayer master with dspr
        sl "Кстати, Семен..."
        "Сказала Славя, внимательно посмотрев на меня."
        me "Что?"
        sl "Я тут недавно свои ключи, кажется, потеряла. Ты не видел?"
        th "И ведь еще как видел!"
        me "Да, вот, я вчера их нашел возле столовой, хотел тебе отдать, но забыл..."
        "Я врал очень неумело – меня выдавал румянец на щеках, бегающие глаза и не находящие себе места руки."
        me "Вот."
        show sl serious pioneer at center onlayer master with dspr
        "Славя взяла ключи, а я уже был готов к любому уместному в данной ситуации наказанию, но она лишь сказала:"
        show sl smile pioneer at center onlayer master with dspr
        sl "Спасибо."
        me "Так зачем приходила?"
        "Нужно было как можно быстрее сменить тему разговора."
        me "Что-то болит?"
        show sl shy pioneer at center onlayer master with dspr
    sl "Да нет, ничего…"
    th "Странно.{w} Всегда такая открытая Славя о чем-то умалчивает?"
    me "Если что, ты говори!{w} Меня сюда и посадили, чтобы лечить всех."
    "Я широко улыбнулся."
    sl "Да нет…{w} То есть да, но нет."
    "После этой фразы деление на ноль для меня стало реальностью."
    me "Ну, так чем могу помочь?"
    show sl smile2 pioneer at center onlayer master with dspr
    sl "Ты?{w} Думаю, ничем."
    "Она улыбнулась и собралась уходить, но вдруг остановилась."
    show sl normal pioneer at center onlayer master with dspr
    sl "Хотя…{w} Можешь выйти на минутку?"
    th "Почему бы и нет?"

    stop ambience fadeout 2

    me "Хорошо…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я вышел из медпункта и облокотился о стену."
    th "Интересно, что она такое там делает, что мне нельзя на это даже смотреть?"
    show sl normal pioneer at center onlayer master with dissolve
    "Через минуту открылась дверь, и вышла Славя."
    "У нее в руках был какой-то небольшой пакетик."
    window hide

    menu:
        "Спросить, что это":
            window show
            me "А что это такое?"
            show sl shy pioneer at center onlayer master with dspr
            sl "Ничего!"
            "Она покраснела."
            sl "Спасибо тебе!"
            me "Да не за что…"
            hide sl onlayer master with dissolve
            "Славя убежала."

            stop music fadeout 3

            th "Кажется, не стоило спрашивать…"
        "Не спрашивать":

            $ day4_sl_compl = 1
            $ lp_sl = lp_sl + 1
            show sl normal pioneer far at center  onlayer master with dissolve
            window show
            me "Удачи!"
            "Крикнул я ей вслед."
            show sl smile2 pioneer far at center onlayer master with dspr
            sl "Спасибо!"

            stop music fadeout 3

            "Одарила она меня напоследок милой улыбкой."
            hide sl onlayer master with dissolve

    window hide

    scene bg black onlayer master
    with dissolve

    stop ambience fadeout 3

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    "Я посмотрел на часы."
    "Время уже приближалось к вечеру, журнал был прочитан вдоль и поперек, а медсестра так и не возвращалась…"

    play sound sfx_open_door_kick

    play music music_list["that_s_our_madhouse"] fadein 3

    show dv normal pioneer at center onlayer master with dissolve
    "Вдруг дверь распахнулась, и в медпункт вбежала Алиса."
    "Она пристально посмотрела на меня."
    dv "А ты что здесь делаешь?"
    me "Сижу…"
    "Честно признался я."
    show dv smile pioneer at center onlayer master with dspr
    dv "Ну и ладно!{w} Так даже лучше, что медсестры нет."
    "Пробормотала она."
    me "Заболела?"
    "Ехидно спросил я."
    "Алиса не ответила и подошла ко мне."
    show dv normal pioneer at center onlayer master with dspr
    dv "Подвинься."
    me "Зачем?"
    dv "Чтобы я ящик смогла открыть, очевидно же!"
    me "Зачем это?"
    "Она разозлилась."
    show dv angry pioneer at center onlayer master with dspr
    dv "Тебе какое дело?"
    me "Ну, я тут вроде как исполняющий обязанности…"
    show dv normal pioneer at center onlayer master with dspr
    "Она задумалась."
    dv "Дай мне тогда активированный уголь!"
    me "Живот болит?"
    show dv grin pioneer at center onlayer master with dspr
    dv "Да."
    "Ехидно усмехнулась она."
    "Я почувствовал, что что-то здесь не так…"
    window hide

    menu:
        "Дать Алисе уголь":
            $ day4_dv_compl = 1
            $ lp_dv = lp_dv + 1
            window show
            th "Но мало ли…{w} Вдруг правда что-то болит."
            me "Ладно."
            window hide

            play sound sfx_open_table

            $ renpy.pause(1)

            window show
            "Я полез в ящик и вытащил оттуда упаковку активированного угля."
            show dv normal pioneer at center onlayer master with dspr
            dv "Спасибо!"
            hide dv onlayer master with dissolve

            stop music fadeout 3

            "Она вырвала ее у меня из рук и убежала."
        "Не давать ей уголь":

            window show
            me "Точно живот болит?"
            dv "Точно-точно!"
            me "Что-то не похоже…"
            show dv angry pioneer at center onlayer master with dspr
            dv "А что, меня здесь разорвать должно, чтобы ты поверил?"
            me "Я не знаю, что можно плохого сделать с активированным углем, но, мне кажется, ты придумаешь…"
            "Она замялась."
            show dv normal pioneer at center onlayer master with dspr
            dv "А даже если так?"
            me "Вот!{w} Я так и думал!{w} Тогда я тебе точно ничего не дам!"
            "Алиса попыталась силой пролезть к ящикам, но я, как Александр Матросов, закрыл грудью амбразуру."
            "При всей ее наглости она все же была девочкой, и оттеснить меня у нее бы никак не получилось."
            show dv angry pioneer at center onlayer master with dspr
            dv "Ну и ладно! В другом месте найду."
            hide dv onlayer master with dissolve
            "Она развернулась и направилась к выходу."
            "В дверях Алиса остановилась и обернулась."
            show dv normal pioneer at center onlayer master with dspr
            dv "Кстати, там вожатая с медсестрой пионера несут, который ногу сломал…{w} Мне-то все равно, но им, наверное, тяжело."
            me "Так я тебе и поверил!"
            dv "Иди сам посмотри…"
            "Казалось, что Алиса врет, но, с другой стороны, пока она была у меня на глазах…"
            hide dv onlayer master with dissolve
            "Я подошел к дверям и выглянул на улицу.{w} Там никого не было."
            show dv normal pioneer at center onlayer master with dissolve
            me "Ну и где?"
            show dv surprise pioneer at center onlayer master with dspr
            dv "Не дошли, значит, еще."
            "Она развела руками."
            show dv smile pioneer at center onlayer master with dspr
            dv "Счастливо!"
            hide dv onlayer master with dissolve
            "Я вернулся к столу и только сейчас обнаружил, что один из ящиков открыт."
            th "Как же она так успела?!"
            th "Всего на секунду отвернулся..."

            stop music fadeout 3

            th "Впрочем, что плохого может выйти из активированного угля…"

    window hide

    scene black onlayer master
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    window show
    "До ужина оставалось минут 15, а медсестры все не было…"
    "Я решил, что вот так уходить не дело."
    th "Все же она меня попросила…"
    th "Да и мало ли что случится, когда я уйду…"
    th "Хотя кому понадобится что-то отсюда воровать?"
    th "Разве что Алисе – активированный уголь…"

    play sound sfx_open_journal

    "Я вновь открыл журнал и принялся листать его по энному кругу."
    "Мода восьмидесятых уже так не забавляла, как вначале."
    "Несколько раз на меня накатывала зевота."
    "На часах было уже шесть, а значит, ужин начался…"
    "Конечно, надо до конца нести свою службу и не покидать пост ни при каких обстоятельствах, но у моего желудка, похоже, на это существовало особое мнение…"
    "Я встал и уверенно направился к выходу."
    "За дверью послышался какой-то шорох."
    th "Неужели опять кто-то отравился, сломал руку или еще что похуже?"

    stop ambience fadeout 2

    play sound sfx_open_door_clubs

    "Я тяжело вздохнул и дернул за ручку."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    window show
    "Однако снаружи никого не было."
    "Похоже, просто показалось…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    window show
    "Я вернулся внутрь и тут же заметил, что в медпункте что-то изменилось."

    play music music_list["mystery_girl_v2"] fadein 3

    "А точнее, на столе появилось яблоко."
    th "Но откуда?"
    "Не могут же фрукты сами собой материализовываться из воздуха?"
    "Хотя в этом лагере возможно все…"
    "Скорее всего, его кто-то просто сюда принес."
    "Возможно, Лена в качестве благодарности."
    th "Ведь она такая стеснительная и…"
    th "Но подождите!{w} Как же она вот так прошла мимо меня?"
    th "Не станет же Лена лезть в окно, в конце концов…"
    th "Значит, здесь что-то другое…"
    "Меня внезапно охватил страх."
    th "А вдруг это яблоко отравлено?!"
    "Хотя зачем идти на такие ухищрения, когда я здесь совершенно беспомощен и убить меня можно гораздо проще?"
    th "Или это яблоко, которое вкусила Ева в саду Эдема?"
    th "Тогда мне точно не стоит его есть!"
    "В ту же секунду живот напомнил о себе, предательски заурчав."
    th "Впрочем, пока я закрою медпункт, пока дойду до столовой, пока возьму еду..."
    "Стенки желудка буквально прилипали к позвоночнику."
    th "Наверное, и ничего страшного…"
    "Я еще раз попытался вспомнить, не лежало ли это яблоко здесь раньше."
    th "В конце концов, откуда-то оно взялось!"
    th "Может быть, залетело в окно?"
    "И действительно, ставня была немного приоткрыта."
    th "Значит, его все-таки кто-то сюда положил."
    th "Получается, ничего страшного нет! Хотя…"
    window hide

    menu:
        "Съесть яблоко":
            $ day4_uv_apple = True
            window show

            play sound sfx_eat_apple

            "Чувство голода все-таки взяло верх, и я с аппетитом принялся грызть спелое зеленое яблоко."
            "На вкус оно казалось вполне обычным."
            th "Впрочем, не думаю, что даже самый сильный яд можно вот так почувствовать."
            th "Хотя что уже сейчас-то говорить…"
        "Не есть":

            window show
            th "Нет!{w} Даже если предположить, что это яблоко вполне обычное, то не стоит есть немытые фрукты!"
            th "Хотя бы так…"
            "Этой мыслью я оправдал свои страхи и отложил яблоко в сторону."

    stop music fadeout 3

    "Пора было выдвигаться на ужин."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show el normal pioneer at center onlayer master with dissolve
    window show
    "По дороге меня догнал Электроник."
    me "Как поиски Шурика?"
    show el upset pioneer at center onlayer master with dspr
    el "Да все так же…"
    me "Ты не расстраивайся…{w} Найдется он!"
    "Я попытался как-то подбодрить его."
    el "Все же долго его нет…{w} Пойду искать дальше."
    me "А как же ужин?"
    el "Это важнее."
    "Глубокомысленно изрек он."
    hide el onlayer master with dissolve
    "На перекрестке наши дороги разминулись, и я пожелал ему удачи."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    window show
    "У столовой было, как всегда, многолюдно."
    "Я ускорил шаг, чтобы хоть сегодня оказаться не последним."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "И мне повезло – в дальнем углу остался полностью свободной столик."
    "Я быстро взял еду и сел."
    "Сегодня на ужин давали фруктовый суп и несколько булочек."
    "Такой набор блюд меня весьма удивил, а после дегустации даже порадовал."
    "Я принялся сосредоточенно есть."
    mi "Лена, давай сюда! Смотри – целых три стула!"
    show un normal pioneer onlayer master at left
    show mi normal pioneer onlayer master at center
    with dissolve
    "Передо мной стояли Лена и Мику."
    un "Тут свободно?"
    "Поинтересовалась Лена."
    me "Да, садитесь…"
    th "Лучше бы, конечно, чтобы она была одна."
    un "Спасибо…"
    show mz normal glasses pioneer at right onlayer master with dissolve
    "Только и успела сказать Лена, как из-за ее спины появилась Женя с подносом."
    mz "Я сяду тут.{w} Больше некуда."
    "Не дождавшись моего ответа, она поставила поднос на стол и села."
    me "Конечно, располагайтесь..."
    "Грустно пробурчал я себе под нос."
    show mz angry glasses pioneer at right onlayer master with dspr
    mz "Что?!"
    me "Ничего..."
    show mz normal glasses pioneer at right onlayer master with dspr
    "Честно говоря, я бы с удовольствием сократил эту компанию до одной Лены, но в то же время ни Мику, ни Женя не доставляли мне каких-то особых проблем."
    "Одна разве что говорливая слишком, другая – мнительная."
    th "Но все равно они обе абсолютно безвредны по сравнению с некоторыми."
    show un surprise pioneer at left onlayer master with dspr
    un "Ой, я ключ, кажется, забыла…"
    show mi smile pioneer at center onlayer master with dspr
    mi "Ничего страшного, возьми мой!"
    show un normal pioneer at left onlayer master with dspr
    "Я даже удивился, что Мику ограничилась такой короткой фразой…"
    me "А вы…{w} вместе живете?"
    mi "Да, конечно! А ты не знал? Вместе. Наш домик самый крайний. То есть самый дальний от столовой. Ну, то есть самый последний."
    "Я бы не удивился, если бы узнал, что Лена живет со Славей.{w} С Женей на худой конец.{w} Да хоть с Электроником."
    th "Но молчаливая и застенчивая Лена и не в меру словоохотливая Мику…{w} Да, это сюрприз!"
    show mi normal pioneer at center onlayer master with dspr
    mz "Нашли своего Шурика?"
    "Я посмотрел на Женю."
    "Странно, что ее вообще волнуют чужие проблемы."
    me "Нет."
    show mz angry glasses pioneer at right onlayer master with dspr
    mz "Небось в деревню убежал за сигаретами.{w} Или за водкой."
    "Она фыркнула."
    me "В деревню?"
    "С этой самой секунды разговор начал живо меня интересовать."
    show mz bukal glasses pioneer at right onlayer master with dspr
    mz "А что такого?"
    "Женя сделала удивленное лицо."
    me "Значит, здесь есть поблизости деревня?"
    show mz normal glasses pioneer at right onlayer master with dspr
    mz "Наверное…"
    "Сказала она неуверенно."
    "Я посмотрел на Лену и Мику, но они были заняты едой и не обращали внимания на наш разговор."
    me "То есть ты точно не знаешь?"
    show mz angry glasses pioneer at right onlayer master with dspr
    mz "Да какое мне дело!"
    "Женя сконцентрировалась на супе."
    me "Но здесь же должны быть какие-то населенные пункты поблизости?"
    show mz angry glasses pioneer at right onlayer master with dspr
    mz "Слушай..."
    me "Слушаю."
    mz "Не знаю я! Дай спокойно поесть."
    show mz normal glasses pioneer at right onlayer master with dspr
    th "Похоже, больше от нее ничего не добиться."
    "Хотя, может быть, она правда не знает..."

    stop ambience fadeout 2

    "Все оставшееся время пришлось слушать, как Мику говорит о каких-то малозначительных вещах, и тихо сходить с ума…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    $ sunset_time()

    window show
    "Так что, выйдя на улицу, я вздохнул с облегчением."
    "Солнце уже садилось."
    th "Можно немного прогуляться..."
    th "Вряд ли сам найду какое-то занятие на вечер, а так, может, что интересное подвернется…"

    play sound sfx_muffled_explosion

    play music music_list["doomed_to_be_defeated"] fadein 3

    "Подходя к площади, я услышал какой-то хлопок.{w} Похоже, что-то взорвалось."
    "Меня словно парализовало."
    th "Я нахожусь во враждебной среде – неизвестно, что там и как…"
    th "Лучше убежать!{w} Но в то же время все же интересно…"
    "Наверное, я бы так и стоял здесь, если бы кто-то не схватил меня за руку."
    show mt normal pioneer at center onlayer master with dissolve
    "Это была Ольга Дмитриевна."
    mt "Чего стоишь?{w} Пойдем разберемся, что там произошло!"
    me "А без меня никак?"
    "Жалобно взмолился я."

    stop music fadeout 3

    show mt surprise pioneer at center onlayer master with dspr
    mt "Да ничего там страшного не должно быть!{w} По идее…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    play music music_list["you_won_t_let_me_down"] fadein 3

    window show
    "Когда мы вышли на площадь, там уже столпились пионеры."
    "Ольга Дмитриевна, решительно расталкивая всех, подошла к месту взрыва."
    "Судя по всему, взрывали Генду."
    "Но у злоумышленников ничего не вышло – памятник устоял."
    "Лишь на пьедестале были видны еле заметные следы копоти."
    show mt angry pioneer at center onlayer master with dissolve
    mt "Ну, и кто это сделал?"
    "Она оглядела толпу пионеров."
    "Понятно, что это не был террористический акт, совершенный группой лиц по предварительному сговору."
    "Они все просто пришли сюда посмотреть, что произошло."
    "В толпе я увидел Ульяну и Алису.{w} Похоже, заметила их и вожатая."
    mt "Вы двое, ко мне!"
    "Они запротестовали, но все же подошли."
    show us surp2 pioneer onlayer master at right
    show dv normal pioneer onlayer master at left
    with dissolve
    us "А что сразу я?"
    dv "Если вы считаете…"
    mt "Двачевская! Покажи-ка руки!"
    show dv surprise pioneer at left onlayer master with dspr
    dv "А что с ними не так?"
    "Я пригляделся и увидел, что руки Алисы были измазаны чем-то черным."
    mt "Теперь понятно…{w} Из чего бомбу делала?!"
    show dv normal pioneer at left onlayer master with dspr
    "Алиса, кажется, раздумывала, сознаваться или нет, но потом гордо выпалила:"
    show dv smile pioneer at left onlayer master with dspr
    dv "Активированный уголь, селитра и сера!"
    if day4_dv_compl != 1:
        th "Стоп!{w} Уголь!{w} Уголь, который она украла из медпункта."
    mt "И почему именно памятник?{w} Чем тебе помешал уважаемый, заслуженный человек? Борец за права…"

    if day4_dv_compl == 1:
        show dv normal pioneer at left onlayer master with dspr
        dv "Уголь, кстати, он мне дал."
        "Она показала пальцем в мою сторону, и тут же вся толпа уставилась на меня."
        "Мысли о том, что такой маленькой бомбочкой памятник не взорвать и лучше бы ей выбрать для своего теракта более подходящий объект, сразу же вылетели у меня из головы."
        me "Она украла!{w} Я тут ни при чем!"
        mt "Даже если и дал, я уверена, что Семен не стал бы участвовать в столь омерзительном антиобщественном акте!"
        me "Да-да, именно!"
        "Подтвердил я."
        "..."
    else:

        show dv angry pioneer at left onlayer master with dspr
        "..."

    stop music fadeout 3

    "Не знаю, сколько бы она еще продолжала отчитывать Алису, но на площадь выбежал Электроник и закричал:"
    hide dv onlayer master
    hide us onlayer master
    hide mt onlayer master
    with dissolve
    show el smile pioneer at center onlayer master with dissolve
    el "Нашел! Нашел!"
    "Все повернулись в его сторону."
    "В руке у него я заметил ботинок."
    el "Вот!"
    "Он победоносно потряс им надо головой."

    play music music_list["into_the_unknown"] fadein 3

    el "Это ботинок Шурика!"
    show mt normal pioneer at right onlayer master with dissolve
    mt "Так, успокойся!{w} Расскажи подробно, где ты его нашел!"
    show el normal pioneer at center onlayer master with dspr
    el "В лесу.{w} На тропинке в старый лагерь!"
    "По рядам прошел какой-то шепот."
    all "Старый лагерь… Старый лагерь…"
    show mt surprise pioneer at right onlayer master with dspr
    mt "Ты уверен?"
    el "Абсолютно!"
    me "А что такого в этом старом лагере?"
    "Вмешался я в разговор."
    mt "Да ничего такого на самом деле…"
    "Она запнулась."
    el "Одна из легенд «Совёнка» гласит, что там живет приведение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
    show us laugh pioneer at left onlayer master with dissolve
    us "Сделала харакири кухонным ножом.{w} А мальчика этого на следующий день сбил автобус…"
    "Я не заметил, как подошла Ульяна."
    me "Автобус?"
    "Я еле удержался, чтобы не спросить о номере маршрута."
    el "Но наука не верит в привидений, поэтому опасаться там нечего!"
    show mt normal pioneer at right onlayer master with dspr
    mt "Все равно кто-то должен туда пойти!"
    "Ряды пионеров внезапно начали редеть."
    sl "Ольга Дмитриевна, ночь уже почти! Может, завтра?"
    hide us onlayer master
    hide el onlayer master
    hide mt onlayer master
    with dissolve
    show sl normal pioneer onlayer master at right
    show un normal pioneer onlayer master at center
    with dissolve
    "Я обернулся и увидел Славю с Леной."
    mt "А если ночью…{w} ночью с ним что-нибудь случится…{w} Нет! Сегодня! Сейчас!"
    me "Кстати, а где это?"
    "Электроник примерно объяснил дорогу и рассказал про историю старого лагеря."
    show mt normal pioneer at left onlayer master with dissolve
    "Вожатая пристально посмотрела на меня."
    me "Если вы думаете, что я…"
    mt "Ты один здесь остался из мужчин."
    "Я оглядел площадь."
    th "И правда ведь…{w} Электроник куда-то слинял!"
    "Однако мне все равно совершенно не хотелось ночью слоняться по лесу в одиночку."
    "Если бы можно было выбирать, я бы..."
    window hide

    menu:
        "Пошел с Алисой":

            if day4_dv_compl == 1:
                window show
                jump day4_dv
            else:
                window show
                "Но кого я обманываю?{w} С чего вдруг ей идти со мной?.."
                jump day4_fail
        "Пошел со Славей":


            if day4_sl_compl == 1:
                window show
                jump day4_sl
            else:
                window show
                th "Согласится ли она?."
                "Я посмотрел на Славю."
                "Она не обращала на меня внимания."
                th "Похоже, не судьба..."
                jump day4_fail
        "Пошел с Ульяной":


            if day4_us_compl == 1:
                window show
                jump day4_us
            else:
                window show
                th "Хотя, наверное, и ее жажда приключений имеет свои пределы."
                jump day4_fail
        "Пошел с Леной":


            if day4_un_compl == 1:
                window show
                jump day4_un
            else:
                window show
                "Хотя глупо думать, что Лена не испугается."
                jump day4_fail
        "Пошел один":

            window show
            jump day4_fail

label day4_fail:

    me "Я же не пойду туда один?!"
    "Ольга Дмитриевна призадумалась."

    stop music fadeout 3

    mt "Пожалуй, ты прав…{w} Тогда завтра с утра пойдем все вместе."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    window show
    "Мы постояли некоторое время молча и разбрелись кто куда."
    "Я с вожатой направился в сторону ее домика."
    "У меня никак из головы не выходила мысль о том, что мог Шурик делать в старом лагере."
    "Он увлекался роботами и кибернетикой, а не страшными историями и привидениями."
    th "И почему он потерял один ботинок?.."
    "Некоторое время назад я решил занять выжидательную позицию, пока что-нибудь не случится…"
    "И сейчас до меня дошло, что вот оно!"
    show mt normal pioneer at center onlayer master with dissolve
    me "Ольга Дмитриевна, я, пожалуй, прогуляюсь перед сном немного…"
    mt "Ладно, только недолго!"
    me "Хорошо!"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    window show
    "Дойдя до площади, я понял, что ночью шляться по лесу, заброшенному лагерю и черти где еще, может быть, и не так страшно…"
    "Но делать это в темноте…"
    "Возвращаться в домик Ольги Дмитриевны мне совсем не хотелось, а фонарик достать было необходимо."
    "Тут я вспомнил, что видел его в одном из ящиков в медпункте."
    th "Как же хорошо, что я там не только читал журнал мод!"
    window hide

    scene bg black onlayer master
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with fade

    window show
    "Фонарик действительно нашелся, и через пару минут я уже вновь стоял на площади, собираясь с силами."
    "Мне оставалось только принять последнее волевое решение и отправиться в лес."
    "Мимо палаток пионеров, по лесной тропинке к заброшенному лагерю..."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    window show
    "Я двинулся в путь."
    "По рассказам Электроника, старое здание построили сразу после войны."
    "Оно было похоже на детский сад (или на барак, как я предполагал) и рассчитано на куда меньшее число пионеров, чем вмещал нынешний лагерь."
    "Забросили же его лет двадцать назад…"

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    window show
    "Уже совсем стемнело…"
    "Ночной лес был совершенно не похож на дневной."
    "За каждым деревом скрывались таинственные тени, отовсюду слышались какие-то шорохи и крики ночных птиц, а под ногами предательски хрустели ветки."
    "Светила полная Луна, так что стоило поберечь батарейку в фонаре – наверняка она мне еще пригодится."
    "Чем дальше я продвигался, тем больше мне в голову лезли всякие неприятные мысли."
    "Нет, я совсем не боялся темноты, не верил в привидений и прочую мистическую чепуху, но при этом за последние несколько дней я столкнулся с таким количеством необъяснимых явлений, что поневоле начал видеть подвох даже в простых вещах."
    "Тем более некомфортно было мне в ночном лесу."
    "Куда ни посмотри, каждая тень, каждое дерево или кустарник представлялись причудливыми созданиями, сбежавшими из фильмов ужасов или рассказов Стивена Кинга."
    "Ветка в темноте казалась рукой, которая норовит схватить тебя за плечо; лежащее бревно – трупом человека, который так и не смог выбраться из чащи; а в каждом небольшом овражке виделась бездонная пропасть."
    "Если бы я попал в этот лес при других обстоятельствах, без всех этих автобусов и пионерлагерей, мне, конечно, тоже было бы не по себе, но тогда бы я смог рационально объяснить все происходящее и понять, что бояться здесь, кроме сов и мышей, нечего."
    "Но сейчас причин для страха было предостаточно."

    stop music fadeout 3

    "Но несмотря на все свои опасения до старого лагеря я добрался без приключений."

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    play music music_list["sunny_day"] fadein 5

    window show
    "На небольшой полянке со всех сторон окруженное деревьями стояло здание, больше напоминающее детский сад."
    "Краска со стен облезла, в окнах почти не осталось стекол, кое-где порушилась кладка, а на крыше местами зияли пробоины словно от бомбежки."
    "Перед зданием раскинулся небольшой садик, огороженный заржавевшим забором."
    "Похоже, когда-то это была детская площадка – там стояли карусель, качели, горки и прочие советские аттракционы."
    "Все они, конечно же, были серьезно потрепаны временем – изуродованы коррозией и изломаны."
    "Довершала картину трава, которая разрослась так, что доходила мне до пояса."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve2

    window show
    "Луна выглянула из-за туч и осветила старый лагерь."
    "Мне показалось, что все вокруг ожило: в окнах появились стекла, на стенах – свежая краска."

    play sound sfx_ghost_children_laugh

    "Я услышал задорный смех, увидел полупрозрачных детей, весело резвящихся и бегающих по двору, строгую вожатую на крыльце, держащую в руках корзину со спелыми яблоками, уборщицу Бабу-Маню, дремлющую в теньке."
    "У меня мурашки побежали по спине."
    "Конечно, все это было плодом моего воображения, но сам этот лагерь настолько похож на все постапокалиптические картины, которые приходилось видеть в жизни, что померещиться может всякое."
    "Я довольно долго стоял на месте, но все же решился идти дальше."
    th "В конце концов, надо искать Шурика!"
    th "Только вот непонятно, что он тут забыл…{w} И здесь ли он вообще…"
    th "Ботинок в лесу рядом с этим местом – это еще ничего не значит…"
    "Впрочем, если его не съели волки (а мне почему-то казалось, что волков в этом лесу нет), то, скорее всего, он здесь."
    "Я аккуратно прошел через двор, раздвигая руками высокую траву и стараясь не напороться на какую-нибудь железку."
    "На крыльце я остановился в нерешительности."
    "Изнутри на меня смотрела непроглядная тьма."
    "Даже яркий лунный свет не вылавливал ни одного предмета, ни одного контура."
    "В голову начали лезть мысли о том, чтобы дальше не ходить и спешно покинуть это место."

    stop ambience fadeout 2

    "Но я собрался с силами, включил фонарик и шагнул через порог."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_old_building_night onlayer master
    with dissolve

    window show
    "Внутри здание напоминало типичный детский сад."
    "У меня еще остались воспоминания из детства, так что все тут было знакомо."
    "Спальная комната с рядами кроватей, тесно прилегающих друг к другу, большая игровая, туалеты, столовая и подсобные помещения."
    "Повсюду виднелись истлевшие следы былой детской радости – иногда фонарь выхватывал из темноты полусгнившую куклу или пластмассовую машинку, проколотый резиновый мячик или разбитый строй оловянных солдатиков."
    "На столе лежала выцветшая от старости книга."
    "Я пролистал несколько страниц."
    "Это была сказка, которую мне читали в глубоком детстве.{w} Что-то про войну…"
    "Враги разрушили детский сад, и все его обитатели вместе с несколькими взрослыми укрылись в небольшом подвальчике, а в это время над ними взрывались бомбы…"
    "Чем закончилось, не помню, но вроде бы никто не умер…"
    "Посмотрев на иллюстрации, я сразу вспомнил все те эмоции, которые вызвала у меня эта книжка тогда – страх, грусть, сочувствие бедным детям и ощущение безысходности."
    "Было довольно странно, что именно здесь, именно при таких обстоятельствах я нашел именно эту сказку."
    th "Все-таки, наверное, кто-то управляет всем происходящим, пишет сценарий к этой нелепой пьесе, шьет костюмы местным пионерам и рисует декорации на манер этого заброшенного лагеря."
    th "Надо заметить, что этот некто весьма талантлив – пристальное внимание уделено даже малейшим деталям."
    "Хотя это место и было заброшено давно, все здесь казалось нетронутым."
    "Конечно, время не пощадило лагерь, но ведь за столько лет наверняка сюда должны были не раз наведываться люди."
    "Тут просто идеальное место для молодежи пубертатного периода – можно, не опасаясь никого, распивать различные спиртные напитки, предаваться любовным утехам да и просто все здесь сжечь ради забавы."
    "Электроник упоминал, что о заброшенном лагере ходят всякие легенды…{w} Что здесь живут привидения, черти..."
    "Одна история с самоубийством вожатой чего стоит."
    "При обычных обстоятельствах никогда бы не поверил, что это может кого-то остановить…{w} Но в этой реальности возможно все."
    "Конечно, я довольно сильно боялся, но решил, что, раз уж пришел, надо дело довести до конца."
    window hide

    with fade

    window show
    "Здание было небольшим, так что осмотреть его полностью не составило труда."
    "Однако никаких следов Шурика здесь найти не удалось."
    th "Может быть, стоит покричать?"
    th "Хотя, с другой стороны, это не самая лучшая идея."
    "Расстроенный, я сел на скамейку в холле и вздохнул."
    me "Приведения, где же вы?"
    "Спросил я лагерь."
    "И тут в глаза мне бросилось какое-то непонятное углубление в углу."
    "При ближайшем рассмотрении это оказался приоткрытый люк."
    "Причем похоже было, что открыли его недавно, так как пыль вокруг была расчищена."
    "Вот тут я уже по-настоящему испугался."
    th "Получается, Шурик полез куда-то…"
    th "Что может скрываться там внизу?{w} Подвал?{w} И что ему там понадобилось?"

    play sound sfx_open_metal_hatch

    "Я полностью открыл люк и направил во тьму луч фонаря."
    "Вниз на пару метров уходила лестница, упирающаяся в бетонный пол."
    "Кажется, там был какой-то узкий коридор."
    "Я долго думал, что делать дальше."
    "С одной стороны, у меня не было совершенно никакого желания лезть туда, с другой – если Шурик и правда там…"
    "Я громко выругался вслух и начал спускаться."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Внизу было настолько темно, что даже фонарь не сильно помогал."
    "Низкий потолок, провода, тянущиеся вдоль стен, разбитые лампы, закованные в железные прутья…"
    window hide

    scene cg d4_catac onlayer master
    with dissolve

    window show
    th "Где-то все это уже было..."
    "Я медленно начал продвигаться вглубь подземелья."
    "Дорога уходила вниз, а через десяток метров пошли крутые высокие ступеньки."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "Вскоре я оказался перед массивной металлической дверью."
    "На ней был нарисован какой-то значок."
    "Присмотревшись, я понял, что он обозначает радиационную опасность."
    th "Неудивительно, если этот лагерь построили после войны и просуществовал он годов до семидесятых."
    th "Значит, это обычное бомбоубежище и бояться здесь нечего…"
    "Впрочем, от этих мыслей страх никуда не исчез."
    "Я решился и с трудом открыл дверь..."
    window hide

    scene black onlayer master
    with dissolve

    play sound sfx_metal_door_large_close_basement

    $ renpy.pause(1)

    window show
    "...которая тут же с резким звуком захлопнулась, как только я переступил порог."
    "От этого меня передернуло так, что руки начали трястись, а в глазах потемнело."
    "Пришел в себя я лишь через минуту и только тогда понял, что к двери, видимо, приделана какая-то пружина."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    with dissolve

    window show
    "Я оказался в довольно просторной комнате."
    "В свете фонаря виднелась двуспальная кровать, какие-то шкафы вдоль стен, а дальнем углу – непонятного назначения приборы."
    "По всему создавалось ощущение, что этим бомбоубежищем никто никогда не пользовался…"
    "Даже и не заходил сюда…{w} Вплоть до того, что кровати были застелены."
    "Что само по себе странно…"
    "Я несколько раз обошел комнату и внимательно все осмотрел."
    "В шкафах лежали противогазы, костюмы химической защиты, сухпайки, различная бытовая мелочевка."
    "Приборы, назначения которых я вначале определить не смог, оказались измерителями радиации, давления воздуха и температуры."
    "В общем, это было вполне такое типичное бомбоубежище."
    "Именно таким я себе его и представлял, хотя, конечно, ни разу в подобном месте не был."
    "Неизученной осталась только дверь в дальнем конце комнаты."

    play sound sfx_metal_door_handle_rattle

    "Я потянул за ручку, но она не открывалась."
    th "Если кто-то недавно спустился сюда, и здесь его не найти, то логично предположить, что он с той стороны."
    "Я шепотом позвал:"
    me "Шурик?.."
    "Ответа не последовало."
    th "Может быть, он заперся…{w} Но зачем?"
    "Что делать дальше, было непонятно."
    "С одной стороны, можно вернуться и завтра привести помощь, но мне почему-то казалось, что за этой дверью скрыты ответы, которые не будут ждать."
    "Я еще раз прошелся по комнате и взял стоявшую в углу фомку."

    play sound sfx_insert_crowbar_door

    "Ей я подцепил дверь снизу и попытался сорвать ее с петель."
    "Как ни странно, спустя некоторое время мне это удалось, благо она была не такой массивной, как предыдущая."
    window hide

    play sound sfx_fall_metal_door

    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living_nodoor onlayer master
    with vpunch

    window show
    "Дверь поддалась и с грохотом упала."
    "Я отдышался и посветил фонарем в проход."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Куда-то вдаль уходил узкий коридор, такой же, как тот, по которому я попал сюда."
    "..."
    window hide

    with fade

    window show
    "Стены становились уже, потолок уже буквально давил на макушку, а конца все не было видно."
    "Шел я аккуратно, тщательно смотрел под ноги, и, наверное, только это спасло меня от того, чтобы не провалиться в яму…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "Отверстие было примерно метр в диаметре, а на дне вместо бетона виднелась земля."
    "Похоже, дыра образовалась от взрыва."
    th "Глубина не такая большая – потом можно вполне выбраться."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play sound sfx_jump_into_hole_2

    pause(1)

    window show
    "Спрыгнув в дыру, я оказался в каком-то подобии шахтерского штрека."
    "Стены и потолок были укреплены деревянными балками."
    "Туннель уходил настолько далеко вперед, что не хватало света фонаря…"

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "Через пару минут я оказался на развилке…"
    "Идти дальше было опасно – существовала реальная возможность заблудиться."
    "Я решил, что неплохо будет как-нибудь обозначить место, с которого придется начать путь в лабиринт, взял с земли камень и сделал довольно большую зарубку на стене."
    th "Что же..."
    window hide

label fail_mine_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    menu:
        "Налево":
            jump fail_mine_4_1
        "Направо":
            jump fail_mine_2

label fail_mine_1_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Я вернулся к тому месту, с которого и начинал."
    th "Значит, где-то не там повернул."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            jump fail_mine_4_1
        "Направо":
            jump fail_mine_2

label fail_mine_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_3
        "Направо":
            jump fail_mine_room

label fail_mine_2_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump fail_mine_1_1
        "Направо":
            jump fail_mine_3

label fail_mine_2_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_room
        "Направо":
            jump fail_mine_1_1

label fail_mine_room:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface onlayer master
    with fade

    if mr1 >= 1:
        window show
        "Здесь я уже был."
        window hide
        jump fail_mine_2_1

    window show
    "Наконец я вышел из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным моим спасением был фонарик…"
    "Сломайся он, и я вряд ли когда-нибудь выйду отсюда…"
    "Именно в его свете я заметил в углу какую-то красную тряпку."
    "Пионерский галстук!"
    "Теперь-то я точно был уверен, что Шурик здесь."
    me "Шурик! Шурик!"
    "Ответом мне стало лишь эхо."
    th "Но куда он мог уйти?"
    "Отсюда не было другого выхода…"
    th "Конечно, возможно, в этих туннелях есть еще места, где я не бывал…"
    th "Значит, придется искать дальше!"
    window hide

    $ mr1 = mr1 + 1

    jump fail_mine_2_1

label fail_mine_3:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_5
        "Направо":
            jump fail_mine_6

label fail_mine_3_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_6
        "Направо":
            jump fail_mine_2_2

label fail_mine_5:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_4
        "Направо":
            jump fail_mine_6

label fail_mine_5_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_6
        "Направо":
            jump fail_mine_3_1

label fail_mine_4:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_1_1
        "Направо":
            jump fail_mine_7

label fail_mine_4_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump fail_mine_7
        "Направо":
            jump fail_mine_5_1

label fail_mine_4_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump fail_mine_5_1
        "Направо":
            jump fail_mine_1_1

label fail_mine_7:

    if prologue == 0 and d1_keys and day2_cards_with_sl == 0 and day4_mi_accept == 1 and not day4_uv_apple:

        $ persistent.sprite_time = "night"
        scene bg int_mine onlayer master
        with fade

        window show
        "Я шел и шел..."
        "Казалось, что этим туннелям нет конца, словно меня заперли в лабиринте Минотавра, и скоро появится ужасное чудовище..."
        "Сил оставалось все меньше, и я с трудом опустился на землю, облокотившись о влажные стены шахты."
        th "Где же этот чертов Шурик?.."
        th "И сколько я уже времени здесь брожу?"
        "Глаза начали закрываться сами собой."
        th "Разве что минутку..."
        window hide

        scene black onlayer master
        with fade3

        stop music fadeout 3

        stop ambience fadeout 2

        $ renpy.pause(3)

        $ backdrop = "epilogue"

        jump epilogue_mi

    if prologue == 1 and not d1_keys and day3_got_fail == 1 and day4_uv_apple:
        if mr3 >= 1:

            $ persistent.sprite_time = "night"
            scene bg int_mine onlayer master
            with fade

            window show
            "Я опять попал в то место, где увидел эту странную ушастую девочку."
            "Но в этот раз ее тут уже не было."
            window hide

            jump fail_mine_4_2
        else:
            jump day4_uv

    if mr2 >= 1:

        $ persistent.sprite_time = "night"
        scene bg int_mine_halt onlayer master
        with fade

        window show
        "Здесь я уже был."
        window hide

        jump fail_mine_4_2

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt onlayer master
    with fade

    window show
    "Я вышел к некоему подобию шахтерского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовал, что выход где-то рядом, поэтому отправился дальше."
    window hide

    $ mr2 = mr2 + 1

    jump fail_mine_4_2

label fail_mine_6:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door onlayer master
    with fade

    window show
    "За последним поворотом из темноты показалась дверь."
    window hide

    play sound sfx_open_door_mines

    pause(1)

    stop ambience fadeout 3

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    window show
    "Я открыл ее и оказался в небольшой комнате."
    "Она была совершенно пустой, не считая…"
    window hide

    scene cg d4_sh_sit onlayer master
    with dissolve

    window show
    "Шурика, который сидел в углу!"
    me "Шурик!"
    "Он посмотрел на меня."
    "Его глаза были полны ужаса."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    show sh rage pioneer at center onlayer master with dissolve    
    window show
    sh "ААА! Не подходи!"
    me "Шурик, это же я! Семен!"
    sh "Я так просто не дамся!"

    play sound sfx_armature_swish

    "Он достал из-за спины кусок арматуры и принялся размахивать им!"
    me "Шурик, ты что?! Успокойся!"
    sh "Сначала сюда меня загнали! Потом по шахте водили! А теперь Семеном прикидываетесь!"
    th "Похоже, у него окончательно поехала крыша…"
    me "Шурик! Успокойся! Никто мной не прикидывается! Это я и есть!"
    "Я старался говорить как можно спокойнее, но сам волновался едва ли не больше него."
    show sh scared pioneer at center onlayer master with dspr
    sh "Семен?"
    "Он прищурился."
    sh "Правда ты?"
    me "Да! А теперь расскажи, что случилось? Как ты здесь оказался?"
    "Шурик отдышался и начал рассказ."
    show sh normal pioneer at center onlayer master with dspr
    sh "Мне нужны были кое-какие детали для робота.{w} И я слышал, что в старом лагере есть бомбоубежище…{w} А в нем могут быть всякие приборы."
    sh "Вот с утра пораньше и пошел…"
    "Он помолчал минуту, унимая дрожь в руках."
    show sh scared pioneer at center onlayer master with dspr
    sh "Детали я нашел, но потом…"
    "В его глазах читался животный страх."
    sh "Голоса… Они сказали мне пойти сюда… Я спустился в шахту… Потом они говорили идти направо, налево, направо, налево, направо, налево…"
    show sh laugh pioneer at center onlayer master with dspr
    "Он истерически захохотал."
    sh "Но теперь я им не дамся! Я буду сидеть здесь! Они меня тут не найдут!"
    "Он потряс арматурой над головой."
    me "Шурик… Нет там никого… Я тоже прилично поплутал по шахте, но никаких голосов не слышал."
    "Он пристально посмотрел на меня."
    show sh rage pioneer at center onlayer master with dspr

    stop music fadeout 2

    sh "Значит, ты с ними заодно!"
    window hide

    scene cg d4_sh_stay onlayer master
    with dissolve

    play music music_list["pile"] fadein 1

    window show
    "Он кинулся на меня."
    "Я только и успел, что увернуться."
    window hide

    play sound sfx_break_flashlight

    with vpunch

    pause(1)

    window show
    "Шурик по мне не попал, а вот фонарю повезло меньше – весь удар он принял на себя."
    window hide

    scene bg black onlayer master
    with dissolve

    window show
    "Мы остались в кромешной темноте."
    "Теперь уже и у меня начала ехать крыша…"
    me "Ты что наделал, идиот?!"
    "Я отмахнулся рукой в ту сторону, где предположительно был Шурик, но безуспешно."
    me "Теперь мы тут вдвоем сдохнем!"
    "Ответом мне стало лишь молчание и тихий истерический смех."

    stop music fadeout 3

    sh "Ничего… Ничего…{w} Я знаю, где выход! Иди за мной!"
    me "Куда это за тобой?! Я ни черта не вижу!"
    sh "На мой голос."
    "Выбора не было…"
    sh "Сюда…"
    "Голос Шурика прозвучал чуть дальше."
    me "А откуда ты знаешь, куда идти?"
    sh "Я здесь все исходил…"
    me "Почему тогда не ушел?"
    sh "Голоса…{w} Тихо! Они могут услышать!"
    "В принципе, я мог поверить в то, что здесь действительно есть какие-то потусторонние силы."
    "В лагере «Совёнок» подобным вещам удивляться не принято."
    "Но пока что я решил не паниковать."
    "Хотя руки тряслись не переставая."
    sh "Сюда…"
    "Я медленно шел за его голосом и вскоре потерял счет времени."
    "Может быть, мы плутали несколько минут, может быть, несколько часов…"
    "Наконец вдали забрезжил лучик света."
    sh "Пришли…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_exit onlayer master
    with dissolve

    window show
    "Мы уперлись в стену.{w} Под потолком была решетка."
    "Я подтянулся и по кусочкам пейзажа понял, что мы находимся под площадью."
    me "Подсади меня!"
    "Шурик покорно выполнил мое требование."
    "Я принялся колотить по решетке кулаками так сильно, что через пару ударов они все были разбиты в кровь…"
    "Но решетка поддалась и отогнулась…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Через минуту мы уже выбрались на поверхность за памятником Генде."
    "Когда я раньше видел эту решетку, то как-то даже на задумывался, что за ней могут скрываться катакомбы…"
    "Я обессилено рухнул на траву."
    show sh laugh pioneer at center onlayer master with dissolve   
    sh "Они придут за тобой!"
    me "Кто?"
    "Устало спросил я."
    sh "Придут!"
    hide sh onlayer master with dissolve
    "Повторил Шурик и убежал…"
    window hide

    with fade

    stop ambience fadeout 2

    window show
    "Я был измучен настолько, что не мог думать о каких-то голосах, вспоминать заброшенный лагерь, бомбоубежище или шахту."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "В полубреду я добрался до домика вожатой и, не раздеваясь, упал на кровать…"

    if day4_uv_mine == 1:
        "И тут у меня перед глазами появилась та девочка из шахты."
        "Я видел ее так отчетливо, как будто она действительно стояла перед моей кроватью."
        window show

        show blink onlayer master

        window hide
        th "Нет, показалось..."
        th "Но почему же все-таки тогда я почти не испугался, смог нормально и почти что спокойно с ней поговорить?"
        th "Ведь вот они – разгадки, – наверняка эта ушастая что-то знает, ведь наверняка."
        "Возможно, старый лагерь, шахта, лабиринт – все это меня слишком измотало, да и нервы были на пределе."
        th "Эх, ведь мог у нее что-нибуль узнать..."
        th "Хотя еще успею..."

    window hide

    scene black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    if prologue == 1 and not d1_keys and day3_got_fail == 1 and day4_uv_apple:
        jump epilogue_uv

    jump day5_main1

label day4_uv:

    $ day4_uv_mine = 1

    stop music fadeout 1

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with fade

    window show
    "За очередным поворотом фонарик выхватил из тьмы какую-то тень."
    "Меня аж затрясло от страха, и я не смог сделать ни шага дальше."
    "Из оцепенения вывела лишь мысль о том, что это вполне мог быть Шурик."
    me "Шурик!"
    "Ответа не последовало…"
    window hide

    scene cg d4_uv_1 onlayer master
    with dissolve

    play music music_list["mystery_girl_v2"] fadein 3

    window show
    "За поворотом, за которым скрылась тень, в свете фонаря я увидел размытые очертания человеческой фигуры..."
    "Кто-то сидел на камне.{w} Или скорее что-то..."
    "Странно, но я совсем не испугался."
    me "Что ты здесь делаешь?"
    "Послышался приятный голос:"
    uv "Ловлю мышей."
    "Я открыл рот…{w} Но сказать ничего не смог."
    me "…"
    uv "Ты здесь их не видел?"
    me "Нет, но уверен, что их тут полно…"
    "Я направил луч фонаря на ее лицо..."
    window hide

    scene cg d4_uv onlayer master
    with dissolve

    window show
    "Было два варианта: либо у этой девочки не все в порядке с головой, либо, судя по ушам и хвосту, у нее не все в порядке с видовой принадлежностью – на человека она не очень похожа."
    me "Много поймала?"
    uv "Ни одной."
    "Серьезно ответила она."
    "Девочка не казалась враждебной, я подсознательно ощущал, что мне не стоит ее бояться, но в то же время совершенно не знал, что у нее спросить, как узнать, кто она и что здесь делает."
    "Но, с другой стороны, встретить кого-то в заброшенной шахте – тут любой останется заикой на всю жизнь."
    "И ведь она явно не пионерка из лагеря!"
    me "А ты... кто?"
    uv "Ты, наверное, {i}его{/i} ищешь..."
    me "Кого?"
    uv "Ну, того мальчика..."
    me "Ну…{w} Да…"
    "Ответил я после небольшой паузы."
    me "Но все же..."
    "Девочка перебила меня:"
    uv "Он тут долго ходил.{w} Я пыталась с ним поговорить, но он меня не услышал."
    me "И где он сейчас?!"
    uv "Не знаю…{w} Наверное, все еще бродит где-то здесь."
    "Она относилась к нашему разговору совершенно индифферентно."
    me "А ты…{w} как сюда…{w} попала?"
    uv "Так же, как и ты. С поверхности."
    me "Без фонаря?"
    uv "Зачем?"
    "Она недоуменно посмотрела на меня."
    "Я окончательно перестал что-либо понимать."
    window hide

    scene bg black onlayer master
    with flash

    window show
    "Фонарь моргнул, и я в ужасе начал стучать по нему кулаком."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with flash

    window show
    "Когда свет вновь зажегся, девочки не было на прежнем месте…"
    th "Не знаю, кто или что она такое, но почему-то думается, что именно она сможет привести меня к разгадке."
    "Как ни странно, я совсем ее не боялся – просто казалось, что эта девочка не причинит мне никакого вреда."
    "Впрочем, сейчас надо искать Шурика!"
    th "А с девочкой этой мне предстоит столкнуться еще не раз..."

    stop music fadeout 2

    "Не знаю почему, но в этом я был уверен."
    window hide

    play music music_list["sunny_day"] fadein 2

    $ mr3 = mr3 + 1

    jump fail_mine_4_2

label day4_sl:

    sl "Я пойду с ним!"
    show mt smile pioneer at left onlayer master with dspr
    mt "Вот и отлично! Вдвоем веселее."
    me "Ты уверена?"
    "Спросил я Славю шепотом."
    "Конечно, хотелось надеяться, но..."
    show sl smile pioneer at right onlayer master with dspr
    "Она ничего не ответила, а лишь улыбнулась."
    "Я долго смотрел на Славю как завороженный."
    th "И почему она всегда мне помогает?"
    show sl normal pioneer at right onlayer master with dspr
    mt "Отлично! Тогда удачи вам."
    me "Она нам пригодится…"

    stop music fadeout 3

    stop ambience fadeout 2

    hide mt onlayer master
    hide un onlayer master
    with dissolve

    show sl normal pioneer onlayer master at right:
        linear 1.0 xalign 0.5

    "Вожатая и остальные девочки попрощались и разошлись кто куда."

    play ambience ambience_camp_center_evening fadein 3

    "Меня несколько удивил тот факт, что они восприняли наш поход ночью…{w} через лес…{w} в заброшенный лагерь как должное."
    th "Но ничего не поделаешь…"
    sl "Подожди минутку, я за фонариком сбегаю."
    th "Точно!{w} Я-то совсем про это забыл."
    hide sl onlayer master with dissolve
    window hide

    with fade

    window show
    "Пока я ждал Славю, в голову пришла странная идея."
    th "Почему она всегда такая добрая, отзывчивая, готова помочь?"
    th "Почему она вызвалась идти со мной не пойми куда…"
    th "В тихом омуте…"
    th "Стоит ли мне ее опасаться?"
    sl "Вот и я!"
    show sl smile pioneer at center onlayer master with dissolve
    "Славя улыбаясь протянула мне фонарик."
    sl "Пойдем?"
    "По рассказам Электроника, старое здание построили сразу после войны."
    "Оно было похоже на детский сад (или на барак, как я предполагал) и рассчитано на куда меньшее число пионеров, чем вмещал нынешний лагерь."

    stop ambience fadeout 2

    "Забросили же его лет двадцать назад…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    window show
    "Уже совсем стемнело."
    "Ночной лес словно опасался нас так же, как и мы его.{w} Деревья вежливо расступались, сгрудившись по краям тропинки и осторожно наблюдая за нами."
    "Где-то вдалеке изредка ухала сова, но тоже тише, чем обычно."
    "Рядом со Славей мне было совсем не страшно."
    "Наверное, в другой ситуации, даже в реальном мире, я бы испугался один идти ночью в лес, толком не зная маршрута."
    "Но сейчас мне просто не хотелось думать об этом."
    "Хотя уже само это было странно – она словно убаюкивала мое чувство реальности и инстинкт самосохранения."
    "Ведь если так пойдет дальше, то я и в пасть к какому-нибудь чудовищу прыгну с улыбкой на лице…"
    show sl normal pioneer at center onlayer master with dissolve
    me "А ты совсем не боишься?"
    show sl smile pioneer onlayer master with dspr
    sl "В смысле?"
    "Славя обернулась и посмотрела на меня, при этом как-то странно улыбнувшись – то ли непонимающе, то ли с долей насмешки.{w} А может, мне все это просто показалось."
    me "Ну, ночь, лес, старый лагерь…"
    sl "Да, не по себе, конечно, немного."
    me "Немного?.."
    show sl normal pioneer onlayer master with dspr
    sl "А ты что, боишься?"
    me "Я… Нет… Ну, то есть да, конечно, это же естественная реакция человека в данной ситуации."
    "Не хотелось показывать, что на самом деле я и не знаю, как реагировать – вроде бы и страха особого нет, но где-то в глубине души понимаю, что бояться стоило бы."
    "А с другой стороны, и дураком выставлять себя тоже не хочется."
    show sl smile pioneer onlayer master with dspr
    sl "Понятно."
    hide sl onlayer master with dissolve
    "Славя опять улыбнулась и продолжила путь."
    "..."
    window hide

    with fade

    window show
    "Тропинка становилась все уже, теснимая по краям деревьями и кустарниками."
    "Чем дальше мы заходили в лес, тем хуже было видно Луну."
    "В одно мгновенье она совсем скрылась за тучи, и все погрузилось практически в кромешный мрак."
    window hide
    show blinking onlayer master

    $ renpy.pause(3)

    window show
    "Я сильно зажмурился, и, когда вновь открыл глаза, Луна уже была на своем месте и окрасила мир в ярко-белые цвета ночного савана."
    th "Все-таки не люблю я темноту…"

    stop music fadeout 3

    stop ambience fadeout 2

    "Наконец вдалеке показался просвет и через минуту мы вышли на поляну…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    play music music_list["sunny_day"] fadein 5

    window show
    "На ней стояло здание старого лагеря – ветхое, размытое дождями и изъеденное ржавчиной и жуками-короедами."
    "Своими разбитыми окнами, словно щербатым ртом, оно улыбалось нам, и в улыбке этой читался немой укор живым от мертвых."
    "Всю поляну окутывал кладбищенский туман, в котором то и дело виделись приведения, вурдалаки, зомби, черти и другая дьявольская нечисть."
    "Этой картины уже было вполне достаточно, чтобы вызвать сердечный приступ или в крайнем случае паническую атаку у любого."
    show sl normal pioneer at center onlayer master with dissolve
    "И я бы наверняка не выдержал, если бы Славя не взяла меня за руку…"
    show sl smile2 pioneer onlayer master with dspr
    sl "Чтобы не так страшно…"
    "Улыбнулась она."
    "Я не смог ничего сказать, лишь покрепче сжал ее руку."
    th "И какого черта меня сюда вообще принесло?{w} Искать Шурика ночью в лесу, {i}здесь{/i}…"
    th "Ну и как я мог на такое согласиться вообще?{w} Ведь ни один нормальный человек бы…"
    th "Но ведь и мир вокруг нормальным не назовешь, как ни пытайся."
    "Я постарался убедить себя, что ищу здесь ответы и хуже, наверное, не будет…"
    "Хотя на самом деле за последние 4 дня в этом пионерлагере со мной не случилось ровным счетом ничего плохого и, более того, не было особых оснований полагать, что случится в дальнейшем."
    "Может быть, человек так устроен, что не может без приключений?.."
    show sl normal pioneer onlayer master with dspr
    sl "Пойдем?"
    me "Ну, да, наверное…"
    "Однако мы не сдвинулись с места."
    "Славя очевидно ждала от меня каких-то действий, а я просто не мог сделать первый шаг."
    hide sl onlayer master with dissolve
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve2

    window show
    "Луна выглянула из-за туч, осветив здание старого лагеря."
    "Теперь оно не так напоминало склеп, но при этом все те картины в моем воображении, которые казались мертвыми, ожили – на приведений словно навели резкость, четче стал вой ветра, шелест травы под ногами, а где-то вдалеке слышались звуки, происхождение которых понять я не мог."
    show sl normal pioneer at center onlayer master with dissolve
    sl "Наверное, тут раньше здорово было…"
    "Я внимательно посмотрел на Славю."
    "Если даже она и боялась, то старалась этого не показывать.{w} Мне сразу же стало как-то легче и спокойнее."
    me "Наверное. Пойдем?"
    sl "Да…"
    hide sl onlayer master with dissolve
    "Я шел медленно, выверяя каждый шажок, стараясь не задеть старую ограду, покосившуюся карусель или ржавую горку."
    "Трава в некоторых местах доходила мне до пояса, так что любое неверное движение могло привести к сломанным ногам или рукам."
    "Наконец мы добрались до входа, и я посветил фонарем внутрь."
    "Тьма, смотревшая на меня оттуда, была куда страшнее, чем вид снаружи – замогильный, но все же при свете Луны."

    stop ambience fadeout 2

    "Я набрался смелости и шагнул через порог."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_old_building_night onlayer master
    with dissolve

    window show
    "Внутри старый лагерь походил на детский сад, в который я ходил в детстве – примерно та же планировка и убранство, даже мебель, хоть и полусгнившая, казалось, была той же."
    me "Да уж…"
    "Я поежился, выхватывая фонарем из темноты все новые останки былой детской радости."
    show sl scared pioneer at center onlayer master with dissolve
    sl "Жутковато."
    "Славя уже давно не просто держала меня за руку, а обхватила ее, плотно прижавшись ко мне всем телом."
    "Однако в ее голосе не чувствовалось особого испуга."
    me "Может, не стоило сюда ночью идти?"
    sl "Наверное."
    me "Вернемся?"
    show sl surprise pioneer at center onlayer master with dspr
    sl "Нет, ну как же! А Шурик?"
    "Сказала она, искренне удивившись."
    me "Да уж, Шурик… И чего он вообще сюда полез? Да и откуда мы знаем, что он здесь?"
    show sl sad pioneer onlayer master with dspr
    sl "Ну, наверное, а где он еще может быть?"
    me "Не знаю. Волки его съели, например."
    show sl serious pioneer onlayer master with dspr
    sl "Не говори так!"
    "Славя нахмурилась и отошла от меня на шаг."
    "Я уже настолько привык к ее близости, что несколько расстроился."
    me "Ну ладно-ладно, волков тут, допустим, не водится."
    th "Хотя откуда мне знать…"
    me "Ну, раз уж пришли, давай искать."
    hide sl onlayer master with dissolve
    "…"
    window hide

    with fade

    window show
    "Мы осмотрели все помещения старого лагеря: игровые комнаты, спальни, столовую и кухню, туалеты, я даже заглянул в кладовку, доверху забитую какими-то пустыми истлевшими коробками."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "Смотри."
    "Когда мы вернулись на то место, с которого начинали, Славя подобрала что-то с пола и протянула мне."
    "Это была старая кукла, выцветшая от сырости, без одной руки и глаза, с торчавшими отовсюду нитками."
    me "Ну, и?"
    show sl sad pioneer onlayer master with dspr
    sl "Жалко…"
    me "Что жалко? Куклу?"
    sl "Да."
    me "А что ее жалеть?"
    sl "Ну, когда-то кто-то с ней играл, а потом вот так вот бросил, забыл, и она столько лет здесь одна, и в дождь, и в холод."
    "Я никак не мог понять, серьезно она или нет."
    "Ведь сейчас не самое подходящее время, чтобы думать о таком."
    "С другой стороны, а для чего сейчас время?"
    "Славя казалась действительно расстроенной."
    me "Да, наверное."
    "Я взял куклу и повертел ее в руках."
    "Помнится, в детстве я так же нашел плюшевого льва в луже, принес домой, отмыл и потом относился к нему не хуже, чем к остальным игрушкам, хотя по виду ему давно было пора на пенсию."
    me "Ульянке подаришь."
    show sl laugh pioneer onlayer master with dspr
    "Славя рассмеялась."

    play sound sfx_wind_gust

    "Внезапно из прохода подул ветер, напевая какую-то неведомую ораторию."

    play sound sfx_bodyfall_1

    with vpunch
    "Фонарь моргнул, и я инстинктивно отпрыгнул к стене, зацепился ногой за что-то и с грохотом полетел на пол."
    show sl scared pioneer onlayer master with dspr
    sl "Живой?"
    "Ко мне подскочила Славя и помогла подняться."
    me "Да, вроде…"
    "Зацепился я за крышку люка."
    "Грязь вокруг него была расчищена – странно, как мы не заметили этого сразу, – так что можно было предположить, что его недавно открывали."
    me "Ведь мы туда не полезем, да?"
    "Стараясь предвосхитить предложение Слави, спросил я."
    show sl sad pioneer onlayer master with dspr
    "Она лишь грустно посмотрела на меня."
    me "Ну вот, еще не хватало в диггеров играть…"
    "Ворчал я, с трудом откидывая крышку люка."
    "Конечно, здравый смысл отчаянно кричал, что не стоит этого делать, но логика, наоборот, подсказывала, что, если бы этот мир хотел меня убить, то давно бы сделал это."
    "Хотя если бы не Славя, то черта с два я бы туда полез!"
    "Вниз на пару метров уходила ржавая металлическая лестница, упирающуюся в грязный бетонный пол."
    "Я свесился в люк и осветил фонарем достаточно узкий коридор, уходящий куда-то во тьму."
    me "И что там такое?"
    show sl normal pioneer onlayer master with dspr
    sl "Кажется, я слышала, что под старым лагерем есть бомбоубежище."
    me "Бомбоубежище?"
    "Ну, если учитывать время его постройки, то это вполне логично."
    me "И что Шурику понадобилось там?"
    show sl sad pioneer onlayer master with dspr
    sl "Не знаю."
    th "Конечно, нельзя быть до конца уверенным, что именно он открывал люк (а то, что его открывали совсем недавно, было очевидно), но кому еще взбредет в голову туда лезть, как не безумному изобретателю?"
    th "Если откинуть теории с потусторонними силами, то больше людей в этом лесу быть не может."
    "По крайней мере тогда я думал именно так."
    me "Ладно, я лезу первым, если все в порядке, ты – за мной."
    show sl scared pioneer onlayer master with dspr
    sl "А что может быть не в порядке?"
    "Испугалась Славя больше из вежливости."
    me "Ну, не знаю… Крысы, например. Боишься, крыс?"
    th "Похоже, зря спросил."
    "Я глубоко вздохнул и начал спуск."
    "…"
    window hide

    scene cg d4_catac_sl onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Мы медленно пробирались вперед, держась за руки."
    "В кромешной темноте фонарь помогал не сильно, лишь изредка освещяя куски старых газет и валяющийся тут и там металлолом."
    "В какой-то момент начало казаться, что стены и потолок, увитые бесконечными линиями проводов, давят на меня и словно становятся уже."
    "Я развел руки в стороны, пытаясь измерить ширину прохода."
    sl "Далеко нам еще?"
    "Грустно спросила Славя."
    me "Далеко до чего? Не имею ни малейшего представления."
    sl "Ладно…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "И тут же передо мной словно из ниоткуда выросла массивная металлическая дверь."
    sl "Ой…"
    "Тихо вскрикнула Славя."
    "Я подергал за ручку, и она, казалось, начала поддаваться."
    me "Готова?"
    show sl scared pioneer at center onlayer master with dissolve
    sl "Не знаю…"
    "Хотя, собственно, к чему надо вообще быть готовым в подобной ситуации?"

    play sound sfx_open_metal_hatch

    "Колесо сделало несколько оборотов, ужасно скрипя при этом, и наконец замолкло, прокрутившись до конца."

    stop ambience fadeout 2

    "Я с силой дернул дверь на себя, и она нехотя открылась.{w} За ней была какая-то комната…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    with flash

    window show
    "Которая оказалась как раз самим бомбоубежищем."
    "Когда мы вошли, внезапно загорелся свет, от чего меня передернуло."
    "С другой стороны, вполне возможно, что здесь существуют какие-то источники автономного питания – в то время, когда строили эти катакомбы, все делали на века."
    "Бомбоубежище было таким, каким я себе его и представлял – здесь имелось все, чтобы поддерживать длительное существование людей во время войны: в шкафах нашлись костюмы химзащиты, противогазы, сухпайки и канистры с водой, у дальней стены я заметил множество различной аппаратуры (измерители давления и радиации, радио и т.д.)."
    "Однако создавалось впечатление, что им никто никогда не пользовался (что, в общем-то, неудивительно).{w} Более того, даже не заходил сюда ни разу после постройки."
    show sl surprise pioneer at center onlayer master with dissolve
    "Славя вопросительно посмотрела на меня."
    me "Ну, тут Шурика точно нет."
    sl "А был?"
    me "Не знаю. Но если был, то не мог же он просто испариться."
    "Я окинул помещение взглядом еще раз и слева от себя в стене заметил дверь."
    me "Может быть, там?"
    "Однако дверь не открывалась."
    show sl sad pioneer onlayer master with dspr
    sl "А вдруг он запер ее с той стороны?"
    me "Но зачем?"
    sl "Не знаю…"
    "Однако такое было вполне возможно, если предположить, что он вообще здесь."
    "По всему было похоже, что Шурик прятался, может быть, бежал от кого-то."
    "От таких мыслей мне стало не по себе и захотелось самому побыстрее оказаться по ту сторону двери."

    play sound sfx_metal_door_handle_rattle

    "Я с силой надавил, но она лишь глухо скрипнула."
    sl "На вот, может, этим?"
    "Славя протянула мне фомку."
    "Я повертел ее в руках, прикидывая, как лучше подцепить дверь."
    hide sl onlayer master with dissolve

    play sound sfx_insert_crowbar_door

    me "Давай попробуем."
    window hide

    play sound sfx_fall_metal_door

    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living_nodoor onlayer master
    with vpunch

    window show
    "Напрягшись изо всех сил, мне все же удалось сорвать дверь с петель, и она с грохотом упала на пол."
    "Пока я приходил в себя от чрезмерных усилий, Славя светила фонарем в образовавшийся проход."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "Там такой же коридор."
    me "Да уж… Тут прямо целый лабиринт."
    sl "Идем?"
    me "Подожди…"
    "Я сел на кровать, снял с подушки пыльную наволочку и вытер пот со лба."
    me "Сейчас, отдышусь немного."
    show sl normal pioneer close at center onlayer master with dissolve
    "Славя села рядом и принялась изучать детали узоров плитки на полу."
    me "Ты бы фонарь пока выключила…"
    show sl shy pioneer close at center onlayer master with dspr
    sl "Ах, да…"
    "Она немного покраснела и тут же щелкнула кнопкой выключения."
    me "Жуть какая-то…"
    "Я поймал себя на мысли, что последние полчаса уже не воспринимаю происходящее как реальность."
    "Словно все это не со мной, словно все это сон."
    "Как тогда, четыре дня назад, в первые минуты после того, как оказался здесь."
    "Да, наверное, в последнее время я начал свыкаться с этим миром, с этой {i}реальностью{/i}, какой она для меня стала."
    "И уже не так ноет где-то в душе необходимость найти выход."
    "А теперь вот опять, в мгновение ока – лес, старый лагерь, бомбоубежище."
    "Во всем этом не было ровным счетом ничего сверхъестественного, но и нормального, привычного мне по прошлой жизни было мало."
    show sl sad pioneer close at center onlayer master with dspr
    sl "Да…"
    "Согласилась Славя."
    me "А тебе не кажется все это странным?"
    show sl surprise pioneer close at center onlayer master with dspr
    sl "Что именно?"
    me "Ну, что мы сидим тут, вдвоем, ночью. Не нормально ли в данной ситуации дождаться утра, вызвать милицию?"
    show sl normal pioneer close at center onlayer master with dspr
    sl "Да, наверное."
    "Сказала она задумчиво."
    me "Конечно, я практически сам вызвался. Не стоило."
    "Ну, «практически» не считается, но все же."
    show sl sad pioneer close at center onlayer master with dspr
    sl "Но ведь ты просто хотел помочь. Если Шурик там, то нужно его найти как можно скорее."
    me "Такими темпами скорее не мы Шурика найдем, а им потом нас придется искать. Ведь он как-то смог тут заблудиться."
    "Славя погрустнела."
    me "Ладно-ладно, я ничего такого не имел в виду. Может, его там нет и он давно вернулся в лагерь."
    show sl smile2 pioneer close at center onlayer master with dspr
    sl "Да, может быть."
    me "Но проверить стоит?"
    sl "Конечно!"
    show sl smile2 pioneer at center onlayer master with dissolve
    "Славя встала и протянула мне руку."
    "Похоже, ей все-таки не было так страшно, как мне."
    "Хотя и я уже устал бояться и сейчас лишь хотел, чтобы это все побыстрее закончилось."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Коридор был действительно точно такой же, как и тот, по которому мы попали сюда."
    "Я шел медленно, тщательно осматривая пол и то и дело проверяя, не сужаются ли стены."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "Смотри!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "Славя крепче сжала мою руку и показала на пролом посреди туннеля."
    "Он был достаточно широкий, чтобы в него пролезть (или провалиться)."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "Может быть…"
    "Я посветил вниз, но на дне не было видно ничего, кроме земли."
    me "Наверное, стоит проверить…"

    stop ambience fadeout 2

    "Глубина ямы позволяла потом выбраться оттуда, так что бояться на первый взгляд было нечего."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "Я аккуратно спустился и помог Славе."
    "Мы оказались в какой-то шахте."
    "Стены и потолок были укреплены деревянными балками, а вдаль уходили рельсы."
    "Кое-где давящая на эту хлипкую конструкцию земля прорвала прогнившие от старости доски, от чего все это сооружение не производило впечатление особой надежности."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "Как думаешь, где мы?"
    me "Не знаю, шахта какая-то. Что здесь могли добывать?"
    sl "Может быть, уголь?"
    me "Может быть…"
    "Мы начали медленно продвигаться вперед."
    "Из-под ног то и дело предательски вылетали камни, свет фонаря, дрожа, прыгал от одной стены к другой, то и дело вылавливая из тьмы какие-то тени, которые исчезали, стоило посветить в их сторону."
    show sl scared pioneer onlayer master with dspr
    sl "Тут страшнее, чем наверху…"
    me "Да, пожалуй."
    "Чем дальше мы продвигались, тем сильнее крепла во мне уверенность, что Шурику тут просто нечего делать!"
    th "Не утащила же его, в самом деле, какая-то Чупакабра?{w} Хотя и этот вариант исключать не стоит."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    window show
    "Наконец мы вышли к развилке."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "И куда нам теперь?"
    me "Не знаю."
    "Я попытался придать своему голосу хотя бы подобие спокойствия, но в действительности и правда ничего не знал.{w} Совершенно ничего – ни куда идти, ни где Шурик, ни зачем мы вообще здесь!"
    show sl scared pioneer onlayer master with dspr
    sl "А вдруг мы заблудимся?.."
    me "Да, точно, давай сделаем пометку, что мы здесь уже были!"
    "Я взял с земли довольно большой камень и тщательно выцарапал на одном из бревен, держащем потолок, крест."
    me "Вот, теперь точно будем знать, что здесь уже проходили. "
    show sl smile2 pioneer onlayer master with dspr
    sl "Хорошо."
    "Славя улыбнулась."
    sl "И куда?"
    "…"
    window hide

label sl_mine_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    menu:
        "Налево":
            jump sl_mine_4_1
        "Направо":
            jump sl_mine_2

label sl_mine_1_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Мы вернулись к тому месту, с которого и начинали."
    th "Значит, где-то не там повернули."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            jump sl_mine_4_1
        "Направо":
            jump sl_mine_2

label sl_mine_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_3
        "Направо":
            jump sl_mine_room

label sl_mine_2_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump sl_mine_1_1
        "Направо":
            jump sl_mine_3

label sl_mine_2_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_room
        "Направо":
            jump sl_mine_1_1

label sl_mine_room:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface onlayer master
    with fade

    if mr1 >= 1:
        window show
        "Здесь мы уже были."
        window hide
        jump sl_mine_2_1

    show sl scared pioneer at center onlayer master with dissolve
    window show
    "Наконец мы вышли из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным нашим спасением был фонарик…"
    "Сломайся он, и мы вряд ли когда-нибудь выбрались бы отсюда…"
    "Именно в его свете я заметил в углу какую-то красную тряпку."
    "Это был пионерский галстук!"
    "Теперь-то я точно был уверен, что Шурик здесь."
    me "Шурик! Шурик!"
    sl "Шурик! Шурик!"
    "Ответом нам стало лишь эхо."
    sl "Не волнуйся, с ним все в порядке!"
    "Честно говоря, в ту минуту я больше волновался за себя…"
    th "Но куда он мог отсюда уйти?"
    "Из этой комнаты не было другого выхода…"
    th "Конечно, возможно, в этих туннелях есть еще места, где мы не бывали…"
    th "Значит, придется искать дальше!"
    window hide

    $ mr1 = mr1 + 1

    jump sl_mine_2_1

label sl_mine_3:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_5
        "Направо":
            jump sl_mine_6

label sl_mine_3_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_6
        "Направо":
            jump sl_mine_2_2

label sl_mine_5:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_4
        "Направо":
            jump sl_mine_6

label sl_mine_5_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_6
        "Направо":
            jump sl_mine_3_1

label sl_mine_4:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_1_1
        "Направо":
            jump sl_mine_7

label sl_mine_4_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump sl_mine_7
        "Направо":
            jump sl_mine_5_1

label sl_mine_4_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump sl_mine_5_1
        "Направо":
            jump sl_mine_1_1

label sl_mine_7:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt onlayer master
    with fade

    if mr2 >= 1:
        window show
        "Здесь мы уже были."
        window hide
        jump sl_mine_4_2

        window show
    "Мы вышли к некоему подобию шахтерского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовал, что выход где-то рядом, поэтому мы отправились дальше."
    window hide

    $ mr2 = mr2 + 1

    jump sl_mine_4_2

label sl_mine_6:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door onlayer master
    with fade

    window show
    "За очередным поворотом фонарь выхватил из тьмы деревянную дверь."
    me "Ну, уже хоть что-то."
    "По правде говоря, я так устал бродить по этой шахте, что и думать забыл о Шурике – хотелось просто поскорее найти выход."
    show sl surprise pioneer at center onlayer master with dissolve
    sl "А что там?"

    stop ambience fadeout 3

    me "Вот сейчас и выясним."
    window hide

    play sound sfx_open_door_mines

    pause(1)

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    window show
    "За дверью скрывалась какая-то комната, похожая то ли на подсобку котельной, то ли на одно из помещений бомбоубежища."
    "Повсюду валялись пустые бутылки, а стены были расписаны лучшими образчиками русского народного фольклора, что говорило о том, что здесь до нас уже кто-то бывал, и не раз.{w} Правда, судя по всему, довольно давно."
    "Я водил фонарем по комнате, стараясь осмотреть все углы, как вдруг…"
    window hide

    scene cg d4_sh_sit onlayer master
    with dissolve

    window show
    "Обнаружил съежившегося в углу Шурика."
    sl "Шурик!"
    "Закричала Славя."
    "Он же, казалось, не обратил на нас никакого внимания."
    me "Так вот ты где! А мы тебя всю ночь ищем! Что ты тут вообще забыл?!"
    "Шурик поднял на меня мутные, невидящие глаза."
    sh "А вы кто?"
    me "Что значит, «мы кто»? Давай уже вставай и пойдем."
    sh "Никуда я с вами не пойду."
    "Он вновь уставился куда-то в темноту."
    sh "Вы опять хотите меня обмануть. Будете водить кругами по подземелью? Будете! Я вас знаю!"
    "Он перешел на какой-то дьявольский шепот."
    me "Хватит уже чушь нести."
    "Я хотел подойти к нему и помочь подняться, но Славя остановила меня."
    sl "Он не в себе."
    me "Ну и я не в себе! Целую ночь тут шляться – любой не в себе будет."
    "Славя укоризненно покачала головой и медленно, стараясь не выходить из света фонаря, подошла к Шурику."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    show sl sad pioneer onlayer master at cleft
    show sh scared pioneer onlayer master at cright
    with dissolve
    sl "Все в порядке, это я, Славя."
    sh "Правда?"
    show sh cry pioneer at cright onlayer master with dspr
    "Он посмотрел на нее, и тут же на его глазах появились слезы."
    sl "Конечно! Кто же еще? И Семен со мной. Мы пришли за тобой. Теперь все в порядке!"
    sh "Вы точно не {i}они{/i}?"
    sl "Нет конечно! Мы – это мы."
    "Шурик попытался встать, но, видимо, потерял ориентацию и был готов уже упасть, если бы Славя не схватила его за руку."
    sl "Вот так! Осторожнее!"
    show sh scared pioneer at cright onlayer master with dspr
    "Когда они подошли ко мне, я сказал:"
    me "Ладно, пора выбираться уже отсюда!"
    show sh upset pioneer at cright onlayer master with dspr
    sh "Назад нельзя…"
    me "Назад – это куда? В шахту?"
    sh "Да."
    "Шурик говорил все это спокойно, но при этом его голос еле заметно дрожал."
    me "Почему?"
    show sh scared pioneer at cright onlayer master with dspr
    sh "Там… {i}они{/i}!"
    me "Кто {i}они{/i}-то?"
    sh "Голоса."
    me "Какие еще голоса?"
    "Я уже начинал терять терпение."
    "Конечно, все это место, эта ситуация не были особо нормальными, но если бы здесь и водилась какая-то чертовщина, то по всем канонам фильмов ужасов, она давно уже должна была показаться."
    show sl serious pioneer at cleft onlayer master with dspr
    sl "Успокойся, Шурик. И расскажи нам все подробно."
    "Он сделал несколько глубоких вдохов и выдохов и начал:"
    show sh normal pioneer at cright onlayer master with dspr
    sh "Мне нужны были кое-какие детали для робота, и я слышал, что в старом лагере есть бомбоубежище. А в бомбоубежищах обычно много всякой аппаратуры. Она, конечно, старая, но разобрать вполне можно – катушки, резисторы всегда найдутся."
    sh "Вот я с утра пораньше и пошел, думал, все быстро сделаю и к завтраку вернусь."
    sh "Все, что нужно, я собрал."
    "Он достал из кармана и показал нам какие-то лампочки и проводочки."
    sh "Но потом из-за двери – там наверху, в бомбоубежище – услышал какие-то звуки. То ли стоны, то ли плач. Сначала стало страшно, но потом я подумал – а вдруг человек в опасности. И пошел…"
    show sh scared pioneer at cright onlayer master with dspr
    sh "А тут вот – шахта, лабиринт этот чертов! Я совсем заблудился. И голоса, голоса повсюду что-то говорят мне – то кричат, то шепчут, а я никак разобрать не могу!"
    show sl sad pioneer at cleft onlayer master with dspr
    "Он уже был готов расплакаться, но Славя нежно погладила его по голове, и Шурик продолжил:"
    show sh normal pioneer at cright onlayer master with dspr
    sh "В общем, нашел я эту комнату, тут хотя бы не слышно {i}их{/i}…"
    me "И решил сидеть и ждать, пока тебя спасут, как в фильмах уровня «Б»?"
    "Саркастически спросил я."
    show sl angry pioneer at cleft onlayer master with dspr
    "Славя бросила на меня гневный взгляд."
    me "Ну, в любом случае, пора выбираться отсюда! Если никто не против, конечно?"
    sh "Пойдемте, я знаю короткий путь!"
    me "Короткий?"
    sh "Да, я же тут все исходил."
    me "Ну ладно…"
    "..."
    window hide

    scene black onlayer master
    with dissolve

    window show
    "Шурик не соврал."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_exit onlayer master
    with dissolve

    window show
    "Действительно, поплутав по шахте всего пару минут, мы оказались возле решетки, за которой виднелось небо."
    me "И почему же ты не выбрался тогда сам?"
    sh "А ты попробуй."
    "Я подтянулся и сильно дернул решетку несколько раз."
    th "Действительно, так просто не сломать.{w} Нужно что-то тяжелое…"
    "Я посмотрел вниз на Славю и Шурика."
    sl "Может, фонарем?"
    me "Фонарем…"
    "Я покрутил его в руках – да, это была не китайская поделка 90-х годов, коих у меня в свое время множество валялось на даче, а настоящий советский, добротно сделанный металлический фонарь.{w} Конечно, не молоток, но при должном усердии…"
    "Я размахнулся и начал долбить по решетке в тех местах, где она крепилась к стене."

    play sound sfx_break_grid

    "Вскоре мне повезло, послышался треск, и на землю полетели болты, удерживающие ее."

    stop music fadeout 3

    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Через минуту я уже валялся на траве возле памятника и с наслаждением вдыхал свежий ночной воздух.{w} Хотя после шахты мне бы любой воздух показался свежим."

    show sh normal pioneer at center onlayer master with dissolve
    sh "Ну ладно, я пойду, спасибо вам…"
    "Шурик выглядел несколько растерянным."
    "Я некоторое время оценивающе смотрел на него, но в итоге ничего не сказал, лишь слабо махнув рукой на прощание."
    hide sh onlayer master with dissolve
    "В конце концов, не было ни сил, ни желания с ним разговаривать."
    th "Да и что сказать?{w} Ругать его сейчас бесполезно, пытаться что-то узнать – наверное, тоже."
    show sl normal pioneer close at center  onlayer master with dissolve
    sl "Ну и ночка…"
    "Славя сидела рядом и мечтательно смотрела на Луну."
    me "Да уж… Если бы мне кто еще неделю назад сказал, что я попаду в пионерлагерь да и еще придется лазать по бомбоубежищам…"
    show sl smile2 pioneer close at center onlayer master with dspr
    sl "Зато весело."
    me "В каком-то смысле."
    "Действительно, что-то забавное в этом всем было.{w} Но было и странное – за последние несколько часов со мной могло произойти все что угодно, но в итоге не случилось ничего."
    "Возможно, через пару лет я буду вспоминать все это лишь как смешной случай из детства.{w} Если доживу…"
    me "Как думаешь, он правда там что-то слышал?"
    show sl serious pioneer close at center onlayer master with dspr
    sl "Не знаю... Возможно, конечно, но, скорее всего, ему просто показалось. В такой ситуации любому что угодно померещится."
    "Это было не только самое логичное объяснение, но и самое правильное – ведь с нами-то не случилось ничего."
    me "А я вот думаю, ему стоит психиатру показаться…"
    show sl laugh pioneer close at center onlayer master with dspr
    sl "Наверное!"
    "Славя рассмеялась."
    show sl smile2 pioneer close at center onlayer master with dspr
    sl "Ну ладно, пора спать."
    me "Угу."

    play music music_list["forest_maiden"] fadein 3

    "Я чувствовал, что надо что-то сказать Славе.{w} Не был уверен, хочу ли, но необходимость чувствовал."
    me "Спасибо тебе!"
    show sl smile2 pioneer close at center onlayer master with dspr
    sl "За что?"
    "Она недоуменно посмотрела на меня."
    me "Без тебя я бы не справился."
    show sl shy pioneer close at center onlayer master with dspr
    sl "Да ничего…"
    "Она покраснела."
    th "Я был у нее в долгу.{w} Опять."
    th "Интересно, как хотя бы частично отплатить ей за все, что она для меня сделала…"
    window hide

    scene stars onlayer master
    with dissolve

    window show
    "Я смотрел на ночное небо и медленно погружался в сон."
    "Все приключения сегодняшнего дня меня настолько утомили, что сил больше не было."
    me "Знаешь, при других обстоятельствах я бы обязательно признался тебе в любви…"
    "Сказал я, теряя контакт с реальностью."
    "Мысль обычно работает куда быстрее, чем здравый смысл..."
    "Но Слави рядом со мной уже не было."
    th "Может, оно и к лучшему – хотя бы не слышала…"
    th "Хотя странно, почему она ушла, не попрощавшись…"

    stop ambience fadeout 2

    th "Ну и ладно, утро вечера мудренее."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "Я так устал, что еле добрался до домика вожатой."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master

    with dissolve

    window show
    "Ольга Дмитриевна уже спала, видимо не дождавшись меня, поэтому я не стал шуметь и быстро шмыгнул под одеяло."
    "В голове еще некоторое время крутились какие-то мысли, но вскоре она начала болеть, и сознание, словно включив безопасный режим, ушло на перезагрузку."
    window hide

    stop music fadeout 5

    scene black onlayer master
    with fade3

    $ renpy.pause(3)

    jump day5_main1

label day4_dv:

    mt "А с тобой пойдет Двачевская!"
    "Ольга Дмитриевна словно угадала мои мысли."
    hide sl onlayer master
    hide un onlayer master
    with dissolve
    show dv angry pioneer at right onlayer master with dissolve
    dv "Это почему?"
    show mt angry pioneer at left onlayer master with dspr
    mt "А кто памятник взрывал?{w} И ладно бы только это! Кто еще пытался оклеветать Семена?!"
    "Она сказала это таким тоном, что Алиса не решилась возражать."
    hide mt onlayer master with dissolve
    show dv angry pioneer onlayer master at right:
        linear 1.0 xalign 0.5
    dv "Доволен?"
    "Выпалила она, когда мы остались вдвоем."
    me "А я-то тут при чем?{w} Я, что ли, памятник взрывал?"
    show dv guilty pioneer at center onlayer master with dspr
    "Алиса фыркнула и отвернулась."
    dv "Никуда я с тобой не пойду!"
    me "Да и ради Бога!"
    dv "Вот и отлично!"
    me "Прекрасно!"
    "Некоторое время мы стояли молча, не смотря друг на друга."
    "Я решился первым нарушить молчание."
    me "Это все?"
    dv "Что все?"
    me "Все, что ты хотела мне сказать?"
    dv "Все!"
    me "Тогда можно поинтересоваться, зачем ты пыталась памятник взорвать?"
    show dv normal pioneer onlayer master with dspr
    dv "Скучно было…"
    th "А это, конечно, помогло бы развеселиться…"
    "Алиса, похоже, действительно не хотела идти со мной."
    "Однако я-то все же решил найти Шурика."
    "Меня не столько интересовал он сам, сколько заброшенный лагерь."
    "Почему-то мне казалось, что там я смогу что-нибудь выяснить."
    "А идти одному ночью как-то совсем не хотелось…"
    me "Значит, боишься?"
    show dv smile pioneer onlayer master with dspr
    dv "На слабо меня хочешь взять?"
    "Она ехидно улыбнулась."
    me "Нет, что ты…{w} Тогда счастливо оставаться!"

    stop music fadeout 3

    stop ambience fadeout 2

    hide dv onlayer master with dissolve
    "Я развернулся и зашагал в ту сторону, где должен был находиться старый лагерь."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_path_sunset onlayer master
    with dissolve

    play ambience ambience_forest_evening fadein 3

    window show
    "На опушке леса меня догнала Алиса."
    show dv normal pioneer at center onlayer master with dissolve
    dv "Стой!{w} Я пойду с тобой!"
    me "С чего это вдруг вы соизволили изменить свое решение?"
    "Съязвил я."
    show dv angry pioneer at center onlayer master with dspr
    dv "Меньше знаешь – лучше спишь!"
    "Огрызнулась она и протянула мне фонарик."
    "Это было очень предусмотрительно."
    "Если бы не Алиса, не знаю, что бы я делал там один в темноте…"
    hide dv onlayer master with dissolve
    "По рассказам Электроника, старое здание построили сразу после войны."
    "Оно было похоже на детский сад (или на барак, как я предполагал) и рассчитано на куда меньшее число пионеров, чем вмещал нынешний лагерь."

    stop ambience fadeout 2

    "Забросили же его лет двадцать назад…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    window show
    "Ночной лес совершенно не похож на дневной."
    "Еще пару часов назад казалось, что это всего лишь небольшая рощица, где невозможно заблудиться даже слепому."
    "Однако с наступлением темноты деревья словно вырастали, кустарники внезапно занимали собой все свободное пространство, а такие широкие в светлое время суток тропинки превращались в еле заметные волны в темно-зеленом лесном океане."
    "Общую картину довершали птицы, насекомые, звери, которые устраивали концерт, каждый со своим инструментом, создавая вместе удивительную, но в то же время пугающую симфонию ноктюрна."
    show dv normal pioneer at center onlayer master with dissolve
    "Мы медленно продвигались вперед, Алиса шла немного впереди, а я – позади, стараясь сильно не отставать."
    "Она вела себя даже чересчур самоуверенно.{w} Совсем не в пример мне – каждый шорох кустов рядом и крик совы над головой заставлял меня ежиться и боязливо оглядываться по сторонам."
    "Конечно, было понятно, что опасаться здесь особо нечего – вряд ли окрестные леса кишат дикими животными, а людей, кроме как в лагере, в этом мире, похоже, нет вообще."
    "Однако на уровне инстинкта я все равно ощущал страх и старался идти как можно аккуратнее и быть как можно более внимательным.{w} В конце концов, береженого Бог бережет."
    "Алиса внезапно остановилась.{w} Так, что я чуть не врезался в нее."
    show dv surprise pioneer onlayer master with dspr
    dv "И куда дальше?"
    me "Что? Ну… Прямо, наверное?"
    show dv normal pioneer onlayer master with dspr
    dv "Ты уверен?"
    "Я прикинул направление."
    "Казалось, мы шли куда надо.{w} По крайней мере туда, куда указал Электроник."
    "Однако без карты, ГПС- или ГЛОНАСС-навигации я бы не поручился даже за то, что все еще нахожусь на этой планете (где бы она ни была)."
    me "Мы не сворачивали, шли все время прямо, Электроник же…"
    show dv angry pioneer onlayer master with dspr
    dv "И почему мы тогда еще не вышли к этому лагерю?"
    me "Откуда я знаю?!"
    "Грубый тон Алисы уже начал выводить меня из себя."
    dv "Может, мы заблудились вообще?"
    me "С какой стати? Мы отошли максимум на километр от лагеря."
    show dv sad pioneer onlayer master with dspr
    dv "Ну и что?"
    "Она заметно погрустнела."
    me "А ничего! Не нравится – можешь возвращаться."
    "Алиса некоторое время расстроенно смотрела на меня, потом резко поменялась в лице."
    show dv angry pioneer onlayer master with dspr
    dv "А вот и вернусь!"
    hide dv onlayer master with dissolve
    "Она внезапно развернулась и бодро зашагала в сторону лагеря."
    me "Вот и счастливо!"
    "Бросил я ей вслед."
    th "Однако, возможно, Алиса все же была права, и мы таки заблудились.{w} Тогда оставаться одному здесь – не лучшая идея…"

    play sound sfx_wind_gust

    "Сильнее задул прохладный ночной ветер, и я поежился."
    th "Но возвращаться за ней – это значит потерять лицо, более того – согласиться с ней.{w} Нет, на это я пойти не готов!"
    "Наверное, я бы мог так рассуждать до утра, если бы не крик Алисы…"
    "Ноги сами понесли меня в ту сторону, куда она ушла."

    scene black onlayer master
    show bg ext_path2_night onlayer master:
        linear 0.2 pos (0,50)
        linear 0.2 pos (0,0)

    play sound sfx_jump_over_hole

    "Через пару десятков метров я чуть не провалился в яму, успев в последний момент перепрыгнуть ее."
    window hide

    play sound sfx_alisa_falls

    pause(1)

    window show
    "А вот Алиса, похоже, не успела…"
    "Я только собирался посветить фонарем в темноту, как понял, что его она забрала с собой.{w} Что же, этого стоило ожидать."
    me "Живая?"
    dv "Да…"
    "Донесся снизу ее приглушенный голос."
    me "Ничего не сломала?"
    dv "Не знаю, блин! Идиот!"
    "В яме замелькал свет, я подошел поближе и наклонился, чтобы рассмотреть, насколько там глубоко."
    "Вниз метра на 3 уходила узкая дыра, но дальше ничего видно не было."
    dv "Помоги мне выбраться!"
    "Недовольно закричала Алиса."
    me "И как ты себе это представляешь?"
    dv "Не знаю как! Придумай!"
    me "Ты где хоть находишься? Опиши."
    dv "Тут туннель какой-то и… Туннель."
    "Туннель? Странно."
    dv "Спускайся давай!"
    me "Ага, еще чего? Я лучше сбегаю в лагерь за веревкой."
    dv "И что, я тут одна останусь?"
    "Нахальства в голосе Алисы заметно поубавилось."
    me "А ты и так одна, вообще-то, там…"
    dv "Эй!"
    "Громко закричала она и направила луч фонаря прямо мне в глаза."
    me "Ладно, не паникуй, авось тебя тролли там не съедят, я быстро!"
    "Алиса что-то отчаянно орала снизу, но слов было не разобрать."
    window hide

    scene black onlayer master
    show bg ext_path2_night onlayer master:
        linear 0.1 pos (0,25)
        linear 0.2 pos (0,-25)
        linear 0.1 pos (0,0)
        repeat

    play sound sfx_simon_fall_1

    pause(1)

    window show
    "Но не успел я сделать и пары шагов, как почва у меня под ногами поехала, и я начал стремительно проваливаться вниз."

    stop music fadeout 3



    stop ambience fadeout 2

    "Рука ухватилась за какой-то корень, который несколько затормозил падение..."
    window hide

    play sound sfx_simon_fall_2

    pause(1)

    window show
    "... однако под моим весом надломился и полетел вниз вместе со мной."
    window hide

    scene black onlayer master
    with dissolve




    $ renpy.pause(1)

    window show
    "…"
    dv "Ты живой?"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    show unblink onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    play music music_list["sunny_day"] fadein 5

    $ renpy.pause(1)

    window show
    "Я с трудом открыл один глаз, в который тут же ударил яркий свет фонаря."
    show dv scared pioneer at center onlayer master with dissolve
    me "Убери…"
    "Алиса сидела рядом и взволнованно смотрела на меня."
    dv "Ничего не сломал?"
    me "Не знаю…"
    "Я пошевелил руками и ногами – боли особой не ощущалось."
    "Учитывая высоту, мне еще повезло, что вообще не разбился!"
    "Я с трудом встал и осмотрел место падения."
    "Мы действительно находились в длинном коридоре, вдоль стен которого были протянуты какие-то провода, а под потолком висели лампы, закованные в металлические держатели."
    "В другой ситуации я бы сказал, что это подсобный туннель метро, но вряд ли пионерлагерь «Совёнок» уже достиг такого уровня развития…"
    show dv sad pioneer at center onlayer master with dspr
    dv "Где мы?"
    me "Не знаю, но надо попытаться выбраться!"
    "Залезть по стене на первый взгляд не представлялось возможным, да и вообще было не очень понятно, как мы, упав с такой высоты, остались живы."
    me "Ну что же, придется искать выход в другом месте."
    show dv scared pioneer at center onlayer master with dspr
    dv "Это как?"
    "Испуганно спросила Алиса."
    "Сейчас на ее лице не осталось и следа былой надменности."
    me "Ну, как-как… Должен же здесь быть выход?"
    show dv sad pioneer at center onlayer master with dspr
    dv "Наверное, но в какую сторону идти?"
    th "Хороший вопрос."
    "Направиться в сторону лагеря (хотя бы туда, где он был по моим прикидкам) казалось разумным, но я не замечал там ничего похожего на выходы из подземелья.{w} Значит, возможно, стоит пойти в противоположную сторону."
    show dv shocked pioneer at center onlayer master with dspr
    me "Дай сюда!"
    "Я грубо вырвал у Алисы из рук фонарь и направил его свет в темноту."
    me "Туда!"
    window hide

    scene black onlayer master
    with dissolve

    window show
    "…"
    window hide

    scene cg d4_catac_dv onlayer master
    with dissolve

    window show
    "Мы медленно пробирались вперед, Алиса крепко сжимала мою руку."
    "В другой ситуации я бы, может быть, удивился, смутился, обрадовался (чем черт не шутит), но сейчас мне лишь хотелось поскорее выбраться отсюда."
    "Ссадины от падения болели, в голове ритмично бил тяжелый маятник, да и дрожащий свет фонаря, выхватывающий из темноты одни и те же бетонные стены, не прибавлял уверенности."
    me "Черт, еще же Шурик…"
    dv "Что?"
    me "Ну, а зачем мы вообще ночью в лес пошли? Чтобы Шурика искать!"
    dv "Ой, да забудь ты."
    me "Может, он тоже провалился, как и мы…"
    "Конечно, Алиса была в чем-то права – сейчас не самое подходящее время, чтобы заниматься его поисками – если не выберемся, придется искать нас самих."
    "Однако я не мог просто так выкинуть эту мысль из головы."
    "Как будто перед глазами стоял Шурик и укоризненно смотрел на меня."
    dv "Осторожно!"
    "Закричала Алиса."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "Я остановился в полушаге от массивной железной двери…"
    "Сразу бросился в глаза значок радиационной опасности."
    me "Значит, мы в бомбоубежище…"
    "Пробубнил я себе под нос."
    show dv scared pioneer at center onlayer master with dissolve
    dv "Да, что-то такое слышала…"
    me "Слышала? А почему раньше не сказала?"
    show dv sad pioneer at center onlayer master with dspr
    dv "Откуда я знала, что это важно?"
    me "Ну, пожалуй, да… Ладно."
    hide dv onlayer master with dissolve
    "Я схватился за колесо двери и что есть мочи начал давить на него, пытаясь провернуть."

    play sound sfx_metal_door_handle_rattle

    "Заржавевший металл скрипел, но никак не хотел поддаваться."
    me "Помоги, что ли, что стоишь!"
    "Алиса некоторое время колебалась, но потом крепко схватилась за ручку и начала дергать на себя."

    play sound sfx_open_metal_hatch

    stop ambience fadeout 2

    "Наконец колесо прокрутилось до конца, и дверь открылась."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    with dissolve

    window show
    "Мы оказались в комнате, назначение которой можно было установить безошибочно – бомбоубежище."
    "Шкафы с противогазами и сухпайками, различная аппаратура, койки и трубы вентиляции – все здесь было сделано для того, чтобы пережить ядерную войну.{w} Ну, или по крайней мере выжить после первого удара."
    show dv scared pioneer at center onlayer master with dissolve
    "Алиса еще крепче сжала мою руку."
    me "Что?"
    dv "Что-что…"
    "Шепотом лепетала она."
    show dv sad pioneer at center onlayer master with dspr
    dv "Страшно…"
    me "А чего тут бояться?"
    th "Действительно, чего?"
    th "Мы провалились в заброшенное бомбоубежище, бродим тут впотьмах, пытаемся найти выход…{w} Чего бояться?"
    show dv sad pioneer close at center  onlayer master with dissolve
    "От этих мыслей меня передернуло, и я инстинктивно подошел ближе к Алисе."
    "Она ничего не сказала, лишь слегка покраснела и отвернулась."
    me "Ладно, в любом случае…"
    dv "Что?"
    me "Надо искать выход."
    dv "Ну, вот еще одна дверь."
    "У дальней стены была точно такая же дверь, как та, через которую мы попали сюда."
    hide dv onlayer master with dissolve
    "Однако, сколько бы я ни пытался, она не поддавалась."
    show dv sad pioneer at center onlayer master with dissolve
    dv "Помочь?"
    me "Нет, тут намертво заклинило…"
    "Я окинул комнату взглядом в поисках чего-нибудь, что могло сойти за рычаг, и в дальнем углу заметил фомку."
    me "Отлично!"
    show dv surprise pioneer at center onlayer master with dspr
    "Алиса непонимающе посмотрела на меня."
    me "Сейчас!"

    play sound sfx_insert_crowbar_door

    "Однако и с помощью фомки ручка не сдвинулась ни на сантиметр…"
    "Я без сил опустился на аккуратно застеленную кровать и вздохнул."
    me "Придется идти назад."
    show dv normal pioneer at center onlayer master with dspr
    dv "Но мы же оттуда пришли!"
    "Похоже, к Алисе немного вернулось самообладание, а с ним и привычное нахальство."
    me "Ты можешь остаться здесь – вода, сухпайки, может, радио еще работает…"
    show dv angry pioneer at center onlayer master with dspr
    "Она злобно посмотрела на меня, но ничего не ответила."
    show dv normal pioneer at center onlayer master with dspr
    "Все тело ужасно болело."
    "Я начал это понимать только в состоянии покоя, расслабившись."
    "На ноге сильно кровоточил глубокий порез, все руки были в ссадинах, а в волосах запеклась кровь."
    me "Ты-то… нормально?"
    "Спросил я Алису то ли из вежливости, то ли действительно беспокоясь за нее."
    "Она ответила не сразу."
    show dv sad pioneer at center onlayer master with dspr
    dv "Ну, как тут в такой ситуации может быть нормально."
    me "Я в том плане, что…"
    "Я показал на свой порез на ноге."
    show dv shocked pioneer at center onlayer master with dspr
    dv "Ой!"
    "Вскрикнула Алиса."
    dv "Надо срочно продезинфицировать."
    me "Не надо. Жить буду."
    dv "Нет-нет! Нельзя так, вдруг заражение пойдет, потом ногу отрежут! У меня у деда на войне отрезали."
    "Алиса выглядела и правда обеспокоенной, и я решил с ней не спорить."
    me "Ладно, но мы сейчас далековато от медпункта."
    show dv smile pioneer at center onlayer master with dspr
    dv "Ничего."
    hide dv onlayer master with dissolve
    "Улыбнулась она и принялась рыться в шкафах."
    show dv smile pioneer at center onlayer master with dissolve
    "Действительно, стоило ожидать, что в бомбоубежище найдутся какие-то средства первой помощи, и вскоре Алиса торжествующе продемонстрировала мне аптечку."
    dv "Не дергайся."
    me "Постараюсь."
    "Ватный тампон, смоченный йодом, прошел по ране, словно раскаленный нож, заставив меня крепко стиснуть зубы и зашипеть от боли."
    show dv guilty pioneer at center onlayer master with dspr
    dv "Ой, да ладно, как будто так больно."
    me "Больно! Сама попробуй!"
    "С остальными ранами было попроще, и вскоре я стал напоминать леопарда – весь усеянный коричневыми пятнами."
    me "Спасибо…"
    show dv shy pioneer at center onlayer master with dspr
    dv "Не подумай ничего, просто надо было обработать раны!"
    "Алиса фыркнула и отвернулась."
    me "Да-да…"
    "Устало сказал я и рывком встал с кровати."
    "Непродолжительный отдых явно пошел мне на пользу."
    show dv normal pioneer at center onlayer master with dspr
    me "Ну что, пойдем?"
    "…"
    window hide

    scene cg d4_catac_dv onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Алиса крепко держала меня за руку, идя ровно шаг в шаг."
    "Мы так же медленно шли назад, внимательно высматривая дыру в потолке."
    "Однако туннель казался бесконечным – нам не удалось найти место падения ни через пять, ни через десять минут."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    show dv sad pioneer at center onlayer master with dissolve
    window show
    dv "Мы заблудились?"
    "Грустно спросила Алиса."
    me "Заблудиться можно в лесу, допустим…"
    "Я тут же вспомнил, что это мы как раз с успехом и провернули полчаса назад, но, чтобы еще больше не пугать ее, продолжил уверенным тоном:"
    me "А тут прямой туннель – не заблудишься!"
    dv "Ну и куда мы выйдем?"
    "Похоже, мои слова не сильно успокоили Алису."
    me "Выйдем куда-нибудь, всегда есть выход."
    dv "Всегда ли?"
    me "Ну конечно! Ведь когда его строили, рабочие как-то выбрались наверх, ведь так?"
    dv "Ну да, наверное."
    "Кажется, она изо всех сил старалась выглядеть как обычно, но выходило с трудом – в тусклом свете фонаря было видно, как тело Алисы изредка подрагивает, а на лице застыло выражение крайнего напряжения."
    me "Ладно, пойдем дальше!"
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "Через пару минут я заметил дыру в полу.{w} Достаточно большую, похоже образовавшуюся от взрыва, в которую вполне можно было пролезть."
    show dv scared pioneer at center onlayer master with dissolve
    dv "А что там?"
    me "Не знаю…"
    "Я наклонился и посветил фонарем вниз – сырая земля, какие-то рельсы."
    me "Наверное, шахта."
    show dv surprise pioneer at center onlayer master with dspr
    "Алиса вопросительно посмотрела на меня."
    "Конечно, дыру можно было легко обойти, но чутье мне подсказывало, что дальше ничего хорошего нас не ждет – тупик или очередная закрытая дверь."
    "Хотя, с другой стороны, рассчитывать на то, что выход может скрываться в шахте, было тоже глупо."
    me "Можно проверить. В крайнем случае вернемся – глубина позволяет выбраться потом."
    show dv sad pioneer at center onlayer master with dspr
    "Она сделала какое-то страдальческое выражение, затем отвернулась от света и тихо сказала:"

    stop ambience fadeout 3

    dv "Как скажешь…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "…"
    "Мы действительно оказались в шахте – вдаль уносились давно заржавевшие рельсы, по которым когда-то, наверное, со скрипом проносились набитые доверху вагонетки; стены были укреплены подгнившими балками, а с потолка изредка капала вода."
    "Не уверен, что здесь было страшнее, чем в катакомбах бомбоубежища – скорее там, «наверху», царила постапокалиптика, а здесь, «внизу» – оккультные истории Средневековья."
    "В любом случае мне еще сильнее захотелось убраться отсюда, и как можно быстрее."
    show dv sad pioneer at center onlayer master with dissolve
    "Алиса не сказала ни слова после того, как мы спустились в шахту – лишь шла рядом, крепко сжимая мою руку, – и я начал волноваться."
    me "Все в порядке?"
    dv "Нет."
    "Тихо сказала она."
    me "Ну, я понимаю, что «в порядке» быть не может, но ты как, держишься?"
    dv "Да."
    "Тем же безучастным тоном ответила Алиса."
    me "Ну, это хорошо, потому что…"
    "Я хотел сказать «потому что если и у тебя еще крыша поедет, то тушите свет»."
    me "Потому что выход мы найдем. Обязательно найдем."
    dv "Угу…"
    "Было похоже, что долго она не выдержит."
    th "А значит, надо идти быстрее!"
    "Я прибавил шагу, и через пару десятков метров мы оказались у развилки."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    window show
    me "Так…"
    show dv sad pioneer at center onlayer master with dissolve
    dv "И куда?"
    "Похоже, Алиса окончательно отключилась от внешнего мира, и ее уже не волновало то, что будет с нами, то, как выбраться отсюда."
    me "Ну, сейчас подумаем..."
    th "Направо или налево?{w} А если заблудимся…"
    "Я решил сделать засечку на стене на случай, если вернемся сюда."
    "Вскоре на одной из балок красовался большой крестик, нацарапанный камнем."
    me "Так, вот теперь можно идти…"
    window hide

label dv_mine_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    menu:
        "Налево":
            jump dv_mine_4_1
        "Направо":
            jump dv_mine_2

label dv_mine_1_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Мы вернулись к тому месту, с которого и начинали."
    th "Значит, где-то не там повернули."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            jump dv_mine_4_1
        "Направо":
            jump dv_mine_2

label dv_mine_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_3
        "Направо":
            jump dv_mine_room

label dv_mine_2_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump dv_mine_1_1
        "Направо":
            jump dv_mine_3

label dv_mine_2_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_room
        "Направо":
            jump dv_mine_1_1

label dv_mine_room:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface onlayer master
    with fade

    if mr1 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump dv_mine_2_1

    show dv sad pioneer at center onlayer master with dissolve
    window show
    "Наконец мы вышли из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным нашим спасением был фонарик…"
    th "Сломайся он, и мы вряд ли когда-нибудь выберемся отсюда…"
    "Именно в его свете я заметил в углу какую-то красную тряпку."
    "Это был пионерский галстук!"
    "Теперь-то я точно был уверен, что Шурик здесь."
    me "Шурик! Шурик!"
    "Ответом мне стало лишь эхо."
    dv "Чего кричать? Как будто он тебя слышит..."
    me "Ну а вдруг?"
    "Алиса ничего не ответила, лишь вздохнула."
    "Из этой комнаты не было другого выхода…"
    th "Конечно, возможно, в этих туннелях есть еще места, где мы не бывали…"
    th "Значит, придется искать дальше!"
    window hide

    $ mr1 = mr1 + 1

    jump dv_mine_2_1

label dv_mine_3:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_5
        "Направо":
            jump dv_mine_6

label dv_mine_3_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_6
        "Направо":
            jump dv_mine_2_2

label dv_mine_5:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_4
        "Направо":
            jump dv_mine_6

label dv_mine_5_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_6
        "Направо":
            jump dv_mine_3_1

label dv_mine_4:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_1_1
        "Направо":
            jump dv_mine_7

label dv_mine_4_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump dv_mine_7
        "Направо":
            jump dv_mine_5_1

label dv_mine_4_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump dv_mine_5_1
        "Направо":
            jump dv_mine_1_1

label dv_mine_7:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt onlayer master
    with fade

    if mr2 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump dv_mine_4_2

        window show
    "Мы вышли к некоему подобию шахтерского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовал, что выход где-то рядом, поэтому мы отправились дальше."
    window hide

    $ mr2 = mr2 + 1

    jump dv_mine_4_2

label dv_mine_6:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door onlayer master
    with fade

    window show
    "За очередным поворотом в свете фонаря я разглядел деревянную дверь."
    me "Ну вот, уже что-то!"
    show dv sad pioneer at center onlayer master with dissolve
    dv "Думаешь?"
    "Алиса немного оживилась."
    me "Конечно!"
    "Хотя, если честно, я был совершенно не уверен, что за этой дверью скрывается выход."
    "В любом случае выбора не было."
    window hide

    play sound sfx_open_door_mines

    pause(1)

    window show
    "Я сильно дернул за ручку…"
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    window show
    "Мы оказались в какой-то комнате, которая напоминала то ли котельную, то ли подсобные помещения бомбоубежища."
    "На полу повсюду валялись пустые бутылки, окурки и другой разнообразный мусор."
    "Это значило хотя бы, что из этих пещер существует выход!"
    "Я поводил фонарем по комнате и в дальнем углу увидел…"
    window hide

    scene cg d4_sh_sit onlayer master
    with dissolve

    window show
    "Шурика, скрючившегося в три погибели и трясущегося всем телом."
    me "Шурик!"
    sh "Кто… кто это?"
    "Залепетал он."
    me "Шурик! Мы тебя всю ночь ищем, а ты тут сидишь! Ну-ка вставай немедленно!"
    sh "Никуда я не пойду…"
    "Начал он тихо, но с каждым словом его тон все больше переходил на крик."
    sh "Никуда я с вами не пойду! Вы не существуете! Вас вообще здесь нет! Это галлюцинации! Антинаучно! Да, антинаучно!"
    me "Что значит «вас нет»?! Вот мы, тебя искать пришли!"
    "Алиса все это время стояла молча, но сейчас отпустила мою руку и сделала несколько шагов по направлению к Шурику."
    me "Ты куда?"
    "Тихо спросил я."
    "Она остановилась на мгновенье, но, словно не слыша меня, направилась дальше."

    "Наконец, приблизившись к потерянному пионеру вплотную, Алиса залепила ему хлесткую пощечину."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    show sh scared pioneer far onlayer master at cright
    show dv rage pioneer far onlayer master at cleft
    with dissolve
    window show
    dv "Да ты! Мы чуть не убились, пока тебя искали! Лес этот чертов ночной, бомбоубежища, шахты какие-то! Я вся в синяках из-за тебя! А ты тут что, самогона обпился и белку поймал, скотина?"
    "Шурик ошарашенно смотрел на нее."
    dv "Ну-ка вставай и пошли! Быстро!"
    sh "Нет…"
    "Тихо зашептал он."
    sh "Нет…"
    "Где-то глубоко, на краю сознания промелькнула мысль, что сейчас что-то случится."

    stop music fadeout 2

    "Так бывает – предчувствие, интуиция или просто анализ ситуации: поза, в которой сидел Шурик, выражение его лица, его возможные дальнейшие действия."
    window hide

    scene cg d4_sh_stay onlayer master
    with dissolve

    play music music_list["pile"] fadein 1

    window show
    "А может быть, и все вместе – я метнулся к Алисе, пятно света бешено запрыгало по комнате, на секунду выхватив из темноты обезображенное гримасой безумия лицо Шурика."
    "В руке он сжимал кусок арматуры, и, опоздай я хоть на мгновение, обязательно размозжил бы им голову Алисы."
    "Но я успел."
    window hide

    play sound sfx_break_flashlight

    with vpunch

    pause(1)

    window show

    scene black onlayer master
    with dissolve

    window show
    "Все произошло как во сне – далекий крик девочки, гулкий звук удара, погасший фонарь и тишина, нарушаемая лишь тяжелым дыханием Шурика."
    "Мне понадобилось какое-то время, чтобы прийти в себя."
    me "Ты что же делаешь, придурок?!"
    "Я ощупал руку, но, похоже, все было в порядке – удар пришелся в фонарь.{w} И поэтому мы остались в темноте…"
    sh "Вы меня не заберете, не заберете!"
    "Дьявольский смех Шурика начал быстро удаляться."
    me "Эй! Ты куда это собрался?! А ну-ка вернись!"
    sh "Не заберете…"
    "Уносилось вдаль."

    stop music fadeout 3

    me "Вот урод…"
    "Я попробовал на ощупь разобрать фонарь – но это было бесполезно, Шурик арматурой почти пополам разбил его – и только тогда вспомнил про Алису."
    me "Ты в порядке?"
    "Лишь тихий всхлип и в ту же секунду я почувствовал, как она крепко прижалась ко мне, обхватив руками."
    me "Ладно-ладно, все хорошо…"
    th "Конечно, ничего хорошего, но нужно, чтобы она успокоилась, иначе нам точно не выбраться отсюда."
    "Я аккуратно погладил ее по голове."
    th "Интересно, а плачущая Алиса – это смешно?{w} Наверное, при других обстоятельствах…"
    dv "Страшно…"
    me "Это нормально, мне тоже…"
    "Я про себя отметил такое резкое, неожиданное преображение Алисы."
    th "Хотя в такой ситуации испугается любой.{w} Тем более она девочка…"
    th "Но почему тогда не боюсь я?{w} Нет, не так – почему я еще сохраняю возможность рассуждать здраво?"
    "Может быть, потому что мне надо беспокоиться не только о себе?.."
    me "Ладно, в любом случае надо как-то выбираться."
    dv "Подожди, сейчас…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    show dv sad pioneer onlayer master at center
    with dissolve

    play sound sfx_alisa_lighter

    pause(1)

    window show
    "Тихо сказала Алиса, и комната осветилась тусклым светом зажигалки."
    me "Откуда?"
    show dv smile pioneer at center onlayer master with dspr
    dv "Памятник…"
    "Она как-то беззлобно улыбнулась и протянула зажигалку мне."
    me "Ладно…"
    hide dv onlayer master with dissolve
    "Я быстро окинул комнату взглядом в поисках чего-то, что можно было использовать как факел."
    "На полу нашлись какие-то старые тряпки, палка, а в одной из бутылок – немного жидкости, по запаху напоминающей то ли машинное масло, то ли технический спирт."
    window hide

    play sound sfx_ignite_torch

    pause(1)

    window show
    "Как бы там ни было, через минуту я уже держал в руках худо-бедно горящее нечто."
    show dv normal pioneer at center onlayer master with dissolve
    me "Не знаю, сколько он продержится, поэтому придется идти быстро."
    dv "А куда?"
    "Алиса, похоже, немного пришла в себя."
    me "Пойдем назад. Хотя бы до бомбоубежища. Там по крайней мере есть свет."
    "Она молча кивнула и взяла меня за руку."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "…"
    "Факел горел плохо, приходилось его поджигать заново каждую минуту, а уж про долговечность тряпки, составляющей его основу, и говорить не приходится."
    "Я все больше боялся, что мы останемся в темноте в этой шахте – на зажигалку особо рассчитывать не приходилось."
    "Однако до дыры, ведущей наверх, в катакомбы, мы добрались довольно быстро – видимо, я все же запомнил дорогу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "Выбрались с трудом, приходилось карабкаться практически на ощупь."
    show dv normal pioneer at center onlayer master with dissolve
    dv "И куда дальше?"
    "Отдышавшись, спросила Алиса."
    me "В смысле? Ну, в ту комнату с кроватями, шкафами."
    show dv surprise pioneer at center onlayer master with dspr
    dv "А в какую она сторону?"
    "Я уже было открыл рот, но потом понял, что не имею ни малейшего представления."
    "Дыра со всех сторон казалась одинаковой, как и стены, пол и потолок, а значит, не было никакой возможности точно установить направление."
    me "Ну…"
    show dv sad pioneer at center onlayer master with dspr
    dv "Не знаешь?"
    "Грустно спросила Алиса и села за землю."
    me "Нет."
    window hide

    scene black onlayer master
    with dissolve

    window show
    "Тихо ответил я, потушил факел, чтобы не сжигать его попусту, и пристроился рядом с ней."
    dv "Значит, мы тут умрем?"
    "Она положила голову мне на плечо."
    "Голос Алисы звучал ровно, можно даже сказать, спокойно, но чувствовалось, как ее тело дрожит – то ли от холода, то ли от страха, то ли от всего вместе."
    me "Да ну, глупости! Неприятная ситуация, конечно, но чтобы прямо «умрем»… Утром за нами придут. Ольга Дмитриевна с милицией. Ну и…"
    th "Хотелось бы мне самому в это верить."
    dv "Хорошо…"
    me "Угу…"
    "…"
    window hide

    with fade

    window show
    "Не знаю, сколько мы просидели так…"
    "Я боялся идти «вперед» или «назад», боялся выбрать, ведь факела точно не хватит на то, чтобы вернуться, а оказаться в полной темноте еще хуже, чем ждать спасения здесь."
    "Так у нас хотя бы будет немного света на крайний случай…"

    $ volume(0.2, "sound")

    play sound sfx_open_metal_door

    "Вдалеке послышался какой-то шум."

    $ volume(1.0, "sound")

    play music music_list["sunny_day"] fadein 2

    th "Вот он, наверное, и тот самый случай!"
    "В шуме я безошибочно определил лязг дверных засовов."
    me "Вставай!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    show dv scared pioneer onlayer master at center
    with dissolve

    play sound sfx_ignite_torch

    pause(1)

    window show
    "Я рывком поднял Алису с земли и трясущимися руками зажег факел."
    dv "Что?.."
    "Испуганно спросила она."
    me "Не знаю, но там кто-то есть. Придется бежать!"
    "По правде говоря, я не был уверен, что это хорошая идея."
    th "Вдруг там безумный Шурик?{w} И ведь это еще самое наименьшее из всех возможных зол…"
    "Однако выбора не оставалось."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    window show
    "Камни летели из-под ног, я отчаянно старался не упасть, вытягивая руку с факелом как можно дальше вперед, а второй буквально таща за собой Алису."
    "Она бежала молча, лишь тяжело дышала."
    "Мне отчаянно хотелось оглянуться на нее, но не было ни сил, ни времени."

    stop ambience fadeout 2

    "Наконец впереди показалась открытая дверь, и я прыжком заскочил в бомбоубежище, приготовившись отбиваться от возможных противников…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    with dissolve

    window show
    "Однако комната была пуста…"
    "Я бешено шарил по ней глазами, стараясь в углах разглядеть прячущихся врагов, Шурика, нечистую силу, но все было таким же, как и в первый раз, когда мы здесь были."
    "Разве что дверь, вторая дверь…{w} Она была открыта!"
    show dv scared pioneer at center onlayer master with dissolve
    me "Значит, здесь кто-то проходил!"
    "Торжествующе сказал я."
    dv "Кто?"
    me "Не знаю, Шурик, может быть…"
    dv "Но как он смог ее открыть?"
    me "Да какая сейчас разница! Пойдем!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    window show
    "…"
    "За дверью оказался еще один коридор, медленно поднимающийся вверх."
    th "Значит, мы приближаемся к поверхности."
    "И действительно, через пару сотен метров я наткнулся на лестницу, упирающуюся под потолком в какой-то люк."

    play sound sfx_open_metal_hatch

    "Открыть его не составило большого труда."
    show dv scared pioneer at center onlayer master with dissolve
    dv "А что там?"
    me "Наверняка лучше, чем здесь…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_old_building_night onlayer master
    with dissolve

    window show
    "Я вылез и оказался в полумраке."
    "Однако темнота была действительно {i}светлее{/i}, чем в катакомбах; когда глаза немного привыкли, начали проступать очертания стен, лестницы, двери на улицу, ярко освещенную лунным светом."

    stop music fadeout 3

    "Я помог Алисе выбраться, и мы буквально выскочили наружу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    window show
    "Выход из подземелья находился в каком-то старом здании, по виду напоминавшем то ли детский сад, то ли сельскую школу."
    show dv normal pioneer at center onlayer master with dissolve
    dv "Это, наверное, старый лагерь…"
    "Алиса села на качели и вытерла тыльной стороной ладони пот с лица."
    me "Наверное… Значит, мы его все-таки нашли."
    "Я невольно улыбнулся."
    show dv angry pioneer at center onlayer master with dspr
    dv "Не вижу ничего смешного!"
    "Она нахмурилась и недовольно надулась.{w} Короче говоря, стала такой же, как обычно."
    me "Что, тут уже не страшно?"
    dv "Да мне и тогда страшно не было!"
    me "Ну-ну!"
    dv "Да!"
    me "Ради Бога…"
    "Я был зол…"
    th "Я действительно обиделся на Алису – если бы не я, она бы до сих пор там и сидела, в шахте этой чертовой!"
    show dv scared pioneer at center onlayer master with dspr
    dv "Ты куда?"
    "Уже менее уверенно спросила она, когда я развернулся и медленно направился в сторону лагеря."
    me "Назад."
    show dv shocked pioneer at center onlayer master with dspr
    dv "Эй!"
    "Алиса тут же подскочила и зашагала рядом."
    "Мне на секунду захотелось сказать какую-то гадость, но вступать в очередную словесную перепалку я был просто не готов…"
    "Мы удивительно быстро нашли тропу, ведущую в лагерь, даже те две ямы, в которые провалились."
    "И ведь нам оставалось до старого лагеря пройти всего каких-то пару сотен метров…"

    stop ambience fadeout 2

    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show dv shy pioneer at center onlayer master with dissolve
    window show
    "На площади я остановился и повернулся к Алисе."
    me "Ладно…"
    dv "Ладно…"
    "Она выглядела неуверенно, даже немного смущенно."
    me "Тогда…"
    dv "Угу…"
    "Где-то в глубине души мне хотелось наорать на нее, обругать, может, обматерить даже.{w} С другой стороны – провести душеспасительную беседу."
    hide dv onlayer master with dissolve
    "Но в итоге я просто промолчал, развернулся и медленно направился в сторону домика вожатой."
    "Однако что-то упорно нарушало ночную тишину…{w} Я прислушался и понял, что это храп…"
    "Шурика, который мирно спал на скамейке!"
    me "Эй!"
    "Крикнул я Алисе, которая еще не успела далеко уйти."
    me "Ну-ка вставай!"
    show sh upset pioneer onlayer master at cright
    show dv angry pioneer onlayer master at cleft
    with dissolve
    "Шурик медленно пришел в себя и непонимающе посмотрел на нас."
    sh "А что, уже утро?"
    me "Утро? Да, утро…"
    "Иногда мысль работает медленнее действия."
    "Конечно, сначала идет импульс в мозгу, по нейронным связям проходит ток, отдавая команду телу."
    "Но, наверное, не всегда этот процесс бывает до конца осознанным.{w} Именно поэтому моя рука на автомате поднялась и быстро влетела Шурику под дых, а только потом я осознал, что сделал."
    show sh scared pioneer at cright onlayer master with dspr
    "Он закашлялся, пытаясь поймать дыхание, и скрючился на скамейке."
    me "Что ты там учудил?!"
    "Мне стало немного стыдно – может быть, не стоило так грубо…"
    sh "Ты… ты о чем?"
    "Шурик со страхом в глазах смотрел на меня."
    me "В шахте!"
    sh "В какой шахте?"
    "Он недоуменно повертел головой."
    sh "И почему я тут?"
    sh "И почему вы тут?"
    show dv rage pioneer at cleft onlayer master with dspr
    dv "Ты что, прикалываешься?"
    "В разговор вмешалась Алиса."
    dv "Ты меня там чуть не убил! А теперь будешь притворяться, что ничего не было?"
    sh "Чего не было?"
    me "Ты правда не помнишь?"
    sh "Нет…"
    me "А что последнее помнишь?"
    show sh upset pioneer at cright onlayer master with dspr
    "Шурик напрягся."
    sh "Ну, я утром пошел в старый лагерь. Там можно найти детали для робота и…"
    me "И?"
    sh "И все… Дальше не помню. Проснулся здесь."
    "Я тяжело вздохнул и отвернулся."
    me "Ладно, спокойной ночи…"
    show dv shocked pioneer at cleft onlayer master with dspr
    dv "Эй, ты куда?"
    hide dv onlayer master
    hide sh onlayer master
    with dissolve
    "Я не обращал внимания на Алису и быстро пошел к домику Ольги Дмитриевны.{w} Она же о чем-то ругалась с Шуриком."

    stop ambience fadeout 2

    "…"
    window hide

    scene stars onlayer master
    with dissolve

    play music music_list["waltz_of_doubts"] fadein 3

    window show
    "Я сидел в гамаке и смотрел на звезды."
    "Сегодня ночью они казались ярче, чем обычно."
    "Может быть, потому что еще недавно моим единственным источников света был фонарь, а потом – факел."
    "Звезды – ярче фонаря, тем более – факела.{w} Многие звезды, наверное, даже ярче Солнца, только они далеко…"
    me "И зачем пришла?"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "Спросил я, не оборачиваясь в сторону дорожки – шаги Алисы в ночи были слышны за много метров."
    show dv shy pioneer at center onlayer master with dissolve
    dv "Да я…"
    me "Что Шурик сказал?"
    dv "Сказал, что ничего не помнит, что «антинаучно», еще какой-то бред нес."
    me "Я думаю, он правда не помнит – шок, стрессовая ситуация."
    th "Кто бы говорил?{w} Ведь я сам еще недавно был в такой же «ситуации»."
    th "Впрочем, я и сейчас в ней.{w} И что же, у меня тоже амнезия?"
    me "Так зачем пришла?"
    "Впрочем, наверное, я и так знал ответ – ведь почему-то спать не лег, а ждал ее здесь."
    show dv shy pioneer close at center  onlayer master with dissolve
    dv "Ну я…"
    "Алиса села рядом."
    dv "Поблагодарить хотела… Ведь там это... Ты это... Ну…"
    me "Не за что."
    "Спокойно сказал я и откинулся назад."
    dv "Ну ладно тогда…"
    show dv shy pioneer at center onlayer master with dissolve
    "Она встала и собралась уходить."
    me "Если ты думаешь, что я злюсь, то не стоит. Все в порядке."
    show dv angry pioneer at center onlayer master with dspr
    dv "Я и не думала!"
    "Завелась Алиса."
    me "Ну тогда хорошо."
    show dv normal pioneer at center onlayer master with dspr
    dv "Ладно…"
    me "Угу…"
    dv "Тогда…"
    me "Да иди уже!"
    "Беззлобно сказал я и махнул рукой."
    show dv angry pioneer at center onlayer master with dspr
    dv "Пойду, когда посчитаю нужным!"
    me "То есть сейчас ты нужным это не считаешь?"
    dv "Считаю!"
    me "Ну? И что тебя останавливает?"
    show dv rage pioneer at center onlayer master with dspr
    dv "Дебил!"
    hide dv onlayer master with dissolve
    "Алиса топнула ногой и быстро направилась прочь от домика вожатой."
    "Я тяжело вздохнул и встал."
    "Голова от усталости кружилась ужасно."

    stop ambience fadeout 2

    th "Хорошо хоть Ольга Дмитриевна уже спит, значит, не придется перед ней объясняться…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    window show
    "Кое-как я доковылял до своей постели и упал, не раздеваясь."
    th "Все же Алиса…{w} Алиса…"
    "Я уже не знал, что о ней думать."
    "И не потому что она вела себя как-то странно.{w} Нет, как раз наоборот – все в ее поведении было весьма логично и объяснимо."
    "Даже то, что она пришла поблагодарить."
    "Я поймал себя на мысли, что гораздо больше думаю об Алисе, чем обо всем, что случилось за ночь."
    "Хотя, если разобраться, в этом не было ничего сверхъестественного."
    "Неприятно – да, пугающе, даже страшно – да.{w} Что-то, имеющее отношение к моему попаданию сюда, – вряд ли."
    "С этими мыслями я заснул."
    window hide

    stop music fadeout 5

    scene black onlayer master
    with fade3

    $ renpy.pause(3)

    jump day5_main1

label day4_us:

    hide u onlayer master
    hide sl onlayer master
    with dissolve
    show us surp1 pioneer at right onlayer master with dissolve
    us "И я пойду тоже!"
    "Я посмотрел на Ульяну с изумлением."
    "Ее жажда приключений, похоже, не имела границ."
    show us laugh2 pioneer at right onlayer master with dspr
    us "А что, ночь, привидения, старый лагерь – весело ведь!"
    th "С одной стороны, такая компания всегда сулит собой неприятности, но с другой – вдвоем оно хотя бы безопаснее…"
    show us surp1 pioneer at right onlayer master with dspr
    show mt smile pioneer at left onlayer master with dspr
    mt "Вот и отлично!"
    hide mt onlayer master
    hide un onlayer master
    with dissolve

    stop music fadeout 3

    "Попрощавшись с остальными девочками и Ольгой Дмитриевной, мы остались одни."

    play ambience ambience_camp_center_evening fadein 3

    me "Ты считаешь, что это просто увеселительная прогулка?"
    show us surp1 pioneer onlayer master at right:
        linear 1.0 xalign 0.5
    us "Ну да, а что такого?"
    "Ульянка хихикнула."
    me "Да нет, ничего… В самом деле…"
    "Я вздохнул."
    show us laugh pioneer onlayer master with dspr
    us "Сейчас, подожди!{w} Я за фонарем сбегаю!"
    me "Давай…"
    hide us onlayer master with dissolve
    "Я как раз сам хотел предложить."
    th "Похоже, мне сегодня предстоит не только идти ночью в заброшенный лагерь, но и следить за неугомонным ребенком…"
    "Ведь как-никак именно им Ульяна и являлась."
    th "В общем, придется быть осторожным вдвойне."
    "По рассказам Электроника, старое здание построили сразу после войны."
    "Оно было похоже на детский сад (или на барак, как я предполагал) и рассчитано на куда меньшее число пионеров, чем вмещал нынешний лагерь."

    stop ambience fadeout 2

    "Забросили же его лет двадцать назад…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    show us laugh pioneer at center onlayer master with dissolve
    window show
    "Ульянка шагала вприпрыжку, словно все происходящее для нее – лишь развлечение."
    "Мне же было откровенно не по себе."
    "Собственно, нормальное состояние для человека в моем положении – ночной лес, так и норовящие выскочить отовсюду страшные звери и птицы, полнолуние и сам этот мир, в который я попал лишь недавно."
    "Возможно, мне было бы даже проще одному – не надо следить за непослушным ребенком, бегущим передо мной."
    th "И как она еще ни за одну кочку не зацепилась?"
    me "Слушай, ты бы поаккуратнее…"
    show us smile pioneer at center onlayer master with dissolve
    us "А то что?"
    "Она так резко обернулась, что я даже вздрогнул."
    me "Ничего. Убьешься где-нибудь."
    show us grin pioneer at center onlayer master with dspr
    us "Значит, переживаешь за меня?"
    me "Конечно. Ну, в смысле, это нормально при данных обстоятельствах."
    show us shy2 pioneer at center onlayer master with dspr
    "Ульянка надулась."
    us "Наверное…"
    me "Слушай…"
    show us normal pioneer at center onlayer master with dspr
    "Я решил продолжить разговор – так спокойнее да и страх ощущается меньше."
    me "А что за старый лагерь вообще? Ты на площади говорила…"
    show us smile pioneer at center onlayer master with dspr
    us "Да, очень страшное место! Говорят, все пионеры там умерли и стали приведениями, которые охраняют свое последнее земное пристанище."
    me "Умерли от чего?"
    "В ее страшные истории вообще верилось с трудом."
    show us dontlike pioneer at center onlayer master with dspr
    us "Ну откуда я знаю? Я даже тогда не родилась еще."
    me "Но рассказываешь уверенно."
    show us grin pioneer at center onlayer master with dspr
    us "Информация из надежного источника!"
    me "Это откуда же? От Алисы?"
    us "Не скажу!"
    me "Ну ладно, и что дальше? Умерли, привидениями стали и?"
    show us normal pioneer at center onlayer master with dspr
    us "Ну и все…"
    me "Как это «все»?"
    show us smile pioneer at center onlayer master with dspr
    us "Теперь по старому лагерю бродят души умерших пионеров и забирают с собой, в мир мертвых, всех, кто осмелится переступить через порог!"
    me "Ой, ладно, шагай давай!"
    hide us onlayer master with dissolve
    window hide

    with fade

    window show
    "…"

    stop ambience fadeout 2

    "Время шло, мы все глубже заходили в чащу, деревья сомкнули ряды, а я вдруг понял, что в лесу внезапно воцарилась почти полная тишина."
    "Как будто ночные птицы затаились в ожидании чего-то, насекомые поспешили зарыться под землю, даже ветер стих."
    "Начало казаться, что лунный свет, изредка пробивающийся сквозь пушистую шапку листвы, издает какие-то звуки – звенит, словно натянутая струна."
    "Наконец деревья начали расступаться, и мы вышли на большую поляну…"
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    window show
    "Посреди нее стояло старое здание, больше напоминающее детский сад."

    play music music_list["sunny_day"] fadein 5

    "Его окружал довольно плотный туман, и создавалось ощущение, что мы попали на кладбище, а этот старый лагерь – его центр, склеп."
    "Ведь если верить Ульянке, там бродят души десятков пионеров – чем не братская могила…"
    "Я поежился и крепче сжал в руке фонарь."
    me "Жуткое место, ей-богу…"
    show us smile pioneer at center onlayer master with dissolve
    us "Ой, да ладно тебе!"
    "Она весело похлопала меня по спине, от чего стало еще страшнее."
    hide us onlayer master with dissolve
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve2

    window show
    "Я уже собирался двинуться вперед, как вдруг Луна выглянула из-за туч, осветив поляну, здание старого лагеря, нас."
    "В ее свете все казалось как будто менее старым – четче стали заметны осыпавшаяся кое-где кладка, проржавевшая горка и карусель, чудом сохранившиеся в некоторых окнах стекла."
    "Однако мне начало чудиться, что из леса, оттуда, где царил вечный мрак, над которым не властна даже Луна, на поляну начали наступать неведомые чудовища."
    th "Хотелось бы надеяться, что они, как вампиры, боятся света…{w} Хотя, возможно, они, наоборот, как оборотни – в полнолунье превращаются в огромных волков…"
    show us normal pioneer at center onlayer master with dissolve
    us "Чего встал?"
    me "Думаю…"
    us "О чем?"
    me "Ну, что Шурик мог забыть в таком месте?"
    show us dontlike pioneer at center onlayer master with dspr
    us "А мне откуда знать? Вот найдем его и спросим."
    me "Ну да, логично…"
    hide us onlayer master with dissolve
    "Пробубнил я себе под нос и направился за Ульянкой."
    "Сейчас она шла куда аккуратнее – смотрела себе под ноги, иногда останавливалась, даже пару раз обернулась на меня."
    "Понятное дело, ведь в некоторых местах трава доходила ей чуть ли не до груди, а кто знает, что может валяться на земле – железки, камни, битое стекло…"
    show us smile pioneer at center onlayer master with dissolve
    "Мы все же добрались до двери, Ульянка остановилась и сказала:"
    us "Ну! Вот и пришли!"
    me "Ты как будто гонку выиграла… Только это не игра."
    show us dontlike pioneer at center onlayer master with dspr
    us "Какой ты… какой ты…"
    me "Какой?"
    show us upset pioneer at center onlayer master with dspr
    us "Скучный!"

    stop ambience fadeout 2

    "Я скорчил гримасу недовольства и уверенно шагнул через порог – все же Ульяну вперед было пускать попросту опасно, и для нее самой, и для меня, и для человечества в целом, наверное."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_old_building_night onlayer master
    with dissolve

    window show
    "Внутри старый лагерь производил еще более удручающее впечатление, чем снаружи – мне даже на секунду стало жалко его.{w} Хотя скорее людей, живших здесь когда-то."
    "Ведь наверняка тут раньше через край плескалась простая детская радость, бегали пионеры, играя в игры, о которых я давно забыл, строгая вожатая, вроде Ольги Дмитриевны, следила за порядком, одна смена заканчивалась, начиналась новая."
    "А теперь все – вот так, стоит разрушенное, гниющее, забытое."
    show us surp2 pioneer at center onlayer master with dissolve
    us "Смотри!"
    "Ульянка протянула мне старую увечную куклу, развалившуюся от сырости – еще один осколок прошлого."
    me "Ну и?"
    show us sad pioneer at center onlayer master with dspr
    us "Ничего…"
    "Она вышла из луча света, но я успел заметить грустное выражение на ее лице."
    me "Грустное место."
    us "Страшное!"
    me "Ничего особо страшного пока не вижу."
    "И действительно, здесь было куда спокойнее, чем снаружи."
    "Как на кладбище – пока ищешь путь до могилы, проходя между бесконечными рядами надгробий, чувствуешь внутренний дискомфорт, но потом, наконец найдя ту самую, на душе становится спокойно.{w} Словно сам лег рядом…"
    "Я поежился и обвел фонарем помещение.{w} Никаких следов Шурика."
    "Впрочем, что я ожидал найти? Его труп?"
    me "Похоже, его тут нет…"
    show us surp2 pioneer at center onlayer master with dspr
    us "Ну, а второй этаж?"
    me "Шурик!"
    "Громко закричал я, но ответом мне стало лишь эхо."
    us "Шурик, выходи!"
    me "Вот видишь…"
    show us smile pioneer at center onlayer master with dspr
    us "Все равно надо проверить."
    me "Ладно-ладно…"
    hide us onlayer master with dissolve
    window hide

    with fade

    window show
    "…"
    "Однако и на втором этаже не оказалось никаких признаков жизни."
    "Я сел на лестницу и обреченно опустил голову на руки."
    me "И куда дальше? Мы же весь лес не сможем обойти. Да и спать уже рубит…"
    show us dontlike pioneer at center onlayer master with dissolve
    us "Что ты все ноешь?"
    "Возмутилась Ульянка."
    us "Ноет и ноет. Как ребенок."
    me "А что, я не прав?"
    us "Прав или нет – какая разница? Раз мы ищем Шурика, то должны найти!"
    me "Но как?"
    "Взмолился я."
    us "Не знаю! Как-нибудь!"
    "Ульянка сейчас напоминала строгую учительницу, а я – нерадивого школьника."
    th "Хотя все же должно быть наоборот?"
    show us surp3 pioneer at center onlayer master with dspr
    us "Смотри!"
    "Я посветил в направлении, указанном ей, и заметил в полу люк, вокруг которого, словно бруствер, валялся мусор.{w} Похоже, его недавно открывали."
    us "Наверняка он там!"
    hide us onlayer master with dissolve
    "Ульянка подскочила к люку и попыталась его открыть, вся надувшись от натуги."
    me "Ну и зачем бы он туда полез? Может, это… Не знаю, жители деревни какой-нибудь. Тут же есть рядом деревни?"
    show us surp2 pioneer at center onlayer master with dissolve
    us "Не знаю…"
    "Тяжело дыша, ответила Ульянка.{w} Открыть люк у нее так и не получилось."
    "Я задумался."
    "Конечно, существовала возможность того, что Шурик действительно там."
    "В конце концов, об этом мире я знаю немного – в сущности, ничего, – с какой стати местные обитатели должны вести себя согласно моей логике?{w} Вдруг он спасался от волков?"
    th "Впрочем, какие тут волки – совы разве что."
    me "Ладно, давай посмотрим…"
    hide us onlayer master with dissolve
    "Я напрягся и с трудом откинул-таки крышку люка."

    play sound sfx_open_metal_hatch

    "Она с грохотом ударилась об рассохшийся деревянный пол, и Ульянка тут же свесилась в образовавшийся проем, освещая фонарем подвал или то, что скрывалось там внизу."
    us "Какой-то туннель!"
    me "Туннель?"
    show us dontlike pioneer at center onlayer master with dissolve
    "Я вынул ее за шкирку из люка, чтобы посмотреть самому."
    us "Эй!"
    me "Любопытной Варваре на базаре нос оторвали!"
    "Действительно, в темноту уходил длинный туннель, напоминающий подземелья из какой-то компьютерной игры."
    "На первый взгляд никакой опасности – ни воды по пояс, ни крыс, ни зомби…"
    me "Ладно, давай спустимся посмотрим. Только аккуратно!"
    show us laugh pioneer at center onlayer master with dspr
    us "Так точно!"
    "Ульянка аж вся засияла."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Внизу было ужасающе темно – фонарь спасал несильно, – из мрака в тусклом свете выскакивали на мгновение бетонные стены, опутанные какими-то проводами, лампы, уцепившиеся за потолок, и мусор, которым был обильно усеян пол."
    window hide

    scene cg d4_catac_us onlayer master
    with dissolve

    window show
    "Мы продвигались медленно, я держал Ульянку за руку, опасаясь, что она убежит вперед."
    "Хотя, наверное, волноваться стоило не только за нее, но и за себя – что останусь один в этой давящей темноте."
    me "Может, вернемся уже? Не мог Шурик так далеко зайти…"
    us "А если у него фонарь был?"
    me "Ну, и с фонарем даже… Что ему вообще здесь делать?"
    us "Не знаю! Разве тебе не интересно, что там дальше?"
    me "Ни капельки, мне сейчас куда интереснее…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "Я не успел закончить фразу – перед нами словно из-под земли возникла тяжелая металлическая дверь."
    "В глаза сразу бросился значок радиационной опасности."
    me "Бомбоубежище?"
    "Тут же догадался я."
    show us laugh pioneer at center onlayer master with dissolve
    us "Наверное."
    me "Ты что-нибудь слышала об этом?"
    show us normal pioneer at center onlayer master with dspr
    us "Не знаю, какая сейчас разница?"
    me "Разница?.. А вдруг там радиация!"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Какая радиация? Откуда?"
    me "Да, пожалуй…"
    hide us onlayer master with dissolve
    "Я схватился за колесо двери и попытался его повернуть."

    play sound sfx_metal_door_handle_rattle

    "К моему удивлению, оно поддалось и заскрипело, словно умирающий динозавр."

    play sound sfx_open_metal_door

    "Наконец дверь открылась, и Ульянка тут же забежала внутрь."

    stop ambience fadeout 3

    me "Эй!"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    with dissolve

    window show
    "За дверью находилось, видимо, основное помещение бомбоубежища."
    "Рядом со мной стояли несколько кроватей, у дальней стены – какие-то приборы, шкафы, а под потолком ярко горели лампы дневного света."
    me "Откуда тут электричество? Аварийные генераторы еще работают, что ли…"
    "Я выключил фонарь, чтобы сэкономить батарейку."
    "Ульянка тут же принялась рыться в шкафах, извлекая оттуда противогазы, какие-то пакеты, различные инструменты."
    me "Тебе больше заняться нечем?"
    show us dontlike pioneer at center onlayer master with dissolve
    us "Нечем!"
    "Она недовольно посмотрела на меня."
    "Я сел на аккуратно застеленную кровать и еще раз осмотрелся."
    "Прямо напротив меня в стене была точно такая же дверь, как та, через которую мы попали сюда."
    th "Может быть, Шурик (если он вообще тут был) пошел туда? Хотя зачем?"
    show us normal pioneer at center onlayer master with dspr
    us "Что загрустил?"
    me "Устал…"
    "Честно признался я."
    show us laugh pioneer at center onlayer master with dspr
    us "Ну так отдохни!"
    "Ульянка подскочила ко мне и сильно толкнула руками в грудь."
    with vpunch
    "От неожиданности я отлетел назад, больно ударившись головой о стену."
    me "Ты что творишь!"
    "Я схватил ее за руки и резко рванул на себя."
    show us surp3 pioneer close at center  onlayer master with dissolve
    "Она потеряла равновесие и плюхнулась рядом."
    us "Больно!"
    me "Сама начала!"
    show us smile pioneer close at center onlayer master with dspr
    "Ульянка показала язык и села."
    me "Ладно, что дальше?"
    us "Ну вот же, еще одна дверь."
    me "Ну да, конечно… Шурик предчувствовал ядерную войну и решил заранее спрятаться, так что ли?"
    show us laugh pioneer close at center onlayer master with dspr
    us "Ну а вдруг!"
    me "Что вдруг? Это бомбоубежище слишком близко к поверхности, оно разве что от радиации защитит, но если бомбы упадут рядом…"
    show us grin pioneer close at center onlayer master with dspr
    us "Ты так серьезно к этому подходишь."
    "Ухмыльнулась она."
    "Я уже и правда не знал, когда с ней нужно быть серьезным, а когда – шутить."
    "Наверное, разница в возрасте действительно сказывалась столь сильно?"
    th "Сколько, 10 лет, больше?"
    "Я вздохнул и встал с кровати."
    me "Ладно, давай попробуем."
    hide us onlayer master with dissolve
    "Однако эта дверь оказалась куда менее сговорчивой, чем предыдущая."

    play sound sfx_metal_door_handle_rattle

    "Засовы скрипели, но колесо не сдвинулось ни на сантиметр."
    me "Заело, похоже…"
    show us surp2 pioneer at center onlayer master with dissolve
    us "Ну-ка дай-ка!"
    hide us onlayer master with dissolve

    play sound sfx_insert_crowbar_door

    "Ульянка подскочила к двери, отталкивая меня, с непонятно откуда взявшейся фомкой в руке и налегла всем своим небольшим весом."
    window hide

    play sound sfx_fall_metal_door

    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living_nodoor onlayer master
    with vpunch

    window show
    "Так у нас действительно появлялись кое-какие шансы – я помог ей, и вскоре дверь с грохотом упала на пол."
    "Оказалось, что петли насквозь проржавели."
    th "Значит, не все {i}тогда{/i} делали на века."
    "За дверью был почти такой же коридор, как тот, по которому мы пришли сюда."
    me "Давай, без глупостей!"
    "Я взял Ульянку за руку и вышел из комнаты."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "…"
    "Туннель словно не имел конца."
    "Потолок как будто становился все ниже, хотя умом я понимал, что его высота не меняется."
    "Однако Ульянке, кажется, было совершенно наплевать – она шла, что-то напевая себе под нос."
    "Меня это раздражало все сильнее и сильнее."
    me "Тебе, похоже, весело…"
    show us laugh pioneer at center onlayer master with dissolve
    us "Конечно весело! А тебе нет?"
    me "Нет. И не вижу вообще причин веселиться. Побыстрее бы найти этого Шурика и выбраться отсюда!"
    us "Может, его вообще тут нет."
    me "Ну и какого черта тогда…"
    show us surp2 pioneer at center onlayer master with dspr
    us "Смотри!"
    "Ульянка выхватила у меня фонарь и посветила куда-то на пол."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "В паре метров от нас зияла довольно большая дыра."
    show us surp2 pioneer at center onlayer master with dissolve
    us "Может, он там!"
    "Она подошла к краю и наклонилась."
    us "Рельсы какие-то…"
    "Похоже, под этим туннелем была шахта."
    "Глубина ямы позволяла выбраться оттуда, и я уже понял, что скажет Ульянка дальше."
    us "Давай!"
    hide us onlayer master with dissolve

    play sound sfx_jump_into_hole_2

    "Я было хотел возразить, но она спрыгнула вниз, оставив меня в кромешной темноте."
    me "Эй!"

    stop ambience fadeout 3

    "Пришлось последовать за ней."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "Не знаю, что здесь добывали, но забросили эту шахту давно – доски, укрепляющие потолок, отсырели, рельсы заржавели, кое-где земля проломила стены."
    "Да и вообще, весь туннель, уходящий в неизвестность, доверия не вызывал – казалось, что он вот-вот готов обвалиться, похоронив нас."
    show us smile pioneer at center onlayer master with dissolve
    us "Пойдем!"
    "Ульянка отчаянно тянула меня за руку."
    me "Куда? Зачем? Ну что Шурику тут делать?"
    show us normal pioneer at center onlayer master with dspr
    us "Ну а вдруг!"
    "Она сделала серьезное лицо."
    us "Вдруг он сидит там, раненый, ждет помощи, а мы вот так развернемся и уйдем, оставив его умирать…"
    "Я еще раз мысленно оценил высоту потолка и медленно направился за неугомонной Ульянкой."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    window show
    "…"
    "Вскоре мы оказались на развилке."
    show us smile pioneer at center onlayer master with dissolve
    us "Давай направо!"
    me "Стой!"
    "Я схватил ее за руку."
    show us dontlike pioneer at center onlayer master with dspr
    us "Ну что еще?"
    me "А если там тупик? Да и ладно бы тупик – если там лабиринт целый?"
    show us normal pioneer at center onlayer master with dspr
    us "Ну…"
    "Она задумалась."
    show us smile pioneer at center onlayer master with dspr
    us "Давай тогда отметим начало маршрута!"
    "Ульянка схватила с земли довольно большой камень и нацарапала на одной из балок, держащих потолок, крестик."
    me "Думаешь, сильно поможет?"
    us "Поможет!"
    th "Не уверен, но выбирать, куда идти, все равно придется мне – такое я не могу доверить Ульянке."
    window hide

label us_mine_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    menu:
        "Налево":
            jump us_mine_4_1
        "Направо":
            jump us_mine_2

label us_mine_1_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Мы вернулись к тому месту, с которого и начинали."
    th "Значит, где-то не там повернули."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            jump us_mine_4_1
        "Направо":
            jump us_mine_2

label us_mine_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_3
        "Направо":
            jump us_mine_room

label us_mine_2_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump us_mine_1_1
        "Направо":
            jump us_mine_3

label us_mine_2_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_room
        "Направо":
            jump us_mine_1_1

label us_mine_room:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface onlayer master
    with fade

    if mr1 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump us_mine_2_1

    window show
    "Наконец мы вышли из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным нашим спасением был фонарик…"
    "Сломайся он, и мы вряд ли когда-нибудь выбрались бы отсюда…"
    "Именно в его свете я заметил в углу какую-то красную тряпку."
    "Это был пионерский галстук!"
    "Теперь-то я точно был уверен, что Шурик здесь."
    me "Шурик! Шурик!"
    show us surp2 pioneer at center onlayer master with dissolve
    us "Шурик!"
    show us normal pioneer at center onlayer master with dspr
    "Ответом нам стало лишь эхо."
    me "Надеюсь, с ним все в порядке…"
    show us surp1 pioneer at center onlayer master with dspr
    us "Ничего! Найдем его!"
    th "Но куда он мог отсюда уйти?"
    "Из этой комнаты не было другого выхода…"
    th "Конечно, возможно, в этих туннелях есть еще места, где мы не бывали…"
    th "Значит, придется искать дальше!"
    window hide

    $ mr1 = mr1 + 1

    jump us_mine_2_1

label us_mine_3:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_5
        "Направо":
            jump us_mine_6

label us_mine_3_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_6
        "Направо":
            jump us_mine_2_2

label us_mine_5:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_4
        "Направо":
            jump us_mine_6

label us_mine_5_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_6
        "Направо":
            jump us_mine_3_1

label us_mine_4:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_1_1
        "Направо":
            jump us_mine_7

label us_mine_4_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump us_mine_7
        "Направо":
            jump us_mine_5_1

label us_mine_4_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump us_mine_5_1
        "Направо":
            jump us_mine_1_1

label us_mine_7:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt onlayer master
    with fade

    if mr2 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump us_mine_4_2

    window show
    "Мы вышли к некоему подобию шахтерского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовал, что выход где-то рядом, поэтому мы отправились дальше."
    window hide

    $ mr2 = mr2 + 1

    jump us_mine_4_2

label us_mine_6:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door onlayer master
    with fade

    window show
    "Наконец луч фонаря выхватил из темноты старую деревянную дверь."
    show us smile pioneer at center onlayer master with dissolve  
    us "Пришли!"
    me "Куда?"
    us "Куда-то. Не знаю."
    "В чем-то она была права – хотя бы нам удалось выбраться из лабиринта."
    "После всех этих поворотов и развилок я был совершенно не уверен, что мы вообще сможем вернуться обратно, но, с другой стороны, почему бы этой шахте не иметь несколько выходов?"
    window hide

    play sound sfx_open_door_mines

    pause(1)

    show us normal pioneer at center onlayer master with dspr
    window show
    "Ульянка открыла дверь и пристально уставилась в темноту."
    me "Что, не пойдешь первая, как обычно?"
    us "Ну…"
    me "Ладно."

    stop ambience fadeout 3

    "Я сделал шаг через порог."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    window show
    "За дверью скрывалась небольшая комната – наверное, подсобное помещение бомбоубежища."
    "На полу повсюду валялись бутылки и окурки, а значит, здесь кто-то был до нас."
    "Не особо ободряющий факт сам по себе, однако теперь я точно знал, что из шахты есть и другой выход (не могли же {i}они{/i} сюда прийти тем же маршрутом, что и мы)."
    "Луч фонаря медленно скользил по помещению, тщательно изучая каждый закуток, и вдруг из темноты появилась фигура человека…"
    window hide

    scene cg d4_sh_sit onlayer master
    with dissolve

    window show
    "Шурика, скрючившегося в три погибели возле одной из стен!"
    me "Эй! Вот ты где! Мы тебя всю ночь ищем, а ты…"
    "Но он, похоже, не обратил особого внимания на факт нашего появления – продолжил сидеть и что-то бормотать себе под нос."
    me "Шурик!"
    sh "Кто… кто это?"
    me "Кто-кто! Спасатели твои! Вставай и пошли отсюда!"
    sh "Никуда я с вами не пойду!"
    "Бессвязно зашептал он."
    sh "Вы опять будете меня водить по туннелям, я знаю! Никуда я не пойду! Буду сидеть здесь – здесь вы меня не достанете!"
    me "Прекрати чушь нести!"
    "Кажется, у него совсем крыша поехала."
    sh "Нет, нет! В этот раз вы меня не обманете."
    me "Да хватит уже…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    play sound sfx_armature_swish

    show sh rage pioneer at center onlayer master with dissolve
    window show
    "Я сделал несколько шагов по направлению к Шурику, но он тут же вскочил и потряс над головой арматурой."
    sh "Не подходи! Отстаньте от меня!"
    me "Да успокойся ты! Это же я, Семен? Не узнал?"
    sh "Семен?.. Нет, ты не Семен!"
    "Я и не заметил, что Ульянка, все это время стоявшая рядом, куда-то исчезла."

    stop music fadeout 2

    sh "Ты не Семен, и я тебя сейчас…"
    window hide

    scene cg d4_sh_stay onlayer master
    with dissolve

    play music music_list["pile"] fadein 1

    window show
    "В дрожащем свете фонаря на секунду мелькнула рука Шурика, сжимающая арматуру, я инстинктивно закрыл голову и…"
    window hide

    scene black onlayer master
    with dissolve

    window show
    "Ничего."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    show us laugh pioneer at center onlayer master with dissolve 
    window show
    "Когда я открыл глаза, он уже исчез, а рядом стояла Ульянка и посмеивалась, держа арматуру в руках."

    stop music fadeout 3

    us "Как настоящий разведчик!"
    me "Разведчик, да…"
    "Откуда-то издалека, из туннелей, донесся дьявольский смех Шурика."
    show us normal pioneer at center onlayer master with dspr
    us "Убежал…"
    me "Да и хрен с ним, пусть хоть сдохнет там!"
    "Я смачно плюнул на пол и облокотился о стену."

    play music music_list["sunny_day"] fadein 3

    th "Пожалуй, если бы не Ульяна…"
    "Я был совершенно не готов к подобному развитию событий!{w} Вряд ли Шурик убил бы меня, но покалечил бы – здорово."
    "А лежать раненым тут равносильно смерти – когда еще придет помощь?{w} И найдут ли меня вообще в этих лабиринтах?"
    "И какого черта я согласился лезть сюда?{w} Все ей потакал…"
    show us smile pioneer at center onlayer master with dspr
    us "У тебя такое выражение лица, как будто ты кого-то сейчас убить собираешься."
    me "Был бы кто под рукой – убил бы."
    show us surp3 pioneer at center onlayer master with dspr
    "Ульянка вздрогнула."
    me "Да нет, не тебя. Тебя бы выпороть неплохо, а убивать, наверное, не за что."
    show us grin pioneer at center onlayer master with dspr
    "Она ухмыльнулась."
    me "Пока…"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Скажешь тоже!"
    me "Ладно, теперь уж точно пора выбираться отсюда! А завтра пусть они сюда присылают спецназ, МЧС, охотников за привидениями, кого угодно – уже не моя забота."
    show us normal pioneer at center onlayer master with dspr
    us "Пойдем назад?"
    "Я еще раз осмотрел комнату и заметил дверь слева от себя."
    me "Ого."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "Дверь была такая же, как в бомбоубежище, – массивная, металлическая."

    play sound sfx_metal_door_handle_rattle

    "Я несколько раз дернул за колесо, но она лишь глухо заскрипела."
    th "Эх, сейчас бы сюда ту фомку…"
    show us sad pioneer at center onlayer master with dissolve
    us "Никак?"
    "Грустно спросила Ульянка."
    me "Нет…"
    "По правде говоря, у меня уже совершенно не было сил."
    "Возможно, в другой ситуации я бы поднапрягся, попросил ее помочь, поискал бы что-нибудь, что можно использовать в качестве рычага, но сейчас мне просто хотелось выбраться из этой шахты."
    "Просто хотелось рассчитывать, что получится пройти по пути наименьшего сопротивления."
    "А это значит – надеяться, что я запомнил дорогу через лабиринт."
    me "Пойдем назад."
    show us smile pioneer at center onlayer master with dspr
    us "Пойдем."
    "Она улыбнулась и взяла меня за руку."
    window hide

    scene cg d4_catac_us_2 onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "…"
    "На обратном пути, плутая по лабиринту, мы двигались еще медленнее."
    "Из-под ног летели камни, с потолка изредка капала вода, словно раскаленное олово обжигая голову."
    "Ульянка притихла и лишь молча шла за мной."
    me "Что-то случилось?"
    us "В смысле?"
    me "Странно, когда ты молчишь дольше минуты."
    us "Да нет, все в порядке…"
    "Но что-то все же явно было не так."
    "Развилка следовала за развилкой."
    "Еще минуту назад я был точно уверен, что за следующим поворотом увижу крестик, выцарапанный Ульяной, но напрасно."
    "Вера в мои способности проводника таяла с каждой секундой."
    me "Ну все-таки!"
    "Я решил отвлечься разговором."
    us "Да ничего! Просто…"
    me "Что?"
    us "Неприятно получилось. С Шуриком. И… теперь мы тут застряли."
    me "Ты мне жизнь спасла, считай – должна гордиться собой."
    "Я попытался подбодрить ее, но Ульянка, похоже, этого не поняла."
    us "Но если бы я не отняла у него арматуру, может быть, он и не убежал бы."
    me "Убежал бы, не убежал бы – какая сейчас разница? Все равно бы пришлось как-то выбираться, правильно?"
    us "Да, но…"
    me "Все в порядке! И этот псих тоже дорогу найдет, уверен."
    "Я действительно был почему-то в этом уверен."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    window show
    "Наконец мы вышли в длинный туннель, на стене которого обнаружился тот самый крестик."
    "Ульянка немного повеселела, и путь на поверхность мы проделали почти бегом."
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    show us smile pioneer at center onlayer master with dissolve
    window show
    me "Ну вот, видишь!"
    "Над нами снова была полная Луна, а здание старого лагеря уже не казалось таким зловещим, как раньше.{w} Уж по сравнению с бомбоубежищем и катакомбами-то – точно."
    show us laugh pioneer at center onlayer master with dspr
    us "Круто было, да?"
    "Похоже, к ней вернулась привычная жизнерадостность."
    me "Не знаю насчет «круто», но я рад, что мы выбрались."
    us "Что, пойдем Шурика искать?"
    me "Что?"
    "Я задохнулся на мгновение, не в силах продолжить предложение."
    me "Ты в уме? Зачем его искать – нашли уже! Завтра Ольга Дмитриевна с милицией спустятся и отловят этого пещерного человека. Для опытов."
    show us sad pioneer at center onlayer master with dspr
    us "Ну!"
    me "Никаких ну! Назад в лагерь! Спать!"
    hide us onlayer master with dissolve

    stop ambience fadeout 2

    "Я быстром шагом направился в сторону деревьев, игнорируя возмущенную Ульянку."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "…"
    "Минут через 10 мы уже стояли на площади."
    show us smile pioneer at center onlayer master with dissolve
    me "Ладно, на сегодня это все, вы свободны, солдат!"
    show us surp2 pioneer at center onlayer master with dspr
    "Ульянка отдала честь и уже собралась уходить, но неожиданно вскрикнула и начала бешено размахивать руками."
    us "Смотри! Смотри!"
    "Я повернулся в сторону лавочек и на одной из них увидел лежащего Шурика."
    me "Ничего себе…"
    hide us onlayer master with dissolve
    "Растолкать его стало настоящей проблемой – похоже, «пещерный человек» решил отоспаться на год вперед."
    show sh scared pioneer at cright onlayer master with dissolve
    sh "А? Что? Где я?"
    "Бубнил он сквозь сон."
    me "Не хочешь объясниться?"
    sh "А что такое?"
    show us angry pioneer at cleft onlayer master with dissolve
    us "Мы тебя всю ночь искали, а ты! И Семена арматурой! И убежал потом!"
    "Ульянка прыгала вокруг лавочки и, кажется, была готова взорваться."
    show sh surprise pioneer at cright onlayer master with dspr
    sh "Что случилось-то? И почему я тут?"
    "Шурик, похоже, пришел в себя."
    me "А вот это ты нам объясни, будь добр! Как из шахты выбрался, зачем вообще туда полез! Все по порядку!"
    sh "Какой шахты?"
    "В его глазах читалось такое искреннее удивление, что я на секунду засомневался.{w} А вдруг правда не помнит?"
    me "Где ты был последние… часов 12?"
    show sh upset pioneer at cright onlayer master with dspr
    sh "Не знаю…"
    "Он сел и на его лице появилось выражение крайнего напряжения."
    sh "Я утром пошел в старый лагерь. Говорят, там осталась старая аппаратура. На детали к роботу. И…"
    show sh surprise pioneer at cright onlayer master with dspr
    "Он непонимающе уставился на нас."
    me "И?"
    sh "И все…"
    me "То есть не помнишь?"
    sh "Не помню."
    me "Понятно."
    "Я сел рядом и откинулся на спинку лавочки."
    "На небе ярко сверкали звезды."
    "Они помнят все.{w} Кроме того, что делал в бомбоубежище Шурик."
    me "Посттравматический шок."
    show us surp2 pioneer at cleft onlayer master with dspr
    us "Постсрама… что?"
    show sh normal pioneer at cright onlayer master with dspr
    sh "Подобные симптомы бывают у людей, переживших сильный стресс. После катастрофы, например."
    "С умным видом заметил он."
    me "Тебе сейчас поспать надо."
    show sh surprise pioneer at cright onlayer master with dspr
    sh "Да, но…"
    me "Завтра поговорим."
    hide sh onlayer master with dissolve
    "Он еще некоторое время смотрел на меня, но потом все же встал и, не прощаясь, медленно направился в сторону своей палатки."
    show us surp2 pioneer onlayer master at cleft:
        linear 1.0 xalign 0.5
    us "Так что с ним такое все-таки?"
    me "Видимо, забыл все, что случилось в шахте."
    show us grin pioneer at center onlayer master with dspr
    us "Врет же небось!"
    me "Ну а зачем ему врать, сама посуди?"
    show us shy2 pioneer at center onlayer master with dspr
    us "Чтобы не отвечать за то, что хотел тебя там… арматурой…"
    "Сказала она неуверенно."
    me "Непохоже. Да и какая уже разница?"
    show us surp2 pioneer at center onlayer master with dspr
    us "Как это какая? Надо выяснить! Виновник должен быть наказан!"
    me "Если бы это правило всегда применялось к тебе, то уже давно бы сидела под домашним арестом. Или что похуже."
    show us dontlike pioneer at center onlayer master with dspr
    us "Причем тут я? Я не кидаюсь на людей со всякими железками!"
    me "Ну и он неспециально."
    us "Врет!"
    me "Ну, может, и врет."
    "Я очень устал за сегодняшний день и ночь, и мне правда было наплевать, говорит правду Шурик или притворяется."
    "Тем более что, похоже, он действительно ничего не помнил."
    me "Я иду спать."
    show us shy pioneer at center onlayer master with dspr
    us "Тогда…"
    "Ульянка вскочила и встала на цыпочки."
    us "Спокойной ночи!"
    me "И тебе…"

    stop ambience fadeout 2

    "Не знаю, может быть, в ее выражении лица в тот момент было что-то особенное – мне было все равно."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Кое-как удалось добраться до домика вожатой и упасть на кровать."
    "На мое счастье, она уже спала."
    "Я с трудом разделся и лег в постель."
    th "И все же это слишком много для одного человека."
    "Искать Шурика там, в подземельях, – занятие для настоящих диггеров.{w} Делать это вместе с Ульянкой – для дипломированных сумасшедших."
    th "И все же, как бы там ни было, весело!"
    "Я заснул с улыбкой на лице…"
    window hide

    scene black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day5_main1

label day4_un:

    me "Я же не пойду туда один?!"
    show mt normal pioneer at left onlayer master with dspr
    "Ольга Дмитриевна призадумалась."
    mt "Пожалуй, ты прав… Тогда завтра с утра пойдем все вместе."
    "Последние пару минут я ловил на себе странные взгляды Лены.{w} Словно она что-то хотела сказать, но не решалась."
    hide un onlayer master
    hide sl onlayer master
    with dissolve
    "Пионеры начали медленно расходиться, об Алисе и взрыве все словно забыли."
    "Даже вожатая, казалось, смягчилась и никак не отреагировала, когда горе-террористка, пытаясь спрятаться за Ульянку, ретировалась с площади."
    mt "И нам пора."

    stop music fadeout 3

    play ambience ambience_camp_center_evening fadein 3

    me "Да…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    window show
    "На лагерь быстро опускалась ночь."
    "Все же здесь, на юге – а может, просто в этом мире, – от первых лучей заходящего солнца до полной темноты – лишь краткий миг, не успеваешь сполна насладиться всем буйством красок заката."
    "Я отметил про себя, что спать еще рано, но вожатая шла в сторону своего домика уверенно, как будто мысленно таща меня за собой."
    show mt normal pioneer at center onlayer master with dissolve
    me "Ольга Дмитриевна, я, пожалуй, прогуляюсь немного."
    mt "Ладно…"
    hide mt onlayer master with dissolve
    "Она пристально посмотрела на меня, но, видимо не найдя поводов возражать, пожала плечами и пошла дальше."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    window show
    "Я вернулся на площадь."
    "Не то чтобы хотелось получше рассмотреть незначительный ущерб, нанесенный памятнику Генде, – просто здесь находился географический центр лагеря, если не знаешь, куда идти, то стоит начинать поиски маршрута именно отсюда."
    "Я сел на лавочку и посмотрел на запад – интересно, {i}здесь{/i} Земля вращается вокруг своей оси именно так, как и должна?{w} Или, может быть, там вообще север? Или юг…"
    "Доподлинно установить было непросто, по крайней мере тогда мне не приходило в голову ни единого способа проверить фундаментальные законы мироздания."
    show un normal pioneer at center onlayer master with dissolve
    un "Привет…"
    "Непонятно откуда рядом со мной появилась Лена."
    me "Привет… Не спится?"
    show un surprise pioneer at center onlayer master with dspr
    "Она удивленно посмотрела на меня."
    me "Ну да, еще рано, конечно."
    show un normal pioneer at center onlayer master with dspr
    un "Можно я присяду?"
    me "Да, конечно, садись."
    "Я аккуратно подвинулся."
    "Аккуратно – так мне казалось, на самом деле я буквально вжался в край лавки."
    un "Спасибо."
    "Лена села и посмотрела на небо, словно забыв о моем присутствии."
    un "Грустно…"
    me "Что грустно?"
    un "Что Шурик пропал."
    me "Да, неприятно получилось."
    "Она, как обычно, вела себя спокойно, большую часть времени молчала; краснела и смущалась только тогда, когда приходилось что-то говорить или делать."
    "Само состояние тишины, которое могло бы показаться многим (в том числе и мне) неловким, для нее, похоже, было вполне естественным, привычным даже."
    "Мне сложно было представить, что Лена на самом деле где-то глубоко внутри силится подобрать слова, как-то начать разговор или вставить удачную реплику, старается не казаться глупой или, наоборот, не производить впечатление слишком нахальной девочки, как Алиса."
    "Я просто не мог ее сравнить ни с кем – наверняка ей вполне комфортно быть такой, какая она есть."
    "А значит, мои попытки как-то разговорить ее – слово «сблизиться» употреблять было страшно – будут восприниматься как вторжение во внутренний мир?"
    "Впрочем, меня отчего-то тянуло к этой девочке."
    "Загадочность ли, в которой ей точно не откажешь, внешняя привлекательность или какие-то другие женские чары – я не мог ответить на этот вопрос."
    th "Поэтому, пока меня в открытую не упрекнут в назойливости…"
    me "Уверен, что он найдется! Ну, в самом деле, куда ты денешься с подводной лодки?"
    "Лена, похоже, шутку не оценила."
    "Ведь этот лагерь был подводной лодкой, наверное, только для меня."
    un "Я надеюсь."
    me "Завтра Ольга Дмитриевна в милицию позвонит. Найдут они его, обязательно найдут!"
    show un sad pioneer at center onlayer master with dspr
    un "А если за ночь…"
    "Она погрустнела."
    me "Да что с ним может случиться!"
    th "Один, ночью, в лесу… Да что угодно!"
    show un normal pioneer at center onlayer master with dspr
    un "Наверное, ему там одиноко."
    me "Как будто его кто-то заставлял туда идти!"
    un "А если он просто потерялся?"
    me "Ну так не надо по лесам шастать одному."
    show un sad pioneer at center onlayer master with dspr
    un "Тебе его совсем не жалко. Вдруг он сидит там, совсем один…"
    me "Жалко, конечно…"
    "Я смутился."
    "Как бы там ни было, Лена права – человек пропал."
    un "И за ночь что угодно может случиться…"
    me "Не пойдем же мы сейчас его искать?"
    show un normal pioneer at center onlayer master with dspr
    "Она ничего не ответила, все так же продолжая смотреть куда-то вдаль – туда, где солнце из последних сил пробивалось сквозь верхушки вековых деревьев, словно стараясь оставить напоследок людям хоть немного своего тепла."
    me "Ты правда думаешь, что на ночь глядя бродить по лесу – это хорошая идея?"
    show un sad pioneer at center onlayer master with dspr
    un "Нет, наверное."
    "Почему-то я был совершенно уверен, что она именно так и думает."
    "В последнее время мне все чаще казалось, что начинаю понимать Лену без слов.{w} И что она как будто психологически давит на меня, заставляя соглашаться с ней."
    "В ее случае молчание куда красноречивее любой болтовни и уговоров."
    me "Да и тем более днем искали уже."
    show un surprise pioneer at center onlayer master with dspr
    un "Везде?"
    "Она наконец оторвалась от созерцания заката и посмотрела на меня."
    me "Не знаю. Вроде бы везде."
    show un normal pioneer at center onlayer master with dspr
    un "А как же старый лагерь?"
    "Впервые ее слова прозвучали не отвлеченно-безразлично, а, кажется, даже уверенно."
    me "А где он? Я вот не знаю."
    un "Электроник рассказывал."
    me "Ну, ему верить…"
    "Я глупо усмехнулся, но Лена продолжала все так же серьезно смотреть на меня."
    me "Конечно, если он не так далеко…"
    show un surprise pioneer at center onlayer master with dspr
    un "Значит, ты хочешь пойти?"
    th "Конечно не хочу!"
    me "Можно, если только быстро и сразу назад…"
    show un smile pioneer at center onlayer master with dspr
    un "Хорошо."
    "Лена улыбнулась и протянула мне непонятно откуда взявшийся фонарь."
    me "Да, полезная штука…"
    th "То есть, получается, она заранее готовилась?{w} И от меня уже ничего не зависело?"

    stop ambience fadeout 2

    hide un onlayer master with dissolve
    "Я обреченно вздохнул и направился вместе с ней в сторону леса."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    window show
    "…"
    "На лагерь опустилась ночь."
    "Мы шли медленно, Лена – рядом со мной, близко, но все же не вплотную."
    "Странно, но, кажется, она совсем не боялась."
    th "Более того, похоже, все происходящее ее вообще волнует мало – словно и не мы сейчас бродим по ночному лесу, а смотрим кино с кем-то другим в главных ролях."
    "Действительно, по рассказам Электроника, старый лагерь был не так далеко, и, если идти по прямой, заблудиться будет достаточно сложно."
    "Впрочем, уже через пару минут я был совершенно не уверен, что мы идем именно по прямой, а еще через некоторое время мне начало казаться, что станет чудом, если мы вообще отсюда выберемся."
    "Но перед Леной лицо терять не хотелось, поэтому шагать я старался бодро."
    "По лесу постоянно прыгали бессловесные тени, отблески Луны, под ногами тихо шуршала трава, а над головой – ветки деревьев."
    "Вековые дубы стояли рядом с совсем молодыми березками, из-под которых приветливо выглядывали большие грибы, словно готовые, салютуя, снять свою широкополую шляпу."
    "В другой день – скорее в другое время суток – здесь наверняка красиво."
    "Возможно, и сейчас бояться нечего, но все же я невольно вздрагивал от каждого дуновения ветерка."
    show un surprise pioneer at center onlayer master with dissolve
    un "Смотри."

    stop ambience fadeout 2

    stop music fadeout 3

    "Лена показала вперед. Я прищурился и увидел просвет между деревьями."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night onlayer master
    with dissolve

    play ambience ambience_old_camp_outside fadein 3

    play music music_list["sunny_day"] fadein 5

    window show
    "Через минуту мы стояли на довольно большой поляне, посредине которой возвышалось здание, напоминающее сельскую школу или детский сад."
    "Краска со стен осыпалась, крыша в нескольких местах зияла пробоинами, словно от артиллерийской бомбежки, а окна, лишенные стекол, смотрели на нас грустно и даже немного угрожающе.{w} Не самое приятное зрелище."
    "Я не мог вспомнить, каким представлял себе это место еще минуту назад, – все картины как будто стерли из памяти, заменив на этот унылый кладбищенский пейзаж."
    me "Да уж, жутковато…"
    show un surprise pioneer at center onlayer master with dissolve
    "Лена стояла все так же молча, но на ее лице появилось вполне нормальное для подобной ситуации выражение испуга."
    un "Думаешь, он там?"
    me "Не знаю…"
    "Если бы мне пришлось оказаться на месте Шурика, то дом с привидениями – последнее место, в котором бы я спрятался."
    un "Пойдем?"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_old_building_night_moonlight onlayer master
    with dissolve2

    window show
    "Ответить я не успел – из-за туч выглянула Луна, в свете которой пейзаж словно заиграл новым красками."
    "Или скорее одним новым цветом – могильно-белым, цветом савана."
    "Яснее стали видны деревья на другом конце поляны, окутывающий их туман, да и температура словно упала сразу градусов на пять – так резко по коже побежали мурашки."
    show un normal pioneer at center onlayer master with dissolve
    un "Боишься?"
    "Спросила Лена спокойно."
    me "Тебе честно или соврать?"
    show un smile pioneer at center onlayer master with dspr
    "Она еле заметно улыбнулась и взяла меня за руку."
    "В другой ситуации наверняка это вызвало бы во мне целую бурю эмоций, но сейчас ощущалось лишь насущной необходимостью."
    "Мы медленно направились вперед."
    hide un onlayer master with dissolve
    window hide

    with fade

    window show
    "…"
    window hide

    play sound sfx_carousel_squeak

    pause(1)

    window show
    "Проходя по детской площадке, я толкнул рукой карусель, от чего она мерзко заскрипела и сделала пол-оборота."
    show un shocked pioneer at center onlayer master with dissolve
    "Лена вздрогнула и крепче сжала мою руку."
    me "Прости… Наверное, просто детство вспомнил."
    show un normal pioneer at center onlayer master with dspr
    un "Любил карусели?"
    me "Да… То есть не знаю, не помню. Наверное. Все дети любят."
    un "А я не любила."
    me "Почему?"
    un "От них голова кружится."
    me "Если быстро крутиться – конечно."
    show un smile pioneer at center onlayer master with dspr
    un "Мне больше качели нравятся."
    me "Так и на качелях можно раскачаться не хуже центрифуги!"
    show un normal pioneer at center onlayer master with dspr
    un "Но зачем?"
    me "Не знаю…"
    "Этот разговор несколько отвлек меня, и на душе стало спокойнее, за все – за Шурика, за наше ночное путешествие, за Лену…"
    th "В конце концов, и этому миру не чуждо ничто человеческое."

    stop ambience fadeout 2

    "Наконец мы дошли до дверей…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_old_building_night onlayer master
    with dissolve

    window show
    "Внутри старый лагерь напомнил мне детский сад, в который я ходил в детстве."
    "На первый взгляд даже расположение комнат было таким же."
    show un surprise pioneer at center onlayer master with dissolve
    me "Шурик!"
    un "Шурик!"
    "Ответа не последовало."
    me "Похоже, нет тут никого."
    show un normal pioneer at center onlayer master with dspr
    un "Надо все равно проверить."
    "Я не переставал удивляться смелости Лены."
    "Или, лучше сказать, отсутствию у нее элементарного инстинкта самосохранения."
    "Странно ли такое поведение для этой девочки или, наоборот, нормально – я уже не знал."
    me "Конечно, давай…"
    hide un onlayer master with dissolve
    window hide

    with fade

    window show
    "…"
    "Мы тщательно осмотрели все помещения старого лагеря, я даже заглянул на чердак."
    "Повсюду можно было найти различные свидетельства того, что люди здесь бывают часто – газеты, пустые бутылки, прочий мусор, но никаких следов Шурика."
    "Мы вернулись в холл, откуда начинали поиски."
    show un normal pioneer at center onlayer master with dissolve
    me "Что будем дальше делать?"
    un "Не знаю…"
    "Лена села на ступеньки и уставилась себе под ноги."
    me "Думаю, стоит вернуться…"
    "Осторожно начал я."
    me "Все-таки уже поздно и… Не будем же мы по всем лесам его искать!"
    show un sad pioneer at center onlayer master with dspr
    un "Наверное, ты прав."
    "Она выглядела расстроенной и всем своим видом давала понять, что поиски еще не закончены."
    me "Ну правда!"
    "Обреченно всплеснул я руками и сел рядом."
    me "В конце концов, стоит подумать и о худшем сценарии…"
    show un scared pioneer at center onlayer master with dspr
    un "Ты хочешь сказать…"
    me "Нет, но… Здесь водятся дикие звери?"
    show un normal pioneer at center onlayer master with dspr
    un "Вряд ли."
    "Лена моментально успокоилась."
    me "Ну, может, он спит где! Утром проснется и вернется в лагерь."
    show un sad pioneer at center onlayer master with dspr
    un "Да, конечно…"
    show un sad pioneer far at center onlayer master with dissolve
    "Я резко встал и принялся наматывать круги по холлу."
    "Очень хотелось поскорее уйти отсюда, поскорее выбраться из леса, но пока Лена сидела вот так, словно какая-то неведомая сила удерживала меня."
    "Я уже было открыл рот, чтобы продолжить уговоры, как вдруг заметил что-то на полу."
    "Это был люк, вокруг которого лежали аккуратные горки мусора и пыли."
    th "Значит, его недавно открывали!"
    me "Смотри."
    show un normal pioneer at center onlayer master with dissolve
    un "Думаешь, Шурик там?"
    "Лена присела на корточки и аккуратно протерла ручку люка."
    me "Может, и не Шурик, но кто-то точно туда лазал за последнее время."
    "Я уже пожалел, что вообще нашел этот чертов вход в преисподнюю."
    un "Посмотрим?"

    play sound sfx_open_metal_hatch

    "Дверца люка оказалась не очень тяжелой – открыть ее не составило особых проблем."
    "Я посветил фонариком и увидел лестницу, уходящую вниз на пару метров."
    me "Похоже, подвал…"
    un "Спустимся?"
    "Я несколько секунд внимательно смотрел на Лену, пытаясь понять, что же у нее на уме."
    th "Неужели проснулась жажда приключений, как у Ульянки?{w} А где же тогда юношеский задор?"
    th "Или она просто не в своем уме..."
    "Но и на сумасшедшую Лена походила мало."
    th "А кто вообще сказал, что она человек и ее можно оценивать исходя из человеческой логики поведения?"
    "Эта мысль должна была испугать меня, но почему-то прошла незамеченной, затерявшись в толпе миллионов других, какие-то из которых – например, о том, что может скрываться там внизу, – были несомненно более важными."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "Я спустился и осмотрелся."
    me "Нормально все."
    "Удостоверившись, что бояться нечего, крикнул я Лене."
    show un normal pioneer at center onlayer master with dissolve
    "Мы стояли в длинном коридоре, который совершенно точно не был ни погребом, ни подвалом."
    "Архитектурой он больше напоминал застенки КГБ или подсобный туннель метро – не знаю даже, что лучше."
    "Вдоль стен тянулись бесчисленные провода, через каждые полметра перехваченные металлическими крюками, под потолком висели лампы, закованные в проржавевшие абажуры, а под ногами мерзко скрипела бетонная крошка."
    un "Пойдем?"
    "Как-то безэмоционально спросила Лена."
    me "Куда? Туда?"
    un "Ну да. Вдруг Шурик там?"
    me "И что ему там делать?"
    "Впрочем, сегодня возражать ей у меня все равно бы не получилось, и мы медленно направились в темноту."
    hide un onlayer master with dissolve
    "…"
    window hide

    scene cg d4_catac_un onlayer master
    with dissolve

    window show
    "Лена шла рядом, держа меня за руку."
    "Тишину подземелья нарушал только шум наших шагов и звуки капающей с потолка воды."
    "Мы пробирались вперед медленно, может быть, даже слишком – у меня внезапно начался приступ клаустрофобии."
    "Я сильно стиснул с зубы и было сжал что есть силы фонарь, но тут же ослабил хватку, испугавшись сломать наш единственный источник света."
    "Лена молчала, и ее молчание начало казаться громче любых слов – мне стало страшно."
    me "Скажи что-нибудь."
    un "Дверь."
    me "Что?"
    un "Дверь."
    "Она показала вперед."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_door onlayer master
    with dissolve

    window show
    "Действительно, мы уперлись в массивную металлическую дверь со значком радиационной опасности."
    show un normal pioneer at center onlayer master with dissolve
    me "Значит, бомбоубежище…"
    un "Да, я что-то слышала."
    me "Зачем оно тут?"
    un "Не знаю. Может быть, Карибский кризис?"
    me "Карибский?"
    "Я прикинул приблизительное время постройки лагеря – действительно, сходится."
    "Впрочем, учитывая глубину, на которой мы находились, да и удаленность этих мест от цивилизации, наличие здесь бомбоубежища казалось неуместным."
    "Колесо двери глухо скрипнуло – пришлось надавить изо всех сил – и прокрутилось несколько раз."

    play sound sfx_open_metal_door

    stop ambience fadeout 3

    "Я решился и с трудом открыл дверь..."
    window hide

    scene bg int_catacombs_living onlayer master
    with dissolve

    window show
    "Мы вошли в комнату – наверное, основное «жилое» помещение."

    $ persistent.sprite_time = "sunset"

    "Несколько кроватей, шкафы, какая-то научная аппаратура – к ядерному апокалипсису готовились на совесть."
    "Впрочем, никаких следов Шурика здесь обнаружить не удалось."
    show un smile pioneer at center onlayer master with dissolve
    un "Смотри."
    "Лена протянула мне сигнальный пистолет и улыбнулась."
    me "Зачем мне это?"
    un "От монстров защищаться."
    me "Но тут нет никаких монстров."
    "По крайней мере очень хотелось в это верить."
    show un normal pioneer at center onlayer master with dspr
    un "Хорошо…"
    me "Ладно."
    "Не хотелось ее расстраивать, поэтому я засунул пистолет за пояс – мало ли что…"
    hide un onlayer master with dissolve
    "Мы еще раз внимательно осмотрели помещение."
    "Из него было два выхода.{w} Один – дверь, через которую мы попали сюда, и еще один – точно такая же дверь в стене слева."
    "На секунду я почувствовал какой-то азарт, желание дойти до конца этого лабиринта и узнать, что за приз меня там ждет."
    "Впрочем, вряд ли это – компьютерная игра, да и возможности сохранения тут явно не предусмотрено."
    show un normal pioneer at center onlayer master with dissolve
    un "Может быть, этим?"
    "Лена держала в руках внушительного размера фомку."
    me "Да нет, давай сначала так попробую."
    hide un onlayer master with dissolve

    play sound sfx_metal_door_handle_rattle

    "Впрочем, дверь никак не хотела поддаваться – лишь противно скрипела, но колесо-ручка не сдвинулась ни на миллиметр."
    show un normal pioneer at center onlayer master with dissolve
    me "Ладно, давай."
    hide un onlayer master with dissolve

    play sound sfx_insert_crowbar_door

    "С фомкой дело пошло лучше, даже слишком легко."
    window hide

    play sound sfx_fall_metal_door

    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living_nodoor onlayer master
    with vpunch

    window show
    "И наконец преграда пала, громко ударившись об пол."
    "Оказалось, что петли насквозь проржавели."
    "Я посветил фонарем в образовавшийся проход – за ним был точно такой же коридор, как тот, по которому мы пришли сюда."
    show un normal pioneer at center onlayer master with dissolve
    un "Пойдем?"
    "Лена словно постоянно подгоняла меня."
    me "Куда ты так спешишь?"
    show un shy pioneer at center onlayer master with dspr
    un "Я? Я не спешу…"
    "Она смутилась и покраснела."
    th "Ну вот, опять… И как мне ее понимать?{w} То ничего не боится, то теряется от каждого слова."
    me "Тебе как будто совсем не страшно."
    show un normal pioneer at center onlayer master with dspr
    un "Не знаю, а чего бояться?"
    show un smile2 pioneer at center onlayer master with dspr
    un "Ты же меня защитишь…"
    "Добавила она еле слышно."
    "Значит, Лена надеется на меня, верит, что, что бы ни произошло…"
    th "Да, это возможно.{w} Глупо, наивно, но возможно."
    "Сам я четко понимал, что никого защитить не смогу, даже себя – здесь, в этом мире, ничего от меня не зависит."
    "Те силы, по воле которых я оказался тут, способны на что угодно!"
    "Хотя это совсем не значит, что в конце туннеля меня ждет неминуемая смерть – она может подстерегать меня где угодно в этом лагере…"
    me "Пойдем!"
    window hide

    scene cg d4_catac_un onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "…"
    "Я старался идти быстрее, но Лене, похоже, это не доставляло совершенно никаких неудобств – она с легкостью поддерживала мой темп."
    "Коридор был действительно точно таким же, как предыдущий.{w} Болезненно таким же, вплоть до деталей."
    "Конечно, удивляться здесь особо нечему, но в какой-то момент у меня появилось ощущение, что мы ходим по кругу."

    scene black onlayer master
    show cg d4_catac_un onlayer master:
        linear 0.1 pos (0,5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat

    "Фонарь в руке начал все заметнее дрожать, пятно света прыгало по стенам и полу и вдруг выхватило из темноты довольно большую дыру…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole onlayer master
    with dissolve

    window show
    "Яма оказалось неглубокой, а внизу виднелись рельсы."
    show un normal pioneer at center onlayer master with dissolve
    un "Что там?"
    me "Шахта, похоже."
    un "Посмотрим?"
    me "А почему не дальше?"
    un "Не знаю, мне кажется, нам туда."
    "Я прикинул высоту ямы – вполне можно было вылезти, подтянувшись."

    stop ambience fadeout 3

    me "Ну ладно, давай проверим."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine onlayer master
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    play sound sfx_jump_into_hole_2

    pause(1)

    window show
    "Я спрыгнул в яму и помог Лене спуститься."
    "Мы действительно оказались в шахте."
    th "Интересно, что здесь могли добывать?"
    show un normal pioneer at center onlayer master with dissolve
    me "А какие полезные ископаемые бывают в этих краях?"
    un "Не знаю."
    me "Ну да, глупый вопрос. Сейчас-то уже, похоже, никаких…"
    hide un onlayer master with dissolve
    "Мы начали медленно углубляться в темноту."
    "Идти было неудобно, потому что я все никак не мог выбрать, куда лучше наступать – на доски, служащие шпалами, или на землю."
    "Идти сбоку не получалось – туннель был слишком узок, а отпускать ленину руку я совершенно не хотел."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    window show
    "Наконец мы вышли к развилке."
    show un normal pioneer at center onlayer master with dissolve
    me "Ну вот, этого еще не хватало."
    un "Куда пойдем?"
    me "Куда? Не факт, что мы вообще выберемся отсюда, а уж если будем играть в пакмана…"
    show un surprise pioneer at center onlayer master with dspr
    un "Во что?"
    me "Неважно. Заблудимся, в общем."
    show un normal pioneer at center onlayer master with dspr
    un "А вдруг там тоже есть выход?"
    me "Даже если есть… А если нет?"
    show un sad pioneer at center onlayer master with dspr
    un "Значит, назад?"
    "Я до крови прикусил губу и что есть силы закричал:"

    scene black onlayer master
    show bg int_mine_crossroad onlayer master:
        linear 0.1 pos (0,5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        linear 0.1 pos (0,5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        linear 0.1 pos (0,5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)

    me "Шурик!"
    "Тут же со всех сторон зазвучало гулкое эхо, а с потолка даже кое-где начала сыпаться земля."
    me "Видишь…"
    show un normal pioneer at center onlayer master with dspr
    un "Ладно, тогда я одна пойду."
    me "Что?"
    "Я расплылся в глупой улыбке."
    me "Как это одна? Куда?"
    show un shy pioneer at center onlayer master with dspr
    un "Но Шурика надо найти все же, вдруг он там…"
    "Лена тут же покраснела и уставилась в пол."
    me "Не-не-не, так не пойдет, если идти, то вместе."
    show un smile2 pioneer at center onlayer master with dspr
    un "Хорошо. Значит, пойдем."
    "Она улыбнулась и снова взяла меня за руку."
    th "И как у нее это вообще получается..."
    me "Только сначала…"
    "Я взял с земли довольно большой камень и выцарапал на одной из балок, укрепляющих стену, крестик."
    me "Теперь хотя бы будем знать, откуда начинали."
    window hide

label un_mine_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with dissolve

    menu:
        "Налево":
            jump un_mine_4_1
        "Направо":
            jump un_mine_2

label un_mine_1_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Мы вернулись к тому месту, с которого и начинали."
    th "Значит, где-то не там повернули."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            jump un_mine_4_1
        "Направо":
            jump un_mine_2

label un_mine_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_3
        "Направо":
            jump un_mine_room

label un_mine_2_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump un_mine_1_1
        "Направо":
            jump un_mine_3

label un_mine_2_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_room
        "Направо":
            jump un_mine_1_1

label un_mine_room:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface onlayer master
    with fade

    if mr1 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump un_mine_2_1

    window show
    "Наконец мы вышли из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным нашим спасением был фонарик."
    "Сломайся он, и мы вряд ли когда-нибудь выбрались бы отсюда…"
    "Именно в его свете я заметил в углу какую-то красную тряпку."
    "Это был пионерский галстук!"
    "Теперь-то я точно был уверен, что Шурик здесь."
    me "Шурик! Шурик!"
    show un surprise pioneer at center onlayer master with dissolve
    un "Шурик! Шурик!"
    "Ответом нам стало лишь эхо."
    un "Раз мы нашли галстук, значит, он где-то рядом."
    "Честно говоря, в ту минуту меня больше интересовало, где это «здесь» вообще находится…"
    th "Но куда он мог отсюда уйти?"
    "Из этой комнаты не было другого выхода…"
    th "Конечно, возможно, в этих туннелях есть еще места, где мы не бывали…"
    th "Значит, придется искать дальше!"
    window hide

    $ mr1 = mr1 + 1

    jump un_mine_2_1

label un_mine_3:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_5
        "Направо":
            jump un_mine_6

label un_mine_3_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_6
        "Направо":
            jump un_mine_2_2

label un_mine_5:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_4
        "Направо":
            jump un_mine_6

label un_mine_5_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_6
        "Направо":
            jump un_mine_3_1

label un_mine_4:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_1_1
        "Направо":
            jump un_mine_7

label un_mine_4_1:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    window show
    "Похоже, еще одна развилка."
    window hide

    menu:
        "Налево":
            jump un_mine_7
        "Направо":
            jump un_mine_5_1

label un_mine_4_2:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad onlayer master
    with fade

    menu:
        "Налево":
            jump un_mine_5_1
        "Направо":
            jump un_mine_1_1

label un_mine_7:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt onlayer master
    with fade

    if mr2 >= 1:
        window show
        "Здесь мы уже были."
        window hide

        jump un_mine_4_2

    window show
    "Мы вышли к некоему подобию шахтерского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовал, что выход где-то рядом, поэтому мы отправились дальше."
    window hide

    $ mr2 = mr2 + 1

    jump un_mine_4_2

label un_mine_6:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door onlayer master
    with fade

    window show
    "За очередным поворотам в свете фонаря появилась деревянная дверь."
    show un normal pioneer at center onlayer master with dissolve
    me "Хоть что-то…"
    un "Что?"
    me "Хотя бы не очередная развилка."
    un "А что там?"
    me "Сейчас у нас уже точно выбора нет – проверим."
    hide un onlayer master with dissolve

    play sound sfx_open_door_1

    stop ambience fadeout 3

    "Я с силой дернул ручку и открыл дверь."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with dissolve

    window show
    "За ней скрывалась комната – возможно, одно из подсобных помещений бомбоубежища."
    "Повсюду валялись пустые бутылки, окурки, стены были исписаны."
    th "А значит, отсюда существует и другой выход!"
    "Мне просто не хотелось верить что те, кто оставил все это, приходили той же дорогой, что и мы."
    "Однако в этой комнате, к несчастью, Шурика не оказалось."
    show un normal pioneer at center onlayer master with dissolve  
    me "Эх…"
    "Я обессиленно сполз по стене на пол."
    me "Вот теперь мы точно все обошли."
    un "Не все."
    "Лена показала на дверь в углу."
    "Примерно такую же, как та, что вела в бомбоубежище."
    me "Там, наверное, выход, как ты и говорила."
    un "Пойдем?"
    me "Давай отдохнем немного."
    un "Хорошо."
    show un normal pioneer close at center  onlayer master with dissolve
    "Лена села рядом – очень близко – и взяла меня за руку."
    show un smile pioneer close at center onlayer master with dspr
    un "Ничего страшного."
    me "В смысле?"
    un "Что мы не нашли Шурика."
    me "Нам бы теперь самим выбраться…"
    un "Выберемся."
    me "Да, наверное, я дорогу запомнил."
    "Или хотя бы думал, что запомнил."
    show un smile2 pioneer close at center onlayer master with dspr
    un "Мне совсем не страшно."
    "Вдруг сказала она после непродолжительного молчания."
    me "Это хорошо."
    un "Потому что я с тобой."
    hide un onlayer master with dissolve

    play sound_loop sfx_shurik_mines_far

    "Вдруг за дверью в шахту послышался какой-то шум."
    show un shocked pioneer at right onlayer master with dissolve
    "Я тут же вскочил и принялся шарить глазами по комнате в поисках чего-то, что можно использовать в качестве оружия."
    "Шум – тяжелые шаги – приближался."
    window hide

    stop sound_loop fadeout 2

    play sound sfx_shurik_opens_door

    pause(1)

    show sh rage pioneer far at center onlayer master with dissolve
    window show
    "Наконец дверь распахнулась, и на пороге появился Шурик."
    "Немая сцена, я застыл, смотря на него."
    sh "Вот вы где! Думали, сможете спрятаться?"
    me "Что?"
    sh "Думали, я вас не найду? А я нашел!"
    "Он совершенно точно был не в себе – его лицо исказила страшная гримаса, глаза под очками дьявольски блестели, а в руках потерявшийся пионер сжимал арматуру."
    me "Ты что, совсем сдурел, что ли?! Это же мы!"
    sh "Я вижу, что вы!"
    show sh rage pioneer at center onlayer master with dissolve  
    "Он сделал несколько шагов по направлению к нам."
    show un shocked pioneer onlayer master at right:
        linear 0.2 xalign 1.2
    "Я инстинктивно закрыл Лену собой."

    stop music fadeout 3

    sh "Думали, можно из меня дурака делать? Водить туда-сюда?! «Направо, налево, направо, налево»?! А я ведь ходил, все ходил…"
    window hide

    scene cg d4_sh_stay onlayer master
    with dissolve

    play music music_list["pile"] fadein 1

    window show
    "Он замахнулся арматурой, и дальше все происходило словно в замедленной съемке: Шурик, летящий на нас; я, отталкивающий Лену в сторону; арматура, медленно опускающаяся мне на голову..."
    window hide

    play sound sfx_break_flashlight

    with vpunch

    pause(1)

    window show
    "... рука с фонарем, взметнувшаяся вверх..."
    window hide

    scene black onlayer master
    with dissolve

    window show
    "Кромешный мрак, последовавший после; учащенное дыхание; кровь, стучащая в висках; и тишина, ужасная, давящая тишина, слившаяся с темнотой."
    "Я шарил рукой, силясь нащупать стену, как вдруг почувствовал, что кто-то несильно ударился в меня."
    un "Не бойся."
    "Послышался рядом знакомый голос."
    me "Ты где, чертов псих?!"
    "Закричал я."
    un "Он ушел."
    me "Как ушел? Куда ушел?"
    "Голос Лены звучал не то чтобы спокойно – но совсем не так, как должен звучать голос человека в подобной ситуации."
    un "Успокойся."
    "Она нежно обняла меня и прижалась всем телом."
    "Я пытался прийти в себя, восстановить дыхание, привыкнуть к темноте."

    stop music fadeout 3

    me "И что теперь делать?"
    un "У тебя же есть пистолет."
    me "Да? И в кого мне стрелять?"
    un "В нем же ракета осветительная."
    "Наверное, она была права."

    play sound sfx_signal_pistol

    "Я достал пистолет из-за пояса, направил его в сторону наугад и нажал на курок."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room onlayer master
    with flash_red

    show un normal pioneer at center onlayer master with dissolve
    window show
    "Комната тут же озарилась ярким красным светом."
    "Ракета, лежащая в углу, была похожа на фейерверк или, может быть, на бенгальский огонь."
    show un surprise pioneer at center onlayer master with dspr
    un "Пойдем скорее, она долго гореть не будет."
    me "Куда?"
    "Лена молча указала на вторую дверь."
    "Открыть ее не составило особого труда, и мы устремились в темноту…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance onlayer master
    with dissolve

    play ambience ambience_catacombs fadein 3

    window show
    "…"
    "Сигнальный огонь горел все тусклее."
    "Я спотыкался на каждом шагу, пару раз даже упал, но темпа не сбавлял."
    th "Если погаснет и он…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_exit onlayer master
    with dissolve

    window show
    "Наконец впереди показался просвет, мы вышли к лестнице, упирающейся под потолком в решетку, и ракета, недовольно зашипев на прощанье, потухла."
    me "Слава Богу…"
    "Оказалось, что мы находимся прямо под памятником Генде."

    play sound sfx_break_grid

    stop ambience fadeout 3

    "Решетка казалась довольно крепкой, но мне все же удалось сломать ее, разбив винты фонарем."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Выбравшись на поверхность, я обессиленно упал на траву."
    me "Ужас какой-то…"
    show un normal pioneer at center onlayer master with dissolve
    "Лена села рядом."
    me "Жуть просто…"
    "Мне уже было наплевать на этот мир, на лагерь, на автобус 410, на свою прошлую жизнь – то, что случилось пару минут назад, я и представить себе не мог."
    "И ведь, что самое страшное, самое противное, в этом не было ничего сверхъестественного!"
    "Просто Шурик спятил, сошел с ума.{w} Ничего удивительного, я бы на его месте наверняка тоже…"

    stop ambience fadeout 2

    play music music_list["what_do_you_think_of_me"] fadein 3

    show un smile2 pioneer at center onlayer master with dspr
    "Лена нежно погладила меня по голове и улыбнулась."
    un "Все закончилось."
    me "Не знаю даже… По лесу бродит свихнувшийся пионер! Маньяк-убийца, можно сказать!"
    un "Думаю, с ним все будет в порядке."
    me "В порядке? Нет, не уверен!"
    un "Главное, что с нами все хорошо."
    "Она все так же улыбалась."
    me "Как ты можешь быть такой спокойной?"
    un "Я же говорила, что с тобой мне бояться нечего."
    "Действительно, тогда я, возможно, спас Лену и себя заодно."
    "Впрочем, это всего лишь случайность, не более."
    "Будь Шурик более ловким…{w} Или более безумным…"
    me "Спасибо за комплимент."
    un "Пожалуйста."
    me "Но все-таки не стоило никуда ходить."
    un "Да, наверное."
    "Сказала она спокойно."
    "Меня начало ужасно клонить в сон.{w} От всего пережитого стресса, от усталости, от того, что уже ночь…"
    "Надо было идти спать."
    th "Но для этого сначала нужно встать, дойти до домика вожатой…{w} Нет, на такие подвиги я не готов."
    "Глаза закрылись сами собой, как будто на минутку…"
    "…"
    window hide

    scene stars onlayer master
    with dissolve

    window show
    "С неба на меня смотрели звезды.{w} Тысячи, может, миллионы."
    "Сейчас их свет совершенно не казался далеким, холодным – напротив, они весело подмигивали мне, словно перешептываясь, рассказывали наперебой какую-то сказку."
    "О далекой, далекой галактике и фиолетовых пушистых поросятах, о таинственном поясе астероидов, в котором пропадают корабли, о бесстрашном капитане звездолета и его бравой команде, о невиданных сокровищах и неприступных вершинах гор планеты на краю Вселенной…"
    th "Интересно, это сон?.."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    show un smile pioneer close at center  onlayer master with dissolve
    window show
    "Я слегка приподнялся и понял, что моя голова лежит на коленях Лены."
    me "Долго я спал?"
    "Спросил я смущенно, но вставать не спешил."
    show un laugh pioneer close at center onlayer master with dspr
    un "Не знаю, у меня же нет часов."
    "Рассмеялась она."
    me "Ну примерно!"
    show un smile pioneer close at center onlayer master with dspr
    un "Нет. Может быть, минут двадцать."
    me "Ааа… Ну ладно тогда."
    "Я снова лег, чувствуя, что мне еще никогда не было так хорошо и спокойно – события этой ночи если не забылись, то стали каким-то далекими, словно из той книжки, которую мне читали звезды."

    stop music fadeout 3

    play ambience ambience_camp_center_night fadein 3

    un "Шурик вернулся."
    me "Что?!"
    show un surprise pioneer at center onlayer master with dissolve
    "Я тут же вскочил."
    un "Вон он, на лавочке спит."
    "Лена удивленно показала в сторону скамеек."
    me "И ты что…"
    un "Ты так мирно спал, я не хотела тебя будить."
    "Мне стало страшно, потому что такое поведение было не просто странным – оно было неадекватным, граничащим с безумием Шурика в подземелье."
    "Мимо проходит сумасшедший, пытавшийся нас убить еще полчаса назад, ложится на лавочку и засыпает, а она просто сидит?.."
    show un smile pioneer at center onlayer master with dspr
    un "Ничего страшного – похоже, он просто был немного не в себе…"
    show un shy pioneer at center onlayer master with dspr
    "Она тут же смутилась и покраснела."
    show un sad pioneer at center onlayer master with dspr
    un "Да и шел он так, шатаясь, в нашу сторону не смотрел. А если бы я начала шуметь…"
    "Лена была готова расплакаться."
    me "Ладно, ничего страшного."
    "Конечно, в ее словах была какая-то логика.{w} Может быть, она поступила и правильно."
    "В любом случае сейчас было необходимо с пристрастием допросить Шурика."
    hide un onlayer master with dissolve
    "Я резко вскочил, быстро подошел к лавочке, на которой он спал, и наотмашь ладонью ударил его по щеке."
    show sh scared pioneer at cright onlayer master with dissolve
    sh "Ай!"
    "Он тут же проснулся."
    sh "Что такое?!"
    me "Ты что творишь, скотина?!"
    sh "Что?"
    "Шурик испуганным – более того, вполне осмысленным – взглядом уставился на меня."
    me "Что это было там внизу?!"
    sh "Что, где?"
    me "В подземелье, в шахте, в бомбоубежище! Совсем крыша поехала?"
    sh "Я тебя не понимаю…"
    "Он осмотрелся по сторонам."
    show sh surprise pioneer at cright onlayer master with dspr
    sh "И почему я здесь?"
    me "А где же тебе надо быть еще, по-твоему?! Хотя нет, подожди, я знаю – в дурдоме тебе надо быть!"
    sh "Я утром пошел в старый лагерь за деталями, а потом…"
    show un normal pioneer at cleft onlayer master with dissolve
    un "А потом ты ничего не помнишь?"
    "Спросила подошедшая Лена."
    sh "Да, и я…"
    me "Не прикидывайся."
    "Сказал я спокойнее и сел рядом с ним."
    "Хотя было действительно похоже, что он не врет."
    show sh upset pioneer at cright onlayer master with dspr
    sh "Ничего не понимаю… Все это антинаучно!"
    me "Как угодно. Только не думай, что я тебе поверю."
    sh "Ведь провалы в памяти просто так…"
    "Он говорил сам с собой, что-то не переставая бубнил себе под нос, не обращая на нас никакого внимания."
    show un smile pioneer at cleft onlayer master with dspr
    un "Пойдем."
    "Тихо сказала Лена."
    me "И что, вот так просто его оставим тут?"
    un "Он не в себе – ему надо выспаться."
    me "Да этого психопата вообще опасно одного оставлять! Может, он Электроника ночью в палатке катушкой индуктивности удавит!"
    un "Все будет нормально, поверь."
    "У меня, пожалуй, не было оснований не верить ей."
    "Впрочем, и оснований верить тоже особо не находилось."
    th "Но, с другой стороны, уже наплевать – поскорее бы заснуть!"
    me "Ладно…"
    hide sh onlayer master
    hide un onlayer master
    with dissolve
    "Мы оставили Шурика, продолжающего что-то бубнить, наедине с собой."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "…"
    show un normal pioneer at center onlayer master with dissolve
    un "Пришли."
    me "Что? Куда?"
    show un smile2 pioneer at center onlayer master with dspr
    un "Твоя палатка, а мне дальше."
    "Лена улыбнулась."
    "Всю дорогу я совершенно ни о чем не думал, просто шел за ней и сам не заметил, как мы оказались возле домика Ольги Дмитриевны."
    me "Да…"
    un "Спасибо тебе… за сегодня."
    me "Да не за что тут благодарить; хорошо хоть живы остались. И посмотрим еще, что завтра Шурик скажет!"
    un "Все равно спасибо…"
    "Загадочно сказала она и отвела взгляд."
    me "Ну, тогда пожалуйста."
    show un smile pioneer at center onlayer master with dspr
    un "Ладно, мне пора!"
    hide un onlayer master with dissolve
    "Лена резко развернулась и быстро зашагала в сторону своей палатки."
    "Я тут же поймал себя на мысли, что все это как-то не так, неправильно."
    th "После всего, что произошло, всего лишь «ладно, мне пора»?"
    th "В таких ситуациях же обычно бывает по-другому, разве не так?"
    "Хотя я и сам точно не знал, чего ожидал…"

    stop ambience fadeout 2

    "Усталость заявила о себе с новой силой, я с трудом поднялся по ступенькам и вошел внутрь."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Вожатая уже спала, и это избавило меня от лишних расспросов."
    "Не раздеваясь, я упал на кровать."
    th "И все же Лена…"
    th "Что вообще сегодня произошло?!"
    "Мысли неумолимо замедляли свой бег, а затем и вовсе остановились…"
    window hide

    scene black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day5_main1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
