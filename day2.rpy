init:
    $ day2_map_necessary_done = 0
    $ day2_cards_with_sl = 0
    $ day2_dv_bet = 0
    $ day2_un = 0
    $ d2_gave_keys = False

label day2_main1:

    $ backdrop = "days"

    $ new_chapter(2, u"День второй")
    $ day_time()

    scene bg black onlayer master

    $ renpy.pause(2)

    window show
    "Мне снился сон…"
    "Казалось, что я нахожусь в каком-то вакууме, а рядом со мной никого и ничего нет."
    "Но не только рядом – нет вообще ничего, кроме меня."
    "Я единственное существо во Вселенной."
    "Как будто она вернулась в некое сингулярное состояние перед самым Большим Взрывом."
    "И вот-вот что-то должно было произойти."
    "И вдруг я начал слышать голос."
    "Невозможно было различить слов, но он показался мне знакомым."
    "Голос что-то нежно нашептывал, как будто убаюкивая."
    "И тут я понял...{w} Это был голос той Незнакомки из автобуса.{w} Той девушки из моего сна."
    th "Но что она хочет мне сказать? Кто она?.."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with fade2

    window show
    "Я проснулся."
    window hide

    play music music_list["my_daily_life"] fadein 5

    with flash

    window show
    "Яркие лучи солнца били в глаза."
    "На будильнике, стоявшем на окне, время приближалось к полудню."
    "Лениво потянувшись и зевнув, я начал вспоминать вчерашний день."
    "За несколько секунд все его события пронеслись перед глазами: автобус, лагерь, местные обитатели."
    "И тут я явственно понял, что все это не так, неправильно!"
    "Нет, не эта ситуация, не мое положение – они неправильны априори, – а мое отношение к ним."
    th "Ведь я вот так запросто заснул здесь, до этого мило беседовал с местными пионерами, даже умудрялся шутить!"
    th "Но как можно себя так вести в подобной ситуации?!"
    th "Я же должен бояться, опасаться каждого шороха, избегать любого контакта с потенциально враждебными существами."
    "Все события вчерашнего дня словно заволокла похмельная дымка."
    th "Да, это очень похоже на утро после хорошей пьянки – то, что тебе накануне представлялось вполне естественным, непредосудительным и вообще в высшей степени нормальным, сегодня кажется каким-то кошмаром, гротескной гравюрой из иллюстраций к «Божественной комедии»."
    th "Да, все именно так, однако прошлого уже не вернуть."
    "Хотя, возможно, ничего такого в моих поступках и не было – оценив обстановку, я действовал по ситуации."
    "В крайнем случае вреда мне это не принесло, так что лучше было сильно не менять свою линию поведения, но впредь быть осмотрительнее."
    "Оглядевшись по сторонам, словно пытаясь понять, не забросило ли меня опять куда-нибудь в другое место, я отметил, что домик Ольги Дмитриевны выглядит так же, как и вчера."
    "Но что-то все же изменилось."
    "Пионерская форма, висящая на спинке кровати!"
    "Я с недоверием покрутил ее в руках, примерил и оделся."
    th "Все равно это лучше, чем ходить в зимней одежде."
    "Я начал искать зеркало."
    "Хотя бы самое маленькое – надо было посмотреть на себя, оценить как я выгляжу."

    "Это не составило большого труда – оно обнаружилось на внутренней стороне дверцы шкафа."

    play sound sfx_open_cabinet_2

    window hide

    scene cg d2_mirror onlayer master:
        pause 0.5
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
    with dissolve

    window show
    "Я взглянул на новоиспеченного пионера и аж отпрыгнул в сторону от неожиданности!"
    "Из зеркала на меня смотрел какой-то подросток, похожий на меня."
    "Но не я!"
    "Куда пропали недельная небритость, мешки под глазами, сутулость и смертельно уставшее выражение лица?!"
    "Похоже, меня не закинули назад во времени или в параллельную реальность, а просто поменяли с кем-то телами."
    th "Действительно просто!{w} Такое же на каждом шагу встречается!"
    "Я пригляделся к незнакомцу повнимательнее и только тогда понял, что это я сам!"
    "Только образца конца школы – начала института."
    th "Ладно, хотя бы так."
    th "Наверное, действительно, человек в стрессовой ситуации…"
    th "А вот вожатая заметила и вчера ночью меня отчитала за неподобающее обращение к ней…"
    th "К черту!"
    window hide

    play sound sfx_close_cabinet

    pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    window show
    "Я решил, что проблема с моим внешним видом, может, и важна, но решение ее сейчас не главное, и вряд ли оно приблизит меня к разгадке всего, что здесь происходит."
    "Если верить часам, то завтрак уже давно позади."
    th "Ну ладно, попробую все же в столовой чего-нибудь найти."
    th "Вчера же со Славей получилось."
    "При воспоминании об этом я невольно улыбнулся."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "На улице ярко светило солнце, дул легкий ветерок."
    th "Прекрасный летний день."
    "Я поймал себя на мысли, что уже несколько лет не чувствовал себя по утрам так хорошо."
    "Все мои проблемы на секунду улетели куда-то далеко..."
    "Как вдруг передо мной словно из ниоткуда возникла Ольга Дмитриевна..."
    show mt normal panama pioneer at center onlayer master with dissolve
    mt "Доброе утро, Семен!"
    me "Доброе!"
    "Я улыбнулся, пытаясь всем своим видом показать, что несмотря ни на что утро мое было действительно добрым."
    mt "У тебя первый день только вчера был, поэтому я тебя будить не стала, но завтрак-то…"
    show mt smile panama pioneer at center onlayer master with dspr
    mt "Впрочем, ладно! Вот, держи!"
    "Она протянула мне какой-то бумажный сверток."
    "При ближайшем рассмотрении по масляным пятнам я определил, что это были бутерброды."
    me "Ой, спасибо!"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "А теперь марш умываться!"
    "Я уже собирался уходить, как она остановила меня."
    mt "Сейчас, подожди."
    hide mt onlayer master with dissolve
    window hide

    pause(1)

    window show
    show mt normal panama pioneer at center onlayer master with dissolve
    "Ольга Дмитриевна забежала в домик и, вернувшись, сунула мне какой-то пакетик."
    "Внутри была зубная щетка, мыло, небольшое полотенце и что-то еще, я особо не всматривался."
    show mt smile panama pioneer at center onlayer master with dspr
    mt "Пионер должен быть всегда чист и опрятен!"
    mt "Дай я тебе галстук правильно завяжу на первый раз, а то он у тебя болтается.{w} Потом научишься, сам будешь!"
    me "А может, не надо? Я сейчас умываться же иду – неудобно будет."
    th "Ну да, вдруг зацеплюсь за кран и удавлюсь..."
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Да, пожалуй…{w} Ладно, тогда потом.{w} И не забудь про линейку."
    th "Карандаши, ручки, линейки…{w} Такие вещи не забываются!"
    me "Какую линейку?"
    show mt angry panama pioneer at center onlayer master with dspr
    mt "Ну как же?!"
    "Она нахмурилась."
    mt "Сегодня же понедельник!"
    th "Странно, а по моим подсчетам – воскресенье…"
    th "Впрочем, смена дня недели – это не самое страшное."
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Обычно у нас линейки рано утром, еще до завтрака, но сегодня, так как понедельник, она будет в 12 часов."
    mt "Не опаздывай!"
    me "Хорошо. А где?"
    mt "На площади, где же еще!"
    "Спорить было бессмысленно."

    stop ambience fadeout 2

    "Я направился в сторону «помывочной»."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    play music music_list["everyday_theme"] fadein 5

    window show
    "Да, отдельного душа и туалета в пионерлагере, конечно, ожидать не стоило, но почему-то при виде этого атавизма загнивающего социализма – причудливой черепашки с панцирем из жести, множеством ног-кранов и кафельным брюшком – мне стало несколько не по себе."
    "Нет, я не был брезгливым человеком."
    "В конце концов, мне даже как-то удалось пережить вчерашний день."
    "Но тем не менее, стоя тут, я осознал, что все же есть какой-то минимальный уровень комфорта, к которому я привык и без которого жить мне довольно проблематично."
    "Вот ведь как бывает – когда теряешь вещи, кажущиеся тебе абсолютно обыденными и естественными, понимаешь, что на самом деле они были незаменимы."
    "С другой стороны, выбора у меня особого и не оставалось."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand2_day onlayer master
    with dissolve

    play sound sfx_open_water_sink

    $ renpy.pause(1)

    play sound_loop sfx_water_sink_stream

    window show
    "Я открыл кран.{w} Вода была просто ледяная."
    "Если помыть руки такой водой не составило особого труда, то вот умыться или прополоскать рот с ее помощью было большой проблемой."
    "В пакетике, который мне дала Ольга Дмитриевна, не нашлось зубной пасты."
    "Я уже было решил, что ничего страшного не будет, если почистить зубы и так, как наткнулся на какую-то кругленькую коробочку."
    "При ближайшем рассмотрении это оказался «Зубной порошок»."
    th "Прелестно! +1 за то, что я где-то в прошлом."
    "Умывание не заняло у меня много времени, хотя и приходилось постоянно корчиться и ежиться от ледяной воды."
    window hide

    stop sound_loop
    play sound sfx_close_water_sink

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    window show
    "Я уже собирался идти назад, как услышал рядом с собой шум шагов."
    show sl normal sport at center onlayer master with dissolve
    "Передо мной стояла Славя в спортивном костюме."
    "Похоже, что эта девочка будет хорошо выглядеть абсолютно во всем – и в пионерской форме, и в купальнике, и, наверное, даже в космическом скафандре."
    show sl smile sport at center onlayer master with dspr
    sl "Физкульт-привет!"
    me "Охай… То есть, бобр… Доброе утро! Вот…"
    "Приветствие мне удалось выбрать не сразу."
    show sl normal sport at center onlayer master with dspr
    sl "Почему на завтраке не был?"
    me "Проспал."
    "Я сказал это так, словно гордился этим своим достижением."
    me "Но мне Ольга Дмитриевна бутерброды принесла."
    show sl smile sport at center onlayer master with dspr
    sl "А, ну отлично тогда! Не забудь на линейку прийти!"
    me "Да, конечно."
    th "Забудешь тут."
    sl "Ладно, я побежала, не скучай!"
    hide sl onlayer master with dissolve
    "Она помахала мне на прощание и скрылась за поворотом тропинки."
    "Судя по всему, линейка должна была начаться через пару минут."

    stop music fadeout 3

    "Стоило быстренько забежать «домой», закинуть пакетик с умывальными принадлежностями, съесть бутерброды и только уже потом идти на площадь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    "Я распахнул дверь домика вожатой и вбежал внутрь так, как будто запрыгивал в последний вагон уходящего поезда."
    window hide

    if persistent.hentai:
        scene cg d2_mt_undressed onlayer master
        with dissolve
    else:
        scene black onlayer master
        with dissolve

    play music music_list["awakening_power"] fadein 0

    window show
    "Но, кажется, это было не лучшим решением – посреди комнаты стояла Ольга Дмитриевна…"
    "И переодевалась!"
    "Я застыл как вкопанный, стараясь даже не дышать."
    if persistent.hentai:
        show cg d2_mt_undressed_2 onlayer master with dspr
    "Наконец вожатая заметила мое присутсвие..."
    mt "Семен!"
    "Я тут же отвернулся."
    mt "Стучаться надо! А теперь выйди!"
    window hide

    stop music fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я вышел."
    th "Да, неудобно получилось."
    "Хотя то, что я увидел, мне весьма понравилось."
    "Через минуту показалась Ольга Дмитриевна."
    show mt normal panama pioneer at center onlayer master with dissolve
    mt "Вот, держи.{w} Теперь это и твой дом тоже."
    window hide

    play sound sfx_keys_rattle

    $ renpy.pause(1)

    window show
    "Она протянула мне ключ.{w} Я положил его в карман."
    th "Дом…"
    th "Конечно, если опустить всю фантасмагоричность происходящего, этот лагерь был далеко не самым плохим местом на Земле, но назвать его домом…"
    th "Всего за день, проведенный здесь."
    "Я не был уверен, что смогу сделать это даже спустя год."
    mt "Ладно, пойдем, опаздываем."
    me "А как же бутерброды?.."
    mt "По дороге съешь!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    window show
    "Мы шли вдоль палаток пионеров, я уплетал бутерброды с колбасой, а Ольга Дмитриевна без умолку о чем-то говорила."
    "Но мое внимание было полностью сосредоточено на еде."
    show mt normal panama pioneer at center onlayer master with dissolve
    mt "Ты меня понял?"
    me "А?"
    show mt angry panama pioneer at center onlayer master with dspr
    mt "Ты не слушаешь!"
    me "Простите…"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Сегодня начинается твоя новая пионерская жизнь!"
    mt "И ты должен приложить все усилия, чтобы она стала счастливой!"
    me "А, да, конечно…"
    show mt surprise panama pioneer at center onlayer master with dspr
    mt "Я серьезно! У пионера много обязанностей, на него возложена большая ответственность – участвовать в общественной работе, помогать младшим, учиться, учиться и еще раз учиться!"
    mt "Мы все тут как одна большая семья.{w} И тебе предстоит стать ее частью."
    th "Да, частью…{w} Я готов даже расписаться в партбилете, лишь бы не слушать этот бред."
    show mt smile panama pioneer at center onlayer master with dspr
    mt "Надеюсь, что по окончании смены у тебя останутся самые лучшие воспоминания о нашем лагере."
    mt "Воспоминания на всю жизнь!"
    me "А когда смена заканчивается?"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Что ты постоянно глупые вопросы задаешь?"
    th "Похоже, от нее мне никаким образом не добиться ответов."
    "А жаль, ведь при всей кажущейся дружелюбности этого мира, {i}он{/i} так и не соизволил представиться."
    th "Возможно, сейчас я к этому отношусь несколько спокойнее, чем еще вчера?"
    "Как будто у нас с {i}ним{/i} негласное перемирие – он не трогает меня, но при этом и мне запрещено задавать какие-либо вопросы."
    "Конечно, такой ситуацией нельзя быть довольным, но что мне остается?{w} Плохой мир лучше доброй ссоры."
    mt "Самое главное для тебя – использовать время, которое ты проведешь здесь, с пользой."
    me "Я постараюсь."
    "Честно говоря, этот разговор меня сильно утомил."

    stop ambience fadeout 2

    "Я бы лучше попытался узнать хотя бы, где это «здесь» находится.{w} Но…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    play music music_list["get_to_know_me_better"] fadein 5

    window show
    "Мы пришли на площадь."
    "Там уже стояли пионеры, выстроившись в шеренгу."
    "Казалось, что их не так уж и много."
    "Если судить даже по количеству палаток, то детей здесь должно было быть в два, а то и в три раза больше."
    show mt normal panama pioneer at center onlayer master with dissolve
    me "А что, еще не все пришли?"
    mt "Да вроде все."
    "Она окинула взглядом пионеров."
    mt "Ладно, иди становись."
    th "Странно.{w} Почему тогда она мне сказала, что больше спальных мест нет."
    hide mt onlayer master with dissolve
    window hide

    scene cg d2_lineup onlayer master
    with dissolve

    window show
    "Пока вожатая рассказывала о плане мероприятий на неделю, я осматривал присутствующих."
    "В паре человек от меня стоял Электроник, чуть дальше – Лена и Славя, а в самом конце – Ульянка и Алиса."
    th "Все знакомые здесь."
    "Пока Ольга Дмитриевна рассказывала про какие-то спортивные соревнования, я с интересом начал рассматривать памятник."
    th "«Генда»..."
    "Я никак не мог вспомнить ни одного революционера с похожей фамилией."
    "Да и поза у него была какая-то странная – казалось, он смотрит на все происходящее с каким-то недоверием, может быть, пренебрежением или даже надменностью."
    th "Наверное, это какой-то местный деятель был…"
    sl "О чем мечтаешь?"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    show sl normal pioneer onlayer master at cright
    show mt normal panama pioneer onlayer master at cleft
    with dissolve

    window show
    "Славя вывела меня из раздумий."
    "Рядом стояла Ольга Дмитриевна."
    mt "Ты запомнил план на неделю?"
    me "План?{w} План я никогда не забуду!"
    show mt smile panama pioneer at cleft onlayer master with dspr
    mt "Вот и отлично!"
    "Она посмотрела на Славю."
    show mt normal panama pioneer at cleft onlayer master with dspr
    mt "Принесла?"
    sl "Да."
    "Славя протянула мне какой-то листок."
    mt "Это обходной лист. Тут четыре позиции. За сегодня тебе нужно везде побывать."
    mt "Во-первых, записаться в клуб, они у нас в здании кружков и отдельно – музыкальный."
    mt "Во-вторых, в медпункт зайти."
    mt "Ну, и в-третьих – в библиотеку."
    mt "Все понял?"
    me "Да."
    "Казалось, что это отличная возможность что-нибудь выяснить, так как в этих локациях я еще не бывал."
    mt "Тогда давай, начинай прямо сейчас."
    me "А как же обед?"
    mt "Ничего страшного! Я тебе еще бутербродов принесу. Обходной лист важнее!"
    sl "Удачи тебе."
    hide sl onlayer master
    hide mt onlayer master
    with dissolve
    "Они ушли так быстро, что я и слова сказать не успел."
    th "Пропустил завтрак, теперь и обед придется."
    th "Да что же это такое?"
    th "Впрочем, может, успею как-нибудь?"
    th "Обед в час.{w} Хотя если я пойду есть, то могу не попасть в какое-нибудь место из списка."

    stop music fadeout 3

    th "Ладно, пока еще все равно в столовую идти рано!"
    window hide

    $ disable_all_zones()

    $ set_zone("music_club","day2_musclub")
    $ set_zone("clubs","day2_clubs")
    $ set_zone("library","day2_library")
    $ set_zone("medic_house","day2_aidpost")
    $ set_zone("dining_hall","day2_dinner")

    jump day2_map

label day2_map:

    if day2_map_necessary_done == 5:
        jump day2_main2
    if day2_map_necessary_done == 2:
        $ reset_zone("dining_hall")
        $ day2_map_necessary_done +=1

    $ show_map()

label day2_musclub:

    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day onlayer master
    with dissolve

    window show
    "Музыкальный клуб располагался на некотором расстоянии от остальных построек лагеря."
    "Снаружи он представлял из себя небольшое одноэтажное здание."
    "Не раздумывая, я зашел."
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    "Внутри обнаружился полный набор музыкальных инструментов, на любой вкус и слух – барабаны, гитары и даже настоящий рояль."
    "Некоторое время мое внимание было плотно приковано к ним – хотелось понять, из какого они примерно временного периода, – но неожиданно под роялем послышалось какое-то копошение."
    window hide

    scene cg d2_miku_piano2 onlayer master
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5

    window show
    "Я наклонился и увидел девочку, которая, кажется, что-то искала."
    "Она стояла на четвереньках в такой пикантной позе, что я не сразу решился начать разговор."
    me "Простите…"
    window hide

    scene cg d2_miku_piano onlayer master
    with dissolve

    window show
    mi "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Она попыталась вскочить, но днище рояля стало для нее непреодолимой преградой."
    mi "Ой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day onlayer master
    with dissolve

    show mi shocked pioneer at center onlayer master with dissolve
    window show
    "С трудом, но она все же выбралась."
    me "Извини, что напугал…"
    show mi normal pioneer at center onlayer master with dspr
    mi "Да ничего! Вижу, у тебя обходной, новенький, значит?"
    me "А? Да."
    show mi smile pioneer at center onlayer master with dspr
    mi "Меня Мику зовут."

    $ meet('mi',"Мику")

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
    mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
    "Она говорила с такой скоростью, что половину слов я не успевал разбирать."
    me "А я Семен."
    show mi happy pioneer at center onlayer master with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Правда, я тут пока одна, но с тобой нас будет двое! Ты на чем-нибудь играть умеешь?"
    "Уже в период моего «отшельничества» я купил себе гитару и по самоучителям выучил пару аккордов, но потом забросил это дело, как и любое другое, которое требовало больше нескольких часов."
    me "Знаешь, я как-то не планировал особо…"
    show mi normal pioneer at center onlayer master with dspr
    mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Я на всем умею, честно-честно."
    "Я не стал спорить с девочкой-мультиинструменталистом, так как в ответ наверняка бы получил очередную пулеметную очередь из слов."
    me "Я подумаю, а пока не могла бы ты подписать?"
    show mi happy pioneer at center onlayer master with dspr
    mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я еще и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
    me "Обязательно… А сейчас мне пора, извини."
    show mi shy pioneer at center onlayer master with dspr
    mi "Конечно, приходи непременно…"
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Окончание ее фразы скрылось за закрытой дверью."
    "С одной стороны, я был бы не против вечерком посидеть побренчать на гитаре, но в такой компании…"
    show dv normal pioneer close at center  onlayer master with dissolve
    "Я повернулся, собираясь уходить, и столкнулся нос к носу с Алисой."
    "Она недобро посмотрела на меня."
    dv "Зачем пришел?"
    me "Обходной…"
    dv "Подписал?"
    me "Да…"
    dv "Свободен!"
    hide dv onlayer master with dissolve
    "Она вошла внутрь, а я поспешил покинуть это место."
    window hide

    stop ambience fadeout 2

    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map

label day2_clubs:

    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    window show
    "Я пошел к зданию кружков."
    "По правде говоря, мне никогда особо не доставляла удовольствия общественная работа."
    "В школе я всегда под любым предлогом пытался пропустить субботники, в институте меня никак не привлекал студенческий совет."
    "Меня не интересовали секции бокса, авиамоделирования или кройки и шитья."
    "Так что сюда я пришел лишь с целью отметиться.{w} Записываться куда-то у меня не было решительно никакого намерения."

    stop ambience fadeout 2

    "Я открыл дверь и вошел."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day onlayer master
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри никого не было."
    "Комната представляла из себя что-то наподобие берлоги юного робототехника – повсюду валялись какие-то провода, нехитрые платы, микросхемы, на столе стоял осциллограф."
    "Из соседнего помещения послышались голоса, и через секунду в комнату вошли двое пионеров."
    show el normal pioneer onlayer master at cleft
    show sh normal pioneer onlayer master at cright
    with dissolve
    "В одном я узнал Электроника, второй же мне был незнаком."
    el "Привет, Семен! А мы тебя ждали."
    th "Кажется, он знает все и обо всех…"
    me "А чего вы меня ждали?"
    el "Ну как же, ты же пришел в наш клуб кибернетиков записываться, так?"
    "Он не дал мне ответить."
    show el smile pioneer at cleft onlayer master with dspr
    el "Знакомься, это Шурик, он у нас главный!"

    $ meet('sh',"Шурик")

    me "А вас в клубе этом только двое, я так полагаю?"
    show el normal pioneer at cleft onlayer master with dspr
    el "Ну, можешь считать, что уже трое."
    "Шурик подошел ко мне и уверенно протянул руку."
    "Его лицо мне казалось почему-то знакомым."
    show sh normal_smile pioneer at cright onlayer master with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal pioneer at cright onlayer master with dspr
    el "Давай я тебе тут все покажу!{w} Ты не стесняйся, располагайся."
    me "Да нет, ребята, я вообще-то…"
    show sh normal_smile pioneer at cright onlayer master with dspr
    sh "Всегда рады новым членам."
    "Он сказал это так, что в голове у меня невольно заиграл гимн Советского Союза."
    "Удивительно, но я еще помнил слова – в первом классе у меня была тетрадка, на обратной стороне которой они были напечатаны."
    me "Да нет, мне бы просто обходной лист подписать."
    show sh normal_smile pioneer at cright onlayer master with dspr
    show el grin pioneer at cleft onlayer master with dspr
    el "Так ты к нам запишись, и мы тебе его подпишем."
    "Он хитро улыбнулся."
    "Я уже подготовился к длинной и нудной дискуссии, как вдруг в комнату кто-то вошел."
    show el normal pioneer onlayer master at left
    show sh normal pioneer onlayer master at right
    show sl normal pioneer onlayer master at center
    with dissolve
    "Я обернулся и увидел Славю."
    sl "А, Семен! Надеюсь, они тут тебя не достают?"
    show sl angry pioneer at center onlayer master with dspr
    "Она строго посмотрела на будущих светил отечественного роботостроения."
    sl "А то я их знаю – они могут!"
    me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
    "Я решил воспользоваться ситуацией."
    show sl normal pioneer at center onlayer master with dspr
    sl "Так это не проблема, давай сюда."
    "Она взяла листок и подошла к Шурику."
    sl "Подписывай!"
    show sh upset pioneer at right onlayer master with dspr
    sh "Ну подожди, мы еще не закончили…"
    show sl angry pioneer at center onlayer master with dspr
    sl "Закончили! Подписывай!"
    "Она посмотрела на него так, что возражать Шурик не решился."

    stop ambience fadeout 2

    "Он поставил свою закорючку, и я, поблагодарив Славю, с чистой совестью направился дальше."
    window hide

    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map

label day2_library:

    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day onlayer master
    with dissolve

    window show
    "Вообще, я, конечно, любил читать, но просиживать днями в библиотеке при нынешних обстоятельствах в мои планы не входило, так что я решил побыстрее пройти этот чекпойнт."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    play ambience ambience_library_day fadein 3

    window show
    "Когда я зашел внутрь, у меня в голове всплыло воспоминание из детства."
    "Оно было очень ярким."
    "Мне лет 7 или 8, я с мамой в библиотеке."
    "Пока она выбирает какие-то книжки, которые мне понадобятся для учебы, я сижу и разглядываю местную подборку комиксов."
    "Тогда мне было сложно понять, почему их здесь так много и почему нельзя забрать часть домой."
    "Понятия коллективной собственности тогда для меня не существовало."
    "Впрочем, как и понятия собственности вообще."
    "Тем более странным было это воспоминание сейчас, когда я находился в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
    "Повсюду висело огромное количество советской символики, а на полках книги были в основном соответствующей тематики."
    "Читать их я никак не планировал – знакомство с полным собранием сочинений Маркса было одной из последних вещей на Земле, которая пришла бы мне в голову."
    "Надо было найти библиотекаря."
    "Оказалось это не так сложно – она спала на столе рядом со мной."
    window hide

    scene cg d2_micu_lib onlayer master
    with dissolve

    window show
    "Я пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
    "Она так мило спала, что мне совсем даже не хотелось ее будить."
    th "Пожалуй, подожду, если через полчаса не проснется, тогда уж что поделать…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    window show
    "Просто так сидеть было скучно, и я взял с полки первую попавшуюся книгу."
    "Артур Шопенгауэр, «Мир как воля и представление»."
    "Я открыл примерно на середине и начал читать:"
    window hide

    $ set_mode_nvl()

    window show
    nvl clear
    "Жизнь человека с ее бесконечными трудами, нуждой и страданием следует рассматривать как объяснение и парафраз акта зачатия, т.е. решительного утверждения воли к жизни; с этим связано и то, что человек обязан природе смертью и с тоской думает об этом обязательстве."
    "Разве это не свидетельствует о том, что в нашей жизни заключена некая вина?"
    "И тем не менее, периодически расплачиваясь смертью за рождения и смерти, мы всегда существуем и испытываем все горести и радости жизни попеременно, когда ни одна из них не может нас миновать: таков результат утверждения воли к жизни."
    "При этом страх смерти, который, несмотря на все страдания жизни, удерживает нас в ней, становится, в сущности, иллюзией; но столь же иллюзорно и влечение, заманившее нас в жизнь."
    "Объективное выражение этого соблазна можно увидеть в обращенных друг на друга страстных взглядах влюбленных: они есть чистейшее выражение воли к жизни в ее утверждении. Как она здесь кротка и нежна!"
    "Она хочет благополучия, спокойного наслаждения и тихой радости для себя, для других, для всех."
    window hide

    $ set_mode_adv()

    play sound sfx_knock_door2

    window show
    "В дверь постучали."
    "Я быстро закрыл книгу и положил ее на место."
    th "Какая отличная привычка – стучать.{w} Надо и мне ее взять на вооружение."

    play sound sfx_open_door_clubs_2

    "В дверь вошла Лена."
    show un normal pioneer at cleft onlayer master with dissolve
    un "Ой…"
    show un shy pioneer at cleft onlayer master with dspr
    me "Привет!"
    "Я улыбнулся."
    un "Привет, а я вот книжку пришла отдать…"
    "У нее в руках была «Унесенные ветром», которую я видел вчера."
    un "Ой, а Женя спит, тогда я попозже зайду…"

    $ meet('mz',"Женя")

    mz "Уже не сплю."
    show mz normal glasses pioneer far at cright  onlayer master with dissolve
    "Я удивленно посмотрел в сторону библиотекарши."
    "Она сидела за столом и пристально наблюдала за мной."
    show mz angry glasses pioneer far at cright onlayer master with dspr
    mz "А тебе чего?"
    me "Мне бы обходной…"
    show mz normal glasses pioneer at cright onlayer master with dissolve
    mz "Давай."
    "Она быстро расписалась и протянула мне его обратно."
    "Вид у нее был такой, что дальнейший разговор казался совершенно неуместным."
    "Лена подошла к ней и отдала книжку, а я поблагодарил Женю и вышел."
    window hide

    stop ambience fadeout 2

    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map

label day2_aidpost:

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я решительно не понимал, что мне делать в медпункте."
    "Здоровье вроде не шалило, тем более местный свежий воздух явно пошел мне на пользу, и самочувствие было куда бодрее, чем обычно."
    th "Но раз надо так надо."
    "Я вошел."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_door_1

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    th "Обычный такой медпункт, у нас в школе был примерно такой же."
    show cs normal stethoscope at center onlayer master with dissolve

    play music music_list["eternal_longing"] fadein 5

    "За столом сидела женщина средних лет."
    "Она бросила на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
    cs "Ну, здравствуй… пионер."
    "Сказала она, не отрываясь от своего занятия."
    me "Добрый день… Мне бы вот…"
    cs "Ты присаживайся."
    "Я оглядел комнату."
    cs "На кушеточку."
    "Я сел."
    cs "Раздевайся."
    "Все это она говорила совершенно ровным тоном."
    me "А зачем?.."
    cs "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center onlayer master with dspr
    cs "Меня, кстати, зовут Виолетта, но ты меня можешь звать просто Виолой."

    $ meet('cs',"Виола")

    "Она повернулась в мою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Я аккуратно протянул ей листок."
    cs "Потом."
    show cs smile at center onlayer master with dissolve
    "Она сняла с шеи стетоскоп и, кажется, намеревалась меня им препарировать."
    window hide

    stop music fadeout 3
    play sound sfx_knock_door7_polite

    $ renpy.pause(1)

    window show
    "Но тут в дверь постучали."
    show cs normal at center onlayer master with dspr
    "Медсестра нехотя ответила:"
    cs "Входите!"

    play sound sfx_open_door_strong

    "Моментально дверь распахнулась и в комнату вбежал Электроник."
    show el fingal pioneer far at left  onlayer master with dissolve   
    show cs normal at center onlayer master with dspr
    el "Здрасьте! Я тут это… На футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
    "У Электроника под глазом красовался здоровенный фингал."
    th "Что-то я сомневаюсь, что такой можно заработать на футболе."
    cs "Садись, сейчас посмотрим."
    "Сказала она ему."
    show cs normal glasses at center onlayer master with dissolve
    cs "А ты давай сюда свой обходной."
    "Медсестра быстро подписала его и продолжила:"
    show cs smile glasses at center onlayer master with dspr
    cs "Если что заболит – сразу ко мне… пионер."

    stop ambience fadeout 2

    "Я не стал ничего отвечать и вышел, закрыв за собой дверь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    window show
    th "Медсестра здесь, конечно, еще та…"
    window hide

    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map

label day2_dinner:

    $ lp_us = lp_us +1

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    "Я решил все же выкроить время, чтобы сходить пообедать."
    th "Обходной лист никуда не денется, потом быстренько подпишу, а вот мой желудок явно ждать до ужина не намерен."
    "С такими мыслями я вошел в столовую."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Там почти никого не было – видимо, большинство пионеров уже пообедало."
    "Я встал в очередь за едой."
    "Впрочем, очередью это назвать нельзя, ибо был я там один."
    "Внушающая уважение своими габаритами повариха выдала мне шикарный обед из трех блюд: суп «Ипрская похлебка», гуляш «от Лаврентия Палыча» с гарниром из картошки, сваренной, видимо, по рецептам конца XV века, и компот «Таблица Менделеева»."
    "Такому меню позавидовали бы и лучшие рестораны мира, но мне было все равно, ибо есть хотелось сильно."
    "А по сравнению с моими обычными пельменями, приправленными макаронами и дошираком, и такой обед казался весьма неплохим."
    "Я сел за первый попавшийся стол и принялся сосредоточенно есть."
    window hide

    play sound sfx_punch_medium
    with vpunch

    play music music_list["eat_some_trouble"] fadein 5

    $ renpy.pause(1)

    window show
    "Однако сосредоточенность моя продлилась недолго – кто-то ударил меня по спине, да так, что я подавился."
    "Я обернулся и увидел Ульянку."
    show us laugh pioneer at center onlayer master with dissolve
    me "Я тебя когда-нибудь удушу!"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Не догонишь!"
    "Она показала мне язык!"
    show us grin pioneer at center onlayer master with dspr
    us "Один раз уже пытался – не догнал же."
    me "Хорошо, тогда я тебя где-нибудь подкараулю!"
    show us surp2 pioneer at center onlayer master with dspr
    us "Так нечестно!"
    me "Ты на себя посмотри, честная!"
    "Я ухмыльнулся."
    show us laugh pioneer at center onlayer master with dspr
    us "Ладно, подожди, сейчас обед возьму и подойду, вместе поедим."
    hide us onlayer master with dissolve
    "Перспектива была не самой радужной, поэтому я постарался побыстрее закончить."
    "Однако мне это не удалось, так как Ульянка вернулась буквально через полминуты."
    show us smile pioneer at center onlayer master with dspr
    "На ее тарелке лежал огромный кусок жареного мяса и несколько отварных картофелин."
    "По сравнению с моей королевской трапезой…"
    me "Это ты как?.. Откуда?.."
    show us laugh2 pioneer at center onlayer master with dspr
    us "Уметь надо!"
    "Она посмотрела на меня и улыбнулась во все свои 32… или сколько их у нее там было… зуба."
    "Такого оскорбления я никак стерпеть не мог!"
    "Я никогда не умел толком над кем-то подшучивать, да и в школе больше прикалывались надо мной."
    "Однако я чувствовал, что просто необходимо ей чем-то отомстить."
    me "А что если Ольга Дмитриевна узнает, что ты воруешь еду?"
    show us surp3 pioneer at center onlayer master with dspr
    us "Так я не ворую!"
    "Возмутилась Ульяна."
    me "А вот это ты ей будешь рассказывать. Думаешь, поверит?"
    show us surp2 pioneer at center onlayer master with dspr
    us "Ты же не собираешься ей меня закладывать?!"
    me "Ну… это зависит от многих обстоятельств."
    show us calml pioneer at center onlayer master with dspr
    us "Например?"
    "Она внимательно посмотрела на меня."
    me "Принеси мне булочку. Сладкую."
    show us shy2 pioneer at center onlayer master with dspr
    us "Откуда же я тебе ее возьму?"
    me "Наверное, оттуда же, где взяла это."
    "Я показал на ее тарелку."
    "Ульянка замялась."
    show us dontlike pioneer at center onlayer master with dspr
    us "Ладно. Но только одну!"
    show us surp2 pioneer at center onlayer master with dspr
    us "И обещай, что после этого не расскажешь Ольге Дмитриевне!"
    me "Слово пионера!"
    hide us onlayer master with dissolve
    "Она убежала в сторону буфета, а я недолго думая взял перечницу, открутил крышку и высыпал все содержимое ей в компот."
    "Только я успел поставить ее на место, как Ульяна вернулась."
    show us laugh pioneer at center onlayer master with dissolve
    me "Держи, вымогатель!"
    th "Кажется, она ничего не заметила."
    me "А теперь давай кто быстрее выпьет компот!"
    show us surp2 pioneer at center onlayer master with dspr
    us "Что еще за глупости!"
    me "Почему глупости? Я выиграю, вот увидишь!"
    show us dontlike pioneer at center onlayer master with dspr
    us "Не буду я с тобой в детские игры играть."
    me "Сама-то не ребенок разве?"
    "Я ехидно улыбнулся."
    show us angry pioneer at center onlayer master with dspr
    us "Ах так! Ладно! Раз, два, три!"
    "Она не дала мне времени даже взять чашку, а сама моментально, одним глотком, выпила весь свой компот."
    window hide

    show bg int_dining_hall_day onlayer master:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat 10

    stop music fadeout 0

    show us fear pioneer at center onlayer master with dspr

    play sound sfx_angry_ulyana

    with flash_red

    $ renpy.pause(5)

    window show
    "Через секунду у нее на лице появилось выражение первобытного ужаса, щеки покраснели, а глаза, казалось, готовы были вылезти из орбит."
    hide us onlayer master with dissolve
    "Она вскочила и побежала в сторону чайников с водой, на ходу выкрикивая:"
    us "Ты! Ты! Ты…"

    stop ambience fadeout 2

    "Я решил не дожидаться, пока она придет в себя и, посмеиваясь, вышел из столовой, на ходу доедая булочку."
    window hide

    $ disable_current_zone()
    jump day2_map

label day2_main2:

    scene black onlayer master
    with dissolve2

    window show
    "..."
    "Итак, я собрал все подписи, следовательно, надо было зайти к Ольге Дмитриевне, чтобы отдать листок."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show mt normal panama pioneer far at center  onlayer master with dissolve
    window show
    "Вожатая сидела возле домика и читала какую-то книжку."
    "Я сразу подумал, что она сама не очень соответствует образу идеального пионера, которого хотела сделать из меня."
    "Круг ее обязанностей сводился, видимо, только к пламенным речам на линейке, отчитыванию Ульяны и наставлению меня на путь истинный."
    show mt normal panama pioneer at center onlayer master with dissolve
    me "Вот…"
    "Я протянул ей обходной."
    "Она, не читая, сунула его в карман."
    th "Отлично! Значит, можно было самому за всех расписаться и вообще никуда не ходить…"
    show mt smile panama pioneer at center onlayer master with dspr
    mt "Молодец! Ну как, познакомился с нашей медсестрой?"
    me "Да…"
    "Почему-то от этого ее вопроса у меня мурашки по коже побежали."
    show mt normal panama pioneer at center onlayer master with dspr
    mt "В какой кружок записался?"
    me "Да пока ни в какой… Нужно время подумать."
    show mt surprise panama pioneer at center onlayer master with dspr
    mt "Ну, что же ты так! Завтра обязательно запишись куда-нибудь!"
    th "Конечно, всенепременно!"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Ладно, пора уже и на ужин идти."
    th "Ну наконец-то! Я уже проголодался."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    "Вместе с Ольгой Дмитриевной мы направились к столовой."
    "Я посмотрел на небо и отметил, что солнце уже начало садиться."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    show dv normal pioneer onlayer master at fright
    show el normal pioneer onlayer master at fleft
    with dissolve
    window show
    "На крыльце стояло несколько человек: Алиса, Электроник..."
    show us normal pioneer onlayer master at cleft
    show sl normal pioneer onlayer master at cright
    with dissolve
    "Ульяна и Славя."
    show dv angry pioneer at fright onlayer master with dspr
    show el surprise pioneer at fleft onlayer master with dspr

    play music music_list["always_ready"] fadein 5

    "Когда мы подошли, я услышал, о чем они говорят:"
    dv "И больше не называй меня ДваЧе, а то еще получишь!"
    el "Да не называл я тебя так! Тебе показалось!"
    show us grin pioneer at cleft onlayer master with dspr
    us "Называл, называл, я все слышала!"
    show el angry pioneer at fleft onlayer master with dspr
    show sl normal pioneer behind el at cright onlayer master with dspr
    el "Да тебя вообще там не было!"
    us "А вот и была! Я в кустах сидела!"
    hide us onlayer master with dissolve
    show sl angry pioneer at cright onlayer master with dspr
    show el angry pioneer behind sl at fleft onlayer master with dspr
    sl "Хватит вам! Прекратите!"
    th "Значит, Электроник свое ранение не на футболе все же получил."
    show mt normal pioneer at center onlayer master with dissolve
    "Ольга Дмитриевна подошла к ним и попыталась выяснить, что происходит:"
    mt "Что вы тут ругаетесь?"
    sl "Алиса Сыроежкину в глаз…"
    dv "Ничего я не делала!"
    hide dv onlayer master with dissolve
    "Алиса обиженно фыркнула и зашла внутрь."

    stop music fadeout 3

    mt "Ладно, пора ужинать уже."
    hide mt onlayer master
    hide el onlayer master
    hide sl onlayer master
    with dissolve
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Последним в столовую зашел я."
    "Похоже, свободных мест осталось не так много."
    "Я окинул взглядом помещение."
    "Вдалеке виднелось несколько свободных стульев рядом с Алисой, но лучше поголодать недельку, чем рискнуть сесть рядом."
    "Также свободно было рядом с Ульяной, но я не сторонник китайской традиционной кухни – «ем все, что ползает»."
    "И, наконец, свободный стул был рядом с Мику."
    "Если выбирать из трех зол…"
    me "Не возражаешь, если я здесь присяду?"
    show mi normal pioneer at center onlayer master with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5

    mi "Ой, да, конечно! То есть нет, не возражаю! То есть да, садись конечно!"
    "Я сел."
    show mi smile pioneer at center onlayer master with dspr
    mi "Сегодня, смотри, гречка. Ты любишь гречку? И вареная курица! Я вообще курицу не люблю. Ну, то есть не то что не люблю..."
    mi "Но если бы меня спросили, что бы мне больше всего хотелось, то бефстроганов или рагу… Нет, может быть, просто котлета! Или ромштекс! Ты любишь ромштексы?"
    me "Я не особо привередливый."
    "И это была сущая правда."
    mi "Понятно. Но вот десерты, знаешь, мне здесь не очень нравятся. Я мороженое люблю! Ты любишь мороженое? Особенно пломбир «48 копеек», но и «Ленинградское» тоже. Ой, прости, я все о себе!"
    mi "Может, ты больше эскимо любишь?"
    "Ужин в компании этой девочки начинал превращаться в пытку."
    "А я по характеру такой человек, что не могу просто так игнорировать собеседника.{w} Даже ее."
    th "Мы все же за одним столом сидим."
    show mi upset pioneer at center onlayer master with dspr
    mi "Знаешь, я однажды купила вафельный рожок, начала есть, а там внутри шуруп! Представляешь? Настоящий такой шуруп! Или болт… Я, честно говоря, в них не разбираюсь!"
    show mi normal pioneer at center onlayer master with dspr
    mi "Шурупы – это которыми закручивают гайки, а болты – это такие, которые отверткой, да?"
    th "Думаю, что если бы проводился чемпионат по скоростному поеданию пищи, я бы занял в нем одно из призовых мест."
    me "Ладно, я пойду, а тебе приятного аппетита!"
    "Я встал и направился к выходу."
    hide mi onlayer master with dissolve

    stop music fadeout 3

    stop ambience fadeout 2

    "Она что-то пыталась сказать мне вслед, но я не слушал."
    window hide

    $ sunset_time()

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset onlayer master
    with dissolve2

    play ambience ambience_camp_center_evening fadein 3

    window show
    "Выйдя из столовой, я сел на ступеньки и решил подождать, пока переварится ужин."
    "Я просто сидел и смотрел на то, как на лагерь опускается ночь."
    "Здесь все было таким живым днем – громкий детский смех, веселые крики, суета и беготня, шум и гам, спортивные игры и купания на пляже."
    "Но с наступлением темноты все это место резко преображалось."
    "Дневные звуки сменялись тишиной, лишь изредка нарушаемой сверчками и ночными птицами."
    "Лагерь засыпал."
    "В каждой тени можно было узнать кого угодно – приведение, лешего, просто дикое животное, но никак не пионера."
    "Все это я понял по вчерашней ночи."
    "Здесь все строго следовали распорядку дня."
    "Дневной лагерь во власти людей, ночной же – скорее сил природы."
    window hide

    play sound sfx_pat_shoulder_hard

    $ renpy.pause(1)

    window show
    "Кто-то легонько похлопал меня по плечу."

    play music music_list["lightness"] fadein 5

    "Я обернулся."
    show el normal pioneer at left onlayer master with dissolve
    "Это был Электроник."
    el "Пойдем в карты играть."
    me "В карты?"
    el "Да! Я игру новую придумал. Интерееесную!"
    me "И какую же?"
    el "Ну, надо сначала карты найти, потом расскажу."
    me "Так ищи, в чем проблема?"
    show el upset pioneer at left onlayer master with dspr
    el "Они есть только у Ольги Дмитриевны, а она мне не даст…"
    me "Почему?"
    el "Ну, в прошлый раз…"
    "На крыльцо вышли Ольга Дмитриевна и Славя."
    show el normal pioneer onlayer master at left
    show mt normal pioneer onlayer master at center
    show sl normal pioneer onlayer master at right
    with dissolve
    el "Ольга Дмитриевна! А Семен хотел как раз у вас карты попросить!"
    me "Я вообще-то…"
    mt "Зачем?"
    show el smile pioneer at left onlayer master with dspr
    el "Мы игру новую придумали!"
    th "Не мы, а ты."
    show mt surprise pioneer at center onlayer master with dspr
    mt "Что за игра?"
    el "Будут карты – я покажу."
    show mt sad pioneer at center onlayer master with dspr
    mt "Ох, не нравится мне эта идея…{w} Но раз и Семен за, то, наверное, ничего страшного…"
    me "Да я вообще-то…"
    show sl smile pioneer at right onlayer master with dspr
    sl "Давайте я с ним схожу принесу!"
    window hide

    menu:
        "Пойти за картами со Славей":
            $ day2_cards_with_sl = 1
            $ lp_sl = lp_sl + 1
            jump day2_cards_with_sl
        "Пойти одному":
            jump day2_cards_without_sl

label day2_cards_with_sl:

    window show
    "Я решил, что это будет неплохой идеей."
    me "Если ты не против…"

    stop ambience fadeout 2

    sl "Конечно! Пошли."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    window show
    "Мы направились в сторону домика вожатой, но, проходя мимо палаток пионеров, Славя вдруг остановилась."
    show sl normal pioneer at center onlayer master with dspr
    sl "Ой, я же совсем забыла, что карты у меня!"
    th "Очень вовремя."
    me "А где твоя палатка?"
    show sl smile pioneer at center onlayer master with dspr
    sl "Да тут рядом, пойдем!"
    "..."
    window hide

    with fade

    window show
    "Мы подошли к домику, который на самом деле больше напоминал вагончик."
    show sl normal pioneer at center onlayer master with dspr
    sl "Подожди тут минутку, я сейчас!"
    hide sl onlayer master with dissolve
    "Минуты ждать не пришлось – она вернулась через пару секунд."
    show sl normal pioneer at center onlayer master with dissolve
    sl "Вот!"
    "Славя показала мне довольно потрепанную колоду карт."
    sl "Пойдем?"
    me "Пойдем."
    hide sl onlayer master with dissolve
    "..."
    window hide

    with fade

    window show
    "На обратном пути я решил поговорить с ней в надежде что-нибудь выяснить:"
    show sl normal pioneer at center onlayer master with dissolve
    me "А ты давно приехала?"
    sl "Ну, уже неделю здесь."
    me "Понятно… А сама откуда?"
    sl "Я с севера."
    me "А поточнее?"
    show sl smile pioneer at center onlayer master with dspr
    sl "Холодного севера."
    "Она посмотрела на меня и улыбнулась."
    th "Кажется, никто в этом лагере не хочет отвечать даже на самые невинные мои вопросы, которые могут хоть чуть-чуть приоткрыть завесу тайны над всем происходящим."
    "Я решил действовать по-другому."
    me "А что тебе нравится?"
    sl "В смысле?"
    me "Ну, твои увлечения?"
    show sl smile2 pioneer at center onlayer master with dspr
    sl "Ааа… Я природу люблю."
    "Странно, но сейчас она была почему-то немногословна."
    me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
    sl "Скорее краеведом. Всегда интересовалась историей родной страны."
    "Это действительно было похоже на нее."
    "Казалось, из всех местных обитателей она единственная, кто не скрывал в себе никаких загадок."
    th "Может быть, ее тоже как-то сюда забросило, как и меня, и она просто, так же, как и я, пока не доверяет никому до конца."
    "Я решил прощупать почву:"
    me "А почему ты именно в этот лагерь поехала?"
    show sl normal pioneer at center onlayer master with dspr
    sl "Родителям путевку на работе дали."
    th "Опять облом."
    me "Ну, предположим, если бы у тебя был выбор?"
    sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь кажется, что ты становишься каким-то другим человеком!"
    "Мне такого совсем не казалось."
    me "В смысле «другим»?"
    sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
    "Сейчас она рассуждала точно так же, как и Ольга Дмитриевна, и это меня насторожило."

    stop music fadeout 3

    "Я решил пока прекратить расспросы."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show sl normal pioneer onlayer master at cleft
    show mt normal pioneer onlayer master at cright
    with dissolve
    window show
    "Когда мы вернулись, Ольга Дмитриевна сказала Славе:"
    mt "Я же вспомнила, что карты у тебя!"
    sl "Да ничего, мы принесли."
    show mt smile pioneer at cright onlayer master with dspr
    mt "Ну и отлично!"

    jump day2_pre_cards

label day2_cards_without_sl:

    window show
    show sl normal pioneer at right onlayer master with dspr
    me "Да я и один могу сходить…"
    show mt normal pioneer at center onlayer master with dspr
    mt "Ладно. Возьмешь у меня в домике в ящике стола."

    stop ambience fadeout 2

    stop music fadeout 3

    "Я встал и пошел к домику Ольги Дмитриевны."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "И чего я вообще согласился?"
    th "С другой стороны, какие у меня были еще варианты?"
    th "Ночью здесь делать особо нечего, а так хоть развлекусь немного."
    "Но в мозгу упорно крутилась мысль о том, что сейчас не самое лучшее время для развлечений."
    th "Хотя, с другой стороны, если {i}здесь{/i} есть этот лагерь, эти пионеры, то это кому-то надо?"
    th "Да даже если и не надо, то самое логичное – ответы искать именно тут, а не в лесах или полях."
    "А в данный момент {i}ответы{/i} собираются играть в карты..."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_sunset onlayer master
    with dissolve

    play ambience ambience_int_cabin_evening fadein 2

    window show
    "Я открыл дверь своим ключом и зашел."
    "К моему удивлению, карт в ящике стола не оказалось."
    "Там было все, что угодно – ножи, вилки, чашки, тарелки, клейкая лента, ножницы, пара садовых перчаток, моток веревки, несколько целлофановых пакетов, карандаш и пара сломанных ручек…"
    "Но карт не было."
    "Я решил посмотреть в шкафу."
    "Там в основном была одежда Ольги Дмитриевны, но внимание мое привлек маленький ящичек с замочной скважиной."
    "Я потянул, но он не открылся."
    th "Интересно, что она там прячет?"
    "Взламывать его было явно не лучшей идей, тем более я абсолютно не был уверен, что найду там карты."

    if d1_keys:
        $ d2_gave_keys = True
        "Я уже собирался уходить и даже сделал несколько шагов, как в кармане что-то зазвенело."
        "Это были ключи, которые вчера забыла Славя."
        th "А что если..."
        "Некоторое время я стоял в раздумьях, но потом уверенно подошел к шкафу и начал прикидывать, какой ключ может подойти к замку."
        "Конечно, на успех особо рассчитывать не стоило, ведь с какой стати у Слави мог быть ключ от личного ящика Ольги Дмитриевны..."
        "Но к моему удивлению, замок приветливо провернулся несколько раз, и я уже собирался потянуть на себя ручку..."
        window hide

        play sound sfx_open_door_kick

        $ renpy.pause(1)

        window show
        "Как вдруг сзади хлопнула дверь."
        "Я подскочил на месте, резко развернулся, но в домике никого, кроме меня, не было."
        th "Наверное, ветер..."
        "Я с опаской выглянул на улицу, но и там не оказалось ни одной живой души."
        "Возможно, ничего страшного и не произошло, но мне все равно было не по себе."
        "..."
        window hide

        with fade2

        window show
        "После тщательного осмотра соседних кустов я все-таки решил закончить начатое и уже собирался все же узнать все страшные секреты вожатой..."
        sl "Семен, что ты тут так долго?"
        show sl normal pioneer at center onlayer master with dissolve
        me "А... я... да..."
        "Трясущимися руками я старался побыстрее закрыть ящик и вынуть ключ."
        "Славя подошла ближе."
        show sl smile pioneer at center onlayer master with dspr
        sl "Ой, мои ключи! А я их обыскалась! Где ты..."
        me "Да вот по дороге... В кустах валялись..."
        "Слава Богу, что я таки успел замести следы."
        me "Пойдем?"
        "И сейчас мне больше всего хотелось поскорее убраться отсюда и забыть о попытке бесцеремонного вторжения в чужую личную жизнь."
        window hide
    else:

        window hide

    stop ambience fadeout 2        

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show mt normal pioneer onlayer master at right
    show sl normal pioneer onlayer master at left
    with dissolve
    window show
    "Когда я вернулся к столовой, Ольга Дмитриевна с невозмутимым видом сказала:"
    mt "Ой, извини, а карты у Слави были в палатке.{w} Пока ты ходил, она сбегала."
    show sl smile2 pioneer at left onlayer master with dspr
    "Я посмотрел на Славю, она виновато улыбнулась."
    th "Да ладно уж, что там, не беспокойтесь обо мне…"

    jump day2_pre_cards

label day2_pre_cards:

    hide mt onlayer master
    hide sl onlayer master
    with dissolve
    "Славя и Ольга Дмитриевна зашли внутрь."
    "Я уже собирался последовать за ними, как вдруг меня кто-то резко дернул за руку."
    show dv normal pioneer at center onlayer master with dspr

    stop ambience fadeout 2

    play music music_list["you_won_t_let_me_down"] fadein 5

    "Это была Алиса."
    "Она смотрела так, что у меня мурашки побежали по спине."
    me "Тебе что-то надо?"
    "Осторожно спросил я."
    dv "Что, тоже планируешь участвовать в этой дурацкой игре?"
    me "Ну... да, а что такого?"
    dv "Нет, ничего."
    show dv smile pioneer at center onlayer master with dspr:
        linear 0.5 xalign 0.72
    "Она уже собиралась уходить, но вдруг обернулась и внимательно посмотрела на меня, улыбнувшись."
    show dv smile pioneer onlayer master at right:
        linear 0.5 xalign 0.5
    dv "А в карты-то играть умеешь?"
    me "Умею немного."
    "Я никак не мог понять, что ей от меня нужно."
    dv "В дурака небось и все?"
    th "Ты-то как будто звезда покера."
    me "Ну, в принципе, да..."
    show dv normal pioneer at center onlayer master with dspr
    dv "Значит, тут у тебя шансов никаких."
    me "Почему?"
    show dv angry pioneer at center onlayer master with dspr
    dv "По кочану!"
    me "То есть ты правила знаешь?"
    show dv smile pioneer at center onlayer master with dspr
    dv "Конечно!"
    me "Ну, значит, у тебя будет преимущество."
    "Я не видел смысла дальше продолжать этот разговор и сделал несколько шагов по направлению к двери."
    show dv angry pioneer at center onlayer master with dspr
    dv "Что ты все уйти-то пытаешься?!"
    th "А о чем, собственно, еще говорить..."
    show dv smile pioneer at center onlayer master with dspr
    dv "Давай поспорим."
    me "Ты про что?"
    show dv normal pioneer at center onlayer master with dspr
    dv "Какой же ты тупой!{w} Про карты, про что же еще!"
    me "И каков же предмет спора?"
    show dv smile pioneer at center onlayer master with dspr
    dv "Что я тебя обыграю!"
    me "Ну, это самый вероятный исход."
    "Спокойно согласился я."
    show dv normal pioneer at center onlayer master with dspr
    dv "Значит, боишься?"
    me "Я не боюсь...{w} Просто не привык спорить, когда не уверен."
    dv "И рисковать ты тоже не привык."
    th "Сама наблюдательность просто-таки."
    me "Ладно, тогда я..."
    show dv angry pioneer at center onlayer master with dspr
    dv "Нет уж!"
    me "Ну что еще?"
    "Обессиленно вздохнул я."
    "Алиса начала мне надоедать своей пустой болтовней про какой-то бессмысленный спор."
    show dv grin pioneer at center onlayer master with dspr
    dv "Если не согласишься спорить, я всем расскажу, что ты ко мне приставал!"
    me "Что?!"
    dv "Что слышал!"
    th "Да, пожалуй, она вполне может..."
    me "Но это же глупо!{w} Тебе никто не поверит – я всего неполных два дня здесь, да и к тому же..."
    show dv normal pioneer at center onlayer master with dspr
    dv "Хочешь проверить?"
    me "Ну, предположим...{w} И что будет, если я выиграю?"
    show dv smile pioneer at center onlayer master with dspr
    dv "Я никому ничего не скажу."
    me "А если проиграю?"
    show dv normal pioneer at center onlayer master with dspr
    dv "Какой же ты тупой!{w} Расскажу, что ты ко мне приставал, говорила же уже."
    me "То есть, получается, мне нужно доказать, что я не делал того, что не делал и так?"
    dv "Считай как хочешь."
    "Передо мной встал непростой выбор."
    "С одной стороны, было глупо соглашаться – я не знал правил, да и вообще, азартные игры не были моим коньком."
    "Но с другой – она вполне могла сильно осложнить мое дальнейшее пребывание здесь."
    th "Хотя можно ли ей верить?"
    th "Даже если я выиграю, не претворит ли она свои угрозы в жизнь?"
    dv "Так что решил?"
    show un normal pioneer at right onlayer master with dissolve
    "Я уже было собирался ответить, как у меня из-за спины бесшумно вынырнула Лена."
    show dv angry pioneer at center onlayer master with dspr
    dv "Чего тебе?"
    show un scared pioneer at right onlayer master with dspr
    un "Ничего..."
    hide un onlayer master with dissolve
    "Лена поспешила ретироваться."
    show dv normal pioneer at center onlayer master with dspr
    dv "Ну?"
    window hide

    menu:
        "Поспорить с Алисой":
            $ day2_dv_bet = 1
            $ lp_dv = lp_dv + 2
            $ lp_un = lp_un - 1
            window show
        "Не спорить с Алисой":
            $ day2_dv_bet = 0
            $ lp_dv = lp_dv - 2
            $ lp_un = lp_un + 1
            window show

    if day2_dv_bet == 1:
        th "Возможно, я еще сто раз пожалею об этом..."
        me "Ладно, идет!"
        show dv smile pioneer at center onlayer master with dspr
        "Она улыбнулась."
        me "Только если я выиграю..."
        dv "Да-да, все честно, без обмана!"
        "Алиса поднялась по лестнице и вошла внутрь."
        hide dv onlayer master with dissolve
        th "И зачем я во все это ввязался?"
        th "Может быть, уверился, что она в любом случае найдет, как мне жизнь испортить."
        th "Раз уж решила..."
    else:
        th "Нет, ни в какие глупые авантюры я пускаться не намерен!"
        me "Извини уж..."
        show dv angry pioneer at center onlayer master with dspr
        dv "Слабак!"
        "Она фыркнула, поднялась по лестнице и у самой двери бросила мне:"
        dv "Готовься к последствиям!"
        hide dv onlayer master with dissolve
        th "Последствиям?.."
        "Я не был уверен, что поступил правильно."
        "В конце концов, она вполне может до предела осложнить мою жизнь здесь."
        "Но с другой стороны, у меня просто не было права на опрометчивые шаги."

    stop music fadeout 3

    "Я тяжело вздохнул и направился за ней в столовую."
    window hide

label day2_cards:

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset onlayer master
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show
    "Внутри все уже было готово."
    "Тут и там толпились пионеры, весело разговаривая о своем."
    "Помещение столовой очистили, чтобы освободить место для игроков и зрителей."
    "Я осмотрелся."
    "В дальнем углу вокруг одного из столов что-то происходило."
    "Подойдя ближе, я увидел большой лист ватмана с какой-то схемой."
    window hide

    show cg lvl_1 onlayer master with dissolve

    window show
    "В списке участников обнаружилось и мое имя."
    me "Эй, и кто придумал такое распределение?"
    "Толкнул я Электроника, стоявшего рядом."
    el "Конечно же ваш покорный слуга!"
    "Он отвесил мне поклон, от чего меня аж передернуло."
    me "Ну, и зачем меня сюда включили?"
    "Спросил я разочарованно."

    if day2_dv_bet == 1:
        "Возможно, еще пару секунд назад у меня оставалась хоть какая-то надежда на то, что не придется участвовать в этом турнире, и благодаря этому появится возможность легально улизнуть от спора с Алисой."
    else:
        "Возможно, еще пару секунд назад у меня оставалась хоть какая-то надежда на то, что не придется участвовать в этом турнире и благодаря этому у Алисы не будет повода предъявить мне претензии из-за того, что я не стал с ней спорить."

    el "Так распорядился слепой жребий."
    th "Хороший жребий – со всеми участниками турнира я так или иначе уже успел познакомиться."
    th "А ведь, помимо них, тут еще не один десяток пионеров!"
    "Я начал испытывать необъяснимое чувство тревоги."
    "Такое, когда кажется, что за тобой кто-то наблюдает в пустой плотно закрытой комнате без окон."
    window hide

    hide cg lvl_1 onlayer master with dissolve

    show el normal pioneer at center onlayer master with dissolve
    window show
    me "А призы какие-нибудь будут?"
    "Спросил я его лениво."
    "Может быть, просто хотелось развеяться бессмысленным разговором."
    show us grin pioneer at left onlayer master with dissolve
    "Электроник только открыл рот, чтобы ответить, как откуда ни возьмись появилась Ульянка и начала прыгать вокруг него."
    us "Призы-призы!"
    show us grin pioneer at right onlayer master with dspr
    us "Я что-то слышала про призы!"
    me "Знаешь, какой главный принцип Олимпийских игр?"
    show us laugh pioneer at right onlayer master with dspr
    us "Нет, какой?"
    me "Вот вырастешь – узнаешь!"
    show us dontlike pioneer at left onlayer master with dspr
    "Она надула губки и обратилась к Электронику:"
    us "Так призы будут?"
    show el surprise pioneer at center onlayer master with dspr
    el "Ну... Я не знаю.{w} Не от меня это зависит."
    "Он обреченно развел руками."
    th "А ведь действительно, раз уж затеяли эту дурацкую игру, то могли хотя бы шоколадными медалями озаботиться."
    hide us onlayer master with dissolve
    "Ульянка неожиданно сорвалась с места и куда-то побежала."
    th "Мне бы чуток ее оптимизма..."
    me "Ну так что, правила объяснишь?"
    show el normal pioneer at center onlayer master with dspr
    el "Всему свое время!{w} Еще не все собрались."
    "Я окинул столовую взглядом и сразу же заметил Алису, Славю, Лену, Мику и Шурика."
    me "Вроде бы все..."
    show el surprise pioneer at center onlayer master with dspr
    el "Как же! Жени нет!"
    "Мне показалось, что он сказал это несколько взволнованным тоном."
    me "Ну нет и нет, что теперь?"
    me "Поставь вместо нее кого-нибудь другого."
    el "Нельзя..."
    "Растягивая каждую букву, ответил он."
    "Я не стал уточнять, почему именно нельзя."
    me "Ну сходи тогда за ней, что ли, я не знаю."
    show el normal pioneer at center onlayer master with dspr
    with None
    show mt normal pioneer at right onlayer master with dspr
    with dissolve
    mt "Не надо ему никуда ходить – он организатор, ему не положено!"
    "Словно из-под земли рядом с нами возникла вожатая."
    show el upset pioneer at center onlayer master with dspr
    el "Но Ольга Дмитриевна!"
    "Взмолился Электроник."
    show mt smile pioneer at right onlayer master with dspr
    mt "Семен сходит.{w} Так, Семен?"
    "Она посмотрела на меня и улыбнулась."
    th "Конечно, везде я..."
    me "А где она?"
    "Спорить не стоило, так как в моем положении это было не лучшей идеей."
    show mt normal pioneer at right onlayer master with dspr
    mt "Наверное, в библиотеке."
    me "Ладно..."
    "Протянул я и направился в сторону выхода из столовой."
    hide el onlayer master
    hide mt onlayer master
    with dissolve
    el "Только быстрее!"

    stop ambience fadeout 3

    "Донесся мне вслед крик Электроника."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "Скоро и ночь уже."
    "Я не спеша, стараясь убить как можно больше времени, направился в сторону библиотеки."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    play music music_list["your_bright_side"] fadein 5

    window show
    "Проходя по площади, я заметил, что кто-то сидит на лавочке."
    th "Странно...{w} Ведь все должны быть в столовой."
    show mz normal glasses pioneer at center onlayer master with dissolve
    "При ближайшем рассмотрении это оказалась Женя."
    me "Ты что тут делаешь?{w} Тебя все обыскались!"
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "Сижу, как видишь."
    "Она нахмурилась."
    me "Пойдем скорее!"
    show mz normal glasses pioneer at center onlayer master with dspr
    mz "Не хочу."
    "Женя отвернулась от меня."
    me "Почему?"
    mz "Не хочу и все!"
    "Я сел рядом."
    me "Слушай, мне тоже не очень нравится вся эта затея, но нельзя же всех подводить."
    "Я слушал себя, словно со стороны."
    "Еще бы пару дней назад мне бы и в голову не пришло сказать подобное."
    show mz bukal glasses pioneer at center onlayer master with dspr
    "Женя удивленно посмотрела на меня."
    mz "Так что, все только меня ждут?"
    th "А я тебе о чем только что говорил?"
    me "Да."
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "Все равно нет!"
    "Она нахмурилась и снова отвернулась."
    me "Но почему?"
    "Я всплеснул руками."
    show mz shy glasses pioneer at center onlayer master with dspr
    mz "Я не умею играть в карты..."
    me "Ну и что?{w} Я тоже не знаю правил."
    show mz normal glasses pioneer at center onlayer master with dspr
    mz "Ну и как тогда играть?"
    me "А что, ты умеешь только то, о чем читала в книгах?"
    show mz bukal glasses pioneer at center onlayer master with dspr
    mz "Конечно."
    "Она удивленно посмотрела на меня."
    me "А если ты попадешь в Антарктиду и тебе придется охотиться на белых медведей?"
    show mz smile glasses pioneer at center onlayer master with dspr
    mz "Белые медведи не живут в Антарктиде."
    "Женя улыбнулась."
    me "Ладно, это просто пример!"
    me "В конце концов, не на корову же играем."
    "Она задумалась и внимательно посмотрела на меня."
    show mz normal glasses pioneer at center onlayer master with dspr
    mz "Просто не хочу подводить ребят."
    me "Да-да."
    "Саркастически согласился я."
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "И не подумай ничего такого!"
    "Я даже и не знал, что она имела в виду."

    stop music fadeout 3

    stop ambience fadeout 2

    "Очевидно было лишь то, что у любого человека есть свои слабые места."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset onlayer master
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show
    "Через минуту мы уже стояли в столовой."
    show el normal pioneer at center onlayer master with dissolve
    "Все внимательно уставились на Электроника."
    el "Итак..."
    "Прокашлялся он."
    el "Каждый тур состоит из одной игры."
    el "Если будет ничья, то тогда исход решит дополнительная партия."
    el "После этого проигравший выбывает, и начинается следующий тур."
    el "Поскольку добровольцев..."
    "Он посмотрел на меня."
    el "Поскольку участников – восемь, то и туров будет три."
    el "Все понятно?"
    "Толпа пионеров весело загалдела."
    show us laugh pioneer at left onlayer master with dissolve
    us "А призы какие, призы?"
    show sl angry pioneer at right onlayer master with dissolve
    sl "Ульяна, хватит!"
    "Вперед выскочила Славя, тщетно пытаясь поймать Ульянку."
    show us laugh pioneer onlayer master at right
    show sl angry pioneer onlayer master at left
    with dissolve
    us "Пока не выиграю приз, не успокоюсь!"
    "Кажется, одной этой девочки было достаточно для варп-прыжка к Альфе Центавра."
    show us laugh pioneer onlayer master at left
    show sl angry pioneer onlayer master at right
    with dissolve
    us "Призы-призы!"
    "Как заведенная кричала Ульяна."
    sl "Прекрати."
    "Уговаривала ее выдохшаяся Славя."
    show el shocked pioneer at center onlayer master with dspr
    "А у Электроника, похоже, от всей этой беготни вокруг него уже закружилась голова."
    show us laugh pioneer onlayer master at right
    show sl angry pioneer onlayer master at left
    with dissolve
    me "Давайте начинать."
    "Спокойно сказал я и добавил, обращаясь к Ульянке:"
    me "А то никаких призов не получишь."
    "Такой аргумент, похоже, подействовал, и она вернулась на свое место."
    hide us onlayer master with dissolve
    show sl smile pioneer at left onlayer master with dspr
    "За ней последовала и Славя, бросив мне на прощание улыбку благодарности."
    hide sl onlayer master with dissolve
    show el normal pioneer at center onlayer master with dspr
    "Пионеры наконец угомонились."
    hide el onlayer master with dissolve
    "Я подошел к столу, где сидела Лена."
    show un normal pioneer at center onlayer master with dissolve
    me "Не возражаете?"
    "Она подняла на меня глаза и покраснела."
    show un shy pioneer at center onlayer master with dspr
    me "Не волнуйся, я тоже правил не знаю."
    th "Хотя почему «тоже»..."
    "Я сел."
    me "Вот вышло так, что первый тур нам с тобой играть."
    un "Да."
    "Я еще некоторое время смотрел на нее, пытаясь придумать, что бы еще сказать."

label day2_cardgame:

    "Но мои мысли прервал Электроник."

label demo_play:
    python:
        dialogs = {
                (3,"rival_select","call"): "demo_play_intro",
                (3,"me_defend_1","call"):  "demo_play_me_defend_1",
                (3,"me_select_1","call"):  "demo_play_me_select_1",
                (3,"rival_defend","call"): "demo_play_rival_defend",
                (2,"rival_select","jump"): "demo_play_after_loop",
            }
        INVISIBLE = False
        VISIBLE = False
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalUn(un_avatar_set,"Пробная игра")
    jump cards_gameloop

label demo_play_intro:
    show el normal pioneer at center onlayer master with dissolve
    $ show_cards()
    el "Посмотрите на карты внимательно."
    $ show_cards()
    el "Перед вами их ровно шесть!"
    $ show_cards()
    th "Надеюсь, считать здесь все умеют."
    $ show_cards()
    el "Теперь вы можете их открыть."

    $ VISIBLE = True
    $ show_cards()
    "Наконец, когда все посмотрели свои карты, Электроник продолжил объяснять."
    $ show_cards()
    el "Правила такие же, как в покере."
    $ show_cards()
    el "Думаю, все играть умеют?"
    $ show_cards()
    "Я-то умел, но вот в остальных не был уверен."
    $ show_cards()
    el "Сначала идет самая старшая карта, потом пара, потом две пары, потом тройка...{w} Ну и так далее."
    $ show_cards()
    el "Первым ходом вы выбираете карту, которую хотите забрать у противника."
    $ show_cards()
    el "У него же, в свою очередь, есть две попытки поменять карты местами."
    $ show_cards()
    el "Но можно и не пользоваться этим, если собираются забрать ненужную карту."
    $ show_cards()
    el "Естественно, смена карт может помочь не всегда – ведь противник видит, какие карты меняются местами, и тоже может изменить свой выбор."
    $ show_cards()
    el "Далее соперник забирает у вас одну карту в соответствии с вышеописанным алгоритмом."
    $ show_cards()
    el "Ну, и так далее – думаю, все понятно."
    $ show_cards()
    "Мне было совершенно ничего не понятно."
    $ show_cards()
    us "Эй, ты, Эйнштейн недоделанный!"
    $ show_cards()
    "Послышался издалека голос Ульянки."
    $ show_cards()
    us "Ничегошеньки не понятно!"
    $ show_cards()
    el "По ходу разберешься."
    hide el onlayer master with dissolve
    $ show_cards()
    "Электроник отошел к столу со схемой, оставив Ульяну злиться в одиночестве."
    $ show_cards()
    me "Ходи первая."
    $ show_cards()
    "Я надеялся, что быстро смогу вникнуть в игру."
    $ show_cards()
    "И Лена, смутившись еще больше, чем обычно, потянулась к моим картам..."
    window hide
    return



label demo_play_me_defend_1:
    $ show_cards()
    window show
    "Но на середине стола ее рука застыла..."
    $ show_cards()
    un "Ты будешь..."
    $ show_cards()
    th "Точно! Я же должен защищать свою карту!"
    $ show_cards()
    "Я вспомнил, что там говорил Электроник..."
    $ show_cards()
    "Чтобы попытаться запутать соперника, можно поменять карты местами.{w} И так два раза."
    $ show_cards()
    "А можно и не менять..."
    $ show_cards()
    "Защищать мне эту карту или нет?"
    $ show_cards()
    "К тому же я могу сразу согласиться и отдать ей карту, которую она выбрала."
    $ show_cards()
    "А Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    window hide
    return



label demo_play_me_select_1:

    window show
    "Понемногу все становилось понятно!{w} Или хотя бы понятнее..."
    $ show_cards()
    me "Теперь моя очередь."
    $ show_cards()
    "Я могу вернуть карту, которую она забрала, или выбрать любую другую..."
    window hide
    return



label demo_play_rival_defend:
    $ show_cards()
    window show
    "Лена может попробовать защитить свою карту."
    $ show_cards()
    "Но если я буду внимателен, то все равно возьму ту, что выбрал с самого начала."
    window hide
    return



label demo_play_after_loop:
    $ show_cards()
    window show
    "Получилось!"
    window hide

    $ ui.jumpsoutofcontext("day_2_cards_continue")



label day_2_cards_continue:
    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    window show
    "Электроник, до этого лишь молча наблюдавший за игрой, удовлетворенно кивнул."
    "Похоже, теперь мы действительно немного разобрались, что к чему."
    show el normal pioneer at center onlayer master with dissolve
    el "Итак, во время игры противники три раза обмениваются картами, а потом вскрываются."
    "У меня вырвался невольный смешок от слова «вскрываются»."
    show el angry pioneer at center onlayer master with dspr
    el "Что смешного?"
    me "Нет, ничего."
    "Сдерживаясь из последних сил, чтобы не прыснуть, ответил я."
    "Он пристально посмотрел на меня и продолжил."
    show el normal pioneer at center onlayer master with dspr
    el "И мы смотрим, у кого лучше карты."
    hide el onlayer master with dissolve
    "Электроник отошел к своему ватману."
    "И начался собственно турнир."
    window hide

label un_play:
    python:
        dialogs = {
                (0,"win","jump"):          "un_play_win",
                (0,"fail","jump"):         "un_play_fail",
                (0,"draw","jump"):         "un_play_draw",
            }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalUn(un_avatar_set,"Лена")
    jump cards_gameloop


label un_play_fail:
    $ day2_card_result = 0
    jump day2_main3

label un_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump un_play

label un_play_win:
    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset onlayer master
    with dissolve

    window show
    "Я победил!"
    "Впервые я понял, как трудно играть в игру, только что придуманную, да еще и не тобой."
    "Но я выиграл!"
    "Правда, радость победы немного огорчало то, что проигравшей оказалась Лена."
    "Она и так была такой неуверенной в себе."
    th "Теперь мне даже неудобно смотреть на нее."
    "Возможно, следовало все-таки проиграть, чтобы повысить ее самооценку."

    if day2_dv_bet == 1:
        th "Но я же поспорил с Алисой..."

    "Электроник тем временем с гордостью объявил, что первый тур окончен."
    window hide

    scene cg lvl_2_semen_win onlayer master
    with dissolve

    window show
    "Через некоторое время на ватмане появилась схема участников второго тура."
    "Пары полуфиналистов составили: Алиса и Женя, Ульяна и..."
    "Я."
    "У меня вырвался обреченный вздох."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset onlayer master
    with dissolve

    show us grin pioneer at center onlayer master with dissolve
    window show
    "И тут же на стул напротив уселась Ульяна!"
    us "Хы!"
    show us laugh pioneer at center onlayer master with dspr
    "С улыбкой до ушей она уставилась на меня."
    us "Как это ты Лену обыграл?"
    "Она прищурилась."
    us "Жульничал, наверное?"
    me "Я же не ты."
    me "Просто я умею играть в карты."
    th "Пусть она хотя бы так думает."
    me "А ты как Шурика обыграла?"
    show us grin pioneer at center onlayer master with dspr
    us "А..."
    "Ульянка махнула рукой, показывая, как это было просто."
    us "Пригрозила, что вступлю в его клуб."
    show us laugh pioneer at center onlayer master with dspr
    "И снова широко улыбнулась."
    us "Будешь мне поддаваться?"
    me "И не надейся!"
    show us dontlike pioneer at center onlayer master with dspr
    us "Ну вот..."
    show us laugh pioneer at center onlayer master with dspr
    us "Тогда я сама буду выбирать, какую карту тебе отдать!"
    me "Ты правила слышала?"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Да плевать!"
    "Похоже, ее действительно это мало волновало."
    me "Что же, тогда и я буду тебе отдавать только те карты, что выберу сам."
    show us laugh pioneer at center onlayer master with dspr
    us "Договорились!"
    "Воодушевленный победой в первом туре, я решился на этот опасный шаг."
    "Конечно, можно было ввязаться в спор, позвать Электроника и в конце концов настоять на своем, но я почему-то был полностью уверен в исходе этой партии."
    "К тому же мы хоть и нарушали правила игры, но находились с Ульянкой в равных условиях."
    "Я посмотрел на Электроника."
    el "Время начинать второй тур!"
    "Скомандовал он."
    "Я взял карты, стараясь, чтобы Ульянке никак не было их видно."
    hide us onlayer master with dissolve
    window hide

label us_play:
    python:
        dialogs = {
                (3,"me_defend_2","call"):  "us_play_me_defend_2",
                (2,"me_defend_2","call"):  "us_play_me_defend_2",
                (1,"me_defend_2","call"):  "us_play_me_defend_2",
                (0,"win","jump"):  "us_play_win",
                (0,"fail","jump"): "us_play_fail",
                (0,"draw","jump"): "us_play_draw",
            }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalUs(us_avatar_set,"Ульяна")
    jump cards_gameloop


label us_play_me_defend_2:
    $ show_cards()
    window show
    us "Эй, не мешай карты – это меня путает!"
    window hide
    $ show_cards()
    window show
    "Ммм..."
    window hide
    return

label us_play_fail:
    $ day2_card_result = 1
    jump day2_main3

label us_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump us_play

label us_play_win:

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    show us dontlike pioneer at center onlayer master with dissolve
    window show
    us "Эй! Так не честно!"
    us "Ты должен был поддаваться и проиграть!"
    "От недовольства она надула щеки и была похожа на колобка."
    us "Давай переиграем, только ты теперь поддавайся, слышишь?!"
    "Но ее слышал не только я, а весь зал."
    "И даже Электроник."
    el "Никаких переигровок!"
    "Но Ульяна не обратила на него ни малейшего внимания."
    show us angry pioneer at center onlayer master with dspr
    us "Ты должен проиграть!"
    me "Я вообще с тобой не собираюсь играть второй раз."
    "Спокойно сказал я."
    us "Ах, так?"
    me "Да, так."
    show us grin pioneer at center onlayer master with dspr
    us "Тогда я всем расскажу о том, что ты к Алисе приставал."
    "Сказала она шепотом."
    me "Эй! Ты чего?!"
    "Я перегнулся через стол и грозно посмотрел на нее."
    me "Значит, подслушивала?"
    us "Не подслушивала, а просто мимо проходила."
    "В конце концов, сыграть лишний раунд – это куда лучше, чем..."
    th "А ведь она может!"
    "Я вздохнул и обратился к Электронику."
    me "Переиграем, ничего страшного."
    el "Как знаете..."
    "Он пожал плечами."
    "Итак, матч-реванш начался."
    hide us onlayer master with dissolve
    window hide

label us2_play:
    python:
        dialogs = {
                (0,"win","jump"):  "us2_play_win",
                (0,"fail","jump"): "us2_play_fail",
                (0,"draw","jump"): "us2_play_draw",
            }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalUs(us_avatar_set,"Ульяна II")
    jump cards_gameloop

label us2_play_fail:
    $ day2_card_result = 1
    jump day2_main3

label us2_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump us2_play

label us2_play_win:

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    show us dontlike pioneer at center onlayer master with dissolve
    window show
    me "Проще простого."
    "Сказал я и вальяжно развалился на стуле."
    us "Так нечестно!"
    th "Надеюсь, она не потребует еще одной переигровки..."
    me "Почему же нечестно?"
    "Усмехнулся я."
    us "Ладно..."
    "Обиженно сказала она и вышла из-за стола."
    hide us onlayer master with dissolve
    "Я внимательно посмотрел в сторону Электроника и схемы турнира, пытаясь установить, кто же мне достался в соперники по финалу."
    show dv normal pioneer at center onlayer master with dissolve
    "В ту же секунду ко мне за стол села Алиса."
    "Я зачем-то глупо и неестественно улыбнулся."
    me "Поздравляю с победой."
    if day2_dv_bet == 0:
        show dv angry pioneer at center onlayer master with dspr
        dv "Ты еще пожалеешь, что струсил."
        "Пожалуй, я уже жалел."
        "И не то, что струсил, а что вообще стал участвовать в этой дурацкой игре."
    else:
        dv "Рассчитываешь выиграть?"
        me "Рассчитываю, что ты сдержишь свое обещание."

    show dv smile pioneer at center onlayer master with dspr
    dv "Что же, начнем!"
    hide dv onlayer master with dissolve
    window hide

    jump dv_play

label dv_play:
    python:
        dialogs = {
                (0,"win","jump"):  "dv_play_win",
                (0,"fail","jump"): "dv_play_fail",
                (0,"draw","jump"): "dv_play_draw",
            }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalDv(dv_avatar_set,"Алиса")
    jump cards_gameloop

label dv_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump dv_play

label dv_play_fail:
    $ day2_card_result = 2
    jump day2_main3

label dv_play_win:
    $ day2_card_result = 3
    jump day2_main3







label day2_main3:

    if day2_card_result == 0:

        scene cg lvl_2_lena_win onlayer master
        with dissolve

        window show
        "Как обидно все-таки проигрывать..."
        window hide
        pass

    if day2_card_result == 1:
        window show
        "Хотя бы один раунд я выиграл."
        window hide
        pass

    if day2_card_result == 2:
        window show
        "Двачевской я проиграл."
        th "И это ой как нехорошо."
        th "Зная ее, можно предположить, что она завтра выкинет."
        th "Опозорит меня на линейке (если я ее, конечно, не просплю), расскажет Ольге Дмитриевне."
        th "Просто пустит слухи по лагерю…"
        th "Причем самое страшное в том, что поверят наверняка ей, а не мне."
        "Я даже не знал точно почему, но был в этом уверен на 100%%."
        window hide
        pass

    if day2_card_result == 3:
        if day2_dv_bet == 1:
            $ lp_dv = lp_dv + 2
            jump day2_dv
        else:
            window show
            th "И неважно, что я не стал спорить с Алисой, главное – выиграл."
            th "А то, зная ее, можно предположить, что бы она завтра выкинула."
            th "Опозорила бы меня на линейке (если я ее, конечно, не проспал бы), рассказала бы Ольге Дмитриевне."
            th "Просто пустила бы слухи по лагерю…"
            th "Причем самое страшное в том, что поверили бы наверняка ей, а не мне.{w} Я даже не знаю точно почему, но уверен в этом на 100%%."
            window hide
            pass

    $ persistent.sprite_time = "night"
    scene bg ext_dining_hall_away_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 2

    $ night_time()

    window show
    "Я вышел из столовой."
    "Спать ложиться было еще рано, так что небольшая прогулка показалась отличным вариантом."
    th "Куда же направиться?"
    window hide

    stop ambience fadeout 3

    $ disable_all_zones()
    $ set_zone("medic_house","day2_aidpost_eve")
    $ set_zone("square","day2_square_eve")
    $ set_zone("beach","day2_beach_eve")
    $ set_zone("boat_station","day2_dock_eve")
    $ set_zone("camp_entrance","day2_busstop_eve")
    $ set_zone("estrade","day2_stage_eve")
    $ set_zone("sport_area","day2_football_eve")
    $ show_map()

label day2_aidpost_eve:

    $ persistent.sprite_time = "night"
    scene bg ext_aidpost_night onlayer master
    with dissolve

    window show
    "Я просто шел вперед, не особо разбирая направления, и оказался у медпункта."
    "Если мне и была нужна скорая помощь, то скорее психологическая, а получать ее у местной медсестры в мои планы никак не входило."
    "..."
    window hide

    jump day2_main4

label day2_square_eve:

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    window show
    "Я вышел на площадь и сел на скамейку."
    "Просто таращиться на памятник Генде казалось мне сейчас лучшим решением."
    "..."
    window hide

    jump day2_main4

label day2_beach_eve:

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    stop ambience fadeout 2

    window show
    "Я вышел на пляж."
    "Настроение было паршивым, и купаться совсем не хотелось, однако я подошел к воде и попробовал температуру рукой."
    "Вода была теплая."
    "Видимо, за день она так нагрелась, что к вечеру еще не успела остыть."
    th "Что же, может, приду еще, искупаюсь…"
    "..."
    window hide

    jump day2_main4

label day2_dock_eve:

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night onlayer master
    with dissolve

    window show
    "Я решил пойти на пристань."
    "Солнце еще не полностью скрылось за горизонтом, и река вдалеке красиво окрашивалась во все оттенки красного, желтого и оранжевого."
    "Казалось, что вода там горит ярким пламенем, но чем дольше я стоял, тем пожар становился меньше и в конце концов совсем потух."
    "..."
    window hide

    jump day2_main4

label day2_busstop_eve:

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "События прошедшего дня все еще ярко мелькали у меня в голове – чертов никому не нужный обходной, глупый турнир…"
    "Сегодня мне не хотелось больше ничего делать, ни с кем разговаривать, и даже разбираться со своей непростой ситуацией у меня не было никакого желания."
    "Я вышел на площадь, уселся на лавочку и уставился на памятник Генде."
    "..."
    window hide

    with fade2

    window show
    "Не знаю, сколько я так сидел, но из раздумий меня вывело назойливое стрекотание сверчков."

    stop ambience fadeout 2 

    "Я встал и бездумно направился куда глаза глядят."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_no_bus_night onlayer master
    with dissolve

    play ambience ambience_camp_entrance_night fadein 3

    window show
    th "Автобусная остановка..."
    "По какому-то непонятному стечению обстоятельств второй день подряд я вечером попадаю сюда."
    th "Может быть, подсознательно надеюсь, что здесь меня будет ждать автобус, на котором я смогу вернуться в привычный мир?"
    th "Вряд ли."
    th "С другой стороны, чем черт не шутит..."
    "Уже стемнело."
    "Я просто стоял там и смотрел в ночное небо."
    "Астрономия никогда меня не привлекала настолько сильно, как астронавтика."
    "Мне было интереснее смотреть на рисунки далеких созвездий, туманностей и галактик, выполненные художниками, чем разбираться в астрономических единицах, угловых скоростях и массах небесных светил."
    "Конечно, я бы смог найти Большую Медведицу."
    "Но потеряйся я в тайге, и единственным моим спасением стало бы лишь знание того, что мох растет с северной стороны дерева."
    "Впрочем, не уверен, что и это бы мне помогло…"

    if day2_cards_with_sl == 1:
        $ lp_sl = lp_sl + 1
        jump day2_sl

    stop ambience fadeout 2

    "Постояв еще пару минут, я направился назад в лагерь."
    "..."
    window hide

    jump day2_main4

label day2_stage_eve:

    if day2_card_result == 1:
        $ lp_us = lp_us + 1
        jump day2_us

    scene black onlayer master
    with dissolve

    window show
    "Я решил пойти на север (по крайней мере туда, где он по моим представлениям находился)."
    window hide

    scene bg ext_stage_big_night onlayer master
    with dissolve

    window show
    "Спустя пару минут я вышел на концертную площадку."
    "Она представляла из себя несколько рядов деревянных скамеек и деревянную же эстраду."
    "Я поднялся на сцену."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night onlayer master
    with dissolve

    window show
    "Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
    "Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьет слепящий свет прожекторов."
    "Вообразив, что в руках у меня гитара, я попытался исполнить длинное красивое соло."
    "Наверное, со стороны это смотрелось смешно – парень на сцене размахивает руками, бегает туда-сюда, корчится и кривляется, при этом строя глупые гримасы."
    th "Хорошо бы меня здесь никто не увидел!"
    "С такими мыслями я поспешно ретировался отсюда."
    "..."
    window hide

    jump day2_main4

label day2_football_eve:

    if day2_card_result == 0 and day2_dv_bet == 0:
        $ lp_un = lp_un + 1
        jump day2_un

    $ persistent.sprite_time = "night"
    scene bg ext_playground_night onlayer master
    with dissolve

    window hide
    "Подойдя к футбольному полю и окинув его взглядом, я понял, что там никого нет и делать мне там совершенно нечего, и пошел назад."
    "..."
    window show

    jump day2_main4

label day2_dv:

    scene cg lvl_4_semen_win onlayer master
    with dissolve

    play music music_list["always_ready"] fadein 5

    window show
    "Ура! Я выиграл! Пусть теперь Алиса знает, что со мной лучше не связываться!"
    if day2_dv_bet == 1:
        th "Значит, не зря все же я с ней поспорил!"
    "Теперь оставалось надеяться, что она от обиды за поражение не станет распускать ложные слухи..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    $ night_time()

    stop ambience fadeout 2

    window show
    "Захотелось вдруг сделать себе подарок в честь победы и пойти искупаться."
    "По правде говоря, я и плавать-то толком не умел, но возможность окунуться в прохладную воду на пляже при Луне представлялась мне не самой плохой перспективой."
    "Тем более после вчерашнего дня, проведенного в зимней одежде, меня можно было выжимать от пота, так что и помыться не мешало."
    "Так как вечером здесь никого не должно было быть, я разделся до трусов (плавок у меня, естественно, не было) и вошел в воду."
    "Однако плескаться возле берега показалось недостаточным."

    stop music fadeout 3

    "Обычно мне вполне хватало 15-20 метров, но в этот раз, возможно, эйфория от победы на турнире подтолкнула меня на попытку побить свой рекорд."
    "Я плыл медленно и размеренно, следил за каждым движением рук и ног, за каждым вдохом и выдохом."
    window hide

    play music music_list["that_s_our_madhouse"] fadein 3

    scene bg ext_beach_night onlayer master:
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        repeat

    window hide

    play sound sfx_shoulder_dive_water

    show blink onlayer master

    $ renpy.pause(1)

    window show
    "Уже почти доплыв до буйков, я почувствовал сильный удар по спине, от которого ушел под воду."
    "Я начал захлебываться, но усилием воли взял себя в руки и удержался на воде, схватившись за буек."
    window hide

    scene cg d2_water_dan onlayer master
    show unblink onlayer master
    with dissolve

    play sound sfx_water_emerge

    $ renpy.pause(1)

    window show
    "Я обернулся и увидел Алису, плывущую за мной."
    me "Ты что делаешь?!"
    dv "Как что? Приветствую победителя."
    me "А если бы я утонул?!"
    dv "Ну, я бы тебя спасла."
    me "Ага, как же…"

    stop music fadeout 3

    "Находиться здесь было попросту опасно – утопит еще, не ровен час – и, вложив все силы в последний рывок, я поплыл к берегу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    play ambience ambience_boat_station_night fadein 3

    window show
    "Растянувшись на песке, я попытался отдышаться."
    show dv normal swim at center onlayer master with dissolve
    "Через некоторое время из воды вышла и Алиса."
    dv "А ты неплохо плаваешь!"
    th "Я бы не сказал."
    me "Ага, и ты тоже."
    show dv smile swim at center onlayer master with dspr
    dv "Ну, я-то понятно…"
    "Я промолчал."
    dv "Ты сегодня у меня уже два раза выиграл.{w} Значит, тебе прощается те два долга."
    th "Какие долги, за что?"
    "Она, похоже, не совсем здраво воспринимала действительность."
    me "Радушно благодарю…"
    "Съязвил я."
    dv "Знаешь, а ты не такой уж и неудачник…"
    window hide

    scene cg d2_2ch_beach onlayer master with dissolve:
        pos (0,-1920)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -250)

    window show
    "После этих слов я повернул голову в ее сторону."
    "Она была одета в купальник, который хорошо подчеркивал все прелести ее фигуры."
    "Да, при всех минусах характера Двачевской этот плюс у нее не отнимешь."
    me "А с чего это вдруг я неудачник?"
    "Она хитро улыбнулась."
    dv "А что, разве не так?"
    me "Нет конечно!"
    dv "И чем докажешь?"
    me "Не собираюсь я тебе ничего доказывать!"
    dv "Ах, вот так, значит..."
    "Сказала она беззлобно."
    me "Да, вот так..."
    "Наступила ожидаемое молчание."
    "Тихий ночной ветерок лениво играл волнами, то обрушивая их на берег, то забирая назад, чтобы собраться с силами и перегруппироваться."
    "Алиса все так же смотрела словно сквозь меня, казалось забыв о том, что я вообще все еще здесь."
    me "Эй, Земля вызывает Алису!"
    "В ее взгляд вмиг вернулась осмысленность."
    dv "Ладно, бывай."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    window show
    "Она забрала лежащую рядом одежду и ушла."
    "..."
    window hide

    with fade2

    window show
    "Было уже поздно, но я решил еще некоторое время полежать и посмотреть на звезды."
    window hide

    scene stars onlayer master
    with dissolve

    window show
    "В конце концов, раньше мне редко представлялась такая возможность."
    "Или просто я сам редко себе ее создавал."
    th "Ведь если подумать, свет от далеких звезд долетает до нас за миллионы лет…"
    th "Вот сейчас я вижу звезду, потому что она светила тогда, а для нее это {i}тогда{/i} – далекое прошлое."
    th "И сейчас она, возможно, уже взорвалась…"

    stop ambience fadeout 0

    play music music_list["that_s_our_madhouse"] fadein 1

    th "Стоп!{w} Она же и мою одежду забрала!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    window show
    "Я вскочил и начал осматривать пляж."
    "Действительно, Алиса унесла и мою пионерскую форму."
    th "Черт возьми!"
    "А ведь я только начинал думать, что она, может быть, и не такая уж плохая…"
    "Надо было что-то срочно придумать."
    th "Конечно, можно пожаловаться Ольге Дмитриевне, но вернуться к ней в одних мокрых трусах…"
    "В какой палатке живет Алиса, я не знал."
    th "Стучаться во все подряд тоже не вариант…"
    th "Может быть, зайти к Славе?"
    th "Да, точно, ночью в одних трусах…{w} Только розы в зубах не хватает…"
    "С какой стороны ни посмотри, я попал, причем попал серьезно…"
    "Но делать что-то надо было в любом случае."
    "К счастью, не так много времени прошло, и я еще успевал ее догнать..."

    stop music fadeout 3

    "... бегом!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Буквально через пару секунд я оказался на площади."
    show dv normal pioneer2 at center onlayer master with dissolve
    "К моему огромному удивлению, Алиса сидела на лавочке и явно скучала."
    "Она уже успела переодеться."
    me "Отдай!"
    show dv guilty pioneer2 at center onlayer master with dspr
    dv "Да бери…"
    "Ответила она каким-то виноватым тоном и протянула мне мою форму."
    me "…"
    show dv shy pioneer2 at center onlayer master with dspr
    dv "Только не думай, что я это специально тут тебя ждала и все такое..."
    hide dv onlayer master with dissolve
    "Алиса развернулась и не спеша пошла в сторону палаток."
    "Я остался стоять как вкопанный."
    "Такой финт ушами был выше моего понимания."
    th "Возможно, у нее проснулась совесть…"
    th "Хотя какое там…"
    th "В любом случае с ней нужно быть поосторожнее, и события сегодняшнего вечера ничего не меняют."

    stop ambience fadeout 2

    "Я направился к домику Ольги Дмитриевны."
    window hide

    jump day2_main4

label day2_sl:

    "Я уже собирался возвращаться в лагерь, как вдруг услышал какой-то шум за воротами."
    th "И кого еще принесло?.."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_clubs_night onlayer master
    with dissolve

    window show
    "Быстро дойдя до здания кружков, я заметил, что кто-то идет по лесной тропинке."
    "Было темно, так что, кроме размытого силуэта, разглядеть ничего не удалось."
    "Мне стало интересно, кто же это ночью еще не спит."
    th "Пионер, нарушающий режим? Ай-яй-яй!"

    stop ambience fadeout 2

    "Я быстро, но по возможности осторожно направился за таинственной тенью."
    window hide

    play ambience ambience_forest_night fadein 3

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    window show
    "Тропинки сменяли друг друга, и вскоре я оказался в чаще леса, окончательно потеряв из виду незнакомца."
    th "Может, стоило повернуть назад?"
    "Деревья расступились, и передо мной открылся замечательный вид на небольшое лесное озеро."
    window hide

    scene cg d2_slavya_forest onlayer master
    with dissolve

    play music music_list["forest_maiden"] fadein 5

    "И тут я увидел Славю…{w} Она шла по бережку вприпрыжку, даже не шла – порхала, на ходу стягивая пионерский галстук и расправляя рубашку."
    "Все это зрелище показалось мне даже более фантастическим, чем само мое пребывание в этом лагере."
    "Славя виделась мне каким-то духом леса, может быть, нимфой."
    "Она настолько сливалась с природой, что уже становилась не просто человеком, а чем-то вроде древнего божества."
    "Я вспомнил все теологические теории, о которых читал когда-то."
    "Эта ситуация больше всего напоминала пантеизм – растворение Бога в природе, во всем сущем."
    th "Вдруг это не какие-то инопланетяне или провал во времени, а божественное провидение закинуло меня сюда."
    th "Действительно, Славя говорила, что любит природу…"
    th "Получается, что и в ней скрыта какая-то загадка…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    window show
    "Я решил не делать поспешных выводов и последовал за ней…"
    "Славя неслышно плыла между деревьями, выбирая самые удобные тропки и изящно обходя поваленные деревья, ямки и коряги."
    "Мне составляло большого труда не отставать, к тому же я совершенно не хотел, чтобы меня обнаружили – во-первых, подглядывать просто нехорошо, во-вторых, еще неизвестно до конца, что именно она тут делала."
    "Хотя почему-то казалось, что ничего такого – и дело даже не в том, что ничего фантастического или связанного с моим попаданием в этот мир..."
    "Просто – {i}ничего такого{/i}.{w} Ничего, за чем бы стоило подглядывать."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    window show
    "Наконец мы вышли на площадь."
    "Славя остановилась и обернулась в мою сторону."
    show sl normal pioneer far at center  onlayer master with dissolve 
    sl "Думаешь, я тебя не заметила?"
    "Я немного растерялся, но постарался сохранить хотя бы видимость спокойствия."
    me "И давно?"
    show sl normal pioneer at center onlayer master with dissolve
    sl "Не знаю..."
    "Славя подошла ближе."
    show sl smile pioneer at center onlayer master with dspr
    sl "Может быть, минут пять."
    me "То есть и там, на озере?.."
    show sl surprise pioneer at center onlayer master with dspr
    sl "На каком озере?"
    me "Ну как же..."
    "Она выглядела искренне удивленной, поэтому я никак не мог понять – она просто притворяется и делает вид, что ничего не произошло, или..."
    me "Ладно, забудь."
    "Как бы там ни было, я решил поступить галантно (насколько это вообще было возможно в таких обстоятельствах) и промолчать."
    show sl happy pioneer at center onlayer master with dspr
    sl "Хорошо."
    "Неожиданно легко согласилась она."
    sl "Какая сегодня ночь замечательная!"
    "Славя села на скамейку и подняла глаза на небо."
    me "Наверное, тут часто бывают такие ночи."
    show sl smile2 pioneer at center onlayer master with dspr
    sl "Ну, наверное..."
    me "Почему так неуверенно?"
    sl "Нет, просто задумалась."
    me "О чем?"
    show sl normal pioneer at center onlayer master with dspr
    "Она внимательно посмотрела на меня, словно что-то искала у меня на лице, но затем вновь вернулась к созерцанию звезд."
    sl "Просто иногда по ночам такое настроение бывает...{w} Днем – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
    sl "Если бы не сверчки и ночные птицы, то кажется, как будто остался наедине с космосом."
    "Почему-то мне казалось, что Славя – не та девочка, которая будет рассуждать о подобных материях."
    me "Да для меня тут даже слишком спокойно."
    show sl serious pioneer at center onlayer master with dspr
    sl "Правда?"
    me "Да, правда, а что такого?"
    show sl smile pioneer at center onlayer master with dspr
    sl "Ничего..."
    show sl normal pioneer at center onlayer master with dspr
    sl "Ладно!"
    "Она резким движением встала и поправила юбку."
    show sl smile pioneer at center onlayer master with dspr
    sl "Уже и спать пора!"
    me "Спокойной ночи!"
    hide sl onlayer master with dissolve
    "Я проводил ее взглядом."
    "Возможно, наш разговор и был ни о чем, но для меня почему-то он казался наполненным каким-то особенным, таинственным смыслом, который мог родиться только {i}здесь{/i}, только вместе со Славей."
    "И пусть даже я не знаю, где я и почему я именно здесь, но такие минуты тишины и покоя, почти что единения со Вселенной необходимы и мне."
    "Просто жизненно необходимы – особенно сейчас!"
    "..."
    window hide

    with fade2

    window show
    "..."

    stop ambience fadeout 2

    stop music fadeout 3

    "Не знаю, сколько я так сидел, но вскоре начало клонить в сон."
    window hide

    jump day2_main4

label day2_un:

    $ day2_un = 1

    $ persistent.sprite_time = "night"
    scene bg ext_playground_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Мне хотелось уйти подальше ото всех."
    th "Проиграть в первом же раунде…"
    "Нет, такого я сам себе простить не мог."
    "Тогда мне показалось, что самым подходящим местом уединения будет спортивная площадка."
    th "И правда, кому вечером взбредет в голову играть в футбол?"
    "Я присел на лавочку рядом с полем и принялся размышлять о произошедшем."
    "Вдруг со стороны волейбольной площадки послышались какие-то звуки."

    play sound sfx_lena_plays_tennis_fail

    "Присмотревшись, я увидел, что кто-то отчаянно машет рукой."
    th "И кому он там семафорит?.."
    "К моему удивлению, это была Лена."
    "Она подкидывала воланчик и пыталась попасть по нему ракеткой."
    "Однако выходило это у нее паршиво, откровенно говоря."
    "Я некоторое время просто смотрел, но потом решил все же подойти."
    "Обойдя волейбольную площадку, я зашел внутрь так, чтобы она меня видела."
    "Учитывая ее привычку пугаться даже малейшего шороха, не стоило повторять прошлых ошибок."
    show un normal sport at center onlayer master with dissolve
    me "Привет!"
    "Она посмотрела на меня и тут же спрятала за спину ракетку и воланчик."
    me "Бадминтон любишь?"
    un "Ну, не то чтобы…"
    me "Смотрю, у тебя не очень получается.{w} Может, тебя научить?"
    "По правде говоря, я и сам толком не умел, но, как и всем детям, в свое время мне приходилось пару раз играть."
    me "Давай покажу."
    show un shy sport at center onlayer master with dspr
    un "Спасибо."
    "Она покраснела."
    un "Хочу попасть в команду по бадминтону, но, видишь, у меня не очень выходит…"
    un "Я бы сегодня и не пришла, но…"
    show un smile sport at center onlayer master with dspr
    "Она подняла глаза на меня."
    un "Мне никогда в карты не везло, а сегодня выиграла и подумала, что, может, и с этим получится…"
    "Да уж, после этих слов я понял, что поражение от Лены – это вдвойне обидно."
    me "Никогда бы не подумал, что ты увлекаешься спортом."
    show un shy sport at center onlayer master with dspr
    "Она опять покраснела."
    me "Ой, прости…{w} Давай, сейчас покажу!"
    "Я взял ракетку, подбросил воланчик и…"

    play sound sfx_tennis_serve_1

    show un surprise sport at center onlayer master with dspr
    "Ударил с такой силой, что он перелетел ограду и скрылся где-то между деревьями."
    me "Ой, прости!"
    "Я даже не ожидал от себя такой силы."
    show un normal sport at center onlayer master with dspr
    un "Ничего…{w} Правда, это был последний…"
    me "Последний? Пойдем тогда поищем его!"
    un "Нет, не стоит…{w} Там в лесу…"
    me "Кто, леший?"
    "Я засмеялся."
    un "Может быть…"
    "Я-то шутил, а вот она, похоже, нет."
    me "Да никого там нет, не бойся, пойдем!"
    un "Ну, если только с тобой…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    window show
    "Мы вышли с площадки, и я начал осматривать деревья."

    play sound sfx_owl_far

    "Вдруг тишину ночи нарушило уханье совы."
    window hide

    stop ambience fadeout 2

    scene cg d2_sovenok onlayer master
    with dissolve

    play music music_list["confession_oboe"] fadein 5

    window show
    "Лена, видимо, так испугалась, что схватила меня сзади, обвив руками."
    "Она настолько крепко прижалась ко мне, что я смутился."
    "Так близко чувствовать тело девочки, ее тепло."
    "Меня обуяла нежность."
    "Мне хотелось защищать ее, не давать в обиду никому, пусть это будет даже всего лишь сова или какая другая ночная птица."
    "Осталось лишь одно желание – чтобы она не отпускала…"
    "Впрочем, хорошее имеет свойство заканчиваться…"
    "Через некоторое время я определил, откуда исходят звуки, и увидел на ветке рядом с собой маленького совенка, держащего наш воланчик."
    me "Это вот его ты боялась?"
    un "Угу…"
    me "Посмотри, он совсем не страшный."
    "Она выглянула у меня из-за спины, все так же продолжая крепко меня обнимать."
    un "Не страшный…"
    me "Сейчас, подожди."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show un shy sport at center onlayer master with dissolve
    window show
    "Я мягко освободился от ее объятий и подошел к совенку."
    "По правде говоря, казалось, что совенок испугается и улетит, выпустив из клюва воланчик."
    "Однако он, похоже, и не собирался двигаться с места."
    "Мне удалось схватить воланчик и аккуратно отобрать его у совенка."
    me "Смотри, он совсем ручной!{w} Хочешь его погладить?"
    un "Может, в другой раз?.."
    "Я протянул Лене воланчик."
    show un smile sport at center onlayer master with dspr
    un "Спасибо тебе."
    "Она еле заметно улыбнулась."
    show un normal sport at center onlayer master with dspr
    un "Мне пора."
    me "Успехов тебе в бадминтоне."
    show un smile sport at center onlayer master with dspr
    "Она вновь улыбнулась и побежала в сторону лагеря."
    hide un onlayer master with dissolve
    th "Какая она все же милая."

    stop ambience fadeout 2

    "..."
    window hide

    jump day2_main4

label day2_us:

    scene black onlayer master
    with dissolve

    window show
    "События прошедшего дня все еще ярко мелькали у меня в голове – чертов никому не нужный обходной, глупый турнир…"
    "Сегодня мне не хотелось больше ничего делать, ни с кем разговаривать, и даже разбираться со своей непростой ситуацией у меня не было никакого желания."
    "Я пошел на север.{w} По крайней мере в ту сторону, где он по моим прикидкам был."
    "Моя традиция с молодости – ходить на север."
    "Я больше любил эту часть своего родного города, чем южные районы."
    "Также меня никогда не прельщал отдых на черноморских курортах – бескрайние леса и поля были мне куда милее, чем пляжи и барханы."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_big_night onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    "Вскоре я вышел к концертной площадке."
    "Она представляла из себя несколько рядов деревянных скамеек и деревянную же эстраду."
    "Я поднялся на сцену."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night onlayer master
    with dissolve

    window show
    "Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
    "Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьет слепящий свет прожекторов."
    "Вообразив, что в руках у меня гитара, я попытался исполнить длинное красивое соло."
    "Наверное, со стороны это смотрелось смешно – парень на сцене размахивает руками, бегает туда-сюда, корчится и кривляется, при этом строя глупые гримасы."
    "Хорошо бы меня здесь никто не увидел."

    stop ambience fadeout 2

    play music music_list["glimmering_coals"] fadein 5

    us "Ого!"
    "Голос доносился откуда-то сверху."
    show us laugh pioneer onlayer master with dissolve:
        xalign 0.5
        yanchor 0.116
        rotate 180
    "Я поднял глаза и увидел Ульянку, свесившуюся с балки под потолком сцены."
    us "Что это мы тут делаем?"
    me "Да я тут просто…"
    "Оправдываться было явно бесполезно."
    me "Сама все видела."
    "Расстроено сказал я и отвернулся."
    show us laugh2 pioneer onlayer master with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "В тебе, я погляжу, умирает талант великого гитариста."
    "Я ничего не ответил."
    show us smile pioneer onlayer master with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Ну, ладно тебе, не дуйся, смотрелось забавно!"
    "Она захихикала."
    me "Забавно говоришь?"
    "Я ехидно ухмыльнулся."
    us "Да."
    "Спокойно сказала она."
    show us grin pioneer onlayer master with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Подойди-ка сюда."
    me "Куда?"
    us "Ко мне!"
    me "Я туда лезть не собираюсь, не думай даже!"
    "Не то чтобы я боялся высоты, но какой смысл был забираться на эту балку?"
    us "Да нет! Просто сюда."
    "Я почувствовал что-то недоброе, но, так как сразу не смог понять, в чем подвох, медленно направился в ее сторону."
    "Когда я оказался точно под ней, она крикнула:"
    us "Лови!"
    window hide

    scene cg d2_ussr_falling onlayer master
    with dissolve

    window show
    "И прыгнула…"
    "За мгновение у меня в голове пронеслись тысячи мыслей."
    th "Как я ее поймаю? А надо ли вообще ловить? А что, если она разобьется? А что, если она мне что-то сломает? Да и почему именно я?!"
    th "Она сама виновата – нечего дурью маяться!"
    "Удивительно, сколько мыслей приходят и уходят за долю секунды."
    "А ведь иногда, чтобы родить хотя бы одну, уходят годы."
    "В конце концов, логика и инстинкт самосохранения выиграли, и я отошел в сторону."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    show us upset pioneer at center onlayer master with dissolve

    $ renpy.pause(1)

    show us sad pioneer at center onlayer master with dspr
    window show
    "Ульянка мягко приземлилась, перекувыркнулась, мгновенно вскочила на ноги и обиженно посмотрела на меня."
    us "Почему не поймал?"
    me "Ну ты же не разбилась..."
    "Ответил я, отведя взгляд."
    show us shy2 pioneer at center onlayer master with dspr
    us "А если бы разбилась?"
    me "Не разбилась!{w} Да и что это вообще такое? Дешевых фильмов обсмотрелась?"
    show us grin pioneer at center onlayer master with dspr
    us "А что, волнуешься за меня?"
    "Она ехидно ухмыльнулась."
    me "В такой ситуации… Ну, естественно, волнуюсь."
    show us surp3 pioneer at center onlayer master with dspr
    us "Я польщена."
    me "Эй, ты не подумай…"
    show us laugh pioneer at center onlayer master with dspr
    us "Ладно-ладно. Прощаю тебе карты."
    me "А вот я тебе это прощать не…"
    hide us onlayer master with dissolve
    "Я не успел закончить – Ульянка спрыгнула со сцены и убежала в сторону лагеря."
    th "Очередная идиотская выходка этой глупой девчонки."
    th "Да, конечно, я испугался за нее."
    th "Да и будь любой другой на ее месте…"
    "В очередной раз мысленно обругав Ульяну, я направился в сторону своей палатки."
    window hide

    stop ambience fadeout 2

    jump day2_main4

label day2_main4:

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "На подходе к домику вожатой меня накрыла дикая усталость."
    "Свет в окне не горел, значит, Ольга Дмитриевна уже спала."
    th "Странно, ведь вчера она меня ждала…"
    th "Может, доверять начала?"
    th "Да вряд ли…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    window show
    "Я зашел, тихо разделся и лег на кровать."
    th "Если поразмыслить, то моя ситуация за сегодня совершенно не прояснилась."
    th "Я не узнал, ни где я, ни почему я тут."
    th "В сущности, я весь день занимался бесполезными делами; в реальном мире мне бы и в голову не пришло тратить свое время на что-то подобное."
    th "Хотя как раз там у меня этого времени было хоть отбавляй."
    th "А сколько его тут – совершенно неизвестно."
    th "Может быть, целая вечность, а может, всего несколько минут."
    "Мне не хотелось больше думать о прошлом, о том, как я попал в этот лагерь."
    "Впервые за очень долгое время я по-настоящему устал – не только эмоционально, но и физически, психологически и Бог знает как еще..."
    "Я хотел лишь, чтобы от меня все отстали – в первую очередь мои мысли.{w} Хотел, чтобы все разрешилось как-нибудь само собой."
    "Ну, или по крайней мере без моего деятельного участия."
    th "А вдруг я тут навсегда?"
    th "Тогда придется привыкать..."
    th "Но как вот так просто... Я... Я не готов...{w} Эх..."
    "Сознание улетало все дальше, и все сложнее было сконцентрироваться на чем-то конкретном."
    th "Наверное, лучше отложить на завтра..."
    "Я перевернулся на другой бок и заснул."
    window hide

    stop music fadeout 3

    scene bg black onlayer master
    with fade3

    $ renpy.pause(3)

    jump day3_main1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
