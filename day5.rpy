init:
    $ day5_us_wire_accept = 0
    $ day5_map_necessary_done = 0

label day5_main1:

    $ backdrop = "days"

    $ new_chapter(5, u"День пятый")

    $ day_time()

    scene black onlayer master
    with fade

    window show
    "Мы бежали…{w} Бежали из последних сил…"
    "Так бежит человек, отчаянно цепляющийся за жизнь."
    "Обреченный человек, который знает, что ему уже не спастись, но все равно борется с неизбежным, с судьбой..."

    play sound sfx_metal_door_heavy_close 

    "Я из последних сил закрыл за собой тяжелую металлическую дверь."
    window hide

    scene bg int_catacombs_living onlayer master:
        linear 0.1 pos (0,20)
        linear 0.1 pos (0,0)
        linear 0.1 pos (20,0)
        linear 0.1 pos (0,0)
        repeat
    show prologue_dream onlayer master
    with fade

    play sound sfx_nightmare_underground_rumble

    window show
    th "Не знаю, насколько глубоко это бомбоубежище и способно ли оно выдержать взрыв бомбы, но сейчас нам больше негде спастись…"
    "Она крепко сжала мою руку."
    me "Не бойся…"
    "С потолка сыпалась штукатурка, стены тряслись."
    "Я приготовился к худшему."
    "Хотя смерть – это такая вещь, к которой никогда нельзя быть готовым…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living onlayer master
    show prologue_dream onlayer master
    with dissolve

    window show
    "Но вдруг наступила полная тишина."
    "Она словно звенела в ушах, пугая еще больше, чем взрывы бомб."
    dreamgirl "Пора прощаться, наверное…"
    "Она всхлипывала."
    "Я хотел ее хоть как-то утешить, но в то же время понимал, что ничего сделать не смогу."
    me "Да…"
    dreamgirl "Знаешь, я…"
    window hide

    scene bg int_catacombs_living onlayer master:
        linear 0.05 pos (0,20)
        linear 0.05 pos (0,0)
        linear 0.05 pos (20,0)
        linear 0.05 pos (0,0)
        repeat
    show prologue_dream onlayer master
    with fade

    play sound sfx_nightmare_explosion

    window show
    "Ужасный грохот, барабанные перепонки словно разорвались."
    "Кажется, меня придавило рухнувшим потолком, но боли я не почувствовал."
    "Мне лишь хотелось не отпускать ее руку…"
    window hide

    scene bg black onlayer master
    with fade2

    $ renpy.pause(3)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with flash

    play ambience ambience_int_cabin_day fadein 3

    window show
    "Я проснулся в холодном поту, задыхаясь, жадно ловя ртом воздух."
    "В себя прийти получилось не сразу."
    me "Это сон…{w} Всего лишь сон…"
    "Я пытался убедить в этом свой воспаленный мозг."
    th "Но что это за девочка была со мной там?"
    "Так хотелось не отпускать ее руку...{w} Однако вспомнить, кто она, мне так и не удалось."
    "Часы показывали начало одиннадцатого."
    "Я постепенно отходил ото сна, и реальность все увереннее заявляла свои права на мое сознание – в животе предательски заурчало."
    me "Война войной, а обед по расписанию!"
    "Ольги Дмитриевны не было – видимо, она решила не будить меня."
    th "Что же, спасибо вожатой за это!"
    "После вчерашних приключений отдых был мне необходим."
    "Сейчас прошедшая ночь казалась лишь размытым воспоминанием, думать о котором не очень хотелось."
    "Более важным сейчас представлялось найти еду и…{w} помыться!"
    th "Точно!"
    th "Ведь пионер должен быть всегда чист и опрятен."

    stop ambience fadeout 2

    "Впрочем, с этим тезисом я бы согласился, и не будь я пионером (которым я, в общем-то, и не являлся)."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я вышел на улицу и направился в сторону умывальников."
    show el normal pioneer far at center  onlayer master with dissolve   
    "По дороге мне встретился Электроник."
    "Заметив меня, он замахал руками и побежал в мою сторону."
    show el smile pioneer at center onlayer master with dissolve
    el "Доброе утро!{w} Спасибо тебе, что нашел Шурика! Без него я бы даже не знаю…"
    me "Да ничего…"
    "Я несколько смутился."
    show el normal pioneer at center onlayer master with dspr
    el "Нет, правда!"
    me "А как Шурик… Как он с утра себя вел?{w} С ним все в порядке?"
    "Памятуя о его вчерашнем помешательстве, я посчитал этот вопрос вполне уместным."
    el "Да, вполне!{w} Разве что он ничего не помнит…"
    me "Вот как?"
    "Я совсем не удивился."
    el "Ну, он говорит, что вчера пошел в старый лагерь, а потом… Проснулся утром в своей кровати.{w} То есть между этими событиями – провал."
    me "Понятно…{w} Ладно, тогда…"
    show el grin pioneer at center onlayer master with dspr
    el "Тебя же на завтраке не было? Заходи к нам в кружок! Мы тебя покормим! У меня кое-что особенное есть."
    "Электроник заговорщически улыбнулся."
    me "Спасибо, зайду, наверное…"
    "Сначала все равно нужно было помыться."
    el "Ждем!"
    hide el onlayer master with dissolve
    "Он помахал мне рукой и направился по своим делам."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    window show
    "Возле умывальников никого не было."
    window hide

    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1

    $ persistent.sprite_time = "day"
    scene bg ext_washstand2_day onlayer master
    with dissolve

    window show
    "Вода сегодня оказалась на удивление теплой."
    th "Наверное, нагрелась уже…"
    "Умыв лицо, я понял, что остальное тело ополоснуть здесь будет не так-то и просто."
    th "Может быть, стоило пойти в душевую…"
    th "Впрочем, если рядом никого…"
    "Я вывернул кран так, что струя воды била под прямым углом, и начал раздеваться."
    "Оставшись в одних трусах, я еще раз переосмыслил всю затею…"
    th "А если кто-то увидит?"
    th "Ладно, быстренько ополоснусь, вытрусь, оденусь…"
    "Вода, которая казалась нормальной для рук и лица, холодом обжигала остальное тело."

    stop sound_loop fadeout 1
    play sound sfx_close_water_sink

    "Процесс купания занял у меня не более десяти секунд, после чего я начал энергично вытираться."

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    "Но закончить мне так и не удалось – со стороны тропинки послышались какие-то звуки."
    "Решение пришло в долю секунды – я схватил свои вещи и бросился в кусты."

    play music music_list["gentle_predator"] fadein 3

    show dv normal pioneer far onlayer master at cleft
    show us normal pioneer far onlayer master at cright
    with dissolve
    "Через мгновение возле умывальников появились Алиса и Ульяна."
    show dv angry pioneer far at cleft onlayer master with dspr
    dv "Сама бы могла! Зачем меня сюда притащила?"
    show us surp2 pioneer far at cright onlayer master with dspr
    us "Ну что, тебе жалко?"
    show dv normal pioneer far at cleft onlayer master with dspr
    dv "Ладно, давай…"
    show us normal pioneer far at cright onlayer master with dspr
    "Я присмотрелся и заметил, что они обе все перепачканы красной краской."
    th "Вот так номер…{w} И откуда?"
    window hide

    if persistent.hentai:
        scene cg d5_dv_us_wash onlayer master
        with dissolve
    else:
        scene black onlayer master
        with dissolve

    window show
    "Алиса включила воду и начала растирать спину Ульяны."
    dv "Сними лифчик!"
    us "А если кто увидит?.."
    dv "А есть на что смотреть?"
    "Усмехнулась она."
    us "Ладно…"
    window hide

    if persistent.hentai:
        scene cg d5_dv_us_wash_2 onlayer master
        with dissolve
    else:
        scene black onlayer master
        with dissolve

    window show
    "Смотреть и правда было особо не на что, но даже при этом я пристально уставился на девочек."
    "Жаль, что они обе стояли ко мне спиной."
    "Через минуту Алисе удалось смыть всю краску."
    dv "Все!"
    us "Спасибо!"
    dv "Не за что…"
    "Лениво ответила Алиса."
    us "Слушай, а дай мне померить…"
    "Она показала на лифчик Алисы."
    dv "Да он тебе не подойдет…"
    us "Ну, интересно же…"
    dv "Да и тут…"
    us "Тут же нет никого, правда?"
    "Ульяна посмотрела в мою сторону и лукаво улыбнулась."
    "Я был абсолютно уверен, что она не могла меня заметить в этих кустах, но…"
    dv "Да хватит глупости…"
    "Ульянка не стала дослушивать, а вместо этого ловким движением сорвала с Алисы лифчик."

    stop music fadeout 3

    "Вот теперь, надо признаться, было на что посмотреть!"
    window hide

    if persistent.hentai:
        scene cg d5_dv_us_wash_3 onlayer master
        with dissolve
    else:
        scene black onlayer master
        with dissolve

    play music music_list["glimmering_coals"] fadein 3

    window show
    "Я, затаив дыхание, наблюдал, как две девочки гоняются друг за другом вокруг умывальников."
    "Алиса закрыла грудь руками, так что рассмотреть что-то было проблематично."
    "Я подался вперед и, споткнувшись о камень, вывалился из кустов…"
    window hide

    play sound sfx_bush_body_fall

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day onlayer master
    with dissolve

    window show
    "Алиса и Ульяна застыли как вкопанные и уставились на меня."
    "Я же с виноватым видом старался прикрыть свою наготу."
    "Немая сцена продолжалась несколько секунд, затем Алиса схватила рубашку и в мгновение ока кое-как напялила ее на себя."
    show dv angry pioneer2 far at cleft onlayer master with dissolve
    dv "Ты! Ты!"
    "Ее лицо из красного стало фиолетовым.{w} Казалось, что сейчас она взорвется, как ядерная бомба."
    "Единственное, что мне хотелось тогда, – это распасться на атомы и улететь подальше от эпицентра."
    show us laugh pioneer far at cright onlayer master with dissolve
    us "Он все время там сидел!"
    th "Значит, все же заметила…"
    dv "Ты! Ты!"
    me "А я…{w} Да я… Случайно…{w} Если ты понимаешь, о чем я…"
    hide us onlayer master with dissolve
    show dv rage pioneer2 far at cleft onlayer master with dspr:
        linear 1.0 xalign 0.5
    show dv rage pioneer2 at center onlayer master with dissolve
    "Алиса бросилась на меня."
    window hide

    if persistent.hentai:
        scene cg d5_dv_us_wash_4 onlayer master
        with dissolve
    else:
        scene black onlayer master
        with dissolve

    window show
    "Я же, прикрывая одной рукой зад, а другой держа свою одежду, бросился в лес."

    stop ambience fadeout 2

    "Тогда мне это показалось лучшим решением – не появляться же голым днем, посреди лагеря, да еще и преследуемый двумя девочками…"
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    play ambience ambience_forest_day fadein 3

    window show
    "Бежал я не оглядываясь."
    "Спустя несколько минут остановился, чтобы отдышаться."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path2_day onlayer master
    with dissolve

    window show
    "Погони, похоже, не было."
    th "Значит, мне все же удалось спастись!"
    "Однако ценой этому стали исколотые в кровь ноги – о ботинках-то думать времени не было."
    "Я сел на пенек и вздохнул…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    window show
    "Через некоторые время уже одетый я выбрался из леса."
    th "Нужно решить, что же делать дальше!"
    th "Ноги болят, значит, мне прямая дорога в медпункт!"
    th "Но, с другой стороны, живот тоже ждать не намерен."
    th "Может быть, стоит воспользоваться приглашением Электроника."
    th "Или пойти в столовую – вдруг что-нибудь осталось?.."
    window hide

    $ disable_all_zones()

    $ set_zone("clubs","day5_clubs")
    $ set_zone("medic_house","day5_aidpost")
    $ set_zone("dining_hall","day5_dining_hall")

    $ show_map()

label day5_dining_hall:

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    window show
    "Я всегда трепетно относился к своему здоровью.{w} Но трепетнее всего в те моменты, когда становилось уже совсем невмоготу."
    "А сейчас ходить я мог, и не особо напрягаясь."
    "Следовательно, ступни и сами заживут, а вот голод ждать не будет – поэтому я решил попытать счастье в столовой."
    th "Не могли же пионеры съесть все совершенно подчистую?"

    stop ambience fadeout 2

    th "Хотя бы пара сосисок, яиц или на худой конец несколько кусочков хлеба должно было остаться!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Возле столовой было настолько пустынно и тихо, что я даже на секунду замешкался."
    "Не здесь ли каждый пионер ищет свое счастье три раза в день (а некоторые и чаще), не здесь ли оазис в этой жаркой летней пустыне, не здесь ли подпольная химическая лаборатория, исследующая влияние неизвестных науке блюд на неокрепший организм подростков?"
    "Сейчас это здание больше напоминало брошенный защитниками бастион, этакую Ла-Рошель, покинутую гугенотами."
    "Зайди внутрь, и тебя окружат призраки героически погибших бойцов…"
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Впрочем, столовая была совершенно такой же, как и обычно."
    "Разве что совершенно пустой, за исключением…{w} Мику, которая протирала стол."
    "Увидев ее, я резко развернулся и попытался незамеченным ретироваться, но сделать этого мне не удалось…"
    show mi smile pioneer at center onlayer master with dissolve
    mi "Привет, Семен! Ты поесть пришел? Тебя же на завтраке не было. То есть я не видела… Может, ты и был, но я не видела. Но все же хорошо, что пришел!"
    me "Эээ, привет…{w} Да я… Да, вот зашел… Думал, может, осталось чего…"
    mi "А ничего не осталось! Надо ждать обеда! Кстати, не поможешь мне? Я вот убираюсь…"
    me "А зачем?"
    show mi upset pioneer at center onlayer master with dspr
    mi "Ну как же?"
    "Она надула губки."
    mi "Кто-то же должен убираться! У нас все по очереди. И до тебя дойдет!"
    th "Нет уж, спасибо…"
    me "Ага, ясно…"
    "Я уже собирался уходить, но Мику никак не унималась."
    show mi normal pioneer at center onlayer master with dspr
    mi "Так поможешь?"
    window hide

    menu:
        "Ладно…":

            play music music_list["so_good_to_be_careless"] fadein 1

            show mi smile pioneer at center onlayer master with dspr
            window show
            "Не знаю, почему я согласился."
            "Так часто бывает – сначала принимаешь решение, потом долго думаешь, почему ты сказал именно то, что сказал."
            "Думаешь, думаешь…{w} И все равно никак не можешь понять, с чего бы вдруг это тебе в голову взбрело."
            "Вот так я себя чувствовал, вытирая тряпкой столы, один за одним."
            window hide

            scene cg d5_mi onlayer master
            with dissolve

            window show
            mi "Знаешь, я песню новую придумала! Хочешь спою?"
            th "Не горю желанием…"
            mi "Хотя нет…"
            "Она задумалась."
            mi "Петь и одновременно убираться будет тяжеловато… Тогда потом!"
            "Мику обезоруживающе улыбнулась."
            me "Да, конечно…"
            mi "А как ты классно вчера Шурика спас! Весь лагерь с самого утра только об этом и говорит!"
            th "Я себя прямо героем ощущаю…"
            me "Да ничего особенного…"
            mi "Нет, правда-правда! Вот я бы никогда не решилась пойти ночью в лес… Да еще и в старый лагерь… Знаешь, сколько про него легенд ходит? Про вожатую, которая застрелилась…"
            th "А раньше говорили, что вроде бы удавилась…"
            mi "Да и вообще, это же так страшно!"
            me "Да ничего особенного…"
            window hide

            $ persistent.sprite_time = "day"
            scene bg int_dining_hall_day onlayer master
            with dissolve

            window show
            "Я постарался полностью отключиться от каких-либо внешних раздражителей и сконцентрироваться на уборке."
            "Это помогло мне закончить довольно быстро."
            show mi normal pioneer at center onlayer master with dissolve
            me "Вот и все!"
            show mi smile pioneer at center onlayer master with dspr
            mi "Спасибо!"

            stop music fadeout 3

            stop ambience fadeout 2

            "До обеда оставалось еще довольно много времени, так что я решил немного пройтись."
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_dining_hall_near_day onlayer master
            with dissolve

            window show
        "Нет, знаешь, у меня дела еще…":

            show mi upset pioneer at center onlayer master with dspr
            window show
            mi "Ладно, ничего страшного…"
            "Кажется, я расстроил Мику."

            stop ambience fadeout 2

            th "Но что же поделать – такова жизнь…"
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_dining_hall_near_day onlayer master
            with dissolve

            window show
            "Выйдя из столовой, я сел на ступеньки и обессиленно вздохнул."
            "Ступни все еще ныли, хоть и не болели так остро, как вначале, а в желудке было все так же пусто…"
            "До обеда оставалось еще довольно много времени, так что я решил немного пройтись."

    "Направление было выбрано случайно, хотя одним словом его можно охарактеризовать как «прямо»."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Через некоторое время я вышел на площадь."
    "Это и неудивительно – памятник Генде, кажется, являлся центральным местом этого лагеря, этаким нулевым километром…"
    "Я сел на лавочку и задумался."
    th "Прошло уже четыре дня, а я ни на йоту не приблизился к разгадке всего, что здесь творится."
    th "Да, за это время произошло довольно много странных событий, но, если разобраться, практически все можно объяснить логически."
    th "Любое из них могло бы произойти и в нормальной жизни…"
    th "{i}Нормальная{/i} жизнь.{w} Этот термин для меня здесь потерял свое первоначальное значение."
    th "И правда, реакция на окружающую действительность, поступки и слова других людей и свои собственные – все это здесь ненормально."
    th "За столь короткое время, проведенное в этом лагере, мое мировоззрение, кажется, получило серию болезненных ударов под дых и апперкотов, после которых находится если не в нокауте, то в глубоком нокдауне."
    th "Иногда я сам не понимаю, почему совершаю те или иные действия, говорю те или иные слова…"
    th "Точнее, понимаю, но только спустя какое-то время."
    th "Однако это понимание никак не помогает мне вести себя по-другому, более здраво, более адекватно сложившейся ситуации."
    th "Моменты просветления случаются со мной все реже и реже."
    th "Если в первый день моей единственной мыслью было как выбраться отсюда, то сейчас меня больше волнует, где найти поесть, как бы похитрее прогулять линейку по утрам и что сказать Ольги Дмитриевне, если Алиса ей нажалуется…"
    th "И ведь все это для меня действительно важно!"
    th "И с каждым днем эта бытовая суматоха все больше вытесняет из моей головы мысли о том, что все здесь – и этот лагерь, и эти девочки, и вообще весь этот мир – совершенно не нормально!"
    th "Однако поделать с собой я ничего не могу.{w} Я просто забываю…"
    th "Так же, как мы дышим неосознанно, я неосознанно все больше вливаюсь в повседневную жизнь здешних обитателей."
    th "Все больше становлюсь среднестатистическим пионером…"
    me "Нет!{w} Это неправильно!"
    "Громко воскликнул я и несколько раз ударил себя по щекам."

    play sound sfx_dinner_jingle_speaker

    "Вдруг из динамиков заиграла музыка, призывающая пионеров на обед."
    me "Наконец-то!"

    stop ambience fadeout 2

    "Я вприпрыжку поскакал в сторону столовой, а трансцендентальные мысли остались на площади, где они могли заинтересовать разве что Генду, будь он живым…"
    window hide

    jump day5_main2

label day5_aidpost:

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    window show
    "Я всегда довольно трепетно относился к своему здоровью.{w} Хотя бы в те моменты, когда что-нибудь начинало сильно болеть."

    stop ambience fadeout 2

    "Поэтому, не раздумывая, направился в медпункт."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Однако перед дверью меня словно остановила какая-то невидимая сила."
    "Совершенно не хотелось лишний раз общаться с местной медсестрой, но, с другой стороны, вчера я совершил практически подвиг, обороняя медпункт."
    "Так что она была мне в какой-то степени обязана…"

    stop ambience fadeout 2

    "Я собрался с духом и открыл дверь."
    window hide

    play sound sfx_open_door_1

    pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    show cs normal at center onlayer master with dissolve
    window show
    cs "Привет, пионер!"
    me "Здравствуйте…"
    cs "Ты извини, что я вчера так долго…"
    me "Да нет, ничего…"
    show cs smile at center onlayer master with dspr
    cs "А ты что пришел?{w} Заболел никак?"
    "Она хитро улыбнулась."
    me "Да я тут…{w} Ступни немного…"
    cs "Немного что?"
    me "Ступни."
    "Глупо ответил я."
    show cs normal at center onlayer master with dspr
    cs "Ну, показывай."
    "Я сел на кушетку и снял ботинки."
    cs "Где же ты это так?"
    "Мне совсем не хотелось рассказывать о случившемся."
    me "Да я…"
    cs "Ладно, неважно.{w} Сейчас…"
    "Она порылась в ящике и вытащила какой-то пузырек, из которого достала большую красную таблетку с крестовой прорезью."
    me "А это зачем?"
    "Меня несколько смутили размеры таблетки и ее странная форма – обычно ломают пополам же, а не на четыре части."
    show cs smile at center onlayer master with dspr
    cs "А это чтобы тебе потом ноги не пришлось отрезать!"
    me "Что?!"
    window hide

    scene cg d5_cs onlayer master
    with dissolve

    window show
    cs "Да ничего, не бойся…{w} пионер!{w} Сейчас выпьешь, и все пройдет."
    me "А почему эта таблетка…{w} такая?"
    cs "А это для больных, которые отказываются принимать лекарства перорально.{w} Таким мы закручиваем их шуруповертом."
    "Куда именно их закручивают, спросить я не решился."
    cs "А теперь потерпи немного."
    "Она достала большой пакет с ватой, обмотала ей палочку и всю эту конструкцию обильно намазала йодом."
    "Я приготовился к адским мукам…"
    me "ЫЫыыыы…"
    "Я негромко застонал."
    "Однако в этот метод дезинфекции мне верилось куда больше, чем в непонятную таблетку, поэтому я стойко вытерпел жжение."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    show cs normal at center onlayer master with dissolve
    window show
    cs "Вот и все!"
    "Я обулся и попробовал пройтись."
    "Ступни все еще ныли, но острой боли уже не чувствовалось."
    me "Спасибо вам!"
    show cs smile at center onlayer master with dspr
    cs "Не за что!{w} Заходи в любое время…{w} пионер!"
    window hide

    stop ambience fadeout 2

    play sound sfx_close_door_campus_1

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    window show
    "Я попрощался и вышел из медпункта."
    "Проблема со здоровьем была решена!"
    th "Теперь самое время и поесть!"
    window hide

    jump day5_main2

label day5_clubs:

    $ persistent.sprite_time = "day"
    scene bg ext_path_day onlayer master
    with dissolve

    window show
    "Есть хотелось просто безумно."
    "Я всегда трепетно относился к своему здоровью.{w} Но трепетнее всего в те моменты, когда становилось уже совсем невмоготу."
    "А сейчас ходить я мог, и не особо напрягаясь."
    th "Следовательно, ступни и сами заживут, а вот голод ждать не будет…"
    "Я решил воспользоваться предложением Электроника."
    "В конце концов, зная местных пионеров, можно было резонно предположить, что в столовой не осталось даже черствой корки хлеба…"

    stop ambience fadeout 2

    th "А кружок кибернетики мне все же кое-чем обязан."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    window show
    "С такими мыслями я подошел к зданию клубов."
    "Изнутри доносились какие-то крики."
    "Я прислушался, но ничего разобрать не смог, поэтому решил войти."
    window hide

    play sound sfx_open_dooor_campus_1

    pause(1)

    scene cg d5_sh_us onlayer master
    with dissolve

    play music music_list["always_ready"] fadein 3

    window show
    sh "Отдай!"
    us "Не отдам!"
    "По комнате носилась Ульянка, держа какой-то моток проволоки в руках, а за ней бегал Шурик."
    me "Ребят, мне как-то даже неудобно вас прерывать, но…"
    sh "Отдай!"
    "Они не обратили на меня ни малейшего внимания."
    us "Не отдам!"
    "Увлеченный погоней, Шурик проскочил мимо меня, чуть не сбив с ног."
    me "Эй!"
    "Ульянка весело смеялась и нарезала круги по комнате."
    th "Интересно, зачем ей эта проволока вообще сдалась?"
    "Тем временем руководитель кружка кибернетики, еще вчера казавшийся безумным, выглядел вполне нормально.{w} Можно даже сказать – свежо."
    "Но это никак не могло помочь ему поймать Ульянку – она была меньше, изворотливее, быстрее, наконец."
    "И вполне могла загонять его до изнеможения..."
    me "Эй!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day onlayer master
    with dissolve

    show us laugh pioneer at center onlayer master with dissolve:
        linear 1.0 xalign 1.2
    hide us onlayer master with dissolve
    window show
    "Ульянка подскочила и спряталась за мной."

    play sound sfx_close_door_campus_1

    "Шурик же, громко хлопнув дверью, вышел."
    th "Обиделся..."
    me "Эй, ты чего?!"
    us "Не поймаешь!"
    show el angry pioneer at center onlayer master with dissolve
    "Она посмотрела на Электроника, который все это время лишь молча наблюдал за глупой беготней, и показала ему язык."
    el "Семен, отбери у нее проволоку!"
    me "А чего она вам, собственно, вообще сдалась?"
    "Он пытался поймать Ульянку, а та в свою очередь пряталась за мной."
    "Он вправо – она влево, он влево – она вправо…"
    "В конце концов, эта ситуация мне порядком надоела, и я ловким движением выхватил проволоку у Ульяны."
    show el angry pioneer onlayer master at cleft
    show us surp2 pioneer onlayer master at cright
    with dissolve
    us "Отдай! Отдай!"
    "Обиженно закричала она."
    me "А вот и нет! Хватит хулиганить!"
    "Я поднял проволоку над головой так, что Ульянка со своим ростом никак не могла достать."
    show el normal pioneer at cleft onlayer master with dspr
    el "Спасибо!"
    show us dontlike pioneer at cright onlayer master with dspr
    us "Ну и ладно!"
    "Она фыркнула и отвернулась."
    me "Да зачем тебе она вообще?"
    us "Не твое дело…"
    show us surp1 pioneer at cright onlayer master with dspr
    "Она хитро посмотрела на меня."
    us "А хочешь, я всем расскажу, что ты…"
    show us surp3 pioneer at cright onlayer master with dspr:
        linear 1.0 xalign 1.5
    hide us onlayer master with dissolve
    "Я зажал ей рот рукой и потащил к выходу."
    me "Ладно, нам пора уже…"
    "Глупо хихикая, сказал я Электронику."
    show el surprise pioneer at cleft onlayer master with dspr
    el "А зачем приходил?"

    stop music fadeout 3

    "Я ничего не ответил."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show us surp1 pioneer at center onlayer master with dissolve
    window show
    "На улице я отпустил брыкающуюся Ульянку."
    me "Слушай, ну ты же понимаешь, что это недоразумение…{w} Тем более ты его сама и подстроила!"
    us "Ничего не знаю!{w} По факту ты за нами подглядывал!"
    us "Ай-яй-яй!{w} Что же подумает Ольга Дмитриевна…"
    "С одной стороны, мне было абсолютно наплевать, что про это скажет вожатая, но с другой – все против меня, а в моем положении в подобные ситуации попадать не стоит."
    me "Ладно, может, мы как-нибудь договориться сможем…"
    show us shy2 pioneer at center onlayer master with dspr
    us "Хм…"
    "Она задумалась."
    show us laugh pioneer at center onlayer master with dspr
    us "А я знаю!"
    "Я уже предчувствовал недоброе."
    us "Ты принесешь мне ту проволоку!"
    me "Но зачем она тебе?"
    show us dontlike pioneer at center onlayer master with dspr
    us "За надом!"
    me "Ну ладно, допустим...{w} И тогда будешь молчать?"
    show us laugh pioneer at center onlayer master with dspr
    us "Честное пионерское!"
    "Верилось ей с трудом."
    "Но с другой стороны, это всего лишь моток проволоки – почему бы не попробовать?"
    window hide

    menu:
        "Согласиться":
            $ day5_us_wire_accept = 1

            window show
            me "Ладно уж..."
            show us laugh pioneer at center onlayer master with dspr
            us "Вот и отлично!"
            me "Но ты учти..."
            us "Да-да-да, конечно!"
            "Перебила она меня."
            me "Жди здесь."

            stop ambience fadeout 2

            "С этими словами я вернулся в помещение кружков."
        "Отказаться":

            $ lp_us = lp_us + 1
            window show
            me "Нет, никаких проволок, хватит уже!"
            show us angry pioneer at center onlayer master with dspr
            us "Тогда я все расскажу!"
            me "Да и так все расскажешь! Или Алиса..."
            show us sad pioneer at center onlayer master with dspr
            us "Да ну тебя!"
            me "Конечно, как будто я во всем виноват..."
            show us grin pioneer at center onlayer master with dspr
            us "Виноват. Ты за нами подглядывал."
            me "Не подглядывал я ничего!"
            "Хотя, как ни крути, подглядывал..."
            us "Алиса так не думает."
            me "Она много о чем {i}не так{/i} думает."
            show us laugh2 pioneer at center onlayer master with dspr
            us "И Ольга Дмитриевна тоже не оценит."
            me "Знаешь что!"
            "Я начал выходить из себя."
            me "Хочешь рассказать – иди прямо сейчас и жалуйся! Не забудь также добавить, что я виноват в дефолте, мировом кризисе, глобальном потеплении, про библейский потоп тоже упомяни!"
            show us upset pioneer at center onlayer master with dspr
            us "Да ладно тебе так реагировать... Я же пошутила."
            me "Пошутила?.."
            "Я внезапно понял, что действительно слишком завелся."
            me "Шутки у тебя дурацкие! Что, мне каждый раз догадываться – серьезно ты или прикалываешься?"
            show us grin pioneer at center onlayer master with dspr
            us "Да."
            "Ухмыльнулась она."
            us "Так веселее."
            hide us onlayer master with dissolve
            "Ульянка развернулась и побежала в сторону площади, маша рукой на прощание."
            th "И все-таки невозможно с ней по-человечески..."

            stop ambience fadeout 2

            "Я вздохнул и вернулся в помещение кружков."

    window hide

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day onlayer master
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    show el normal pioneer at center onlayer master with dissolve
    window show
    "Внутри я застал Электроника, который сосредоточенно что-то мастерил."
    me "Теперь я со всем разобрался…{w} Думал, может, ты меня чем угостишь, как обещал…"
    "Мой тон звучал несколько заискивающе, и это меня просто взбесило."
    me "Я, конечно, не настаиваю, просто раз уж…"
    show el smile pioneer at center onlayer master with dspr
    el "Сейчас."
    "Он оторвался от своего занятия и достал из стола пару булочек и треугольник кефира."
    el "Прошу."
    me "Спасибо…"
    hide el onlayer master with dissolve
    "Пока я увлеченно ел, Электроник ни на секунду не отрывался от своего приспособления."
    "Он наматывал на катушку проволоку, которую я отнял у Ульянки."
    if day5_us_wire_accept == 1:
        th "И именно эта катушка ей и нужна!"
    show el normal pioneer at center onlayer master with dissolve
    me "А что это?"
    el "Катушка индуктивности."
    me "Индюктивности?"
    show el smile pioneer at center onlayer master with dspr
    el "Вступай в наш клуб – будешь все знать!"
    "Он поднял на меня глаза и хитро улыбнулся."
    me "Я подумаю…"
    "Конечно, никуда я вступать не собирался, но с учетом того, что он меня все же накормил, стоило казаться вежливым."
    show el normal pioneer at center onlayer master with dspr
    el "Кстати, я же тебе говорил, что у меня еще кое-что есть…"
    me "Ну да…"
    el "Сейчас."
    hide el onlayer master with dissolve
    "Он зашел в соседнюю комнату и через минуту вернулся с каким-то пакетом."
    show el smile pioneer at center onlayer master with dissolve
    el "Ту-тту-ру!"
    "Он протянул его мне."
    "Внутри лежала большая бутылка водки «Столичная»."
    me "Эээ, я все понимаю, но еще утро только…"
    th "Или Электронику близок принцип «с утра выпил – весь день свободен»?"
    show el shocked pioneer at center onlayer master with dspr
    el "Ты что?!{w} Я же не предлагаю ее пить! Это нам на протирку оптики!"
    th "Ага, протирку…{w} Внутриутробно…"
    me "Ясно…"
    show el normal pioneer at center onlayer master with dspr
    "Я отдал ему пакет."
    if day5_us_wire_accept == 1:
        me "Кстати! А можно у тебя эту катушка позаимствовать?"
        show el surprise pioneer at center onlayer master with dspr
        el "А зачем тебе?"
        me "Ну..."
        "Пожалуй, это стоило придумать заранее."
        me "Просто нужна."
        show el upset pioneer at center onlayer master with dspr
        el "Так и нам без нее никак."
        me "Да? Ну ладно тогда..."
        th "Не буду же я выбивать у него ее силой?"

    me "Тогда я пойду…"
    show el smile pioneer at center onlayer master with dspr
    el "Обязательно приходи еще!"
    me "Конечно…"

    stop ambience fadeout 2

    th "Как только выпить захочется…"

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    "На улице я задумался, зачем он мне вообще показывал водку…"

    if day5_us_wire_accept == 1:
        show us laugh2 pioneer at center onlayer master with dissolve
        "Ко мне тут же подскочила Ульянка."
        us "Ну? Ну? Достал?"
        me "Нет..."
        show us upset pioneer at center onlayer master with dspr
        us "Значит, сам виноват!"
        me "Сдалась тебе эта катушка вообще..."
        show us grin pioneer at center onlayer master with dspr
        us "Но за старания хвалю!"
        me "Что?"
        "Удивился я."
        show us laugh2 pioneer at center onlayer master with dspr
        us "Алиса бы все равно рассказала!"
        "Она рассмеялась."
        show us surp1 pioneer at center onlayer master with dspr
        us "Она на тебя очень злится."
        me "Надо думать…"
        "Пробурчал я себе под нос."
        show us laugh pioneer at center onlayer master with dspr
        us "Ладно, бывай!"
        hide us onlayer master with dissolve
        "Она помахала мне рукой и убежала."
        th "Что же, просто в очередной раз попал в идиотскую ситуацию, только и всего."
        th "Мне не привыкать..."

    play sound sfx_stomach_growl

    "Голод внезапно вновь напомнил о себе…"
    "Конечно, булочки и кефир – это здорово, но одними ими не наешься."

    play sound sfx_dinner_jingle_speaker

    "Хорошо, что в этот момент заиграла музыка, призывающую пионеров на обед."
    window hide

    jump day5_main2

label day5_main2:

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    th "День только начался, а мне уже столько всего пришлось пережить…"
    th "Но я выстоял и теперь имею законное право наесться до отвала!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    stop sound fadeout 2

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Сегодня я пришел не позже всех, так что смог занять свободный столик."
    "На обед был гороховый суп и рыба с картофельным пюре."
    "Это меня довольно сильно разочаровало, так как рыбу я не ел ни в каком виде, а значит, калорий мой организм получит меньше, чем обычно."
    "Когда с первым было покончено, к моему столику подошли Славя и Лена."
    show sl smile pioneer onlayer master at cright
    show un normal pioneer onlayer master at cleft
    with dissolve
    sl "Можно?"
    "Она мило улыбнулась."
    me "А?{w} Да, конечно!"
    "Я встал и выдвинул стул для нее."
    me "Прошу!"
    "Мое настроение в тот момент было лучше некуда."
    un "Приятного аппетита…"
    "Сказав это, Лена некоторое время пристально смотрела на меня, но потом, видимо, поняла, что выглядит несколько странно, и уткнулась в свою тарелку."
    me "И тебе."
    show sl normal pioneer at cright onlayer master with dspr
    sl "Семен, есть какие-нибудь планы на день?"
    me "Нет."
    "Искренне ответил я – планов действительно никаких не было."
    sl "Тогда не хочешь ли с нами прокатиться на лодке до острова?"
    th "Остров…{w} Кажется, я видел его с пристани."
    me "Зачем?"
    show sl smile2 pioneer at cright onlayer master with dspr
    sl "Ольга Дмитриевна просила земляники собрать.{w} Там ее много, и она такая вкусная!"
    "По выражению лица Слави можно было представить вкус этой земляники, даже не пробуя."
    me "Земляника…{w} А зачем?"
    sl "Не знаю, но, по-моему, идея отличная!"
    th "По-моему, тоже.{w} Тем более на острове я еще не был…"

    stop ambience fadeout 2

    me "Да, пожалуй."
    window hide

    scene bg black onlayer master
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_boathouse_day onlayer master
    with dissolve

    play ambience ambience_boat_station_day fadein 3

    show sl normal pioneer onlayer master at cright
    show un normal pioneer onlayer master at cleft
    with dissolve
    window show
    "Через десять минут мы уже стояли на пристани."
    sl "Вот лодка.{w} Подожди, я сейчас за веслами схожу."
    hide sl onlayer master with dissolve
    "Я остался наедине с Леной."
    me "А ты землянику любишь?"
    show un smile pioneer at cleft onlayer master with dspr
    un "Не то чтобы очень…{w} Но она вкусная."
    "Лена улыбнулась."
    me "Ясно…"
    "Я не знал, что сказать дальше, как поддержать разговор."
    "Если бы Славя не вернулась, мы бы, наверное, так и сидели молча до самого вечера."
    show sl normal pioneer at cright onlayer master with dissolve
    sl "Вот!"
    "Она протянула мне два увесистых весла."
    me "Ага… Да…"
    window hide

    scene cg d5_boat onlayer master
    with dissolve

    stop ambience fadeout 2

    play sound_loop sfx_rowboat_loop fadein 2

    play music music_list["everyday_theme"] fadein 3

    window show
    "Мы забрались в лодку, я отвязал ее, оттолкнул от берега и кое-как начал грести."
    me "А куда именно плыть?"
    sl "Вон туда!"
    "Она показала пальцем в сторону острова."
    sl "Остров «Ближний»."
    th "Интересно, какой капитан его так назвал?{w} Остров-то действительно близко к берегу."
    me "Вас понял!"
    th "Если бы заранее знать, что меня ждет впереди…"
    "Я никогда не был крутым гребцом, более того – я и на лодке-то плавал до этого всего раз или два в жизни."
    "До острова было всего метров пятьсот, но весь путь благодаря моим стараниям мы шли зигзагами."
    "Примерно на середине руки заболели так сильно, что я бросил весла, чтобы передохнуть."
    me "А что…{w} Земляника больше нигде не растет?{w} Я имею в виду места более доступные."
    sl "Но там она самая вкусная."
    "Удивленно посмотрела на меня Славя."
    un "Тебе, наверное, тяжело одному грести?"
    "Вот Лена сразу поняла, в чем дело."
    me "Да нет…{w} Нормально…"
    "Все-таки нельзя же допустить, чтобы мне помогала хрупкая девочка."
    "Остальную часть пути я думал только о том, как бы живым добраться до острова."
    "Славя с Леной о чем-то говорили, но я их не слушал – просто не было сил."

    stop music fadeout 3
    stop sound_loop fadeout 2

    "Наконец мы приплыли."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_island_day onlayer master
    with dissolve

    play ambience ambience_lake_shore_day fadein 3

    window show
    "Совершенно обессиленный, я выбрался на берег и посмотрел на лодочную станцию."
    "Она казалась так далеко, что я ощутил себя первым человеком на Луне, который наблюдает восход Земли."
    show un normal pioneer onlayer master at cleft
    show sl normal pioneer onlayer master at cright
    with dissolve
    sl "Вот!"
    "Славя протянула мне корзинку."
    me "Да…"
    "Остров был небольшим – метров 100 в длину, не более."
    "Он скорее напоминал березовую рощу – ровные ряды деревьев покрывали всю его поверхность."
    "Под ногами расстилалось спокойное зеленое море, ветерок лишь изредка вызывал волны на поверхности."
    "Этот островок казался просто-таки райским местом."
    th "Неудивительно, что именно здесь растет самая вкусная земляника."
    sl "Нам бы надо разделиться, так быстрее все соберем."
    me "Да, наверное."
    show un surprise pioneer at cleft onlayer master with dspr
    un "Но корзинки-то только две."
    "Робко заметила Лена."
    show sl sad pioneer at cright onlayer master with dspr
    sl "Да, точно, это я недоглядела!"
    un "И как мы разделимся?"
    window hide

    menu:
        "Пойти с Леной":
            $ lp_un = lp_un + 2
            window show
            me "Давай я пойду с тобой."
            un "Давай…"
            show sl smile pioneer at cright onlayer master with dspr
            sl "Вот и славно!"
            hide sl onlayer master with dissolve
            "Славя взяла вторую корзинку и пошла в дальнюю часть острова."
            show un surprise pioneer onlayer master at cleft:
                linear 1.0 xalign 0.5
            me "Ну что?"
            un "Что?"
            me "Пойдем?"
            show un smile pioneer at center onlayer master with dspr
            un "Ага."
            "Лена улыбнулась."
            me "Только собирай внимательнее! Не пропускай ни одной ягодки!"

            stop ambience fadeout 2

            un "И ты тоже."

            play music music_list["she_is_kind"] fadein 3

            hide un onlayer master with dissolve
            "..."
            window hide

            with fade

            window show
            "Жатва началась."
            "Земляника здесь действительно была вкусная."
            "Я бы, наверное, съел ее всю, если бы вовремя не остановился."
            th "Ягоды размером с клубнику ярко-красного цвета – да, мы точно не зря сюда приплыли."
            "Я чувствовал себя грибником, заглядывая под каждый кустик и внимательно роясь в траве."
            "Лена шла совсем рядом, так как корзинка у нас была всего одна."
            show un surprise pioneer at center onlayer master with dissolve
            un "У тебя как-то лучше получается…"
            me "Да?{w} Я их не считаю, если честно."
            un "Нет, правда!"
            "Корзинка была уже наполовину заполнена."
            me "А ты, наверное, любишь природу?"
            show un smile2 pioneer at center onlayer master with dspr
            un "Да."
            window hide

            with flash

            window show
            "Яркий луч солнца, пробившийся сквозь кроны деревьев, ослепил меня на секунду."
            "Я опустился на землю и прислонился к дереву."
            me "Красиво все же здесь!"
            show un smile2 pioneer close at center  onlayer master with dissolve
            "Лена села рядом.{w} Близко настолько, что ее локоть касался моего."
            un "Да!"
            "Мы просто сидели.{w} Время, кажется, остановилось."
            "Ветерок нежно колыхал листья на деревьях, в траве прыгали какие-то букашки, а вдалеке на воде резвились солнечные зайчики."
            window hide

            scene cg d5_un_sleep onlayer master
            with dissolve

            window show
            "Я почувствовал, как Лена опустила голову мне на плечо."
            "Сначала это немного удивило меня, но потом, прислушавшись к ее размеренному дыханию, я решил, что так и надо."
            "Видимо, разморило, и она решила вздремнуть."
            "Несколько минут я просто сидел и ни о чем не думал."
            "Но потом в моей голове со сверхзвуковой скоростью начали скакать мысли."
            th "Лена.{w} Рядом.{w} Спит.{w} Тепло.{w} Нежность.{w} Чувства…"
            "Я посмотрел на нее."
            "На лице девушки было такое спокойное, умиротворенное выражение, что, казалось, она сейчас где-то не здесь, где-то в лучшем мире."
            "Не знаю, что бы случилось в следующую секунду, если бы я не услышал голос Слави."
            sl "Семен! Лена!"

            stop music fadeout 3

            "Я несколько раз резко тряхнул головой в разные стороны, чтобы прийти в себя.{w} Лена начала просыпаться."
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_island_day onlayer master
            with dissolve

            play ambience ambience_forest_day fadein 3

            show un normal pioneer close at center  onlayer master with dissolve
            window show
            "Она открыла глаза и отсутствующим взглядом посмотрела на меня."
            me "Что снилось?"
            un "А?"
            show un shy pioneer close at center onlayer master with dspr
            "Поняв, что она задремала у меня на плече, Лена покраснела."
            un "Извини…"
            me "Да ничего."
            "К нам подошла Славя, и Лена поспешила встать."
            show un shy pioneer onlayer master at cright
            show sl smile pioneer onlayer master at cleft
            with dissolve
            sl "И как улов?"
            "Я показал на корзинку."
            show sl normal pioneer at cleft onlayer master with dspr
            sl "Что-то негусто…"
            "Она показала нам свою.{w} Земляника оттуда так и вываливалась."
            sl "Впрочем, собрали более чем достаточно!{w} Пора возвращаться!"

            stop ambience fadeout 2

            "Я взял корзинку, и мы направились назад к лодке."
        "Пойти со Славей":

            $ lp_sl = lp_sl + 1
            window show
            "Мне не хотелось бродить здесь одному, и я надеялся, что Славя составит мне компанию, но сказать это вслух не решился."
            me "Одна корзинка у меня, одна – у вас; все очевидно."
            show sl smile pioneer at cright onlayer master with dspr
            sl "Нет, давай я с тобой пойду!"
            "Славя улыбнулась."
            me "Давай…"
            "Я несколько удивился, но в то же время обрадовался."
            hide un onlayer master with dissolve

            stop ambience fadeout 2

            "Лена, кажется, совсем не обиделась из-за того, что подруга не пойдет с ней."
            hide sl onlayer master with dissolve
            "..."
            window hide

            with fade

            play music music_list["timid_girl"] fadein 3

            window show
            "Жатва началась."
            "Земляника здесь действительно была вкусная."
            "Я бы, наверное, съел ее всю, если бы вовремя не остановился."
            th "Ягоды размером с клубнику ярко-красного цвета – да, мы точно не зря сюда приплыли."
            "Я чувствовал себя грибником, заглядывая под каждый кустик и внимательно роясь в траве."
            "Славя шла совсем рядом, так как корзинка у нас была всего одна."
            show sl normal pioneer at center onlayer master with dissolve
            sl "Внимательнее!"
            "Она показала на пропущенный мной кустик."
            me "А, да…{w} Извини."
            show sl smile pioneer at center onlayer master with dspr
            sl "Ничего."
            me "Тебе, наверное, здесь нравится?{w} Ты ведь любишь природу."
            show sl smile2 pioneer at center onlayer master with dspr
            sl "Конечно!"
            "Славя улыбнулась."
            sl "Напоминает о доме – у нас там такие же красивые березы."
            "Она мечтательно посмотрела куда-то вдаль."
            me "Слушай, давно хотел спросить – а чем ты вообще увлекаешься?"
            me "А то ты целыми днями занята – кажется, времени на отдых совсем не остается."
            show sl normal pioneer at center onlayer master with dspr
            sl "Ну…"
            "Она задумалась."
            show sl smile pioneer at center onlayer master with dspr
            sl "Не знаю даже.{w} Для меня отдых – это смена вида деятельности."
            me "Нет, это понятно, но все же?"
            sl "Я вышивать люблю и вязать!{w} Вот…"
            "Она достала из кармана платочек.{w} На нем были вышиты цветы – красные, желтые, зеленые…"
            "Они переплетались причудливым образом, образуя сложные геометрические фигуры."
            "Такой типично русский рукодельный платочек."
            "При виде его я сразу же представил Славю в старинном сарафане, сидящую на лавочке возле покосившейся избы, окруженную толпой резвящейся детворы."
            me "Очень мило."
            show sl smile2 pioneer at center onlayer master with dspr
            sl "Спасибо!{w} Давай я его тебе подарю!"
            "Я несколько смутился."
            me "Да не стоит…"
            sl "Нет, бери!"
            "Я еще раз посмотрел на платочек и спрятал его в карман."
            me "Спасибо…"
            "..."
            window hide

            with fade

            window show
            "Земляники здесь было столько, что через каких-то полчаса корзинка уже наполнилась до краев."
            me "Ну, видимо, все…"

            stop music fadeout 3

            show sl normal pioneer at center onlayer master with dspr
            sl "Да.{w} Набрали немало, этого с запасом хватит."
            window hide

            with fade

            play ambience ambience_lake_shore_day fadein 3

            window show
            "Когда мы вернулись к лодке, Лена еще не подошла."
            sl "Ей одной больше времени надо, чтобы полную корзинку набрать."
            me "Да, наверное…"
            "Я посмотрел на реку."
            "По воде весело прыгали солнечные зайчики, и это было единственным, что напоминало о том, что передо мной все же водная гладь, а не зеркало – настолько река казалась спокойной."
            sl "О чем думаешь?"
            me "Ни о чем…{w} А ты?"
            show sl sad pioneer at center onlayer master with dspr
            sl "А я…{w} Что будет, когда закончатся каникулы? Придется вернуться домой, покинуть этот лагерь…"
            show sl tender pioneer at center onlayer master with dspr
            sl "Увижусь ли я когда-нибудь со всеми, с кем здесь познакомилась?{w} Увижусь ли я когда-нибудь с тобой?.."
            "Она посмотрела на меня, и в ее взгляде было столько тоски, что я не нашелся, что ответить."
            show sl normal pioneer at center onlayer master with dspr
            show un normal pioneer at right onlayer master with dissolve
            "На помощь мне пришла Лена, которая словно из ниоткуда появилась перед нами."
            un "Ой, а вы уже тут…{w} Вот."
            "Она показала полную корзинку земляники."
            show sl smile pioneer at center onlayer master with dspr
            sl "Отлично!{w} Теперь можно отправляться назад."
            "А у меня перед глазами все еще стояло лицо Слави, в ушах звенели ее слова."
            "Грусть, тоска – это те эмоции, которые так были нехарактерны для нее."
            th "Может быть, она все время их скрывает за маской жизнерадостности?"
            "Ответа на этот вопрос я не знал да и не мог знать."

            stop ambience fadeout 2

            th "Возможно, позже…"

    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_boathouse_day onlayer master
    with dissolve

    play ambience ambience_boat_station_day fadein 3

    window show
    "Обратно мы доплыли быстрее, потому что я постарался сконцентрироваться на гребле и не отвлекаться ни на что другое."
    "Это было необходимо, чтобы вернуться на пристань живым, так как первый заплыв не прошел бесследно, и в этот раз руки начали болеть уже после нескольких взмахов веслами."
    "Пришвартовав лодку, я обессилено рухнул на землю."
    "Славя и Лена склонились надо мной."
    show sl serious pioneer onlayer master at cright
    show un normal pioneer onlayer master at cleft
    with dissolve
    sl "Если тебе было так тяжело, то сказал бы!"
    un "Да…"
    me "Да нет, ничего…{w} Сейчас полежу, и все пройдет…"
    show sl smile pioneer at cright onlayer master with dspr
    sl "Ладно, тогда отнеси корзинки, пожалуйста, Ольге Дмитриевне, а то у нас еще дела есть."
    me "Да, конечно."
    "Сейчас я был готов согласиться на что угодно, лишь бы не вставать."
    hide sl onlayer master
    hide un onlayer master
    with dissolve
    "Славя поставила корзинки, полные земляники, рядом со мной, и они вместе с Леной, весело о чем-то болтая, направились в сторону площади."
    me "Самое тяжелое сделано…"
    "Так я думал, пока не встал и не взял корзинки…"

    stop ambience fadeout 2

    "После спортивной гребли они казались мешками с цементом, хотя вряд ли весили больше пары килограмм каждая."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Из-за этого путь до домика вожатой занял у меня куда больше обычного – приходилось останавливаться через каждые пятьдесят метров, чтобы отдохнуть."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    "Когда я все же дошел, то поставил корзинки на землю, а сам обессилено рухнул в гамак."
    me "Ольга Дмитриевна!{w} Ольга Дмитриевна, я вам гостинцы принес!"
    "Ответа не последовало."
    "Я с трудом поднялся и зашел в домик."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    window show
    "Внутри никого не было."
    me "Не хотите – как хотите…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    window show
    "Я улегся в гамак и задремал."
    window hide

    scene bg black onlayer master
    with fade

    play music music_list["sparkles"] fadein 3

    scene cg d5_strawberry_race onlayer master
    with dissolve

    window show
    "Мне приснился странный сон про земляничные гонки."
    "Я плыл на лодке, греб изо всех сил, чтобы спастись от огромных ягод, которые гнались за мной."
    "Руки уже отказывали, глаза заливал пот так, что ничего не было видно, кровь стучала в висках, но земляники были все ближе."
    "Я обернулся и увидел, как они скалят на меня свои хищные пасти."
    th "Но постойте…{w} Пасти у земляники?!"
    mt "… Семен! Семен!"
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    show mt normal panama pioneer onlayer master at center
    with fade

    play ambience ambience_camp_center_day fadein 2

    window show
    "Я проснулся."

    play music music_list["sweet_darkness"] fadein 3

    "Передо мной стояла Ольга Дмитриевна и трясла меня за плечи."
    show mt smile panama pioneer at center onlayer master with dissolve
    mt "Я смотрю, урожай вы собрали неплохой, не так ли?"
    window hide

    menu:
        "Да, я старался!":
            pass
        "Это все благодаря помощи девочек!":
            $ day5_sl_helped = 1
            $ lp_sl = lp_sl + 1
            pass

    window show
    mt "Понятно. Но это еще не все!"
    th "Действительно, а я-то уже размечтался, хотел спокойно полежать…"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Ты же знаешь, зачем эта земляника?"
    me "Не имею ни малейшего понятия…"
    "Признался я честно."
    mt "Будем из нее делать торт!"
    me "Ясно…"
    th "Что же, весьма логично."
    show mt smile panama pioneer at center onlayer master with dspr
    mt "В честь чудесного спасения Шурика!{w} Ведь это все благодаря тебе!"
    "Было понятно, что земляникой дело не ограничится."
    th "И почему, скажите на милость, если я такой герой, то праздник в честь себя должен организовывать сам?.."
    me "Ну, наверное…"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Так вот…{w} У меня для тебя есть ответственное задание!"
    mt "Для торта не хватает еще дрожжей, муки и сахара.{w} Все это надо принести в столовую до ужина!"
    me "А те, кто торт будут печь, не могут как-то сами?.."
    "Жалостливо поинтересовался я."
    show mt surprise panama pioneer at center onlayer master with dspr
    mt "Конечно нет!{w} Они все заняты!{w} А без дела у нас в лагере слоняешься только ты!"
    "Хоть в ее словах и была изрядная доля правды, сейчас мне от этого никак не становилось легче."
    "Более того, они послужили контрольным выстрелом!"
    show mt normal panama pioneer at center onlayer master with dspr
    mt "Итак, запоминай!{w} Дрожжи возьмешь в медпункте. Муку – в библиотеке. Сахар – в здании кружков."
    me "Подождите, а..."
    show mt grin panama pioneer at center onlayer master with dspr
    mt "Мне некогда, я спешу!{w} Удачи тебе!"
    hide mt onlayer master with dissolve
    "Она хитро улыбнулась и ушла."
    th "Конечно, в этом лагере много странного, но…{w} Дрожжи в медпункте? Ок, это я понять могу. Но!{w} Мука в библиотеке?"
    th "Сахар…{w} Нет, это уже выходит за рамки разумного!"
    "Я смачно плюнул себе под ноги."
    me "Не хочу, не желаю в это верить! Скажите же, скажите, что вы меня разыгрываете!"
    "Если бы сейчас передо мной появилась толпа зеленых жирных троллей, каждый из которых считал бы себя обязанным вдоволь посмеяться надо мной, я бы и не удивился."
    th "Может быть, ну его, этот торт?.."
    "Некоторое время я обдумывал, как поступить."
    th "Нет, если такая масштабная задумка Ольги Дмитриевны сорвется, то мне влетит так, что мало не покажется."
    th "И усложнится все – и поиски ответов, которыми я уже давно не занимаюсь, и просто моя обычная жизнь в лагере."

    stop music fadeout 3

    th "Похоже, придется все же…"
    window hide

    $ disable_all_zones()

    $ set_zone("clubs","day5_clubs_2")
    $ set_zone("library","day5_library_2")
    $ set_zone("medic_house","day5_aidpost_2")

    jump day5_map

label day5_map:
    if day5_map_necessary_done == 3:
        jump day5_main3
    $ show_map()

label day5_aidpost_2:

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    th "Мне начинает казаться, что последнее время я слишком уж часто бываю в медпункте."
    th "Что же, ничего не поделаешь – так складываются обстоятельства."

    play sound sfx_knock_door2

    "Я вздохнул и постучался."
    cs "Войдите!"
    "Несколько нараспев ответила медсестра."

    stop ambience fadeout 2

    play sound sfx_open_door_2

    "Я открыл дверь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day onlayer master
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    show cs normal at center onlayer master with dissolve
    window show
    me "Здравствуйте!{w} Меня Ольга Дмитриевна прислала за…"
    "Я несколько замялся."
    me "Дрожжами…"
    show cs smile at center onlayer master with dspr
    cs "А, да, конечно."
    "Она широко улыбнулась."
    cs "Только у меня их нет…{w} пионер."
    me "Как так?{w} Она сказала, что…"
    show cs normal at center onlayer master with dspr
    cs "Ну, раньше были, да кончились."
    "Я даже не стал спрашивать, зачем они вообще понадобились медсестре."
    show cs smile at center onlayer master with dspr
    cs "Впрочем, ты не расстраивайся.{w} Могу предложить тебе аспирин, например."
    th "Может быть, он мне и не помешал бы…"
    me "Где же мне тогда их достать…"
    "Я вздохнул."
    cs "А вот!"
    "Она открыла ящик и достала какую-то бутылку."

    play music music_list["that_s_our_madhouse"] fadein 2

    "Я присмотрелся.{w} Это было пиво «Останкинское»."
    me "…"
    show cs normal at center onlayer master with dspr
    cs "А что такого?{w} Пиво тоже продукт брожения."
    "Она пристально посмотрела на меня."
    show cs smile at center onlayer master with dspr
    cs "Никто и не заметит!"
    "Да, в ее словах была логика, но все происходящее казалось мне настолько гротескным, что я не сразу нашелся, что ответить."
    me "А вы уверены?"
    cs "Абсолютно!"
    me "Ну, ладно…"
    "Я взял бутылку и попытался запихнуть ее в карман шорт, но мне это не удалось."
    me "Спасибо…"

    stop ambience fadeout 2

    "Неуверенно промямлил я и вышел из медпункта."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    th "Нет, пиво наверняка может заменить дрожжи."
    th "Даже моих скудных знаний по химии и биологии хватит, чтобы увериться в этом.{w} Но…"
    "Вообще, ходить с бутылкой в руках мне сразу показалось не лучшей идеей, поэтому я решил отнести ее в домик Ольги Дмитриевны и спрятать там."
    "Но надо было и до туда как-то дойти, чтобы пиво не заметили."
    "Я засунул бутылку под рубашку."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    show sl normal pioneer at center onlayer master with dissolve
    window show
    "Все бы и хорошо, но на площади меня окликнула Славя."
    "Точнее, она вынырнула у меня из-за спины так неожиданно, что я даже вздрогнул."
    sl "Как продвигается?"
    me "Что?"
    sl "Поиски ингредиентов."
    me "А ты уже знаешь…"
    show sl smile pioneer at center onlayer master with dspr
    sl "Да!"
    "Славя улыбнулась."
    me "Нормально…"
    "Стараясь не показывать свое волнение, ответил я."
    show sl normal pioneer at center onlayer master with dspr
    sl "А что у тебя там?"
    "Она показала на выпячивающуюся из-под рубашки бутылку."
    me "А это…"
    th "Кажется, попал…"
    me "Да так, ничего особенного…"
    "Я глупо захихикал."
    me "Мне пора…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    window show
    "Я поспешно ретировался, оставив Славю в недоумении."
    th "Хорошо, что она не из тех людей, которые будут задавать лишние вопросы."
    "Но есть в этом лагере те, кого хлебом не корми, дай засунуть нос в чужие дела…"
    "Проходя мимо палаток пионеров, я столкнулся с Ульяной."
    show us surp1 pioneer at center onlayer master with dissolve
    us "Что прячешь?"
    "Она хитро посмотрела на меня."
    "Я решил, что отпираться нет смысла, и поэтому вызывающе ответил:"
    me "А не твое дело! Шифровку в штаб несу."
    show us grin pioneer at center onlayer master with dspr
    us "Большая…{w} шифровка…"
    "Бутылку я держал на уровне пояса, поэтому несколько смутился."
    us "Может, тебе помочь?"
    me "Сам справлюсь!"
    hide us onlayer master with dissolve
    "Я уверенно обошел Ульяну и продолжил путь."
    "К моему удивлению, она ничего не сказала и не стала преследовать меня."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day onlayer master
    with dissolve

    window show
    "Ольги Дмитриевны в домике не было, так что мне удалось спокойно спрятать бутылку к себе под кровать."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Выйдя на улицу, я облегченно вздохнул."
    "Действительно, никогда бы не подумал, что буду так переживать из-за одной бутылки пива!{w} Словно вернулся в старшие классы школы."
    th "Хорошо, что сейчас она в безопасности…"
    th "А если даже и найдут, скажу, что не мое – опыт в придумывании оправданий у меня был хороший."
    window hide

    $ day5_map_necessary_done +=1
    $ disable_current_zone()
    jump day5_map

label day5_clubs_2:

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    window show
    "Казалось, что за сегодня мне пришлось пережить столько же, сколько за все предыдущие дни."
    "Так что, подходя к зданию кружков, я и думать забыл о том, что искать здесь сахар, вообще говоря, несколько странновато."

    stop ambience fadeout 2

    "Некоторое время постояв на ступеньках, я вздохнул и открыл дверь."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    scene cg d5_clubs_robot onlayer master
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри были Шурик и Электроник.{w} Они что-то увлеченно мастерили."
    "Увлеченно настолько, что даже не заметили меня."
    "Я присмотрелся."
    "Это был какой-то робот…{w} Хотя бы его корпус."
    "Причем робот женского пола да еще и с ушами."
    "Мне не хотелось строить теорий для чего светилам лагерной кибернетики могло понадобиться это устройство."
    "Хоть конструкция и выглядела относительно технологично, у меня были большие сомнения в том, что этот робот сможет в будущем завоевать мир или хотя бы вообще будет способен на какие-либо действия."
    "Однако для них, кажется, более важен был сам процесс, нежели конечный результат."
    "И в этом я их мог понять, хотя мне и не хотелось признаваться в этом самому себе."
    "С другой стороны, они не боялись провала, критики, насмешек...{w} Шли и шли себе к намеченной цели, не обращая внимания на то, что кому-то она может показаться недостижимой или вовсе абсурдной."
    th "Как будто я правда их сравниваю с какими-то светилами науки..."
    me "Привет, ребята…"
    "Неуверенно поздоровался я."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day onlayer master
    with dissolve

    show sh smile pioneer onlayer master at cleft
    show el smile pioneer onlayer master at cright
    with dissolve
    window show
    sh "О! Семен! Заходи, всегда рады!"
    th "Да я и так уже зашел, вообще-то…"
    show sh normal pioneer at cleft onlayer master with dspr
    sh "Ты это…{w} Извини за вчерашнее!{w} Хотя я почти ничего не помню, но мало ли что…{w} В общем…"
    me "Ничего-ничего!"
    show el grin pioneer at cright onlayer master with dspr
    el "А что тебя привело в нашу скромную обитель?"
    "Электроник хитро посмотрел на меня."
    "Порой мне казалось, что, когда он делает такое выражение лица, то полностью уверен, что знает про собеседника нечто, чем может козырнуть в подходящий момент."
    me "Сахар.{w} Мне нужен сахар."
    "Перед глазами сразу всплыла картинка из старой компьютерной игры, где какой-то юнит, строитель или что-то подобное, во все свои пять пикселей кричал “More! We need more!”"
    show el normal pioneer at cright onlayer master with dspr
    el "Это есть у нас."
    "Спокойно ответил Электроник."
    sh "А зачем он тебе?"
    "Я не хотел объяснять Шурику, что в его честь хотят испечь торт.{w} Не хотел портить сюрприз."
    me "Не знаю…{w} Ольга Дмитриевна попросила принести…"
    el "Ладно, сейчас."
    hide el onlayer master with dissolve
    "Электроник скрылся за дверью в соседнюю комнату."
    me "А почему сахар именно у вас лежит, а не в столовой?"
    show sh serious pioneer at cleft onlayer master with dspr
    sh "Когда последний раз машина с продуктами приезжала, то его выгружали последним."
    sh "А так как наше здание ближе всего к проходной, то, чтобы далеко не носить…"
    th "Логично."
    show el normal pioneer at cright onlayer master with dissolve
    "Открылась дверь, и появился Электроник, тащивший за собой огромный мешок."
    "Я, конечно, не знал, какого размера торт планирует испечь Ольга Дмитриевна, но здесь сахара явно многовато."
    me "Спасибо, конечно, но мне столько не надо…"
    show el surprise pioneer at cright onlayer master with dspr
    el "А куда же нам его переложить?"
    "Электроник удивленно посмотрел на меня."
    show el smile pioneer at cright onlayer master with dspr
    el "Нам некуда.{w} Просил сахар – забирай."
    th "Похоже, та его улыбка все же не была беспричинной."
    me "Может быть, тогда поможете мне дотащить?{w} Тут недалеко же…"
    show el normal pioneer at cright onlayer master with dspr
    el "А мы заняты."
    "Он показал рукой на робота."
    "Я пристально посмотрел на Шурика.{w} В конце концов, он мне был обязан."
    show sh upset pioneer at cleft onlayer master with dspr
    "Тот замялся, но все же стыдливо отвел глаза."
    "Я вздохнул, взял мешок и направился к выходу."
    me "Спасибо, что же…"

    stop ambience fadeout 2

    "Надрываясь, сказал я на прощание."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Однако далеко я уйти не смог."
    "Уже через каких-то двадцать метров мне пришлось поставить мешок на землю, чтобы передохнуть."
    "Не знаю, сколько он весил, но казалось, что не менее двадцати килограмм точно."
    "С одной стороны, до столовой было всего каких-то пару сотен метров."
    "С другой же – даже такое расстояние с подобным грузом на плечах (а иногда в руках, ногах, под мышкой или даже на голове) казалось мне тогда непосильным."
    "Я уже твердо решил передвигаться небольшими рывками с длительными остановками (к ночи как раз добрался бы), как услышал голос позади себя:"
    un "Может, тебе помочь?"

    play music music_list["she_is_kind"] fadein 3

    show un normal pioneer at center onlayer master with dissolve
    "Я обернулся.{w} Передо мной стояла Лена."
    me "Не думаю, что у тебя это выйдет…"
    "Именно в такие минуты я мучительно тяжело ощущал, что мне катастрофически не хватает физической формы…"
    un "Я могу за тележкой сходить…"
    th "Тележка…{w} Почему я сам об этом не подумал?!"
    me "Да, это было бы здорово!"
    show un smile3 pioneer at center onlayer master with dspr
    un "Подожди тут, я быстро!"
    hide un onlayer master with dissolve
    "Она улыбнулась и убежала в сторону площади."
    th "И что бы я без нее делал…"
    th "Хорошо, что Лена все же не всегда такая застенчивая, а иногда и вполне может проявлять инициативу."
    "Я задумался."
    "Сейчас она выглядела довольно странно.{w} Ни тени робости на лице, наоборот – улыбка, уверенность…"
    "Предложение помочь само по себе не было чем-то из ряда вон выходящим, но от Лены…"
    window hide

    with fade

    show un smile2 pioneer at center onlayer master with dissolve
    window show
    "Через пару минут она вернулась с небольшой тележкой."

    play sound sfx_put_sugar_cart

    "Я поставил на нее мешок."
    me "Спасибо…"
    show un shy pioneer at center onlayer master with dspr
    un "Не за что…"
    "Она покраснела и уставилась себе под ноги."
    th "Ну вот опять…"
    un "Тогда я пойду…"
    hide un onlayer master with dissolve
    me "Да, удачи!{w} И еще раз спасибо!"
    "Крикнул я ей вслед."
    "Иногда мне казалось, что в Лене живут два разных человека."
    "Но второй – уверенный в себе, веселый, местами даже какой-то дерзкий – появляется только передо мной."

    stop music fadeout 3

    stop ambience fadeout 2

    th "Или мне опять все это кажется?.."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day onlayer master
    with dissolve

    window show
    "Я решил, что лучше принесу все ингредиенты одновременно, поэтому направился с тележкой в сторону домика Ольги Дмитриевны."
    window hide

    $ day5_map_necessary_done +=1
    $ disable_current_zone()
    jump day5_map

label day5_library_2:

    $ persistent.sprite_time = "day"
    scene bg ext_library_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Если все остальные пункты в списке продуктов для торта хоть как-то укладывались у меня в голове, то мука в библиотеке – нет."
    "Я долго думал, кому и зачем она могла там понадобиться, но ни одного сколько-нибудь толкового объяснения на ум не приходило."
    "Памятуя о суровом характере Жени, я решил сначала постучаться."
    window hide

    stop ambience fadeout 2

    play sound sfx_knock_door7_polite

    $ renpy.pause(2)

    window show
    mz "Открыто."
    window hide

    play sound sfx_open_door_1

    $ persistent.sprite_time = "day"
    scene bg int_library_day onlayer master
    with dissolve

    play ambience ambience_library_day fadein 3

    show mz normal glasses pioneer at center onlayer master with dissolve
    window show
    "Я вошел."
    "Женя внимательно посмотрела на меня из-под очков."
    mz "Чего тебе?"
    me "Эээ…{w} Ты не подумай ничего, мне бы…"
    "Я не хотел выглядеть идиотом, поэтому решил предельно подробно объяснить сложившуюся ситуацию."
    me "Мне мука нужна. Ольга Дмитриевна сказала, что она здесь есть. Я понимаю, что это странно – держать муку в библиотеке, но…"
    me "Меня к тебе послали. А нужна она для торта. Отметить спасение Шурика."

    play music music_list["my_daily_life"] fadein 3

    show mz bukal glasses pioneer at center onlayer master with dspr
    mz "Да, есть у меня мука, что тут такого."
    "Удивленно ответила Женя."
    "В ту секунду мне показалось, что я получил тяжелой гирей по голове и перестал что-либо понимать."
    th "Мука в библиотеке…{w} Действительно, что здесь такого…"
    th "Мы же в Зазеркалье, я Алиса, сейчас съем волшебный гриб и отправлюсь домой…"
    show mz normal glasses pioneer at center onlayer master with dspr
    mz "Эй!"
    me "А? Да!"
    "Я замечтался."
    mz "Подожди здесь, сейчас принесу."
    hide mz onlayer master with dissolve
    "Она скрылась за книжными шкафами, а я скрестил руки на груди и принялся ждать."

    play sound sfx_cellar_open    

    "Через пару секунд послышался звук скрипящих петель."
    me "Может, тебе помочь?"
    "Крикнул я."
    mz "Сама справлюсь!"
    "Буркнула Женя в ответ."
    mz "Она в погребе, так что придется немного подождать."
    me "Хорошо-хорошо…"
    "Вздохнул я."
    window hide

    with fade

    window show
    "Прошло уже несколько минут, а Женя так и не возвращалась."
    "Я уже начал волноваться, как вдруг дверь сзади меня открылась, и вошла Алиса."

    play sound sfx_open_door_2

    show dv normal pioneer2 at center onlayer master with dissolve
    "Кажется, она совсем не ожидала обнаружить меня здесь."
    show dv surprise pioneer2 at center onlayer master with dspr
    dv "А ты что тут делаешь?"
    me "А что, нельзя?"
    "Грубо ответил я."
    "Алиса немного опешила."
    show dv angry pioneer2 at center onlayer master with dspr
    dv "Да мне какое дело…"
    "Она фыркнула и направилась к столу Жени."
    me "А ты сама зачем пришла?"
    "Алиса пристально посмотрела на меня оценивающим взглядом, затем открыла рот, собираясь что-то сказать, но вдруг спохватилась и отвернулась, пряча что-то за спиной."
    me "Книгу отдать?"
    "Сказал я первое, что пришло в голову."
    show dv sad pioneer2 at center onlayer master with dspr
    dv "Не твое дело…"
    "Не очень уверенно ответила она."
    me "А что за книга?"
    "Алиса промолчала."
    me "Ну, дай посмотреть!{w} Интересно ведь, что читает мисс «Не-влезай-убьет!»"
    show dv guilty pioneer2 at center onlayer master with dspr
    dv "Не твое дело…"
    "В ее голосе было еще меньше уверенности."
    me "Ладно-ладно, я не настаиваю…"
    "Хотя на самом деле мне было очень интересно, что же такое читает Алиса."
    "Более того, я вообще удивился, увидев у нее в руках книгу."
    "Телевизор, кино, компьютер, если бы он здесь был, – все это казалось более подходящими развлечениями для девочки вроде нее."
    "А тут – книга…"
    window hide

    menu:
        "Попытаться выхватить книгу у Алисы":
            window show
            "Все же любопытство взяло вверх – я воспользовался тем, что Алиса не смотрит на меня и, тихо подкравшись, аккуратно выхватил книгу."
            show dv shocked pioneer2 at center onlayer master with dspr
            dv "Ай!"
            "Взвизгнула она."
            show dv rage pioneer2 at center onlayer master with dspr
            "В следующую секунду ее лицо приняло такое выражение, что я уже начал сомневаться в правильности своего решения."
            th "Раз уж скоро умирать, то хотя бы посмотрю ради чего."
            "В руках у меня была «Унесенные ветром»."
            "Такая же книга, которую тогда вечером на скамеечке читала Лена."
            "От удивления я даже забыл о неминуемой смерти."
            me "Интересно?"
            show dv shy pioneer2 at center onlayer master with dspr
            dv "Да…"
            "Покраснев, нехотя ответила Алиса."
            me "Ладно, тогда…"
            "Я протянул ей книгу."
            "Алиса бросила ее на стол Жени и быстро, не смотря на меня, вышла из библиотеки."
            hide dv onlayer master with dissolve
            th "Значит, и ей ничто человеческое не чуждо.{w} В конце концов, она тоже девочка."
            "Быстро проанализировав произошедшее, я заключил, что ничего такого странного и не случилось."
        "Ничего не делать":

            $ lp_dv = lp_dv + 1
            window show
            "Я все же переборол свое любопытство."
            "В конце концов, зная Алису, все могло закончиться очень плачевно, а мне еще продукты для торта надо было собрать."
            dv "Ладно, я потом зайду…"
            hide dv onlayer master with dissolve
            "Алиса, не смотря на меня, быстро вышла из библиотеки."
            "Я задумался."
            th "Что могло быть в этой книге такого, чего она так стеснялась?"
            th "Во-первых, смущенная Алиса – это уже само по себе из ряда вон…{w} А тут еще и смущенная книгой."
            th "Хотя чего теперь думать-то – узнать никак не получится…"

    "Наконец библиотека огласилась громогласным стоном Жени."
    mz "Забирай!"
    show mz bukal glasses pioneer at center onlayer master with dissolve
    "Я обошел шкафы с книгами и увидел вспотевшую библиотекаршу, сидевшую рядом с люком в погреб, а рядом с ней – небольшой мешок."
    th "Может быть, у них тут что-то типа склада?.."
    me "Спасибо!"

    stop music fadeout 3

    "Я взял мешок и вышел из библиотеки."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_library_day onlayer master
    with dissolve

    window show
    "Слава Богу, что он оказался не очень тяжелым, и до домика Ольги Дмитриевны я его донес без особых усилий."
    window hide

    $ day5_map_necessary_done +=1
    $ disable_current_zone()
    jump day5_map

label day5_main3:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day onlayer master
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Наконец все необходимое было собрано."
    "Я вытащил тележку с сахаром на улицу и положил на нее мешочек с мукой, а сверху приспособил кое-как две корзинки с ягодами."
    "Пиво же я предусмотрительно засунул под рубашку от греха подальше."
    "День близился к вечеру, а это значило, что пора спешить – ведь торт еще надо испечь."
    "Конечно, я бы куда с большим удовольствием сейчас просто лег, закрыл глаза и заснул, но нельзя было подводить Ольгу Дмитриевну."
    "Более того, после всех сегодняшних приключений я уже чувствовал и собственную ответственность за успех всего этого мероприятия."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    window show
    "Выйдя на площадь, я ненадолго остановился, чтобы отдышаться."
    "Нет, тележка не была тяжелой, ехала она легко, и не приходилось прилагать особых усилий, но сейчас любая физическая активность казалась мне непосильной."
    window hide
    show blink onlayer master

    $ renpy.pause(1)

    window show
    "Я присел на лавочку, опустил голову на руки и закрыл глаза."

    scene black onlayer master

    dreamgirl "А что это?"
    "Послышался рядом чей-то голос."
    "Мне было совсем не интересно, кто это – наверняка просто какая-нибудь пионерка, заинтересовавшаяся необычным коллегой по несчастью."
    me "Ты о чем?"
    "Устало спросил я."
    "Она ничего не ответила."
    me "Ингредиенты для торта...{w} Ты любишь торты?"
    dreamgirl "Не знаю…"
    me "Что, никогда не пробовала?"
    dreamgirl "Не знаю…"
    "Девочка, очевидно, не понимала, о чем я говорю, но мне тогда это совсем не показалось странным."
    "Разговор меня совершенно не интересовал, так как я устал настолько, что не имел никакого желания как бы то ни было классифицировать внешние раздражители, разделять их на обычные и необычные."
    me "Понятно…"
    "Вздохнул я.."
    me "Ты приходи, попробуешь."
    dreamgirl "Правда?"
    me "Правда…"
    dreamgirl "А из чего их делают?"
    me "Кого?"
    "Рассеянно спросил я."
    dreamgirl "Эти твои…{w} Торты!"
    me "Ну…{w} Мука, сахар, начинки всякие…"
    th "Какой-то странный вопрос, неужели она не знает, из чего состоит торт?"
    dreamgirl "Это все у тебя там?"
    me "Да, частично."
    dreamgirl "И сахар?"
    me "И сахар…"
    dreamgirl "А можешь мне немного отсыпать?"
    me "Зачем?"
    "Вся эта ситуация начала казаться мне несколько странной."
    window hide

    play sound sfx_wind_gust

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    show unblink onlayer master
    with dissolve

    $ renpy.pause(1)

    window show
    "Внезапно налетел ветер, я инстинктивно схватился за тележку и открыл глаза."
    "Однако передо мной никого не было."
    th "Неужели мне все это почудилось?"
    "Я внимательно осмотрел тележку и заметил, что мешок с сахаром развязался, и некоторое его количество высыпалось на землю."
    th "Может быть, она ветра испугалась и убежала?.."
    "Поправив поклажу, я встал со скамейки и продолжил свой нелегкий земляничный путь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    window show
    "Возле столовой не было ни души.{w} Ничего удивительного, ведь до ужина оставался еще час."
    "Я подкатил тележку к заднему входу и сдал продукты с рук на руки местной поварихе."
    "Наверное, она уже была в курсе, что с ними делать, поэтому и посмотрела на меня так недобро – не уверен, сколько по времени занимает приготовление торта, но, видимо, ей придется поспешить."
    "Что-либо делать до ужина в мои планы не входило."
    "Проще говоря, я слишком устал, поэтому просто сел на ступеньки и принялся ждать."
    show blink onlayer master
    window hide

    $ renpy.pause(1)

    window show
    "Глаза закрывались сами собой – наверное, за весь день меня слишком сильно разморило – поэтому я и не заметил, как кто-то подошел и легонько стукнул меня по плечу."
    show unblink onlayer master
    hide blink onlayer master
    window hide

    $ renpy.pause(1)

    play music music_list["so_good_to_be_careless"] fadein 3

    show mi smile pioneer at center onlayer master with dissolve
    window show
    mi "Привет!"
    "Передо мной стояла Мику."
    me "И тебе…"
    "Даже без зеркала я мог представить выражение крайнего скептицизма и раздражения у себя на лице."
    show mi normal pioneer at center onlayer master with dspr
    mi "Извини, я помешала, наверное…"
    me "Да нет, я просто сидел."
    show mi smile pioneer at center onlayer master with dspr
    mi "А, ну тогда ладно!"
    "Мику расплылась в улыбке."
    mi "Я просто шла на ужин, думала, что уже пора, а оказалось, что еще рано, но я все же решила проверить – может, не я ошиблась, а часы!"
    show mi upset pioneer at center onlayer master with dspr
    mi "Ну, то есть часы не могут ошибаться, просто я их не так поняла…"
    "Кажется, она окончательно запуталась и замолчала."
    me "Еще полчаса примерно до ужина."
    show mi smile pioneer at center onlayer master with dspr
    mi "Отлично, тогда я с тобой тут посижу подожду, не возражаешь?"
    "Откровенно говоря, я возражал."

    stop music fadeout 3

    me "Знаешь, у меня еще дела кое-какие…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day onlayer master
    with dissolve

    window show
    "Я поспешно встал и, не прощаясь, удалился, как обычно игнорируя Мику, что-то кричащую вслед."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day onlayer master
    with dissolve

    play music music_list["silhouette_in_sunset"] fadein 3

    window show
    "Через минуту я вышел на площадь и сел на лавочку с твердым намерением хотя бы здесь дождаться ужина в тишине и спокойствии."
    "Я поймал себя на мысли, что впервые за все время пребывания здесь начал выходить из себя."
    "Не просто злиться на какие-то незначительные неудобства, а по-настоящему беситься."
    "Меня абсолютно перестало волновать, где я и почему я здесь."
    "Не волновало меня и то, как выбраться отсюда."
    "Сейчас я больше негодовал из-за того, что именно мне постоянно приходится выполнять всякие глупые поручения вожатой, именно я вечно попадаю во всевозможные идиотские ситуации, а иногда и вообще выступаю шутом."
    th "Если это проделки инопланетян или задумка вселенского разума, то им неплохо бы показаться психиатру!"
    "Я скрипнул зубами и сжал кулаки."
    th "И самое обидное в том, что все происходит как-то само собой!"
    th "Я бы и рад не таскать пудовые мешки с сахаром, но выбора-то никакого нет!"
    th "Точнее, альтернатива приведет к куда худшим последствиям, чем растянутые мышцы и ущемленное самолюбие…"
    us "На кого злишься?"
    show us surp1 pioneer at center onlayer master with dissolve
    "Я поднял взгляд и увидел Ульянку, стоящую передо мной и ехидно улыбающуюся."
    me "Ни на кого…"
    "Рассеянно ответил я."
    "Однако кулаки меня выдавали."
    me "Так, просто…"
    show us grin pioneer at center onlayer master with dspr
    us "Ладно-ладно, дело твое…{w} Ты лучше скажи мне, зачем весь день по лагерю бегал со всякими мешками?"
    me "Дела были…"
    "Нехотя ответил я."
    show us laugh pioneer at center onlayer master with dspr
    us "Судя по всему, это продукты…"
    me "Может, и продукты…"

    play sound sfx_dinner_jingle_speaker

    "Ульяна собиралась что-то сказать, но в это время заиграла музыка, призывающая пионеров на ужин."

    stop music fadeout 3

    "Я с облегчением вздохнул и быстро направился в сторону столовой, оставив Ульяну позади."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day onlayer master
    with dissolve

    show mt smile pioneer at center onlayer master with dissolve
    window show
    mt "Семен, спасибо тебе огромное!"
    me "За что?"
    "Передо мной стояла вожатая и приветливо улыбалась."
    mt "За торт!"
    me "Ах, да…"
    "В тот момент я как нельзя лучше понял смысл поговорки «спасибо в карман не положишь»."
    mt "Ты же никому не рассказывал? Это должен быть сюрприз!"
    me "Да…"
    mt "Вот и молодец!{w} А теперь давай – марш на ужин!"
    "Ольга Дмитриевна махнула рукой в сторону столовой."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master
    with dissolve

    stop sound fadeout 2

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Я медленно переступил порог и принялся искать свободные места."
    "Сегодня их было много, так что появилась возможность поесть в одиночестве."
    "На ужин давали рыбу с картофельным пюре."
    th "Опять неудача – останусь полуголодным.{w} Да и к тому же рыба была в обед…"
    th "Сегодня что, рыбный день?!"
    window hide
    show blink onlayer master

    $ renpy.pause(1)

    window show
    "Отодвинув в сторону тарелку с жареным морским обитателем, я опустил голову на руки и закрыл глаза."

    scene bg black onlayer master

    "Но долго мне в таком состоянии пребывать не пришлось…"
    sl "Что с тобой?"
    me "Ничего…"
    "Ответил я, не меняя положения."
    sl "Устал?"
    me "Да, есть немного…"
    "Я вздохнул."
    sl "Это плохо."
    "Серьезно сказала Славя."
    me "Еще бы…"
    sl "Ты же помнишь, что после ужина мы все в поход идем? Уже собрался?"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day onlayer master

    show sl normal pioneer onlayer master at cright
    show un normal pioneer onlayer master at cleft
    show unblink onlayer master
    with dissolve

    $ renpy.pause(1)

    window show
    me "Чего? Куда?"
    "Я моментально открыл глаза и поднял голову."
    "Рядом со Славей стояла Лена."
    show sl surprise pioneer at cright onlayer master with dspr
    sl "Поход…"
    "Она удивилась."
    sl "Ты не знал?"
    me "Нет…"
    window hide

    scene bg black onlayer master
    with fade

    window show
    "Я опустил голову на стол и закрыл ее руками."
    th "Если бы сейчас была возможность провалиться под землю..."
    "Девочки молчали."

    stop ambience fadeout 2

    "Несколько минут я находился наедине со своими мыслями, и меня это вполне устраивало."

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    "Может быть, я бы даже смог так просидеть до конца ужина, но все мои планы спутал громкий голос Ольги Дмитриевны, донесшийся из дальнего угла столовой:"
    mt "Ребята!{w} В честь чудесного спасения нашего друга и товарища, Шурика, мы приготовили для вас этот торт!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    show sl normal pioneer onlayer master at cright
    show un normal pioneer onlayer master at cleft
    with fade

    window show
    "Я нехотя поднял голову и посмотрел в сторону вожатой, но ничего не увидел за плотно сомкнутыми спинами пионеров."
    mt "Сейчас… Сейчас…"
    th "А про меня даже и не упомянули.{w} Что я Шурика спасал, что продукты для торта таскал…"
    th "Как будто так и положено."
    th "Что же, ожидаемая реакция со стороны Ольги Дмитриевны."
    show sl smile pioneer at cright onlayer master with dspr
    sl "Пойдем!{w} А то без нас съедят!"
    "Славя улыбнулась."
    show un smile pioneer at cleft onlayer master with dspr
    un "Пойдем."
    "Согласилась с ней Лена."
    me "Да, конечно…"
    hide un onlayer master
    hide sl onlayer master
    with dissolve
    "Я нехотя встал и последовал за девочками."
    show mt smile pioneer far at center  onlayer master with dissolve
    "Когда мы подошли к толпе пионеров, Ольга Дмитриевна как раз поставила торт на середину стола."

    stop ambience fadeout 2

    mt "А теперь…"
    window hide

    scene cg d5_cake onlayer master
    with dissolve

    play music music_list["awakening_power"] fadein 2

    window show
    "Закончить вожатая не успела, так как из толпы пионеров выскочила Ульянка и накинулась на торт."
    "Она надкусила его в нескольких местах до того, как ее начали оттаскивать."
    "Она упиралась и визжала, но ничего поделать не могла."
    "За всей этой картиной я безучастно наблюдал со стороны: улыбающаяся Алиса; Лена, которая пальцем подцепила немного крема; негодующие пионеры вокруг меня; визжащая Ульянка."
    "Казалось, что я не имею отношения ко всему происходящему, сейчас закрою глаза, открою – и вот я уже дома перед компьютером…"
    window hide

    show blinking onlayer master

    $ renpy.pause(3)

    window show
    "Я моргнул, но ничего не изменилось, только шум, гам и крики стали отчетливее:"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day onlayer master
    with dissolve

    show mt rage pioneer onlayer master at center
    show us normal pioneer onlayer master at right
    with dissolve
    window show
    mt "Ульяна! Это уже переходит все границы!"
    show us sad pioneer at right onlayer master with dspr
    us "Я…{w} Я…"
    "Действительно, такое поведение было странным даже для нее."
    "Вдруг словно из ниоткуда рядом со мной возник Шурик."
    show sh normal pioneer at left onlayer master with dissolve
    sh "Да ладно вам, Ольга Дмитриевна! Раз уж торт в мою честь, то ничего страшного…"
    "Он замялся."
    show mt angry pioneer at center onlayer master with dspr
    mt "Неважно!"
    "Она повернулась в сторону Ульяны."
    mt "А ты…{w} Тебя я сегодня накажу по-настоящему, чтобы в следующий раз знала!"
    show us dontlike pioneer at right onlayer master with dspr
    us "Ради Бога!"
    "Она фыркнула и отвернулась."
    mt "Сегодня с нами в поход не идешь!"
    us "Да больно надо было!"
    "Я бы с удовольствием поменялся ролями с Ульянкой и не пошел бы в поход вместо нее, но кто же знал…"
    "Если бы догадаться заранее, я бы первым полез крушить этот чертов торт!"

    stop music fadeout 3

    hide sh onlayer master with dissolve
    "После пары минут замешательства пионеры стали потихоньку расходиться."
    show mt normal pioneer at center onlayer master with dspr
    mt "И тебе пора собираться!{w} Через полчаса построение на площади."
    "Я посмотрел в глаза вожатой, пытаясь невербально передать все свое отношение к происходящему, но вышло у меня, видимо, не очень."
    mt "Не опаздывай!"
    hide mt onlayer master with dissolve
    show us sad pioneer at right onlayer master with dspr:
        linear 0.5 xalign 0.5
    "Направляясь к выходу, я подошел к Ульянке, которая сидела на столе."
    me "И зачем?"
    "Она казалась крайне обиженной.{w} Впрочем, было на что."
    show us dontlike pioneer at center onlayer master with dspr
    us "Захотелось."
    "Резко ответила Ульяна."
    me "Довольна результатом?"
    show us shy2 pioneer at center onlayer master with dspr
    us "Довольна!{w} А тебе удачно в поход сходить!"
    show us laugh pioneer at center onlayer master with dspr:
        linear 1.5 xalign 1.5
    hide us onlayer master with dissolve
    "Она ехидно улыбнулась, вскочила и выбежала из столовой."
    th "Удача мне не помешает…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset onlayer master
    with dissolve

    $ sunset_time()

    play ambience ambience_camp_center_evening fadein 3

    window show
    "«Дорогу осилит идущий» – эта поговорка крутилась у меня в голове все время, пока я шел до домика вожатой."
    "Почему-то я даже не думал возражать, ссылаться на плохое самочувствие или попросту откосить без причины."
    "События этого дня научили меня терпению.{w} Хотя иногда и было непонятно, зачем все это…"
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_sunset onlayer master
    with dissolve

    play ambience ambience_int_cabin_evening fadein 2

    window show
    "Войдя внутрь, я остановился в задумчивости."
    th "А что, собственно, мне собирать?"
    th "У меня из вещей – пальто да джинсы.{w} К тому же забыл спросить, поход с ночевкой или без."
    "В общем, делать было нечего, поэтому я на всякий случай захватил свитер, в котором попал сюда (ночью может быть холодно), и медленно поплелся в сторону площади."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    play music music_list["lightness"] fadein 3

    window show
    "Там уже собрался весь лагерь, хотя до назначенного Ольгой Дмитриевной времени оставалось еще минут десять."
    "Я примостился с краю и принялся терпеливо ждать."
    "Вечерело."
    th "Если посмотреть на нас со стороны, то вырисовывается довольно забавная картина: толпа пионеров, по привычке выстроившихся в шеренгу, словно ждет приказа молчаливого бронзового Генды."
    th "И все это в алых лучах заката."
    "Вот он машет рукой с криком «в атаку» и ревущие солдаты в красных галстуках сходятся в битве с невидимым противником…"
    "Впрочем, вместо Генды заговорила появившаяся Ольга Дмитриевна:"
    show mt normal pioneer far at center  onlayer master with dissolve
    mt "Вроде все на месте…{w} Отлично!"
    "Я не мог думать ни о чем, потому что за сегодня слишком устал, поэтому решил просто послушать вожатую."
    mt "Итак, сегодня мы отправляемся в поход!"
    mt "Важным для любого пионера является умение прийти на выручку товарищу, протянуть руку помощи в трудную минуту, просто спасти его в безвыходной ситуации, наконец!"
    mt "Всему этому нам с вами предстоит научиться!"
    "По толпе пионеров пробежал шепот, общий смысл которого был в том, что вся эта былинная экспедиция закончится в паре сот метров от лагеря около костра."
    "Почему-то и мне казалось так же."
    mt "Идти будем парами.{w} Так что, если вы еще не выбрали себе партнера, сейчас самое время!"
    "Пионеры начали быстро группироваться по двое."
    "Похоже, пары не нашлось только для меня."
    "Славя о чем-то увлеченно разговаривала с Ольгой Дмитриевной, Лена – с Мику, а Электроник, естественно, – с Шуриком."
    th "Может быть, идти одному и не так уж плохо."
    mt "Семен!"
    "Голос вожатой вывел меня из задумчивости."
    show mt normal pioneer at center onlayer master with dissolve
    "Я нехотя подошел к ней."
    mt "Тебе пары не нашлось, как я погляжу."
    me "Видимо так…"
    mt "Тогда пойдешь с Женей – она тоже без пары."
    "После этих слов на меня нахлынуло то особенное отчаяние, в которое может впасть только одинокий человек."
    "То есть, получается, что я настолько же оказался никому не нужен, насколько и библиотекарша-йети, провести с которой наедине пару часов я не согласился бы даже за деньги?"
    th "Впрочем, сейчас мы находимся в равных условиях…"
    hide mt onlayer master with dissolve
    show mz normal glasses pioneer at center onlayer master with dissolve
    "Я медленно подошел к ней."
    me "По ходу дела, нам с тобой идти…"
    show mz bukal glasses pioneer at center onlayer master with dspr
    "Она подняла на меня глаза."
    mz "Только не думай, что я рада!"
    "Женя сказала это серьезным тоном, но смысла в ее словах я не видел."
    me "А с чего тебе радоваться?"
    "Наивно спросил я."
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "Неважно!{w} Будет еще лучше, если ты помолчишь."
    hide mz onlayer master with dissolve
    th "Куда уж лучше…"

    stop music fadeout 3

    "Она развернулась и направилась за остальными пионерами."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg ext_path_sunset onlayer master
    with dissolve

    play ambience ambience_forest_evening fadein 3

    window show
    "Я не видел никакого потаенного смысла идти парами."
    "В конце концов, наш путь пролегал по исхоженным лесным тропинкам, и заблудиться здесь было весьма проблематично даже при желании."
    "Более того, мы шли уже полчаса, но не прорывались вглубь леса, ища опасностей, которые помогут проверить нашу храбрость и закалить в нас пионерский дух, а попросту ходили кругами."
    "Впрочем, если учесть, что нашим вожаком была Ольга Дмитриевна, такой поход можно считать броском хоббитов из Шира в Мордор…"
    "Как и просила Женя, я шел молча на некотором расстоянии от нее."
    "Библиотекаршу, похоже, вся эта ситуация нисколько не смущала."
    me "Слушай, а ты не знаешь, когда мы уже придем?"
    show mz normal glasses pioneer at center onlayer master with dissolve
    mz "Придем куда?"
    me "Ну, туда, где планируется разбить лагерь."
    show mz bukal glasses pioneer at center onlayer master with dspr
    mz "Смысл похода не в лагере, а в ходьбе пешком!{w} Ты ничего не понимаешь!"
    "Да, в походах я и правда ничего не понимал…"
    me "Ну, наверное, но все же…"
    show mz angry glasses pioneer at center onlayer master with dspr
    mz "Не знаю!"
    show mz angry glasses pioneer far at center  onlayer master with dissolve
    "Резко ответила она и ускорила шаг."
    "Я догнал ее и спросил:"
    show mz angry glasses pioneer at center onlayer master with dissolve
    me "Слушай, а почему ты всегда…"
    "Я хотел сказать «злая», но осекся."
    me "Я же тебе ничего плохого не делал и не собираюсь!"
    show mz bukal glasses pioneer at center onlayer master with dspr
    "Она удивленно посмотрела на меня."
    mz "Какая?"
    me "Ну, нелюдимая, что ли…{w} Или это ты только со мной так?"
    show mz rage glasses pioneer at center onlayer master with dspr
    mz "Опять ты чушь какую-то несешь!"
    me "Как знаешь…"
    hide mz onlayer master with dissolve
    "Я решил больше не заговаривать с ней первым до конца похода."
    "..."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_polyana_sunset onlayer master
    with dissolve

    window show
    "Наконец Ольга Дмитриевна решила, что пора заканчивать наши хождения по мукам."

    stop ambience fadeout 2

    show mt normal pioneer at center onlayer master with dissolve
    mt "Здесь сделаем привал."
    hide mt onlayer master with dissolve

    play music music_list["dance_of_fireflies"] fadein 3

    "Мы находились на довольно большой поляне, на которой лежало полукругом несколько деревьев, образуя что-то вроде импровизированной беседки, посредине которой земля была выжжена и валялись угли от костра."
    "По всему было заметно, что такие походы были традиционными для этого лагеря."
    "Меня вместе с остальными парнями отправили на поиски дров."
    "Это занятие оказалось несложным, так как вокруг валялось большое количество веток и бревен разного размера."
    "В конце концов, с помощью каких-то газет Ольга Дмитриевна разожгла костер."
    "Мне было очень интересно почитать, что в них пишут, но ничего, кроме советской символики, я разглядеть не смог."
    "Пионеры расселись на бревнах и начали говорить кто о чем."
    "Похоже, конечная цель всего этого мероприятия была достигнута."
    th "Не хватает только котелка с ухой, алюминиевых чашек с водкой и гитары."
    "Впрочем, я бы не удивился, если бы и все это откуда-нибудь здесь появилось."
    show sl normal pioneer at center onlayer master with dissolve
    sl "О чем думаешь?"
    "Ко мне подсела Славя."
    me "Да так, ни о чем…{w} Наслаждаюсь походом."
    "Съязвил я."
    sl "Ясно."
    hide sl onlayer master with dissolve
    "Она еще некоторое время посидела рядом, но, поняв, что я не очень настроен разговаривать, ушла."
    "Единственным, что мне хотелось сейчас, было поскорее улечься в постель и заснуть, но вместо этого я все больше пропитывался дымом от костра и пустой болтовней окружающих."
    "Я принялся наблюдать за пионерами.{w} Все веселились, смеялись, в общем, наслаждались теплым летним вечером."
    "В дальнем конце поляны я увидел Лену, которая о чем-то оживленно спорила с Алисой."
    "«Оживленно» и Лена – понятия несовместимые, так мне казалось."
    "Славя, похоже, после разговора со мной куда-то ушла."
    "Электроник с Шуриком что-то яростно доказывали Ольге Дмитриевне."
    "Кажется, только я был лишним на этом празднике жизни."
    window hide

    menu:
        "Попытаться узнать, о чем спорят Лена и Алиса":
            if lp_dv >= 6 and lp_un < 6:
                window show
                jump day5_dv

            elif lp_un >= 6 and lp_dv < 6:
                window show
                jump day5_un

            window show
            th "Хотя, с другой стороны, какая разница?"
        "Не делать ничего, просто сидеть":

            window show
            pass

    "За сегодняшний день я так устал, что не хотелось совершать ни единого лишнего телодвижения."
    "Я просто смотрел на огонь."
    th "Говорят, что на него, как и на воду, можно смотреть вечно."
    "Но была и какая-то третья вещь…"
    th "Какая же?"
    mt "Вечно можно смотреть на огонь, воду и на то, как работают другие люди!"
    show mt normal pioneer at center onlayer master with dissolve
    "Вожатая вывела меня из задумчивости."
    mt "Семен, тебе не кажется, что ты расслабился слишком рано?"
    me "А что мне еще нужно сделать?"
    "Я искренне не понимал, чего от меня хочет Ольга Дмитриевна."
    mt "Не знаю…"
    "Она замолчала на минуту."
    show mt grin pioneer at center onlayer master with dspr
    mt "Но если что-то будет нужно, то сделай обязательно."
    hide mt onlayer master with dissolve
    "Она как-то двусмысленно улыбнулась и подошла к костру, чтобы подкинуть веток."
    "После этих слов я окончательно убедился, что состою у нее на положении раба."
    "Или в крайнем случае бесплатной рабочей силы, что, в общем-то, то же самое."
    "Я вздохнул и опустил голову на руки.{w} Но и так мне не удалось долго просидеть."
    "Кто-то похлопал меня по плечу."
    show sh normal pioneer onlayer master at cright
    show el normal pioneer onlayer master at cleft
    with dissolve
    "Я поднял глаза и увидел Шурика и Электроника, севших рядом."
    me "Чего вам?"
    "Устало спросил я."
    el "Не грусти!"
    me "А что еще остается?"
    sh "Слушай, мы сейчас с Ольгой Дмитриевной обсуждали перспективы развития кружка кибернетики…"
    sh "И такое дело – нам не хватает членов.{w} Если бы ты…"
    "Он замялся."
    th "«Развитие» и эти ребята – несовместимые понятия."
    "Я ничего не ответил и начал осматривать окружающих меня пионеров."
    sh "Ну?"
    me "У меня времени нет…{w} Видите, как я постоянно занят поручениями вожатой."
    show sh upset pioneer at cright onlayer master with dspr
    sh "Да, пожалуй, ты прав…{w} Неудобно сегодня с Ульяной получилось."
    "Я удивленно посмотрел на него."
    th "Похоже, Шурик чувствует себя виноватым в том инциденте с тортом."
    me "Не очень, да…"
    "Все пионеры вроде бы были тут, но я никак не мог найти глазами Славю."
    sh "Мне кажется, что она злится на меня…"
    me "Что?"
    "Рассеянно спросил я."
    sh "Ульяна.{w} Может, мне стоит извиниться?"
    me "Да нет, тут нет никакой твоей вины…"
    "Мы сидели молча еще какое-то время, после чего я встал и сказал:"
    me "Ноги затекли, пойду пройдусь."
    "Они ничего не ответили."
    hide sh onlayer master
    hide el onlayer master
    with dissolve
    "Я несколько раз обошел импровизированный лагерь, ловя на себе пристальные взгляды вожатой."
    "Похоже, Ольге Дмитриевне не терпелось придумать для меня какое-нибудь занятие."
    "Славю я так и не нашел."
    th "Может, стоит отправиться на поиски?"
    "С другой стороны, вспоминая расстроенное лицо Ульянки, мне становилось очень жалко ее."
    th "Может, поход и не самое лучшее развлечение, но сидеть одной тоже удовольствие ниже среднего."
    "Но при всем при этом идти куда-то совершенно не хотелось…"
    window hide

    menu:
        "Попытаться найти Славю":
            if lp_sl >= 6:
                window show
                jump day5_sl

            window show
            "Почему-то я был абсолютно уверен, что со Славей все в порядке, поэтому решил никуда не ходить."
        "Пойти к Ульяне":

            if lp_us >= 6:
                window show
                jump day5_us

            window show
            th "С другой стороны, сдалась мне эта бестия!"
        "Ничего не делать":

            window show
            pass

    th "Пожалуй, на сегодня с меня хватит."
    "Я сел на прежнее место и принялся терпеливо ждать конца похода, практически физически ощущая на себе взгляды вожатой."
    "Наконец через некоторое время она встала и объявила:"
    show mt smile pioneer at center onlayer master with dissolve
    mt "А теперь давайте, как всегда, играть в города!"
    hide mt onlayer master with dissolve
    "Вообще, ничего против я не имел – игра как игра."
    th "Однако из-за этого поход неизбежно затянется…"
    "Все пионеры расселись вокруг костра."
    "Я заметил Лену и Алису, устроившихся на бревне напротив меня."
    th "Выглядели они как обычно, так что, наверное, их мелкая ссора не была чем-то серьезным."
    th "Хотя всякое может быть…"
    "Я бы с удовольствием узнал, о чем они говорили, но сейчас это не представлялось возможным, да и усталость все отчетливее заявляла о себе."
    "В голове было совершенно пусто."
    "Точнее, она была настолько тяжелой, что в ней не оставалось пространства для развертывания идей."
    "Если в лучшие времена мой мозг представляет из себя широкую автостраду, по которой с бешеной скоростью проносятся миллионы мыслей, обгоняя, подрезая друг друга, устраивая чудовищные аварии, то сейчас он не более чем затерянная в лесу тропинка, по которой ходят только в случае крайней необходимости."
    "Славя так и не появилась."
    th "Может, у нее возникли какие-то дела?"
    "Впрочем, сейчас опять же я никак этого узнать не мог."
    show mt smile pioneer at center onlayer master with dissolve
    mt "Итак, начнем!{w} Москва!"
    hide mt onlayer master with dissolve
    "Пионеры начали по очереди называть различные города."
    "Наконец очередь дошла и до меня."
    "Я старался слушать, чтобы не пропустить первую букву своего города."
    me "Архангельск."
    "Игра сделала несколько кругов."
    "С каждым новым названием мне все тяжелее было запоминать все, что говорили до этого."
    "Внимание рассеивалось, и я терялся в разнообразных столицах, городах-миллионниках, деревнях и поселках городского типа."
    show mt normal pioneer at center onlayer master with dissolve
    mt "Семен! Семен! Твоя очередь!"
    "Ольга Дмитриевна вернула меня к реальности."
    me "Простите, а что было до меня?"
    show mt angry pioneer at center onlayer master with dspr
    mt "Опять ты где-то в облаках витаешь!{w} Севастополь был."
    me "Тогда Лондон…"
    mt "Было уже."
    me "Ну, тогда…"
    "Я задумался.{w} Городов на букву «л» в мире множество, но сейчас хотя бы один из них вспомнить было тяжело."
    me "Ливерпуль?"
    mt "Было!"
    me "Лос-Анджелес?"
    show mt surprise pioneer at center onlayer master with dspr
    mt "Наконец-то!"
    hide mt onlayer master with dissolve
    "Она несколько презрительно посмотрела на меня, и игра продолжилась."
    "Наверное, еще одного города на «л» я бы не выдержал, но, к счастью, этот кон стал последним."
    show mt normal pioneer at center onlayer master with dissolve
    mt "Ладно, пожалуй, хватит на сегодня! Уже поздно, пора в лагерь!"
    "Я с облегчением вздохнул."

    stop ambience fadeout 2

    stop music fadeout 3

    "Назад мы шли уже не парами, а как придется."
    window hide

    scene bg ext_path_night onlayer master
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    window show
    "На лагерь опустилась ночь.{w} Совершенно обычная и ничем не примечательная."
    "Одна из тех ночей, когда и темное небо, и звезды, и полумесяц не вызывают никаких особенных эмоций, а стрекотание сверчков и пение ночных птиц кажется скорее обыденной работой, чем очарованием ноктюрна."

    stop ambience fadeout 2

    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Вскоре все пионеры построились на площади."
    "Время уже было позднее, усталость давала о себе знать, поэтому линейка получилась не очень ровная."
    "Мне она больше напоминала строй викингов после удачного сражения – воины довольны, улыбаются, ждут возвращения к семьям и уже не задумываются о правильном боевом порядке."
    "Хотя, с другой стороны, можно было увидеть в них и разбитый наголову отряд, небольшую горстку уцелевших, из последних сил совершающих бросок к родным землям."
    show mt normal pioneer at center onlayer master with dissolve
    mt "Всем спасибо!{w} А теперь марш спать, поздно уже!"
    "Пионеры почти мгновенно разбрелись кто куда, и я остался вдвоем с вожатой."

    stop ambience fadeout 2

    mt "И нам пора!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "До домика Ольги Дмитриевны мы шли молча."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_night onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    show mt normal pioneer at center onlayer master with dissolve
    window show
    mt "Все, спать!"
    window hide

    scene bg int_house_of_mt_night2 onlayer master
    with dissolve2

    window show
    "Сказала она, гася свет."
    "Я долго ворочался, прокручивая в голове все события сегодняшнего дня."
    "С одной стороны, я дико устал.{w} С другой – мне казалось, что что-то я забыл, что-то не сделал, что-то не так сказал…"
    "И это чувство незаконченности терзало меня."
    "Был уже второй час ночи."
    "Все плохое имеет свойство заканчиваться.{w} Или хотя бы делать перерыв…"
    window hide

    scene bg black onlayer master
    with fade3

    window show
    "Я погрузился в сон."
    window hide

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day6_main

label day5_dv:

    "Из всего благолепия выбивались только Лена и Алиса."
    "Нет, само по себе то, что Алиса с кем-то ссорится, было абсолютно естественным."
    "Но Лена, разговаривающая на повышенных тонах…"
    "Я аккуратно подошел поближе, пытаясь понять, что происходит."

    stop music fadeout 3

    show dv angry pioneer far onlayer master at cleft
    show un angry pioneer far onlayer master at cright
    with dissolve
    dv "Нет, это ты меня послушай!"
    un "Думай, как хочешь, я уже все сказала!"
    th "Похоже, дело серьезное."
    "Я старался, как мог, не привлекать внимания и делать вид, что просто стою рядом, не интересуясь их разговором."
    dv "Тут ничего и думать не надо – все и так видно!"
    dv "Рассказывай кому-нибудь другому, кто не так хорошо тебя знает."
    un "Да, ты все знаешь! Что же сама тогда ему не скажешь?"
    "Лена злилась.{w} Одно это уже было в высшей степени странно, даже учитывая то, что я не знал предмета спора."
    dv "А вот это уже не твое дело!"
    show dv surprise pioneer far at cleft onlayer master with dspr
    "Алиса фыркнула, отвернулась от нее и встретилась глазами со мной."
    show un normal pioneer far at cright onlayer master with dspr
    "Через секунду посмотрела на меня и Лена."
    "Некоторое время девочки стояли в растерянности."
    show dv rage pioneer onlayer master at cleft
    show un normal pioneer onlayer master at cright
    with dissolve

    play music music_list["blow_with_the_fires"] fadein 3

    dv "А ты…{w} Подслушиваешь?!"
    me "Я?{w} Нет-нет! Просто мимо крокодил… проходил."
    "Я натянул самую милую улыбку, которую только мог изобразить, но, кажется, не помогло."
    show dv grin pioneer at cleft onlayer master with dspr
    dv "Кстати, он сегодня за мной подглядывал!"
    "Ехидно ухмыльнулась Алиса."
    show un surprise pioneer at cright onlayer master with dspr
    "Лена вопросительно посмотрела на меня."
    th "И почему бы ей для начала не усомниться в словах этой рыжей бестии?"
    me "И ничего я не подглядывал!{w} Ты же сама знаешь, что все это случайность! К тому же спровоцированная Ульянкой!"
    dv "Ври больше!"
    th "Похоже, оправдаться не получится."
    show dv laugh pioneer at cleft onlayer master with dspr
    dv "Сиськи-то мои хоть понравились?"
    "Я почувствовал, как спина покрылась ледяным потом."
    show un shocked pioneer at cright onlayer master with dspr
    un "Это…{w} правда?"
    "Умоляюще посмотрела на меня Лена."
    me "Понимаешь, это случайно вышло…{w} И ничего я там не видел."
    show dv rage pioneer at cleft onlayer master with dspr
    dv "Не видел? Так я могу повторить!"
    "Гневно воскликнула Алиса."
    "Я просто не знал, что на это ответить."
    show dv normal pioneer at cleft onlayer master with dspr
    dv "Видишь, я же говорила!"
    un "Нет… Нет…"
    "Начала бормотать Лена и через мгновение бросилась бежать."
    show un shocked pioneer at cright onlayer master with dspr:
        linear 1.0 xalign 1.5
    hide un onlayer master with dissolve
    me "Подожди, ты чего!"
    "Крикнул я ей вслед."
    show dv smile pioneer at cleft onlayer master with dspr:
        linear 1.0 xalign 0.5
    dv "Вот видишь – девочку расстроил!"
    "Ехидно ухмыльнулась Алиса."
    me "Во-первых, не я ее расстроил!{w} Во-вторых, неизвестно, о чем вы тут спорили!"
    "Мое терпение было на пределе."
    show dv normal pioneer at center onlayer master with dspr
    dv "А тебе все возьми да расскажи."
    "Кажется, она посчитала, что наш разговор на этом закончен, и собиралась уходить."
    "Я резко схватил ее за руку."
    show dv scared pioneer at center onlayer master with dspr
    "Алиса испуганно посмотрела на меня, но ничего не сказала."
    "В тот момент я был зол.{w} Очень зол!"
    "Во-первых, меня дико бесило, что Лена расстроилась из-за меня (пусть и виноват я только косвенно)."
    "Во-вторых, меня бесила наглость Алисы."
    "А в-третьих, я был настолько измотан за сегодня, что мог выйти из себя из-за любого пустяка."
    me "Довольна?"
    "Прошипел я, показывая в ту сторону, в которую убежала Лена."
    me "Только и можешь, что памятники взрывать да беззащитных девочек обижать!"
    "Она выглядела испуганной, расстроенной и растерянной одновременно."
    show dv guilty pioneer at center onlayer master with dspr
    dv "Она сама…{w} кого хочешь обидит!{w} Ты ее просто плохо знаешь!"
    me "Верно только то, что я ее плохо знаю. Но при этом абсолютно уверен, что никого она обидеть не может! Это исключительно твоя прерогатива!"
    "Некоторое время мы стояли молча."
    "Я держал руку Алисы и не знал, что делать дальше."
    "Решение пришло как-то само собой."
    me "Ты пойдешь и извинишься!"
    show dv surprise pioneer at center onlayer master with dspr
    dv "С чего бы это вдруг?"
    "Алиса пыталась казаться надменной как всегда, но выходило не очень."
    me "Потому что я так сказал!"
    "Не став слушать дальнейшие возражения, я потащил ее к костру."
    me "Ольга Дмитриевна, у нас тут дела кое-какие появились неотложные, так что мы пораньше уйдем."

    stop music fadeout 3

    "Вожатая попыталась что-то сказать, но я не слушал и направился за Леной, ведя Алису за руку."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_path_sunset onlayer master
    with dissolve

    show dv normal pioneer at center onlayer master with dissolve
    window show
    "Через несколько сот метров я отпустил ее."
    me "Возражения?"
    "Вся спесь и надменность давно исчезли с ее лица."
    show dv guilty pioneer at center onlayer master with dspr:
        linear 0.05 xalign 0.495
        linear 0.05 xalign 0.5
        linear 0.05 xalign 0.515
        linear 0.05 xalign 0.5
        pause 2.0
        repeat
    dv "Если ты так хочешь, я пойду с тобой, но извиняться мне не за что – я сказала правду."
    me "На месте разберемся."
    "Отрезал я."

    stop ambience fadeout 2

    "До лагеря мы шли в молчании."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset onlayer master
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show dv guilty pioneer at center onlayer master with dissolve
    window show
    "На площади я спросил Алису:"
    me "А дальше куда?"
    show dv surprise pioneer at center onlayer master with dspr
    dv "А мне откуда знать?"
    me "А кто говорил, что хорошо знает Лену? Я?!"
    "Алиса замялась."
    show dv guilty pioneer at center onlayer master with dspr
    dv "Может быть, на острове…{w} Она часто там, когда хочет побыть одна."
    me "Отлично!"

    stop ambience fadeout 2

    "Мы пошли к лодочной станции."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night onlayer master
    with dissolve

    $ night_time()

    play music music_list["reflection_on_water"] fadein 3

    window show
    "Пока я искал весла и возился с канатами, на лагерь уже спустилась ночь."
    show dv normal pioneer at center onlayer master with dissolve
    "Одной лодки действительно не было."
    me "Сегодня у тебя есть отличная возможность заняться упражнениями на укрепление бицепсов, трицепсов и прочих мышц рук."
    "Съязвил я."
    show dv scared pioneer at center onlayer master with dspr
    dv "Ты это серьезно?"
    "Она испуганно посмотрела на меня."
    th "Наверное, все же последние десять минут я веду себя слишком.{w} Даже по отношению к ней…"
    me "Ладно, грести я тебя, конечно, не заставлю…"
    "Мои слова прозвучали неуверенно."
    hide dv onlayer master with dissolve
    "В этот раз махать веслами оказалось намного сложнее."
    "Ничего удивительного, ведь руки за сегодня выполнили, наверное, годовую норму по нагрузкам."
    "На середине реки я остановился, чтобы передохнуть."
    window hide

    scene cg d5_boat_2 onlayer master
    with dissolve

    window show
    "В лагере царила ночь.{w} Совершенно обычная и ничем не примечательная."
    "Одна из тех ночей, когда и темное небо, и звезды, и полумесяц не вызывают никаких особенных эмоций, а стрекотание сверчков и пение ночных птиц кажется скорее обыденной работой, чем очарованием ноктюрна."
    "Я всматривался в темноту, пытаясь разглядеть вдалеке очертания острова."
    me "А откуда ты ее знаешь?"
    "Внезапно спросил я, от чего Алиса даже вздрогнула."
    dv "Мы выросли вместе."
    "Через некоторое время нехотя ответила она."
    me "И попали вместе в один пионерлагерь.{w} Какое чудесное совпадение!"
    "В голове у меня внезапно вспыхнули с новой силой все те вопросы, загадки и страхи, которые так хорошо прятались до этого."
    th "Ведь сейчас здесь я могу просто выкинуть ее из лодки и утопить."
    th "Могу потребовать ответы."
    th "Правда, конечно, не зная, что происходит, это может быть опасно."
    "Но все же мне казалось, что именно я играю белыми и могу сделать первый ход, а не только отбиваться от уколов противника."
    me "И что же это за лагерь?"
    "Алиса недоуменно посмотрела на меня."
    me "Где мы? Почему я здесь?"
    "Она молчала."
    me "Отвечай!"
    "Крикнул я."
    "Алиса вздрогнула и с ужасом в глазах посмотрела на меня."
    dv "Ты чего?..{w} Если хочешь, чтобы я перед Леной извинилась, то я извинюсь…"
    "И тут я понял, что поступил как минимум неразумно."
    th "Во-первых, она, возможно, и ни при чем."
    th "Во-вторых…{w} не может человек так искусно врать."
    "А выражение испуга на лице Алисы подтверждало то, что она говорит правду."
    me "Извини…"
    "Коротко бросил я."
    "При всем при том все же не хотелось сдавать позиции."

    stop music fadeout 3

    "Последние метры до острова я греб уже на пределе возможностей."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_island_night onlayer master
    with dissolve

    play ambience ambience_lake_shore_night fadein 3

    window show
    "Выбравшись из лодки, я обессилено упал на холодную землю."
    show dv guilty pioneer at center onlayer master with dissolve
    "Алиса стояла рядом и смотрела на меня."
    "Сейчас бы стоило ожидать насмешки, какой-нибудь едкой фразочки, но она, наверное, еще не отошла от шока, поэтому просто молчала."
    "Остров был маленький, и хоть на дворе и стояла ночь, проще спрятаться в моей старой квартире, чем здесь."
    "Да и наверняка Лена слышала, как мы приплыли, так что стоило выяснить все вопросы с Алисой заранее."
    me "Слушай…"
    "Я внимательно посмотрел на нее, но ничего не увидел – мешала ночь и не самое идеальное зрение."
    me "Значит, когда найдем Лену, скажешь ей, что не хотела ее обидеть и что вся утренняя ситуация – это недоразумение, хорошо?"
    "Мой голос уже не звучал так уверенно, как пару минут назад, но и этого оказалось достаточно."
    "Алиса ничего не ответила, но по ее лицу было видно, что она согласна."
    "Я встал, и мы отправились на поиски Лены."
    hide dv onlayer master with dissolve
    window hide

    with fade

    window show
    "Ее лодка оказалась привязанной к коряге на дальнем конце острова."
    me "Умно!{w} Чтобы никто не увидел издалека."
    "Промычал я себе под нос."
    me "Значит, она где-то в лесу, пойдем!"
    "Я уверенно сделал несколько шагов по направлению к рощице, но Алиса осталась стоять на месте."
    show dv scared pioneer at center onlayer master with dissolve
    me "Что такое?{w} Мы же вроде все уже выяснили…"
    dv "Да нет…{w} Не в этом дело…{w} Просто там…{w} Темно…"
    "Я прищурился, чтобы получше разглядеть ее лицо."
    me "Это садик метр на метр. Чего тут бояться?"
    "Алиса не ответила."
    me "Да я бы тебя и здесь оставил – нужна больно, – только кто знает, что ты выкинуть можешь!"
    dv "Тогда…"
    "Она подошла ко мне вплотную."
    dv "Пойдем так…"

    stop ambience fadeout 2

    "Алиса взяла меня под руку."
    window hide

    scene cg d5_dv_island onlayer master
    with dissolve

    play ambience ambience_forest_night fadein 3

    window show
    "Такого поворота событий я никак не ожидал."
    "Мои щеки пылали, а к горлу подступил комок, мешающий выговорить хоть слово."
    "Впрочем, сейчас было лучше молчать, так как ничего путного я все равно бы не сказал."
    "Мы медленно направились в лес."
    "Через пару минут я овладел собой."
    me "Слушай, здесь правда бояться нечего.{w} Мы тут днем были, землянику собирали – ничего страшного. Обычная березовая рощица…"
    me "Тут днем красиво."
    "Добавил я спустя пару секунд."
    "Алиса не смотрела на меня, она уставилась куда-то вдаль, в темноту."
    me "Впрочем, дело твое…"
    "Через некоторое время она показала пальцем куда-то вперед."
    dv "Вон она."
    "Я прищурился, но не смог ничего разглядеть."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_island_night onlayer master
    with dissolve

    stop ambience fadeout 3

    play music music_list["lets_be_friends"] fadein 3

    show dv guilty pioneer onlayer master at cright
    show un cry pioneer onlayer master at cleft
    with dissolve
    window show
    "Подойдя ближе, мы увидели Лену, сидящую возле дерева.{w} Она плакала."
    un "И зачем вы пришли?"
    "Спросила она сквозь слезы."
    un "А ты…"
    "Она посмотрела на Алису и не закончила фразу."
    show dv sad pioneer at cright onlayer master with dissolve
    "Та в свою очередь отпустила мою руку."
    me "Лена, понимаешь…"
    show dv normal pioneer at cright onlayer master with dspr
    dv "Просто я хотела извиниться, что несколько резко и грубо все это…"
    "Перебила меня Алиса.{w} В ее голос вернулись обычные надменные нотки."
    "Может быть, она просто не хотела показывать свою слабость перед Леной."
    un "Извинилась, отлично!{w} Сначала говоришь одно, а делаешь совсем другое!"
    un "Очень умно сначала доказывать мне, что я не права, а потом делать то же самое!"
    "Она сорвалась на крик."
    show dv guilty pioneer at cright onlayer master with dspr
    dv "Ты все не так поняла…"
    un "Я поняла ровно то, что видела!"
    me "Девочки, тут такое дело…{w} Вы опять спорите о чем-то, и я вроде как виноват во всем, но я-то ничего не понимаю совсем!"
    show un grin pioneer at cleft onlayer master with dspr
    un "Объясни ему."
    "Сказала Лена Алисе, усмехнувшись."
    dv "А нечего и объяснять…"
    un "Может, тогда лучше мне?"
    show dv sad pioneer at cright onlayer master with dspr
    dv "Как знаешь!"
    "Она скрестила руки на груди и отвернулась."
    show un normal pioneer at cleft onlayer master with dspr
    un "Так вот, Семен…{w} Она упрекала меня, что я за тобой гоняюсь."
    "На минуту наступило полное молчание."
    "Лена, похоже, не намерена была что-то дальше объяснять, а я просто стоял и пытался осознать то, что она только что сказала."
    me "В каком смысле?"
    un "В прямом."
    dv "И ничего я такого не имела в виду."
    "Вмешалась в разговор Алиса."
    show un cry pioneer at cleft onlayer master with dspr
    un "Конечно…{w} Ты всегда так…"
    "Лена снова расплакалась."
    me "Подождите, да как же это…"
    th "Получается, я типа как нравлюсь Лене?"
    un "Сама-то! За руку его держишь! А мне пытаешь доказать, что все это неправильно!"
    th "То есть я нравлюсь Алисе?!{w} Нет, в первый вариант как-то больше верится."
    show dv guilty pioneer at cright onlayer master with dspr
    dv "Просто тут было темно и…"
    un "Да, это так на тебя похоже.{w} Всегда такая надменная, пытаешься всеми управлять, а когда до самой дело доходит..."
    "Алиса не ответила."
    "Я чувствовал, что должен что-то сказать, как-то разрядить сложившуюся ситуацию."
    me "Ну подождите…{w} Может быть, мы просто все не так поняли…{w} Я…"
    show dv angry pioneer at cright onlayer master with dspr
    dv "Речь вообще не про тебя…"
    "Каким-то отсутствующим тоном сказала Алиса."
    me "Ну, судя по разговору, как раз таки про меня."
    un "Да, про тебя!{w} Спроси у нее, что она о тебе думает и почему говорила мне, что не стоит за тобой гоняться!"
    th "Да и не помню, чтобы Лена за мной «гонялась»."
    dv "Я еще раз повторяю…"
    un "А нечего повторять!"
    show un cry pioneer at cleft onlayer master with dspr:
        linear 1.0 xalign -0.5
    hide un onlayer master with dissolve
    "Лена вскочила и убежала в темноту."
    "Я стоял в нерешительности, не зная, что делать дальше."
    th "Если я сейчас брошусь вдогонку за Леной, что ей сказать?"
    th "В конце концов, я даже толком не понимаю, что здесь происходит, из-за чего весь этот спор."
    th "И своим молчанием или глупыми попытками утешить могу еще больше ее расстроить."
    me "Наверное, лучше дать ей побыть одной…"
    "Неуверенно начал я."
    dv "Как знаешь."
    hide dv onlayer master with dissolve
    "Алиса молча направилась в сторону лодки.{w} Я последовал за ней."
    window hide

    stop music fadeout 3

    with fade

    window show
    "..."
    window hide

    with fade

    scene cg d5_boat_2 onlayer master
    with dissolve

    play ambience ambience_lake_shore_night fadein 3

    window show
    "Назад я греб с большим трудом, останавливаясь, чтобы передохнуть, через каждые десять-двадцать метров."
    "Алиса сидела и смотрела на реку, не обращая на меня никакого внимания."
    "Пожалуй, впервые за все время, проведенное в этом лагере, произошло что-то, выходящее за рамки моего понимания."
    "И самое удивительное, что это, по сути, вполне обычная, житейская ситуация."
    "Я не был так растерян даже во время ночного похода в старый лагерь."
    th "А ведь, если разобраться, ничего странного и не случилось."
    th "Да, Лена – девочка скромная и даже замкнутая, но при этом она все равно человек и должна реагировать на происходящие события."
    th "И в такой ситуации реакция ее вполне объяснима."
    "Может, я не до конца понимал всю важность их спора, но при этом прекрасно осознавал, что у девочек была причина ссориться."
    "И этой причиной, по всей видимости, был я."
    "И вот это как раз самое странное."
    me "Слушай, ты прости, что так вышло…{w} Если бы я тогда вас не подслушал…"
    "Почему-то у меня была просто патологическая потребность в чем-то извиниться."
    dv "Да ты ни в чем не виноват."
    "Рассеянно сказала она."
    dv "Просто ты оказался в подходящее время в нужном месте и заставил крутиться те механизмы, которые давно стояли без работы."
    me "Я не понимаю…"
    dv "Конечно не понимаешь.{w} Сейчас ты и не должен.{w} Поймешь потом."
    "Она внимательно посмотрела на меня."
    me "Черт!{w} И почему всегда это именно со мной происходит!"
    "Действительно, и в школьные годы, и в институте мне всегда казалось, что все несчастья сыплются обязательно на меня."
    "Закрыл кто-то на швабру кабинет труда? Замечание в дневнике мне."
    "Подрались? Зачинщик – я."
    "Недопуск к сессии? Виноват, конечно, опять я, а не преподаватель, с первого дня меня невзлюбивший."
    "Дома родители всегда в любом событии моей жизни видели мою вину, а не досадное стечение обстоятельств, влияние третьих лиц или, наконец, волю провидения."
    "И в какой-то момент я сам начал верить, что если плохое должно случиться, то оно обязательно случится именно со мной.{w} Как по закону Мерфи."
    "Поэтому и старался как можно тщательнее избегать ситуаций, в которых мог бы оказаться крайним."
    "Но, судя по сегодняшнему дню, удавалось мне это не очень…"
    dv "А у тебя аура такая, похоже, притягиваешь все и всех к себе."
    "Я с удивлением посмотрел на Алису."
    "Она улыбалась."
    th "Кажется, она читает мои мысли…"
    me "Пока что только плохое…"
    dv "Не скажи… Не скажи…"
    "Мечтательно произнесла она и уставилась на реку."
    dv "Красивая ночь, правда?"
    me "Ночь как ночь."
    "Устало ответил я."
    dv "Вот и я думаю…{w} Обычная ночь, ничего особенного. Прекрасное время, чтобы осчастливить нашу замечательную вожатую."
    dv "Пусть она узнает, что ее любимый пионер – грязный извращенец, подглядывающий за девочками!"
    "У меня внутри словно что-то защемило."
    me "Ты же это несерьезно?"
    dv "Почему же…{w} Очень даже серьезно!"
    "По ее виду можно было сказать, что она и правда шутить не намеревалась."
    me "Ладно, дело твое, конечно, но сейчас не самый подходящий момент, не находишь?"
    dv "Ты грести-то будешь?"
    "Только сейчас я понял, что наша лодка мирно покачивается на середине реки."
    me "Подожди!{w} Не меняй тему!"
    dv "До берега доберемся…{w} А я пока подумаю."
    "Ночевать здесь тоже не входило в мои планы, поэтому я из последних сил налег на весла."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night onlayer master
    with dissolve

    show dv normal pioneer at center onlayer master with dissolve
    window show
    "Выбравшись на берег, я в изнеможении упал на землю."
    "Усталость была не столько физической, сколько от мыслей о том, что Алиса может воплотить свою угрозу в жизнь и действительно рассказать Ольге Дмитриевне об утреннем инциденте."
    "А зная вожатую, можно догадаться, как она отреагирует на это."
    me "Ты на самом деле собираешься сейчас идти к Ольге Дмитриевне?"
    show dv grin pioneer at center onlayer master with dspr
    dv "А почему нет?"
    "Она лукаво улыбнулась."
    me "Ну, хотя бы потому что сейчас ночь.{w} Может, она уже спит."
    dv "А может, и не спит…"
    me "Ты ведь сама понимаешь, что это случайность! Спровоцированное Ульянкой недоразумение!"
    show dv normal pioneer at center onlayer master with dspr
    dv "Не понимаю…"
    hide dv onlayer master with dissolve
    "Она всплеснула руками и направилась в сторону лагеря."
    "Я собрал все оставшиеся силы в кулак, вскочил и кинулся за ней."
    "В первую секунду мне хотелось схватить ее за руку, остановить, но потом я осознал, что после всего, что произошло сегодня, это не лучшая идея."
    me "Подожди…"
    "Я безвольно плелся рядом с ней."
    me "Давай обсудим."
    show dv surprise pioneer at center onlayer master with dissolve
    dv "А что обсуждать?"
    "Некоторое время мы просто молча шагали рядом."
    "Я был благодарен Алисе хотя бы за то, что она шла медленно, и мне не приходилось прилагать сверхусилий, чтобы не отставать."
    me "Слушай, может, я могу что-то сделать, чтобы ты не говорила ей?"

    stop ambience fadeout 2

    show dv normal pioneer at center onlayer master with dspr
    dv "Не знаю, может, и можешь…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show dv normal pioneer at center onlayer master with dissolve
    window show
    "Мы вышли на площадь."
    me "И что же?"
    dv "Например, не бегать за Леной…"
    th "Да где же я за ней бегаю-то?!"
    "Я начал опять выходить из себя."
    me "Да с чего ты это взяла?!{w} В лесу тогда устроила ссору, из-за тебя пришлось плыть на остров, и вот опять!{w} Может, хватит уже?"
    me "Не бегаю я за ней!"
    window hide

    stop ambience fadeout 2

    scene cg d5_dv_argue onlayer master
    with dissolve

    play music music_list["you_won_t_let_me_down"] fadein 3

    window show
    "Алиса остановилась, яркий лунный свет осветил ее лицо, на котором проглядывала обида и недовольство."
    dv "Думаешь, я не вижу, как ты на нее смотришь?"
    me "И как же я на нее смотрю?"
    dv "Так!"
    me "Как?"

    scene cg d5_dv_argue_2 onlayer master with dspr

    dv "Сам знаешь!"
    "Она отвела взгляд, но осталась стоять на месте."
    me "Слушай, хватит свою больную фантазию на всех проецировать! Хочешь придумывать глупости, так держи их при себе!"
    me "Другие люди не должны страдать из-за них! И ладно еще я, так и Лена тоже!"
    "Я окончательно взбесился, но она ничего не ответила."
    "Над нами повисла тишина, в которой только изредка доносились всхлипывания Алисы."
    me "Ну вот, теперь и ты туда же…{w} Вы что, тут все с ума посходили?"
    "Я обреченно всплеснул руками."
    "Слезы Лены были понятны.{w} Но такая же реакция со стороны Алисы…"
    "Тем более опять ничем не мотивированная."
    "Самое время было удивляться, но у меня уже не осталось сил."
    "В голове было совершенно пусто."
    "Точнее, она была настолько тяжелой, что в ней не оставалось пространства для развертывания идей."
    "Если в лучшие времена мой мозг представляет из себя широкую автостраду, по которой с бешеной скоростью проносятся миллионы мыслей, обгоняя, подрезая друг друга, устраивая чудовищные аварии, то сейчас он не более чем затерянная в лесу тропинка, по которой ходят только в случае крайней необходимости."
    "Алиса все еще молчала, но всхлипывать перестала."
    me "Если это все для тебя так серьезно, можешь рассказать Ольге Дмитриевне…{w} Может, полегчает…"
    dv "Ладно, не буду…"
    "Тихо произнесла она и повернулась ко мне."

    scene cg d5_dv_argue onlayer master with dspr

    "Странно, но слез я не увидел, хотя на ее лице словно отразилась вся мирская скорбь."
    dv "Просто мне обидно…"
    me "Что тебе обидно?"
    "Устало спросил я."
    dv "Так всегда получается.{w} Все смотрят на нее, а я остаюсь в стороне."
    "Я попытался понять, что она имеет в виду, но получилось не очень, поэтому решил ей подыграть."
    th "Лишь бы она хотя бы на сегодня отстала от меня."
    me "Нет, ты не права.{w} Смотрят на тебя тоже. Вот я смотрю."
    "Я поднял глаза на Алису."
    "На ее лице удивление смешалось с выражением томительного ожидания чего-то."
    me "Видишь?"

    scene cg d5_dv_argue_3 onlayer master with dspr

    dv "А ты…{w} Ты бы смог…"
    "Ее голос вдруг стал настолько нежным, что меня аж передернуло от удивления."
    "Алиса покраснела и потупила взгляд."
    dv "То есть…{w} Ты правда считаешь, что я не хуже нее?"
    "Я хотел сказать что-то типа «Даже лучше!», но осекся."
    me "Да, считаю…"

    stop music fadeout 3

    play ambience ambience_camp_center_night fadein 3

    "Похоже, она не понимала, что я говорю все это совершенно неискренне."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    show dv laugh pioneer at center onlayer master with dissolve
    window show
    dv "Ладно, спать пора!"
    "Вдруг весело прокричала Алиса."
    "Теперь она снова была похожа на себя."
    dv "Завтра увидимся."
    hide dv onlayer master with dissolve
    "Помахав мне рукой, она убежала."
    "Я с облегчением вздохнул."

    stop ambience fadeout 2

    th "Хотя бы сегодня пронесло."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "Последние силы были потрачены на рывок до домика Ольги Дмитриевны."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Свет не горел, поэтому я, чтобы не будить ее, как можно тише разделся и лег."
    th "Все же интересно, что имела в виду Алиса?"
    th "А Лена?.."
    "Я совершенно перестал понимать, что происходит с ними, со мной – как будто нас засосало в какой-то водоворот событий, начавший раскручиваться с бешеной силой."
    th "Только что будет дальше?"
    th "И куда в итоге выкинет меня?"
    "..."
    window hide

    scene bg black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day6_dv

label day5_sl:

    "Мне было действительно интересно, куда ушла Славя."
    "Впрочем, я также хотел поскорее убраться отсюда, и, если и не улечься наконец спать, то хотя бы побыть наедине с собой, вдали от всех этих пионеров и Ольги Дмитриевны, которой так не терпелось меня опять чем-нибудь занять."

    stop music fadeout 2

    "Я выбрал подходящий момент и скрылся в лесу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    $ night_time()

    play music music_list["a_promise_from_distant_days"] fadein 3

    window show
    "На лагерь опустилась ночь.{w} Совершенно обычная и ничем не примечательная."
    "Одна из тех ночей, когда и темное небо, и звезды, и полумесяц не вызывают никаких особенных эмоций, а стрекотание сверчков и пение ночных птиц кажется скорее обыденной работой, чем очарованием ноктюрна."
    "Я бродил по лесу без особой цели, стараясь не удаляться далеко от лагеря."
    "В конце концов, там был шанс столкнуться с Ульянкой, а это стихийное бедствие, возможно, еще и похуже вожатой."
    "Я сел на поваленное дерево и задумался."
    "Почему все это именно со мной происходит? Почему я всегда и везде попадаю в дурацкие ситуации?"
    th "Даже внезапно оказавшись в непонятном пионерлагере, неизвестно где, я не могу, как нормальный герой фантастических романов, стать подопытным кроликом, жертвой больного вселенского разума или участником межгалактической войны на стороне группы пацифистов-самоубийц."
    th "Нет, я должен ночью в лесу прятаться от бесноватой вожатой и ее пионеров-стахановцев…"
    "Звезды на небе ярко сверкали."
    th "Наверное, они светят не только для меня и этого лагеря, но и освещают город, где я родился, и мой старый дом…"
    "В груди словно что-то защемило."
    window hide
    show bg semen_room onlayer master with fade

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with fade

    window show
    "Я явственно представил свою старую квартиру, и какое-то жжение начало подниматься из желудка к горлу."
    "Нет, это была не тоска.{w} Скорее грустное воспоминание."
    "Ведь несмотря ни на что за неполные пять дней здесь я чувствовал себя более живым, чем за последние несколько лет."
    "И теперь уже не знал, хочу ли возвращаться назад."
    "Меня терзал лишь один вопрос – как и почему я здесь оказался.{w} Он разгорелся с новой силой в моем мозгу."
    "Последнее время я не часто искал ответы, не часто и просто думал о своем положении."
    "Мои мысли были заняты житейскими, обыденными делами."
    "И сейчас для того, чтобы сломаться и окончательно захотеть остаться здесь, мне нужно было понять природу этого места."
    "Ведь даже соловей в золотой клетке имеет право знать, как и по чьей воле он туда попал.{w} И уже потом делать выбор, оставаться или нет…"

    stop music fadeout 3

    play ambience ambience_forest_night fadein 3

    "Возможно, я бы мог еще долго предаваться этим экзистенциальным размышлениям, но совсем рядом послышались голоса, и я понял, что это Ольга Дмитриевна с пионерами."
    th "Наверное, они продолжают поход…"
    "Я быстрыми шагами направился в сторону лагеря."

    stop ambience fadeout 3

    th "В домик вожатой возвращаться не хочется, потому что наверняка получу от нее нагоняй, а просто сидеть и ждать этого куда хуже."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night onlayer master
    with dissolve

    play ambience ambience_boat_station_night fadein 3

    window show
    "Вскоре я вышел на пляж."
    "Там уже был кто-то, кроме меня, – на песке лежала пионерская форма.{w} Женская..."
    "Но в воде вроде бы никто не плавал."
    "Я уже было подумал на очередную чертовщину, как вдруг услышал сзади голос:"
    sl "Прогуливаешь поход?"
    me "…"
    sl "Я думала, что все еще в лесу…"
    show sl shy swim at center onlayer master with dissolve
    "Я обернулся и увидел Славю в купальнике."
    me "Извини, я помешал, наверное?"
    sl "Да ничего, я уже заканчивала."
    me "А чего это ты решила ночью искупаться?"
    show sl smile swim at center onlayer master with dspr
    sl "А что, нельзя?"
    "Она улыбнулась."
    me "Да нет…{w} Просто…{w} А Ольга Дмитриевна не будет против, что ты ушла раньше?.."
    sl "Ну, так и ты тоже!"
    "Славя стрельнула в меня глазами."
    me "Да, и я тоже…"
    "Я сел на песок и уставился на реку."
    show sl normal swim at center onlayer master with dspr
    me "Не понравился поход?"
    sl "Нет, почему…{w} Просто захотелось побыть одной немного."
    me "А я тебе помешал."
    sl "Нет, все нормально."
    me "Это на тебя не похоже."
    sl "Ты о чем?"
    me "Ну, вот так вот уходить…"
    show sl laugh swim at center onlayer master with dspr
    sl "Я же не робот все-таки, чтобы постоянно действовать по заведенной программе."
    "Она рассмеялась."
    me "Да, точно…"
    "Меня все еще мучили вопросы, да и к тому же усталость становилась все сильнее и сильнее."
    "В голове было совершенно пусто."
    "Точнее, она была настолько тяжелой, что в ней не оставалось пространства для развертывания идей."
    "Если в лучшие времена мой мозг представляет из себя широкую автостраду, по которой с бешеной скоростью проносятся миллионы мыслей, обгоняя, подрезая друг друга, устраивая чудовищные аварии, то сейчас он не более чем затерянная в лесу тропинка, по которой ходят только в случае крайней необходимости."
    "Поэтому я сказал первое, что пришло в голову:"

    stop ambience fadeout 2

    play music music_list["forest_maiden"] fadein 3

    me "А тебе не кажется все это странным?"
    show sl normal swim at center onlayer master with dspr
    sl "Странным?"
    me "Все, что здесь происходит.{w} Идеальная модель пионерлагеря."
    me "Конечно, я о них знаю не много, но все именно так, как я себе и представлял."
    show sl surprise swim at center onlayer master with dspr
    sl "Ты о чем?"
    "Славя недоуменно посмотрела на меня."
    me "Тебе никогда не казалось, что ты находишься не на своем месте?"
    sl "Не знаю…"
    me "Точнее, совсем не там, где надо.{w} Как будто за тысячи километров от дома или вообще в другой галактике."
    sl "Я тебя не понимаю…"
    me "Я порой сам себя не понимаю."
    "Я лег на спину и посмотрел на звезды."
    me "А что, если я тебе скажу, что я пришелец из будущего?"
    show sl serious swim at center onlayer master with dspr
    sl "А ты пришелец из будущего?"
    "Славя совершенно серьезно посмотрела на меня."
    me "Ну, допустим.{w} И как мне вернуться в свое время?"
    show sl normal swim at center onlayer master with dspr
    sl "А ты этого хочешь?"
    th "Да, все разговоры с ней о моей ситуации, даже малейшие намеки всегда заканчиваются одним и тем же."
    th "Она словно предлагает мне остаться.{w} Настойчиво предлагает."
    me "Ну, допустим, я не знаю.{w} {i}Там{/i}, назовем это так, все родное…{w} Нет, точнее, привычное."
    me "Практически все знакомо и к любой ситуации ты готов."
    me "А тут, наоборот, буквально каждая мелочь становится для тебя неожиданностью. И вообще все…{w} другое."
    show sl smile swim at center onlayer master with dspr
    sl "Разве это плохо?"
    me "Я не говорил, что плохо…{w} Непривычно. Непонятно.{w} Иногда бывает сложно что-то менять. Особенно людям с моим характером."
    show sl normal swim at center onlayer master with dspr
    sl "А чего ты сам хочешь?"
    me "Начнем с того, что я не могу ответить на этот вопрос, пока точно не пойму, где это «тут»."
    show sl smile swim at center onlayer master with dspr
    sl "Так выясни!"
    me "Если бы все было так просто…"
    show sl normal swim at center onlayer master with dspr
    sl "А что сложного?"
    me "Все сложно!{w} Я даже не знаю, с какой стороны начать…{w} Да и меня постоянно отвлекают!"
    show sl laugh swim at center onlayer master with dspr
    sl "Ты так серьезно об этом рассуждаешь, как будто это все на самом деле!"
    "Она рассмеялась."
    me "Кто знает…"
    show sl normal swim at center onlayer master with dspr
    "Наступило довольно долгое молчание.{w} Вдруг Славя чихнула."
    me "Будь здорова."
    show sl smile swim at center onlayer master with dspr
    sl "Спасибо!"
    me "Не надо было ночью-то купаться. Простудишься. Иди скорее в палатку, а то холодно."
    sl "Да ничего, я лучше еще с тобой посижу.{w} Сейчас, только оденусь."
    hide sl onlayer master with dissolve
    "Мне было, конечно, приятно, но…"
    show sl normal pioneer at center onlayer master with dissolve
    me "Пойдем, я тебя провожу."
    "Но не успели мы сделать и десятка шагов, как Славя оперлась на мою руку."
    me "Что с тобой?"
    show sl serious pioneer at center onlayer master with dspr
    sl "Да что-то голова закружилась…"
    "Я потрогал ее лоб.{w} Он просто пылал."
    "Никогда не умел определять температуру тела на ощупь, но тут все было очевидно."
    me "Я же тебе говорил!"
    show sl sad pioneer at center onlayer master with dspr
    sl "Апчхи!"
    me "Пойдем скорее!"
    sl "Нет… Я Женю заражу…{w} Слушай, давай лучше в медпункт."
    me "И что ты будешь делать в медпункте ночью одна? Глупости!"
    show sl angry pioneer at center onlayer master with dspr
    sl "Нет, не глупости! Не хочешь – я сама пойду!"
    "Она отпустила мою руку и уже собралась уходить."
    me "Не обижайся!{w} На вот, накинь, а то холодно!"
    "Я протянул ей свитер, который прихватил с собой в поход."
    th "Хоть пригодился…"
    show sl smile2 pioneer at center onlayer master with dspr
    sl "Спасибо!"
    "Она закуталась в него и посмотрела на меня таким нежным взглядом, что я решил не спорить."
    me "Медпункт так медпункт, как скажете!"
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_aidpost_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Через пару минут мы уже стояли у дверей медпункта, и Славя подбирала ключ."
    "Мне вновь показалось, что это весьма глупая затея.{w} От обычной простуды еще никто не умирал…"
    "По крайней мере в последние лет сто."

    stop ambience fadeout 2

    "И я не видел никакой особой причины, чтобы проводить ночь в медпункте."
    window hide

    play sound sfx_medpunkt_door_open

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_night onlayer master
    with dissolve

    play ambience ambience_medstation_inside_night fadein 3

    show sl shy pioneer at center onlayer master with dissolve
    window show
    "Наконец Славя открыла дверь и облокотилась о мою руку."
    sl "Голова немного кружится."
    "Виновато сказала она."
    show sl normal pioneer at center onlayer master with dspr
    "Славя села на койку, а я – на стул рядом."
    me "Слушай, ну все-таки! Ночью одной в медпункте…"
    th "В конце концов, та же самая Женя может в крайнем случае хоть стакан воды подать.{w} Да и не заразится она – молодая, здоровая еще."
    show sl sad pioneer at center onlayer master with dspr
    sl "Все нормально.{w} Не хочу никого стеснять. Завтра придет медсестра тем более."
    "Я вдруг представил себя на месте Слави, что мне придется провести здесь ночь одному..."
    "И от этого у меня мурашки побежали по коже."
    me "Слушай, может, я с тобой побуду…"
    "Я был многим обязан ей за все время, проведенное в лагере.{w} Да и просто не хотелось оставлять ее одну."
    show sl smile pioneer at center onlayer master with dspr
    sl "Зачем?{w} Все в порядке будет. Спасибо, что проводил. Иди и ты спать."
    me "Мне кажется, что все же…"
    sl "Все в порядке!"
    "Я на мгновение задумался."
    "Конечно, с ней ничего страшного здесь не случится, но все же мне будет спокойнее, если останусь."
    me "Я все-таки..."
    show sl angry pioneer at center onlayer master with dspr
    sl "Не надо, говорю же!"
    "Обиженно воскликнула Славя."
    me "Ты же меня не выгонишь."
    "Лукаво улыбнулся я."
    show sl normal pioneer at center onlayer master with dspr
    sl "Ладно…"
    "Я был доволен своей маленькой победой."
    sl "И чем займемся?"
    "В ящике стола должны были быть карты."
    me "В дурака?"
    "По правде говоря, кроме этой игры и покера, я никаких и не знал."
    show sl smile pioneer at center onlayer master with dspr
    sl "Давай."
    hide sl onlayer master with dissolve
    window hide

    with fade

    window show
    "Играли мы долго.{w} Я совершенно забыл о времени."
    "Мы разговаривали на разные темы, много смеялись."
    "Казалось, что Славя и не болеет вовсе."
    "Но вот и наступила полночь…"
    show sl normal pioneer at center onlayer master with dissolve
    sl "Пора спать."
    me "Пожалуй…"
    sl "А ты где собираешься?"
    "Она пристально посмотрела на меня."
    show sl serious pioneer at center onlayer master with dspr
    sl "Иди все же!{w} Не надо со мной тут сидеть."
    me "Да я и так…"
    th "Сейчас бы заснул и стоя..."
    "Славя довольно долго смотрела на меня, потом задернула занавеску и сказала:"
    hide sl onlayer master with dissolve
    sl "Спокойной ночи!"
    me "Спокойной."
    window hide

    stop ambience fadeout 2

    scene anim prolog_1 onlayer master
    with fade

    play music music_list["sparkles"] fadein 3

    window show
    "Я опустил голову на руки и моментально провалился в сон."
    "Несмотря на то что очень сильно устал, спал я беспокойно.{w} Даже можно сказать, что скорее дремал."
    "Сознание то уходило, то возвращалось."
    "Это самое лучшее состояние для созерцания всяких бредовых картин…"
    "Сначала по комнате с ревом проехал автобус под номером 410, потом с потолка пошел снег, а на столе возник монитор моего компьютера."
    "На стенах появились обои, на полу – горы мусора, в углу – старая кровать."
    "Я снова оказался в своей квартире."
    "Потом пейзаж сменился на улицы родного города."
    "Я как будто пролетал по ним, проходя сквозь бесчисленные толпы снующих туда-сюда людей."

    stop music fadeout 3

    "А потом на меня опустилась темнота.{w} Первобытный вселенский мрак."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_night onlayer master
    with fade

    play ambience ambience_medstation_inside_night fadein 3

    window show
    "Я в ужасе вскочил.{w} С меня ручьем лил холодный пот."
    show sl surprise pioneer at center onlayer master with dissolve   
    "С кушетки испуганно смотрела Славя."
    me "Просто плохой сон…"
    "Я попытался улыбнуться, но вышло, видимо, не очень."
    sl "Ты кричал…"
    me "И что я кричал?"
    sl "Не знаю…{w} Неразборчиво."
    "Я посмотрел на часы.{w} Было всего без двадцати час."
    show sl shy pioneer at center onlayer master with dspr
    sl "Семен."
    me "А?"
    sl "Мне холодно…"
    "Я посмотрел на нее.{w} Славя куталась в мой свитер и ежилась."
    me "Сейчас, поищу одеяло."
    "Я перерывал один шкаф за другим и про себя чертыхался, что в медпункте даже укрыться больным нечем."
    me "Извини, ничего нет…"
    me "Подожди, сейчас сбегаю принесу."
    sl "Не надо…{w} Может, ты ляжешь со мной? Так будет теплее."
    "Она сказала это совершенно серьезно."
    "Ее голос прозвучал нежно и настолько жалобно, что у меня на секунду перехватило дыхание."
    me "А ты уверена, что это…{w} что…{w} это нормально?"
    show sl sad pioneer at center onlayer master with dspr
    sl "Значит, нельзя?"
    "Расстроено спросила она."
    me "Нет, почему…"
    window hide

    stop ambience fadeout 2

    scene cg d5_sl_sleep onlayer master
    with dissolve

    play music music_list["trapped_in_dreams"] fadein 3

    window show
    "Я медленно снял ботинки и лег на кушетку с краю, стараясь занимать как можно меньше места, весь сжался и практически не дышал."
    "Славя нежно обняла меня и положила голову на грудь."
    sl "Да, так лучше."
    "Промурчала она."
    "Я же был не в состоянии что-либо сказать, поэтому просто лежал."
    me "Хорошо..."
    sl "Спасибо тебе."
    me "За что?"
    "Славя лежала с закрытыми глазами и, кажется, была готова заснуть в любую секунду."
    sl "За то, что ты здесь."
    me "Да нет, ничего такого..."
    th "Хотя еще пару минут назад она упорно пыталась выпроводить меня."
    sl "Нет, правда."
    me "Ну тогда – пожалуйста."
    "Она ничего не сказала, но я был уверен, что Славя улыбается."
    me "Обращайтесь в любое время, так сказать!"
    sl "Ты такой заботливый, внимательный."
    me "Стараюсь."

    show cg d5_sl_sleep_2 onlayer master with dspr

    sl "Ты хороший друг."
    me "Друг? Ну, да, наверное..."
    "Почему-то это слово больно задело меня."
    "С одной стороны, не было особых оснований полагать, что для Слави я значу нечто большее, чем просто друг..."
    th "Да и к чему вообще эти мысли?"
    me "Мне тоже..."
    "Я никак не мог подобрать нужные слова."
    th "Что «мне тоже»?{w} Приятно с вами работать, надеемся на дальнейшее взаимовыгодное сотрудничество?"
    th "Или – с тобой тоже классно дружить, пойдем лепить куличики?"
    "Вдвойне тяжело было мне и потому, что Славя лежала рядом – ни скрыться, ни убежать, и даже не смотря мне в глаза, она, казалось, видит меня насквозь."
    sl "Ты чем-то расстроен?"
    me "Нет, все в порядке."
    sl "Но я же вижу."
    me "Может быть..."
    sl "Не хочешь об этом говорить?"
    me "Да не то чтобы... Просто и не о чем говорить на самом деле."
    sl "Получается, ты не знаешь, чем расстроен?"
    me "Наверное, так."
    sl "А зачем тогда расстраиваться?"
    "Славя рассмеялась."
    me "Выходит, что и незачем."
    sl "Вот и хорошо!"

    show cg d5_sl_sleep onlayer master with dspr

    "Она еще крепче прижалась ко мне."
    me "Не холодно?"
    sl "Нет, спасибо, но если тебе неудобно, то ты скажи!"
    me "Ничего, нормально."
    sl "Как тогда, с лодкой?"
    "Мышцы рук, словно вспомнив соревнования по гребле, отозвались ноющей болью."
    me "Там совсем другое дело было же!"

    show cg d5_sl_sleep_2 onlayer master with dspr

    sl "Хорошо-хорошо."
    "Сказала она лукаво и слегка приподняла голову."
    sl "Значит, точно все в порядке?"
    me "Да, в полном."
    "Я уже начал не на шутку волноваться – Славя совершенно явно чего-то от меня хотела."
    "Скорее всего, чтобы я что-то сказал или сделал."
    th "Вот только что?.."
    sl "Ты уверен?"
    me "Да...{w} Наверное."
    sl "Ну хорошо. Тогда спокойной ночи!"
    me "И тебе."

    show cg d5_sl_sleep onlayer master with dspr

    "..."
    window hide

    with fade2

    window show
    "Через некоторое время она заснула."
    "Я краем глаза поглядел на время.{w} Был всего лишь час, а это значило, что мне предстоит в таком положении пролежать до утра."
    "И меня совсем не волновало то, что онемеет рука."
    "Просто рядом со Славей, в такой опасной близости, я совершенно не мог заснуть."
    "А всякие мысли так и лезли в голову..."
    th "Интересно, она правда считает всю эту ситуацию нормальной?.."
    window hide

    scene bg black onlayer master
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_night onlayer master
    with dissolve

    play ambience ambience_medstation_inside_night fadein 3

    stop music fadeout 2

    play sound sfx_open_door_1

    show mt surprise pioneer at center onlayer master with dissolve

    pause(1)

    window show
    "Я только задумался о том, что будет плохо, если нас кто-нибудь здесь найдет, как дверь распахнулась, зажегся свет, и я увидел Ольгу Дмитриевну, стоявшую на пороге."
    "Сердце екнуло и остановилось на мгновение."
    show mt angry pioneer at center onlayer master with dspr
    mt "Семен…"
    "Дьявольски спокойно начала вожатая."
    show mt rage pioneer at center onlayer master with dspr
    mt "Я тебя везде ищу, а ты – смылся из леса раньше времени, не пришел вовремя ночевать и развращаешь нашу лучшую пионерку!"
    "От голоса Ольги Дмитриевны проснулась Славя."
    "Она некоторое время заспанными глазами смотрела на вожатую, потом, похоже, поняла, что происходит, и быстро вскочила с койки."
    show sl scared pioneer at right onlayer master with dissolve
    sl "Ольга Дмитриевна! Это совсем не то, что вы думаете! Я просто заболела, и Семен проводил меня сюда."
    sl "А потом мне стало холодно и…{w} Я ему говорила, чтобы шел к себе!"
    mt "Да-да, конечно! Значит, заболела, говоришь?"
    sl "Да…"
    "Робко ответила Славя."
    show mt angry pioneer at center onlayer master with dspr
    mt "Так вот и лечись!"
    "Она грозно посмотрела на меня."
    show mt rage pioneer at center onlayer master with dspr
    mt "А ты! Быстро со мной!"

    stop ambience fadeout 2

    "Я понял, что спорить было неуместно, встал и вышел из медпункта, даже не взглянув на Славю."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Мы молча дошли до площади."
    show mt angry pioneer at center onlayer master with dissolve
    "Ольга Дмитриевна грозно посмотрела на меня и сказала:"
    mt "В палатку! Там поговорим!"
    hide mt onlayer master with dissolve
    window hide

    with fade

    window show
    "Всю дорогу я находился в ужасном состоянии."
    "Вожатая шла рядом, но ничего не говорила."
    "Я думал о том, что опять попал в глупую ситуацию, которую абсолютно все поймут не так, как было на самом деле."
    th "Да что говорить…"
    "Будь я на месте Ольги Дмитриевны…{w} Двое подростков лежат в обнимку ночью в пустом медпункте…{w} Сложно придумать оправдание."
    "Самое обидное, что вновь и вновь это случается именно со мной!"

    stop ambience fadeout 2

    "Я всегда считал, что обладаю аналитическим складом ума, но почему-то он редко, а зачастую никогда не проявлялся на практике…"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_night onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Войдя в домик, вожатая продолжила допрос."
    show mt angry pioneer at center onlayer master with dissolve
    mt "Не хочешь мне ничего объяснить?"
    "Она, похоже, немного успокоилась."
    "Хоть это в Ольге Дмитриевне мне нравилось – она, конечно, была импульсивным человеком, но в то же время и отходила быстро."
    me "Славя же вам все рассказала…"
    mt "И ты думаешь, что я в это поверю."
    me "Я не заставляю вас в это верить, но и никаких оправданий я придумывать не собираюсь, так как это правда."
    "Она долго смотрела на меня и потом сказала:"
    show mt normal pioneer at center onlayer master with dspr
    mt "Ладно, я завтра буду думать, что с тобой делать."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    window show
    "Вожатая выключила свет, и я, не раздеваясь, накрылся одеялом и отвернулся к стенке."
    th "Интересно, а почему она только меня винит?{w} Я же там не один лежал все-таки."
    th "Конечно, Славя – образцовая пионерка, но…"
    "Нет, я совсем не собирался перекладывать на нее ответственность, просто мне было жутко обидно, что опять попал в дурацкую ситуацию."
    "Неспециально, не по своей воле, не имея никакого злого умысла и не ожидая подвоха…"
    "Я бы еще долго мог жалеть себя и мучиться, но усталость взяла свое, и я отключился."
    window hide

    scene bg black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day6_sl

label day5_us:

    "Почему-то сегодня вечером я совсем не думал об Ульяне."
    th "Весь этот случай с тортом…"
    "Я был так измотан, что не обратил на это должного внимания."
    "Хотя ее обиженное, расстроенное лицо мне хорошо запомнилось."
    "Может быть, в другой ситуации и в голову бы не пришло идти к ней, но сейчас подвернулся прекрасный повод улизнуть отсюда, закончить пораньше этот дурацкий поход."

    stop ambience fadeout 2

    stop music fadeout 3

    "Вспомнив, что Ольга Дмитриевна сказала мне быть готовым к новым заданиям, я решил не отпрашиваться у нее, а, выбрав подходящий момент, скрылся в лесу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    play ambience ambience_forest_night fadein 3

    $ night_time()

    window show
    "На лагерь опустилась ночь."
    "Мысленно я поблагодарил вожатую за то, что она не усердствовала в ориентировании на местности, и до цивилизации было каких-то сто метров."
    "Очередной затяжной поход по ночному лесу не входил в мои планы."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Вскоре я вышел на площадь и остановился в нерешительности."
    th "Что я скажу Ульянке?{w} Более того, зачем вообще я к ней иду?"
    th "Не будет ли это выглядеть глупо?"
    "Голова была настолько тяжелой, что в ней не оставалось пространства для развертывания идей."
    "Если в лучшие времена мой мозг представляет из себя широкую автостраду, по которой с бешеной скоростью проносятся миллионы мыслей, обгоняя, подрезая друг друга, устраивая чудовищные аварии, то сейчас он не более чем затерянная в лесу тропинка, по которой ходят только в случае крайней необходимости."
    "Так что, лучшим решением было ни о чем не думать и просто действовать."
    th "Но куда пойти?{w} Может быть, к ней в палатку?{w} А вдруг ее там нет?"
    "Я задумчиво почесал затылок."

    play sound sfx_body_bump

    with vpunch

    stop ambience fadeout 2

    play music music_list["eat_some_trouble"] fadein 3

    "Вдруг что-то сбило меня с ног, и я упал на асфальт.{w} Хорошо, что успел поставить руки, а то остался бы без носа…"
    us "Попался!"
    show us laugh2 pioneer at center onlayer master with dissolve
    "Я быстро вскочил с земли и увидел Ульянку, стоящую передо мной."
    me "Ты что делаешь?!"
    "Крик у меня вырвался сам собой."
    show us surp1 pioneer at center onlayer master with dspr
    us "А нечего рот разевать!"
    "Ехидно ответила она."
    me "А если бы я нос разбил? Руку сломал?"
    "Сказал я уже спокойнее."
    show us grin pioneer at center onlayer master with dspr
    us "Но не разбил же, не сломал."
    me "Слушай, почему ты постоянно надо мной издеваешься?"
    "Я уже пожалел о своем первоначальном решении прийти сюда, чтобы ей не было одиноко."
    me "Тебе мало, что ли, сегодняшнего наказания? Выводы вообще делать не умеешь?"
    show us normal pioneer at center onlayer master with dspr
    us "Это все ты виноват."
    "Улыбка моментально пропала с ее лица."
    me "В чем же я виноват?"
    us "Во всем!"
    me "То есть я всегда виноват?"
    show us dontlike pioneer at center onlayer master with dspr
    us "Да!"
    "Она скрестила руки на груди и отвернулась."
    me "Замечательно…"
    hide us onlayer master with dissolve
    "Я намеревался в ту же секунду покинуть площадь, бросив напоследок:"
    me "А ведь я сюда ради тебя пришел…"
    show us shy pioneer at center onlayer master with dissolve
    us "Что?"
    "Я остановился."
    me "Тебе же, наверное, не очень весело, когда все в походе, а ты тут одна…"
    show us laugh pioneer at center onlayer master with dspr
    us "Да плевать!"
    "Весело воскликнула она."
    show us surp1 pioneer at center onlayer master with dspr
    us "Но раз так, то чем хочешь заняться?"
    me "В каком смысле?"
    us "Ну, если ты сюда пришел ради меня!"
    "Такая мысль меня не посещала."
    "Впрочем, я же действительно не знал, зачем я здесь…"
    me "Не знаю…{w} После такого приема уже ничего не хочется."
    show us laugh2 pioneer at center onlayer master with dspr
    us "Тогда выбирать мне!"
    show us shy2 pioneer at center onlayer master with dspr
    "Весело сказала она и задумалась."
    "Я смотрел на нее некоторое время, потом не выдержал:"
    me "Слушай, если ты опять планируешь…"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Я знаю!{w} Давай напугаем остальных! Нарядимся, например, привидениями! Во смеха-то будет!"
    th "Ничего смешного в этом не нахожу."
    me "Слушай…"
    "Начал я устало, но осекся."
    th "Может быть, это и не самая плохая идея."
    "В конце концов, пока она все обдумает, пока соберется, Ольга Дмитриевна с пионерами уже вернется."
    "Раз уж я сюда пришел ради нее, то стоит подыграть."
    me "Пожалуй, ты права…"
    show us surp3 pioneer at center onlayer master with dspr
    us "Что?"
    "Ульяна смотрела на меня глазами по пять рублей."
    show us normal pioneer at center onlayer master with dspr
    us "И ты вот так просто согласишься?"
    me "Ну, а что такого?..{w} Тем более ты настаиваешь…"
    "Она внимательно, изучающе смотрела на меня несколько секунд и потом выпалила:"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Отлично!{w} Тогда нам нужны простыни! Мы же хотим казаться настоящими привидениями."
    me "Наверное…"
    show us laugh pioneer at center onlayer master with dspr
    us "Ты их достанешь!"
    "Безапелляционно заявила она."
    me "И где же я их, по-твоему, достану?"
    us "Возьми в своей палатке, очевидно же."
    me "Мне что-то не настолько очевидно…"
    show us dontlike pioneer at center onlayer master with dspr
    us "Значит, не хочешь?"
    "Она мгновенно состроила кислую мину."
    me "Ладно-ладно!"
    "Я вспомнил, что в шкафу Ольги Дмитриевны были запасные комплекты белья, так что, может быть, и ничего страшного…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    show us laugh pioneer at center onlayer master with dissolve
    window show
    "Мы подошли к домику вожатой, и я сказал Ульяне:"
    me "Подожди здесь."
    show us laugh2 pioneer at center onlayer master with dspr
    us "Слушаюсь, сэр!"
    "Выпалила она и отдала мне честь."
    "Похоже, Ульянка была полностью поглощена игрой."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_night onlayer master
    with dissolve

    window show
    "Я быстро нашел две чистые белоснежные простыни."
    th "Жаль, конечно, что их придется испачкать…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show us surp1 pioneer at center onlayer master with dissolve
    window show
    me "Вот."
    "Я протянул ей одну простыню."
    us "Она мне велика."
    "Сказала Ульянка, повертев ее в руках."
    th "Учитывая ее рост, ничего удивительного."
    me "Дай сюда."
    "Я сложил простыню пополам и отдал ей."
    show us laugh2 pioneer at center onlayer master with dspr
    us "Вот теперь куда лучше.{w} За мной!"
    hide us onlayer master with dissolve
    "Она накинула на себя белую ткань и бросилась в лес."
    me "Подожди!"

    stop music fadeout 3

    "Я кинулся за ней."
    window hide
    stop ambience fadeout 2

    scene cg d5_us_ghost onlayer master
    with dissolve

    play ambience ambience_forest_night fadein 3

    play sound_loop sfx_forest_fireplace fadein 3

    window show
    "Буквально через несколько минут мы уже были рядом с привалом пионеров, прячась за деревьями."
    "Теперь стало понятно, что безобидная поначалу затея принимает неприятный оборот."
    "Почему-то я изначально уверился, что поход закончится до того, как Ульянка перейдет к активным действиям, а теперь мы стояли в десятке метров от пионеров, облаченные в белые простыни, и выглядели абсолютно не устрашающе, а скорее комично."
    us "Готовься! По моей команде!"
    me "Подожди-подожди.{w} Я, вообще-то, шутил, когда соглашался на все это…{w} Ты подумай еще раз! Ведь ничем хорошим это точно не закончится! Попадешь под домашний арест до конца смены!"
    me "Да и я вместе с тобой…"
    us "Не отступать и не сдаваться!{w} Готов? На счет три!"
    "Я лихорадочно начал прокручивать в голове все возможные варианты развития событий.{w} А было их не так уж и много…"
    "Первое. Я с Ульянкой выбегаю из-за деревьев под общий смех пионеров и получаю хороший нагоняй от вожатой и, возможно, еще что похлеще."
    "Ульянка же приговаривается к высшей мере по законам пионерлагеря."
    "Второе. Я остаюсь тут и вместе со всеми наблюдаю, как Ульянка бегает по поляне в простыне."
    "Она получает высшую меру, как и в первом варианте, а я остаюсь в относительной безопасности."
    "Третье. Я всеми правдами и неправдами не даю ей совершить этот акт морального вандализма, и никто не страдает, кроме ее самолюбия."
    window hide

    stop sound_loop fadeout 2

    stop ambience fadeout 2

    scene cg d5_us_ghost_2 onlayer master
    with dissolve

    play music music_list["always_ready"] fadein 3

    window show
    "Все бы хорошо, но то ли эти размышления заняли у меня больше трех секунд, то ли Ульянка сократила отсчет, но я и опомниться не успел, как она выскочила на поляну, издавая какие-то нечеловеческие вопли."
    "Как и ожидалось, все пионеры громко засмеялись, кто-то даже упал с бревна, на котором сидел, и начал кататься по земле."
    "Я попытался спасти ситуацию и как можно громче, но все же так, чтобы меня не услышал никто, кроме Ульянки, закричал:"
    me "Дура! Прекращай! Иди сюда!"
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night onlayer master
    with dissolve

    show us cry2 pioneer far at center onlayer master with dissolve:

    $ renpy.pause(2)

    play ambience ambience_forest_night fadein 3

    hide us onlayer master with dissolve
    window show
    "Не знаю, то ли сработала моя сила убеждения, то ли Ульянка поняла, что ее номер провалился, но она быстро побежала в мою сторону и, не останавливаясь, скрылась в лесу."
    "Я, не теряя времени, направился за ней."
    "При таком финале оставались хотя бы минимальные шансы, что ее не накажут в очередной раз."
    "Хорошо, что я не засветился в этом трагикомическом акте."
    "Оставалось найти Ульянку."
    "Сделать это оказалось не так сложно, так как она не успела далеко убежать."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_polyana_night onlayer master
    with dissolve

    show us cry2 pioneer far at center onlayer master with dissolve
    window show
    "Вскоре я увидел ее сидящей на пеньке.{w} Она плакала."
    "Я остановился в нерешительности."
    "Конечно, такого исхода событий стоило ожидать, но сейчас было совершенно непонятно, что делать, как ее утешить."
    "Более того, я специально вернулся в лагерь, согласился на это представление ради нее…"
    "А вышло все только хуже."
    "К тому же я устал, смертельно устал."
    "Сейчас мне хотелось, чтобы этого всего не было.{w} Просто закрыть глаза и оказаться где-нибудь в другом месте."
    "Желательно в тишине и спокойствии."
    "Однако вид рыдающей Ульяны вынуждал меня к действиям."
    "Я подошел к ней и сел рядом на землю."
    show us cry2 pioneer at center onlayer master with dissolve    
    me "Ну, а чего ты ожидала?.."
    "Философски начал я."
    me "Все и должно было так закончиться."
    us "Это ты во всем виноват! Ты!"
    "Сквозь слезы прокричала Ульянка."
    me "И что бы изменилось, если бы я тогда выскочил с тобой?{w} Засмеяли бы нас обоих, только и всего."
    us "Ты всегда так! Всегда так!"
    show us cry2 pioneer close at center  onlayer master with dissolve
    "Ее рыдания становились все громче, и вдруг она бросилась на меня и начала стучать кулаками мне по груди.{w} Удары были несильные."
    "Ульяной владело скорее отчаяние, чем действительно желание меня побить."
    me "Успокойся уже!"
    "Твердо сказал я."
    "Она на секунду прекратила плакать и обняла меня."
    show us sad pioneer close at center onlayer master with dspr
    us "Может быть, ничего не изменилось, но вдвоем мне было бы спокойнее."
    "Я не знал, что сказать, поэтому просто погладил ее по голове."
    us "Можно, я еще немного так посижу?"
    me "Можно."
    "Сейчас мне казалось, что она не просто взрывоопасный ядерный реактор в форме маленькой девочки, а моя младшая нашкодившая сестренка."
    "Я совсем не злился на Ульянку, более того, мне начало казаться, что я сам начинаю переживать неудачу номера с приведениями."
    me "Ладно-ладно…{w} Напугаем их в следующий раз как следует!"
    show us shy pioneer close at center onlayer master with dspr
    us "Угу…"
    window hide

    stop ambience fadeout 2

    scene cg d5_us_sit onlayer master
    with dissolve

    play music music_list["waltz_of_doubts"] fadein 3

    window show
    "Не знаю, сколько еще мы просидели в молчании."
    "Ульянка перестала плакать, а мне не хотелось ее тревожить, ведь она только что успокоилась."
    "Но и ночевать в лесу тоже не было ни малейшего желания."
    me "Эй, пойдем уже назад в лагерь."
    "Я легонько потряс ее за плечо, но ответа не последовало."
    "Ульянка заснула."
    me "Эй!"
    "Я потряс сильнее.{w} Эффекта никакого."
    "Я обессилено вздохнул и закрыл лицо руками."
    "Сейчас мне хотелось плакать."
    th "Почему все это именно со мной происходит?{w} Почему я всегда и везде попадаю в дурацкие ситуации?"
    th "Даже внезапно оказавшись в непонятном пионерлагере, неизвестно где, я не могу, как нормальный герой фантастических романов, стать подопытным кроликом, жертвой больного вселенского разума или участником межгалактической войны на стороне группы пацифистов-самоубийц."
    th "Нет, я должен ночью в лесу сидеть с маленькой девочкой, закутанной в простыню, на руках."
    th "Пожалуй, в следующий раз закажу чудовищные эксперименты…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_polyana_night onlayer master
    with dissolve

    window show
    "Я встал и взвалил спящую Ульянку на плечо."
    "Может быть, и был способ ее разбудить, но, во-первых, мне не хотелось, во-вторых, одним грузом больше, одним меньше – особого значения уже не имело."
    "Хорошо, что груз был нетяжелым…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    window show
    "Идя по ночному лагерю, я явственно ощутил, что даже легкую с виду девочку нести столь долгое время непросто."
    "Я остановился на площади, положил Ульянку на скамейку и обессилено повалился рядом."
    "Звезды на небе ярко сверкали."
    th "Наверное, они светят не только для меня и этого лагеря, но и освещают город, где я родился, и мой старый дом…"
    "В груди словно что-то защемило."
    window hide
    show bg semen_room onlayer master with fade

    pause(1)

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with fade

    window show
    "Я явственно представил свою старую квартиру и какое-то жжение начало подниматься из желудка к горлу."
    "Нет, это была не тоска.{w} Скорее грустное воспоминание."
    "Ведь несмотря ни на что за неполные пять дней здесь я чувствовал себя более живым, чем за последние несколько лет."
    "И теперь я уже не знал, хочу ли возвращаться назад."
    "Меня терзал лишь один вопрос – как и почему я здесь.{w} Он разгорелся с новой силой в моем мозгу."
    "Последнее время я не часто искал ответы, нечасто и просто думал о своем положении."
    "Мои мысли были заняты житейскими, обыденными делами."
    "И сейчас для того, чтобы сломаться, и окончательно захотеть остаться здесь, мне нужно было понять природу этого места."
    "Ведь даже соловей в золотой клетке имеет право знать, как и по чьей воле он туда попал.{w} И уже потом делать выбор, оставаться или нет…"

    stop music fadeout 3

    play ambience ambience_camp_center_night fadein 3

    "Не знаю, сколько бы я еще предавался экзистенциальным размышлениям, но меня вывел из них громкий храп Ульянки."
    me "Такая маленькая, а так храпит…"
    "Я вздохнул, вновь взвалил Ульянку на плечо и направился в сторону ее палатки."
    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_dv_night onlayer master
    with dissolve

    window show
    "Объясняться с Алисой не хотелось, так что я просто положил спящую Ульянку на крыльцо, постучался и поспешил ретироваться."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night onlayer master
    with dissolve

    window show
    "К домику Ольги Дмитриевны я шел со смешанными чувствами."
    "С одной стороны, выполнил то, что хотел – утешил и развлек Ульянку."
    "С другой…"
    "Две скомканные простыни в руках больше напоминали обрывки смирительной рубашки…"

    stop ambience fadeout 2

    play sound sfx_open_door_2

    "Я легонько открыл дверь и вошел."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_night onlayer master
    with dissolve

    play music music_list["you_won_t_let_me_down"] fadein 3

    show mt angry pioneer at center onlayer master with dissolve
    window show
    mt "Семен!"
    "Ольга Дмитриевна сидела за столом и, похоже, ждала меня."
    mt "Ты ничего не хочешь мне объяснить?"
    me "Ну, это…{w} Вы ее только не ругайте опять…{w} Это моя вина!"
    "Вот так я неожиданно для себя стал героем."
    "Язык сработал быстрее мысли."
    "Наверное, во мне взыграли какие-то лучшие черты характера, о которых я даже не подозревал."
    "Человеколюбие вопреки здравому смыслу."
    mt "Да?"
    "Я решил гнуть свою линию, раз уж начал."
    me "Ну, я вот простыни достал. И стоял тогда за деревом."
    show mt surprise pioneer at center onlayer master with dspr
    mt "За каким деревом?"
    "Вожатая удивленно посмотрела на меня."
    mt "И зачем тебе понадобились простыни?"
    "Я понял, что облажался."
    me "Так вы не про то, что в лесу?"
    show mt normal pioneer at center onlayer master with dspr
    mt "Семен, я тебя не понимаю."
    mt "Я хотела узнать, куда ты так таинственно исчез посреди похода, но теперь с удовольствием выслушаю историю про простыни."
    "Я закрыл глаза и опустил голову."
    th "Но ведь просто не может быть, что она и все остальные не видели представления Ульянки!"
    th "Смеющиеся взахлеб пионеры не могли мне просто померещиться."
    me "Ольга Дмитриевна, я серьезно…{w} Вы же буквально недавно в лесу видели кого-то в белой простыне, кто выскочил на вас?"
    show mt surprise pioneer at center onlayer master with dspr
    mt "Так это ты был?"
    "Она пристально посмотрела на меня."
    me "Нет, не я…"
    th "А по росту не догадаться было?"
    show mt normal pioneer at center onlayer master with dspr
    mt "Но простыни у тебя…"
    me "У меня…"
    "Я не мог понять, то ли вожатая играет со мной в дурачка, то ли правда не понимает, о чем идет речь."
    me "Ольга Дмитриевна, давайте представим, что этого разговора не было.{w} Я очень устал за сегодня."
    mt "Хорошо, ложись спать."
    "Внезапно быстро согласилась она."
    window hide

    stop music fadeout 3

    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Я, конечно, удивился такой реакции, но решил воспользоваться моментом и быстро укутался одеялом, отвернувшись к стенке."
    "Но сон почему-то не шел."
    "Мыслей не было, голова болела, но отключиться никак не получалось."
    "Я перевернулся на другой бок, и у меня перед глазами замелькали картины прошедшего дня."
    window hide

    scene bg black onlayer master
    with fade

    window show
    "Я сильно зажмурился, чтобы прогнать их, но ничего не вышло."

    stop ambience fadeout 1

    play sound sfx_knock_glass

    window hide

    pause(1)

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Вдруг со стороны окна донесся какой-то стук."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with fade

    window show
    "Ольга Дмитриевна, похоже, крепко спала."
    "Я оделся и вышел на улицу."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    play music music_list["went_fishing_caught_a_girl"] fadein 3

    show us grin pioneer at center onlayer master with dissolve
    window show
    "Передо мной стояла Ульянка и хитро улыбалась."
    us "Как ты меня до палатки донес…{w} Тяжело было?"
    me "Нет, ты что…{w} Чего пришла?"
    "Мне не спалось, но в тот момент постель казалась мне единственным местом, где я мог находиться без мучений, поэтому внезапный визит Ульянки меня совсем не обрадовал."
    us "Как она? Получил втык?"
    me "Нет, обошлось как-то…"
    show us laugh2 pioneer at center onlayer master with dspr
    us "Вот и отлично! Мне всегда везет!"
    me "Это точно..."
    "Я почувствовал, как глаза начали закрываться сами собой.{w} Кажется, наконец пришел сон."
    me "Слушай, я устал очень…"
    show us surp1 pioneer at center onlayer master with dspr
    us "Я ненадолго.{w} Закрой глаза."
    "Это сделать было проще всего, да и выяснять, зачем ей это, мне совершенно не хотелось – может, побыстрее отвяжется."
    show blink onlayer master
    "Я закрыл глаза."
    window hide

    scene cg d5_us_kiss onlayer master
    with dissolve

    $ renpy.pause(2)

    window show
    "И через мгновение почувствовал короткий поцелуй."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with fade

    window show
    "Глаза открылись сами собой, но Ульянка уже убегала, маша мне рукой."
    "Я застыл в оцепенении и даже не смог что-то крикнуть ей вслед."

    stop music fadeout 4

    play ambience ambience_int_cabin_night fadein 2

    "Не знаю, сколько так стоял, но из ступора меня вывело чувство холода."
    "Я поежился и вернулся в постель."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with fade

    window show
    "Вот как раз сейчас мне совсем не хотелось спать и очень даже хотелось подумать, но глаза, начавшие закрываться перед Ульянкой, похоже, отдали команду остальному организму, и я провалился в сон, так и не успев понять, что же произошло…"
    window hide

    scene bg black onlayer master
    with fade3

    stop ambience fadeout 3

    $ renpy.pause(3)

    jump day6_us

label day5_un:

    "Из всего благолепия выбивались только Лена и Алиса."
    "Нет, само по себе то, что Алиса с кем-то ссорится, было абсолютно естественным."
    "Но Лена, разговаривающая на повышенных тонах…"
    "Я аккуратно подошел поближе, пытаясь понять, что происходит."

    stop music fadeout 3

    show dv angry pioneer far onlayer master at cleft
    show un angry pioneer far onlayer master at cright
    with dissolve
    dv "Нет, это ты меня послушай!"
    un "Ничего я слушать не собираюсь!"
    dv "Да? Ну и отлично!"
    show dv surprise pioneer far onlayer master at cleft
    show un surprise pioneer far onlayer master at cright
    with dspr
    "Алиса отвернулась и встретилась глазами со мной."
    "Сначала она явно не поняла, что происходит, но потом…"

    play music music_list["blow_with_the_fires"] fadein 3

    show dv angry pioneer far at cleft onlayer master with dspr
    dv "Так ты подслушиваешь!"
    me "Что? Я? Нет!"
    show dv angry pioneer at cleft onlayer master with dissolve
    "Она медленно пошла в мою сторону, от чего я сделал несколько шагов назад."
    "Лена же осталась стоять на месте."
    show dv normal pioneer at cleft onlayer master with dspr
    dv "Хотя ладно, слушай!"
    "Алиса остановилась на полпути и обернулась к Лене."
    dv "А знаешь, кстати, что он сегодня за мной подглядывал?"
    un "Что?"
    dv "Подглядывал. И {i}все{/i} видел!"
    show un shocked pioneer far at cright onlayer master with dspr
    un "Это… это правда?"
    "Лена жалобно заломила руки, бросила на меня короткий взгляд и уставилась себе под ноги, словно отключившись от реальности."
    me "Нет-нет, ничего такого не было!"
    show un shocked pioneer onlayer master at cright
    show dv normal pioneer far onlayer master at cleft
    with dissolve
    "Я подошел к Лене, бросив на Алису гневный взгляд."
    show dv grin pioneer far at cleft onlayer master with dspr
    dv "Как же не было? У меня и свидетели есть!"
    me "Да твои свидетели еще похлеще тебя!"
    dv "Значит, будешь говорить, что не было?"
    "Я на секунду задумался."
    th "И правда, почему у меня такое патологическое желание оправдаться перед Леной?{w} Словно мне это жизненно необходимо, необходимо, чтобы ее мнение обо мне не изменилось."
    th "Впрочем, откуда я вообще знаю, что она обо мне думает?"
    me "Нет! Не было!"
    show un sad pioneer at cright onlayer master with dspr
    "Лена бросила на Алису гневный взгляд и тут же подняла на меня глаза, полные томления и надежды."
    "Мне вдруг стало невыносимо тяжело смотреть в них."
    me "Нет, не было…"
    "Повторил я уже менее уверенно."
    show dv laugh pioneer far at cleft onlayer master with dspr
    dv "Ну, как знаешь."
    "Усмехнулась позади меня Алиса."
    dv "Тебе решать кому верить."
    hide dv onlayer master with dissolve
    "Бросила она Лене, развернулась и направилась к костру."
    show un sad pioneer at cright onlayer master:
        linear 1.0 xalign 0.5
    un "Точно?"
    "Мне было неудобно, не по себе, я ощущал дискомфорт и острое желание побыстрее закончить с этим."
    th "И с какой стати мне перед ней оправдываться?"
    me "Ну а если и было?"
    show un cry pioneer at center onlayer master with dspr
    "Я вызывающе посмотрел на Лену, но смог заметить лишь яркий луч заката, отразившийся в слезе, стекавшей по ее щеке."
    me "Нет, то есть я хотел сказать…"
    show un cry_smile pioneer at center onlayer master with dspr
    un "Тебе не нужно врать."
    "Она вытерла слезы и попыталась улыбнуться."
    un "В конце концов, это меня не касается."
    me "Нет, почему же не касается…"
    th "А почему касается?"
    me "Просто я… Ну… Это вышло случайно, понимаешь?{w} Случайность, спровоцированная Ульянкой, все это, не более."
    un "Да, конечно…"
    me "Правда!"
    un "Я верю."
    "Лена говорила все это совершенно безэмоционально, словно происходящее ее нисколько не волновало."
    "Я даже был бы готов в это поверить, если бы не слезы пару секунд назад…"
    me "А мне кажется, не веришь."
    show un normal pioneer at center onlayer master with dspr
    un "Это что, какая-то игра?"
    "Сказала Лена тихо, но в ее голосе проскакивали нотки злости."
    un "Тебе обязательно нужно меня в этом убедить? И даже если я поверю, то что? Все так и будет на самом деле?"
    me "Я не пытаюсь тебя ни в чем убедить, просто хочу, чтобы ты поняла, что я не виноват… и не хотел…"
    show un rage pioneer at center onlayer master with dspr
    un "Да какое мне вообще дело!"
    "Закричала Лена."
    "Я стоял спиной к костру, но был уверен, что все пионеры обернулись на нас."
    un "Хочешь подглядывать за кем-то – подглядывай! Что хочешь, то и делай! Но ко мне ты зачем лезешь?"
    me "Я не…"
    "А ведь действительно, как ни посмотри, все выглядело именно так – я безуспешно пытаюсь оправдаться перед Леной.{w} Как провинившийся ребенок или, может быть, даже как проштрафившийся муж…"
    show un angry pioneer at center onlayer master with dspr
    un "Знаешь что! Мне все равно!"
    hide un onlayer master with dissolve
    "Лена развернулась и быстро зашагала в сторону лагеря."
    "Я не пытался ее остановить – сейчас это было точно не лучшим решением."
    "Она на взводе, уговоры и призывы к голосу разума не помогут."
    th "И давно с ней вообще такое?{w} Чтобы она вот так кричала, выходила из себя?.."
    "В раздумьях я вернулся к костру и сел на бревно."

    stop music fadeout 3

    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_polyana_night onlayer master
    with dissolve2

    $ night_time()

    play ambience ambience_forest_night fadein 3

    show dv normal pioneer at center onlayer master with dissolve
    window show
    dv "Ну?"
    "Спросила Алиса, устроившись рядом."
    me "Что?"
    dv "Не очень удачно вышло?"
    me "Как видишь…"
    "Буркнул я, ковыряя палкой угли."
    "Уже совсем стемнело, поляна погрузилась во мрак."
    "Окружающий пейзаж напоминал картинку из детской книжки про лешего – вот-вот из-за дерева готово выпрыгнуть неведомое лесное чудище, в ветвях деревьев угрожающе ухают хищные совы, даже мышки-норушки, выглядывающие из-под коряг, смотрят на тебя с недоверием. "
    "Впрочем, сейчас я совсем не боялся – не так, как вчера, в старом лагере, в подземелье…"
    "Луна светила ярко, внимательно следя за нашим бравым пионеротрядом, и в ее свете мир словно застыл, до утра погрузившись в спячку."
    dv "Ясно."
    me "А почему…"
    "Мне наконец удалось подцепить самый большой уголь и закинуть его в центр костра, от чего пламя поднялось на полметра вверх и во все стороны полетели искры."
    me "Лена часто так себя ведет?"
    show dv surprise pioneer at center onlayer master with dspr
    dv "Как?"
    "Непонимающе спросила Алиса."
    me "Кричит.{w} Не думал, что она так отреагирует."
    show dv laugh pioneer at center onlayer master with dspr
    dv "Что она, не человек, что ли?"
    "Она засмеялась."
    dv "Как будто ты раньше не замечал."
    me "Что не замечал?"
    show dv normal pioneer at center onlayer master with dspr
    dv "Ее."
    me "В смысле?"
    dv "В прямом. Что она вот такая."
    me "Какая «такая»?"
    show dv angry pioneer at center onlayer master with dspr
    dv "Какой же ты тупой!"
    me "Нет, подожди, раз начала – договаривай уж."
    show dv normal pioneer at center onlayer master with dspr
    dv "Что она не такая, как кажется, как ты о ней думал."
    me "А какая?"
    dv "Ладно, мне надоело уже…"
    "Алиса встала и собралась уходить."
    "Я ничего не стал говорить, просто сидел и всматривался в ночное безмолвие леса."
    show dv grin pioneer at center onlayer master with dspr
    dv "Кстати, если захочешь за ней пойти, то, думаю, она на острове."
    me "На каком острове?"
    dv "На котором вы землянику собирали сегодня."
    me "А что она там делает?"
    show dv angry pioneer at center onlayer master with dspr
    dv "Тьфу, ты правда идиот!"
    hide dv onlayer master with dissolve
    "Алиса топнула ногой, обошла костер и села поодаль от остальных."
    "Может быть, сейчас я и правда многого не понимал."
    "В голове было совершенно пусто."
    "Точнее, в ней просто не оставалось пространства для развертывания идей."
    "Если в лучшие времена мой мозг представляет из себя широкую автостраду, по которой с бешеной скоростью проносятся миллионы мыслей, обгоняя, подрезая друг друга, устраивая чудовищные аварии, то сейчас он не более чем затерянная в лесу тропинка, по которой ходят только в случае крайней необходимости."
    "Я пытался думать о том, что произошло, как-то проанализировать это, но словно упирался в невидимую стену."
    "Более того, не получалось найти в душе ни единой эмоции, ни одного отклика, словно все случилось попросту не со мной."
    "Лену не получилось убедить в том, что я не виноват?{w} Ну и ладно."
    "Лена плакала, кричала, потом ушла?{w} Ну и ладно."
    "Я ничего не чувствую по этому поводу?{w} Ну и ладно."
    "Я до крови прикусил губу и встал."
    "Находиться среди смеющихся пионеров было просто невыносимо."
    th "Куда угодно – хоть в лес, хоть в шахту, хоть в космос – лишь бы подальше отсюда!"
    "Улучив удобный момент, когда вожатая не смотрела в мою сторону, я скрылся между деревьями."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night onlayer master
    with dissolve

    window show
    "..."
    "Давно не было дождя…"
    th "Впрочем, бывают ли тут вообще дожди?"
    th "Глупости, наверняка бывают – растениям-то необходима влага."
    "Ночью стало посвежее, чем днем, но воздух все равно еще не успел до конца остыть, от духоты немного кружилась голова."
    "Внезапно мне очень захотелось искупаться."

    stop ambience fadeout 2

    "Вполне нормальное желание – за день здесь успевает семь потов сойти."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night onlayer master
    with dissolve

    play ambience ambience_lake_shore_night fadein 3

    window show
    "Я и сам не заметил, как оказался на лодочной станции."
    th "Почему не на пляже?"
    "Мысли о Лене нахлынули с новой силой, все то, что я так тщательно пытался игнорировать, вылезло наружу, таща за собой неудобные вопросы, неподходящие ответы, непонятные чувства и неопределенные желания."
    "Было очевидно – на пристань меня привело подсознание."
    th "Но чего я {i}действительно{/i} хочу?"
    th "Извиниться перед ней за что-то, убедить в чем-то?{w} Нет, навряд ли."
    "Я просто хотел от нее какой-то реакции, хотел, чтобы она сказала «да, я все понимаю» и просто улыбнулась."
    "И тогда я бы перестал чувствовать себя {i}так{/i}…"
    "Мне просто было необходимо, чтобы кто-то – пусть и в {i}этом{/i} мире – меня понял."
    "Я быстро отвязал лодку, столкнул ее в воду, залез и взялся за весла."
    "…"
    window hide

    with fade

    window show
    "В этот раз грести было проще – руки болели, но удалось выработать некую технику, которая позволяла плыть более-менее по прямой."
    "Река словно застыла, прозрачным ковром расстилаясь под лодкой."
    "Лунный свет проникал глубоко под воду, настолько, что еще чуть-чуть и можно было бы увидеть дно."
    "Я налег на весла."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_island_night onlayer master
    with dissolve

    window show
    "Удивительно, но сейчас остров казался таким же, как и днем."
    "{i}Здесь{/i} все обычно по-другому – ночью, с наступлением сумерек, как будто оказываешься в другом мире – мире загадочном, иногда пугающем, но по-своему красивом, мире теней, шорохов, застывшем мире ноктюрна."
    "Я медленно обходил остров, высматривая лодку, на которой приплыла Лена."
    "Под ногами тихо шелестела трава, редкие волны мирно ударялись о берег и отскакивали назад, как мошка, которой уже надоело биться об стекло."
    "Ветерок с воды лениво шевелил листья на деревьях, скорее по привычке, чем действительно желая заставить петь ночную рощицу."
    window hide

    play sound sfx_boat_impact

    with vpunch

    window show
    "Я засмотрелся на эту прекрасную картину и сам не заметил, как налетел на что-то."
    "Это была лодка."
    th "Что же, ничего удивительного – не вплавь же она сюда добралась."
    "Я направился вглубь острова."

    stop ambience fadeout 2

    "…"
    window hide

    with fade

    window show
    "Через сотню метров за деревом послышался какой-то шорох."
    un "Не подходи…"
    "Это был шепот Лены."
    me "…"
    "Я остановился в нерешительности."
    un "Не подходи."
    "Сказала она громче."
    me "Откуда ты знаешь, что это я?"
    "Хотя она ничего такого и не говорила."
    me "Хорошо…"
    window hide

    scene cg d5_un_island onlayer master
    with dissolve

    play music music_list["raindrops"] fadein 3

    window show
    "Я прислонился к дереву, не пытаясь заглянуть за него."
    me "Алиса сказала, что ты можешь быть тут."
    un "И что?"
    "Мне было сложно сказать, какие эмоции сейчас испытывала Лена."
    "Ее голос звучал достаточно ровно, но в нем читалось какое-то раздражение, досада, однако я все равно не мог понять – то ли она злится, то ли ей все равно."
    me "Неудобно получилось."
    "Я всеми силами пытался избегать ненужных извинений и оправданий, но других слов подобрать не мог."
    un "Ты только за этим сюда пришел?"
    me "Нет… Ну то есть я не знаю."
    un "Не знаешь, но пришел?"
    me "Да."
    un "Не стоило."
    me "Почему? Если, конечно, я мешаю…"
    un "Зачем ты за мной бегаешь?"
    me "Я…"
    "А ведь она была права – все выглядело именно так, более того – меня самого к ней определенно тянуло."
    me "Не подумай ничего такого."
    un "А что я должна думать?"
    me "Не знаю."
    un "Я лишь делаю выводы по твоему поведению."
    me "Я правда не знаю… Наверное, мне лучше уйти."
    "Я окончательно запутался, и сейчас было тяжело находиться рядом с ней."
    un "Зачем? Раз уж пришел…"
    "Показалось, что в ее голосе послышались какие-то игривые нотки."
    me "Ладно."
    un "И?"
    me "Что?"
    un "Что Алиса сказала?"
    me "Да ничего особенного."
    un "Вот как."
    me "Да."
    un "Ну ладно тогда."
    me "Угу…"
    "Некоторое время мы просто молчали."
    un "Расскажи о чем-нибудь, раз уж пришел."
    me "Я даже не знаю…"
    un "Например, про то, что было утром."
    me "А что было утром?"
    un "Ты знаешь."
    me "Ты же сама не хотела об этом говорить."
    un "Не хотела, а сейчас хочу!"
    "Голос Лены задрожал."
    "Я же совершенно перестал понимать, что происходит."
    th "Может быть, за деревом совсем и не она стоит?"
    un "Не оборачивайся!"
    me "Ладно-ладно… Но что такого?"
    un "Ничего. Просто не смотри."
    me "Хорошо, как хочешь."
    un "Значит, ничего не было?"
    me "Ну, было… Но все это лишь глупая случайность!"
    un "Почему ты тогда так переживаешь о том, что я об этом подумаю?"
    me "Не переживаю я!"
    me "Да и вообще, ты-то сама тоже!"
    "Добавил я громче, начиная заводиться."
    un "Что я?"
    me "Почему тебя так волнует эта ситуация?"
    un "А кто тебе сказал, что меня волнует именно эта ситуация?"
    me "Ну а что тогда?"
    un "Ничего…"
    "Сказал она шепотом и замолчала."
    "Такой разговор ни к чему нас не приведет."
    th "Лена постоянно что-то не договаривает, а я, похоже, слишком глуп, чтобы догадаться, да и даже просто разобраться с собой не получается."
    me "Прости, наверное, я виноват. Но я просто не понимаю…"
    un "Почему…"
    me "Что?"
    un "Почему ты постоянно извиняешься? За все. За то, что делал, за то, что собираешься сделать, даже за то, что не делал."
    me "Но…"
    "Может быть, она и была права, однако я уже не мог вести себя по-другому; я чувствовал необходимость извиниться – перед ней, перед всеми."
    "Чтобы меня не считали плохим, чтобы не смеялись, чтобы не осталось недопонимания и недосказанного."
    un "Впрочем, твое дело!"
    "Лена разозлилась."
    un "Извиняйся, оправдывайся! Какая мне разница…"
    me "Ладно, хорошо, я не виноват! На самом деле, я и не считаю, что в чем-то виноват, но что тогда не так? Что с тобой не так?"
    un "А почему со мной что-то не так?"
    me "Не знаю… Мне так кажется."
    un "Ах, кажется!"
    "Рассмеялась она."
    un "Ты говоришь так, как будто знаешь меня."
    me "…"
    "Я промолчал."
    un "Уходи…"
    "Сказала Лена через некоторое время."
    "Я же не сдвинулся с места, просто не мог, не было сил."
    "Уже ничего не хотелось – ни оправдываться, ни извиняться, больше не нужно было ее понимание."
    "Я слишком устал от всего этого."
    me "Почему?"
    un "Просто уходи…"
    "Прошептала она."
    me "Не хочу."
    un "Тогда я уйду."
    me "Пойдем уж вместе."
    un "Нет."
    me "И долго ты будешь на меня обижаться? За что? Что вообще с тобой происходит? Все ведут себя нормально, кроме тебя."
    "Мне было совершенно все равно, что значат все мои слова – словно их говорил кто-то другой, а тема разговора меня совершенно не интересовала."
    un "Ты правда ничего не понимаешь, Алиса была права."
    me "Права в чем?"
    un "Да так…"
    window hide

    show blink onlayer master

    pause(1)

    window show
    "Я закрыл глаза и задумался."

    scene black onlayer master

    th "Нет, больше не могу так, не понимаю, не знаю, что думать, что делать."
    th "И давно меня перестало волновать мое положение в этом мире, вопрос о том, как вернуться назад?"
    th "Давно ли единственное, о чем я могу думать, – это Лена, то, как на меня будут смотреть остальные, как выглядят мои поступки со стороны?"
    th "Это же просто глупо и совершенно не похоже на меня, более того – неуместно в данной ситуации!"
    me "В общем, я ни в чем не виноват и не намерен оправдываться в том, чего не делал!"
    "Ответа не последовало."
    me "Эй! Ты меня слушаешь?"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_island_night onlayer master
    with dissolve

    window show
    "Я все-таки решил посмотреть, кто же на самом деле скрывался за деревом, но там никого не оказалось."
    th "Значит, ушла!"
    window hide

    with fade

    window show
    "Я бросился к лениной лодке, но она была уже далеко, почти около пристани."
    me "Ну и ладно!"
    "Крикнул я и побрел вдоль берега."
    "…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night onlayer master
    with dissolve

    window show
    "Назад удалось доплыть относительно быстро и без особых потерь."
    "Однако руки все равно болели ужасно, а глаза закрывались сами собой."
    "Наверное, такая физическая, а главное, эмоциональная нагрузка – это слишком для одного человека."
    "Я медленно брел в сторону домика вожатой, уставившись себе под ноги и ни о чем не думая…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night onlayer master
    with dissolve

    window show
    "На площади меня кто-то окликнул."
    dv "Эй!"
    show dv normal pioneer at center onlayer master with dissolve
    "Ко мне подбежала Алиса."
    dv "На острове был?"
    me "Да…"
    "По правде говоря, совершенно не хотелось с ней ни о чем разговаривать, но и врать уже не было никаких сил."
    dv "И как?"
    me "Никак… Я очень устал, иду спать."
    show dv grin pioneer at center onlayer master with dspr
    dv "Ну расскажи уж!"
    "На ее лице появилась такая мерзкая гримаса, что меня буквально передернуло от злобы."
    me "Тебе какое дело?!"
    show dv scared pioneer at center onlayer master with dspr
    dv "Ну, нет, просто…"
    "Испуганно пролепетала она."
    me "Иди куда шла!"
    hide dv onlayer master with dissolve
    "Рявкнул я и, ускорив шаг, направился по направлению к палаткам."
    "Алиса не стала меня останавливать."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    window show
    "Как назло, Ольга Дмитриевна еще не вернулась, а свой ключ я найти не мог."
    th "Неужели потерял?"
    "Оставалось лишь ждать…"

    stop music fadeout 3

    "Я плюхнулся в гамак и закрыл глаза."
    window hide

    scene black onlayer master
    with fade

    play music music_list["drown"] fadein 3

    window show
    "На сердце было тяжело, душу разрывали какие-то неопределенные томления."
    "Иногда даже казалось, что я уже умер (просто еще не понял этого) и попал в ад."
    th "Ведь действительно, вместо того, чтобы пытаться выбраться отсюда, я все сильнее раскручиваюсь на некоем дьявольском колесе, все сильнее врастаю в жизнь этого мира, этого лагеря."
    "Как будто и не было прошлой жизни – реальной жизни."
    "Как будто меня всегда только и волновало что мнение окружающих…"
    th "Да черт возьми, ведь никогда оно меня не волновало!"
    th "Почему именно сейчас, почему именно здесь?"
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_polyana_sunset onlayer master
    show un cry pioneer onlayer master at center
    show prologue_dream onlayer master
    with dissolve

    window show
    "Перед глазами встало заплаканное лицо Лены."
    th "Да, наверное, не мнение окружающих, а именно ее мнение меня волнует…"
    window hide

    scene bg ext_house_of_mt_night_without_light onlayer master
    with dissolve

    $ persistent.sprite_time = "night"

    show mt normal pioneer at center onlayer master with dissolve
    window show
    "Вдалеке послышались шаги, и через некоторое время показалась Ольга Дмитриевна."
    hide mt onlayer master with dissolve
    "Она пару секунд внимательно смотрела на меня, видимо, собираясь что-то сказать, но потом лишь вздохнула, открыла своим ключом дверь и вошла внутрь."
    "Я последовал за ней."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 onlayer master
    with dissolve

    window show
    "Бесформенные тени, размытые воспоминания, обрывки чувств и эмоций кружились в голове еще долго."
    "Так долго, что в какой-то момент я уже перестал понимать, где нахожусь и что со мной происходит."
    "Единственным спасением стал сон…"
    window hide

    stop music fadeout 4

    scene bg black onlayer master
    with fade3

    $ renpy.pause(3)

    jump day6_un
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
