texts = {
    "help": {
        "message": {
            "en_US": "Help!\n"
                     "/start - see start message\n"
                     "/help - see this message\n"
                     "/cancel - cancel pending action (list of available actions is below)\n"
                     "---\n"
                     "/createpack - create new stickerpack\n"
                     "/addpack - add existing stickerpack to your collection\n"
                     "/mypacks - list of your stickerpacks\n"
                     "/createpackinvite - create invite to your stickerpack\n"
                     "/deletepackinvite - delete invite to your stickerpack\n"
                     "/removepack - remove your stickerpack from your collection\n"
                     "/togglepack - turn on/off your stickerpack\n"
                     "/deletepack - erase your stickerpack from the bot\n"
                     "---\n"
                     "/addsticker - add sticker to your stickerpack\n"
                     "/insertsticker - insert sticker to the <n> position of your stickerpack\n"
                     "/removesticker - remove sticker from your stickerpack\n"
                     "/movesticker - move sticker in your stickerpack\n"
                     "---\n"
                     "/resetstickerkeywords - reset sticker keywords and write them again\n"
                     "---\n"
                     "/feedback - send feedback",
            "ru_RU": "Помощь!\n"
                     "/start - просмотреть стартовое сообщение\n"
                     "/help - просмотреть это сообщение\n"
                     "/cancel - отменить текущее действие (список доступных действий ниже)\n"
                     "---\n"
                     "/createpack - создать новый стикерпак\n"
                     "/addpack - добавить существующий стикерпак к себе в коллекцию\n"
                     "/mypacks - просмотреть свою коллекцию стикерпаков\n"
                     "/createpackinvite - создать приглашение к стикерпаку\n"
                     "/deletepackinvite - удалить приглашение к стикерпаку\n"
                     "/removepack - убрать стикерпак из своей коллекции\n"
                     "/togglepack - включить или выключить стикерпак\n"
                     "/deletepack - стереть стикерпак из бота\n"
                     "---\n"
                     "/addsticker - добавить стикер в стикерпак\n"
                     "/insertsticker - добавить стикер на n-ную позицию в стикерпак\n"
                     "/removesticker - убрать стикер из стикерпака\n"
                     "/movesticker - переместить стикер в стикерпаке\n"
                     "---\n"
                     "/resetstickerkeywords - сбросить ключевые слова стикера и написать их заново\n"
                     "---\n"
                     "/feedback - обратная связь"
        }

    },

    "start": {
        "message": {
            "en_US": "Hello! This bot can help you create and use private stickerpacks. To create new stickerpack, "
                     "type /createpack. To add existing stickerpack to your colelction, type /addpack. For anything else, "
                     "/help is available.",
            "ru_RU": "Привет! Этот бот поможет тебе создавать и использовать приватные стикерпаки. Чтобы создать новый "
                     "стикерпак, напишите /createpack. Чтобы добавить существующий стикерпак к себе в коллекцию, "
                     "напишите /addpack. Для любых других действий, воспользуйтесь /help."
        }
    },

    "feedback": {
        "message": {
            "en_US": "Feedback is important! If you have any suggestions like correcting translation, adding commands "
                     "or changing description of some actions, feel free to send your feedback here: "
                     "https://forms.gle/xuiP5D7krXct1qdB6.",
            "ru_RU": "Обратная связь важна! Если у вас есть предложения, такие как исправление перевода, добавление "
                     "команд или изменение описания какого-либо действие, не бойтесь написать Ваш обратный отзыв тут: "
                     "https://forms.gle/FnGtbyxjC8WjZYVDA."
        },
    },

    "cancel": {
        "action_is_cancelled": {
            "en_US": "Action is cancelled. /help",
            "ru_RU": "Действие отменено. /help"
        },
        "you_dont_have_pending_actions": {
            "en_US": "You don't have any pending actions to cancel. /help",
            "ru_RU": "У Вас нет текущих действий. /help"
        }
    },

    "finish": {
        "you_dont_have_pending_actions": {
            "en_US": "You don't have any pending actions to finish. /help",
            "ru_RU": "У Вас нет текущих действий. /help"
        },
    },

    "general": {
        "didnt_understand_ya": {
            "en_US": "Didn't understand ya. Try using some command! /help",
            "ru_RU": "Не понял Вас. Попробуйте воспользоваться командой! /help"
        },

        "dont_send_another_command_while_in_action": {
            "en_US": "You didn't finish your recent action ($0$). Please finish your action or /cancel it.",
            "ru_RU": "Вы не завершили Ваше предыдущее действие ($0$). Сначала завершите это действие либо отмените его, использовав команду /cancel."
        },

        "good": {
            "en_US": "Good!",
            "ru_RU": "Хорошо!"
        },

        "photo_is_too_big": {
            "en_US": "Unfortunately, this photo is too big. Send photo with size up to 20MB.",
            "ru_RU": "К сожалению, фотография слишком большая. Отправьте фото рзамером не более 20 МБ."
        },
        "trying_to_convert_photo_to_sticker": {
            "en_US": "Trying to convert photo to sticker, please wait...",
            "ru_RU": "Пытаемся конвертировать фото в стикер, пожалуйста, подождите..."
        },
        "your_sticker_from_photo": {
            "en_US": "Here's the sticker created from the photo you've sent:",
            "ru_RU": "Вот стикер, созданный из фотографии, которую Вы отправили:"
        },

        "video_is_too_big": {
            "en_US": "Unfortunately, this video is too big. Send video with size up to 20MB.",
            "ru_RU": "К сожалению, видео слишком большое. Отправьте видео рзамером не более 20 МБ."
        },
        "trying_to_convert_video_to_sticker": {
            "en_US": "Trying to convert video to sticker, please wait...",
            "ru_RU": "Пытаемся конвертировать видео в стикер, пожалуйста, подождите..."
        },
        "your_sticker_from_video": {
            "en_US": "Here's the sticker created from the video you've sent:",
            "ru_RU": "Вот стикер, созданный из видео, которое Вы отправили:"
        },

        "animation_is_too_big": {
            "en_US": "Unfortunately, this GIF is too big. Send GIF with size up to 20MB.",
            "ru_RU": "К сожалению, GIF слишком большой. Отправьте GIF рзамером не более 20 МБ."
        },
        "trying_to_convert_animation_to_sticker": {
            "en_US": "Trying to convert GIF to sticker, please wait...",
            "ru_RU": "Пытаемся конвертировать GIF в стикер, пожалуйста, подождите..."
        },
        "your_sticker_from_animation": {
            "en_US": "Here's the sticker created from the GIF you've sent:",
            "ru_RU": "Вот стикер, созданный из GIF, который Вы отправили:"
        },
    },

    "chooselanguage": {
        "youll_be_able_to_change_language_later": {
            "en_US": "Thank you! You'll be able to change your preferred language later via /chooselanguage.",
            "ru_RU": "Спасибо! Вы можете в любой момент поменять выбранный язык при помощи команды /chooselanguage."
        },
    },

    "createpack": {
        "write_name_of_new_stickerpack": {
            "en_US": "Please write the name of your new stickerpack. To cancel, /cancel",
            "ru_RU": "Пожалуйста, напишите имя Вашего нового стикерпака. Отменить действие - /cancel"
        },
        "new_stickerpack_is_created": {
            "en_US": "New stickerpack is created! Now add some stickers via /addsticker command. To let somebody add "
                     "your stickerpack into their collection, create invite code using /createpackinvite. For "
                     "anything else, /help is available.",
            "ru_RU": "Новый стикерпак создан! Теперь добавьте в него стикеры при помощи команды /addsticker. А чтобы "
                     "другие могли добавить Ваш стикерпак к себе в коллекцию, создайте код приглашения командой "
                     "/createpackinvite. Для любых других действий, воспользуйтесь /help."
        },
        "there_was_an_exception": {
            "en_US": "There was an exception. Action is cancelled. /help",
            "ru_RU": "Произошла ошибка. Действие отменено. /help"
        }
    },

    "addpack": {
        "send_invite": {
            "en_US": "Please send the invite code. To cancel, /cancel",
            "ru_RU": "Пожалуйста, отправьте код приглашения. Отменить действие - /cancel"
        },
        "you_already_have_this_stickerpack": {
            "en_US": "You already have this stickerpack.",
            "ru_RU": "У Вас уже есть этот стикерпак."
        },
        "couldnt_find_invite_code": {
            "en_US": "Couldn't find any invite with this code. Ask owner to check whether invite is expired.",
            "ru_RU": "Не смогли найти приглашение с таким кодом. Уточните у владельца стикерпака, истек ли срок "
                     "действия приглашения."
        },
        "stickerpack_added_successfully": {
            "en_US": "Stickerpack added successfully!",
            "ru_RU": "Стикерпак успешно добавлен!"
        },
    },

    "choosepack": {
        "internal": {
            "en_US": "This command is internal can be called only from another commands such as /addsticker or "
                     "/createpackinvite. /help",
            "ru_RU": "Эта команда - внутренняя и может быть вызвана только из других команд, таких как /addsticker или "
                     "/createpackinvite. /help"
        },
        "create_new_stickerpack": {
            "en_US": "🆕 New stickerpack",
            "ru_RU": "🆕 Новый стикерпак"
        },
        "you_dont_have_own_stickerpacks": {
            "en_US": "There are no stickerpacks you are the owner of. Create new one using /createpack.",
            "ru_RU": "Нет стикерпаков, владельцем которых являетесь Вы. Создайте новый стикерпак при помощи команды "
                     "/createpack."
        },
        "you_dont_have_stickerpacks": {
            "en_US": "You don't have any stickerpacks in your collection. Create new one using /createpack or add "
                     "existing one using /addpack.",
            "ru_RU": "В Вашей коллекции нет стикерпаков. Создайте свой стикерпак при помощи команды /createpack или "
                     "добавьте существующий при помощи команды /addpack."
        },
        "you_dont_have_stickerpack": {
            "en_US": "You don't have this stickerpack in your collection. /help",
            "ru_RU": "В Вашей коллекции нет такого стикерпака. /help"
        },
        "you_dont_own_stickerpack": {
            "en_US": "You don't own this stickerpack. /help",
            "ru_RU": "Вы не владеете данным стикерпаком. /help"
        },
        "you_have_only_one_own_stickerpack_choosing_it": {
            "en_US": "You have only one stickerpack you own ($0$) so choosing it automatically...",
            "ru_RU": "Вы владеете только одним стикерпаком ($0$), выбрали его автоматически..."
        },
        "you_have_only_one_stickerpack_choosing_it": {
            "en_US": "You have only one stickerpack in your collection ($0$) so choosing it automatically...",
            "ru_RU": "В Вашей коллекции только один стикерпак ($0$), выбрали его автоматически..."
        },
        "this_stickerpack_does_not_exist": {
            "en_US": "There's no stickerpack with given ID in the database. /help",
            "ru_RU": "Стикерпака с таким ID нет в базе данных. /help"
        },
        "there_was_an_exception": {
            "en_US": "There was an exception. Try again or /cancel",
            "ru_RU": "Произошла ошибка. Попробуйте ещё раз или /cancel"
        },
    },

    "removepack": {
        "choose_stickerpack": {
            "en_US": "Choose stickerpack below (or send its ID) to remove. Removing means that it will be removed "
                     "only from your collection. To delete it for everyone, check /deletepack. To cancel, /cancel",
            "ru_RU": "Выберите стикерпак ниже (или отправьте его ID), чтобы убрать его. Стикерпак удалится только из "
                     "вашей библиотеки. Чтобы удалить стикерпак для всех, воспользуйтесь командой /deletepack. "
                     "Отменить действие - /cancel"
        },
        "by_the_way_you_are_the_owner": {
            "en_US": "It should be mentioned that you are the owner of this stickerpack. You'll still be able to "
                     "manage it (e.g. create invites, add stickers, etc) even though you won't be able to use it.",
            "ru_RU": "Напомним, что Вы - владелец этого стикерпака. Вы всё ещё сможете управлять им (например "
                     "создавать приглашения или добавлять стикеры) даже несмотря на то, что Вы не сможете им "
                     "воспользоваться."
        },
        "this_action_is_irreversible": {
            "en_US": "Are you really sure? Removing stickerpack from your collection is irreversible\! To "
                     "confirm, please send `I totally want to remove stickerpack\.` To cancel, /cancel",
            "ru_RU": "Вы уверены? Убирание стикерпака из Вашей коллекции необратимо\! Чтобы "
                     "продолжить, отправьте `Да, я точно хочу убрать стикерпак\.` Отменить действие \- /cancel"
        },
        "i_am_totally_sure": {
            "en_US": "I totally want to remove stickerpack.",
            "ru_RU": "Да, я точно хочу убрать стикерпак."
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
        "stickerpack_was_removed": {
            "en_US": "Stickerpack was removed. /help",
            "ru_RU": "Стикерпак убран. /help"
        }
    },

    "deletepack": {
        "choose_stickerpack": {
            "en_US": "Choose stickerpack below (or send its ID) to delete. Deleting means that the stickerpack will "
                     "be erased for everyone, and no one will be able to use it. To remove it only from your "
                     "collection, check /removepack. To cancel, /cancel",
            "ru_RU": "Выберите стикерпак ниже (или отправьте его ID), чтобы удалить его. Удаление приведёт к "
                     "исчезновению стикерпака для всех - никто не сможет им воспользоваться. Чтобы убрать стикерпак "
                     "только из своей коллекции, воспользуйтесь командой /removepack. Отменить действие - /cancel"
        },
        "this_action_is_irreversible": {
            "en_US": "Are you really sure? Deleting stickerpack is irreversible\! No one will be able to use it\! To "
                     "confirm, please send `I totally want to delete stickerpack\.` To cancel, /cancel",
            "ru_RU": "Вы уверены? Удаление стикерпака необратимо\! Никто не сможет им воспользоваться\! Чтобы "
                     "продолжить, отправьте `Да, я точно хочу удалить стикерпак\.` Отменить действие \- /cancel"
        },
        "i_am_totally_sure": {
            "en_US": "I totally want to delete stickerpack.",
            "ru_RU": "Да, я точно хочу удалить стикерпак."
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
        "stickerpack_was_deleted": {
            "en_US": "Stickerpack was deleted. /help",
            "ru_RU": "Стикерпак удалён. /help"
        }
    },

    "togglepack": {
        "choose_stickerpack": {
            "en_US": "Choose stickerpack below (or send its ID). To cancel, /cancel",
            "ru_RU": "Выберите стикерпак ниже (или отправьте его ID). Отменить действие - /cancel"
        },
        "stickerpack_enabled": {
            "en_US": "Stickerpack has been enabled. It can be used again. To turn off, /togglepack",
            "ru_RU": "Стикерпак включён. Им снова можно пользоваться. Выключить - /togglepack"
        },
        "stickerpack_disabled": {
            "en_US": "Stickerpack has been disabled. It can't be used anymore. To turn on, /togglepack",
            "ru_RU": "Стикерпак выключен. Им больше нельзя пользоваться. Включить - /togglepack"
        },
    },

    "usersentsticker": {
        "internal": {
            "en_US": "This is an internal command issued only when user send a sticker. Just try to send one!",
            "ru_RU": "Это внутренная команда, которая вызывается только тогда, когда пользователь отправляет стикер. Попробуйте отправить какой-нибудь!"
        },
        "what_you_want_to_do": {
            "en_US": "You sent us sticker. What do you want to do with it?",
            "ru_RU": "Вы отправили нам стикер. Что хотите с ним сделать?"
        },
        "i_want_to_add_sticker": {
            "en_US": "Add sticker to stickerpack",
            "ru_RU": "Добавить стикер в стикерпак"
        },
        "i_want_to_cancel": {
            "en_US": "Cancel",
            "ru_RU": "Отменить"
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
    },

    "createpackinvite": {
        "choose_stickerpack": {
            "en_US": "Choose stickerpack below (or send its ID). To cancel, /cancel",
            "ru_RU": "Выберите стикерпак ниже (или отправьте его ID). Отменить действие - /cancel"
        },
        "how_many_people_can_add_your_stickerpack_via_this_invite": {
            "en_US": "How many people can add your stickerpack via this invite? Write any positive number or 0 for no "
                     "limit at all.",
            "ru_RU": "Как много людей смогут добавить Ваш стикерпак при помощи этого приглашения? Напишите любое "
                     "положительное число или 0 для отсутсвия лимита."
        },
        "for_how_many_hours_this_invite_can_be_used": {
            "en_US": "Okay, now for how many hours this invite can be used? Again, write any positive number or 0 for "
                     "no limit at all.",
            "ru_RU": "Хорошо. На сколько часов будет действовать это приглашение? Напишите любое положительное число "
                     "или 0 для отсутствия лимита времени."
        },
        "write_a_number": {
            "en_US": "No, write a number.",
            "ru_RU": "Нет, напишите число."
        },
        "write_a_positive_number_or_zero": {
            "en_US": "No, write a positive number or zero.",
            "ru_RU": "Нет, напишите положительное число или ноль."
        },
        "write_the_name_of_invite": {
            "en_US": "Now please write the name of your invite. To skip, /finish",
            "ru_RU": "Теперь отправьте, пожалуйста, название приглашения. Чтобы пропустить, отправьте /finish."
        },
        "your_invite_code_is": {
            "en_US": "Thank you\! Invite code is `$0$`\. Send it to your nearest and dearest\. They should send /addpack command to me and then send this code to add your stickerpack to their collections\.",
            "ru_RU": "Спасибо\! Код приглашения: `$0$`\. Отправьте его близким\. Они должны отправить боту команду /addpack и отправить этот код, чтобы добавить Ваш стикерпак к себе в коллекцию\."
        },
    },

    "deletepackinvite": {
        "send_invite_you_own": {
            "en_US": "Send the invite code of the stickerpack you own. To cancel, /cancel",
            "ru_RU": "Отправьте код приглашения стикерпака, которым Вы владеете. Отменить действие - /cancel"
        },
        "you_dont_own_invites_stickerpack": {
            "en_US": "You don't own stickerpack associated with this invite. /help",
            "ru_RU": "Вы не владеете стикерпаком, который связан с этим кодом приглашения. /help"
        },
        "couldnt_find_invite_code": {
            "en_US": "Couldn't find any invite with this code. Ask owner to check whether invite is expired.",
            "ru_RU": "Не смогли найти приглашение с таким кодом. Уточните у владельца стикерпака, истек ли срок действия "
                     "приглашения."
        },
        "this_action_is_irreversible": {
            "en_US": "Are you really sure? Deleting invite is irreversible\! No one will be able to use it\! To "
                     "confirm, please send `I totally want to delete invite\.` To cancel, /cancel",
            "ru_RU": "Вы уверены? Удаление приглашения необратимо\! Никто не сможет им воспользоваться\! Чтобы "
                     "продолжить, отправьте `Да, я точно хочу удалить приглашение\.` Отменить действие \- /cancel"
        },
        "i_am_totally_sure": {
            "en_US": "I totally want to delete invite.",
            "ru_RU": "Да, я точно хочу удалить приглашение."
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
        "invite_was_deleted": {
            "en_US": "Stickerpack invite was deleted. /help",
            "ru_RU": "Приглашение в стикерпак удалено. /help"
        },
    },

    "usersentphoto": {
        "internal": {
            "en_US": "This is an internal command issued only when user send a photo. Just try to send one!",
            "ru_RU": "Это внутренная команда, которая вызывается только тогда, когда пользователь отправляет фото. "
                     "Попробуйте отправить какое-нибудь!"
        },
        "what_you_want_to_do": {
            "en_US": "You sent us photo. What do you want to do with it?",
            "ru_RU": "Вы отправили нам фотографию. Что хотите с ней сделать?"
        },
        "i_want_to_convert_photo": {
            "en_US": "Just convert to sticker",
            "ru_RU": "Просто переделать в стикер"
        },
        "i_want_to_add_photo": {
            "en_US": "Add photo to stickerpack",
            "ru_RU": "Добавить фото в стикерпак"
        },
        "i_want_to_cancel": {
            "en_US": "Cancel",
            "ru_RU": "Отменить"
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
    },

    "usersentvideo": {
        "internal": {
            "en_US": "This is an internal command issued only when user send a video. Just try to send one!",
            "ru_RU": "Это внутренная команда, которая вызывается только тогда, когда пользователь отправляет видео. "
                     "Попробуйте отправить какое-нибудь!"
        },
        "what_you_want_to_do": {
            "en_US": "You sent us video. What do you want to do with it?\n\nBeware that the video will be cut to just "
                     "three seconds.",
            "ru_RU": "Вы отправили нам видео. Что хотите с ним сделать?\n\nУчтите, что видео обрежется до первых трёх "
                     "секунд."
        },
        "i_want_to_convert_video": {
            "en_US": "Just convert to sticker",
            "ru_RU": "Просто переделать в стикер"
        },
        "i_want_to_add_video": {
            "en_US": "Add video to stickerpack",
            "ru_RU": "Добавить видео в стикерпак"
        },
        "i_want_to_cancel": {
            "en_US": "Cancel",
            "ru_RU": "Отменить"
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
    },

    "usersentanimation": {
        "internal": {
            "en_US": "This is an internal command issued only when user send a GIF. Just try to send one!",
            "ru_RU": "Это внутренная команда, которая вызывается только тогда, когда пользователь отправляет GIF. "
                     "Попробуйте отправить какой-нибудь!"
        },
        "what_you_want_to_do": {
            "en_US": "You sent us GIF. What do you want to do with it?\n\nBeware that the GIF will be cut to just "
                     "three seconds.",
            "ru_RU": "Вы отправили нам GIF. Что хотите с ним сделать?\n\nУчтите, что GIF обрежется до первых трёх "
                     "секунд."
        },
        "i_want_to_convert_animation": {
            "en_US": "Just convert to sticker",
            "ru_RU": "Просто переделать в стикер"
        },
        "i_want_to_add_animation": {
            "en_US": "Add GIF to stickerpack",
            "ru_RU": "Добавить GIF в стикерпак"
        },
        "i_want_to_cancel": {
            "en_US": "Cancel",
            "ru_RU": "Отменить"
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
    },

    "choosesticker": {
        "internal": {
            "en_US": "This command is internal and can be called only from another commands such as /removesticker. /help",
            "ru_RU": "Эта команда - внутренняя и может быть вызвана только из других команд, таких как "
                     "/removesticker. /help"
        },
        "send_sticker_via_inline_query": {
            "en_US": "Send sticker via inline query (type @$0$ and press spacebar). To cancel, /cancel",
            "ru_RU": "Отправьте стикер при помощи Inline query (напишите @$0$ и нажмите пробел). Отменить действие - "
                     "/cancel"
        },
        "you_dont_own_stickerpack": {
            "en_US": "You don't own this stickerpack. /help",
            "ru_RU": "Вы не владеете данным стикерпаком. /help"
        },
        "you_dont_have_or_own_stickerpack": {
            "en_US": "You don't have stickerpack in your collection or you don't own stickerpack which has the "
                     "sticker you've sent. /help",
            "ru_RU": "В Вашей коллекции нет стикерпака или Вы не являетесь владельцем стикерпака, в котором находится "
                     "отправленный Вами стикер. /help"
        },
        "sticker_is_not_in_this_stickerpack": {
            "en_US": "This sticker is not in this stickerpack. This is an internal error. Action is cancelled. /help",
            "ru_RU": "Тот стикер не из этого стикерпака. Это внутренняя ошибка. Действие отменено. /help"
        },
        "youve_sent_actual_sticker_not_string": {
            "en_US": "It seems you've sent us actual sticker and not textual representation of it. It's okay! Wait "
                     "some time (at least one minute) and try to send sticker via bot again.",
            "ru_RU": "Кажется, Вы отправили настоящий стикер, а не его текстовую репрезентацию. Всё хорошо! Подождите "
                     "совсем немного (хотя бы минуту) и снова попробуйте отправить стикер через бота."
        },
        "there_was_an_exception": {
            "en_US": "There was an exception. Action cancelled. /help",
            "ru_RU": "Произошла ошибка. Действие отменено. /help"
        },
    },

    "addsticker": {
        "choose_stickerpack": {
            "en_US": "Choose stickerpack below (or send its ID). To cancel, /cancel",
            "ru_RU": "Выберите стикерпак ниже (или отправьте его ID). Отменить действие - /cancel"
        },
        "send_the_sticker": {
            "en_US": "Send sticker, image, GIF, video or file. To preserve transparency, consider sending file "
                     "without compression. To cancel, /cancel",
            "ru_RU": "Отправьте стикер, фото, GIF, видео или файл. Для сохранения прозрачности лучше отправить файл "
                     "без сжатия. Отменить действие - /cancel"
        },
        "no_send_sticker": {
            "en_US": "No, send sticker, image, GIF, video or file.",
            "ru_RU": "Нет, отправьте стикер, фото, GIF, видео или файл."
        },
        "this_sticker_is_public": {
            "en_US": "It seems that this sticker is from public Telegram stickerpack. "
                     "Should I anonimyze it so the sticker you've sent becomes unclickable "
                     "and detached from public stickerpack?",
            "ru_RU": "Кажется, этот стикер из публичного стикерпака Телеграма. "
                     "Должны ли мы его анонимизировать, чтобы стикер стал некликабельным "
                     "и был отвязан от публичного стикерпака?"
        },
        "yes": {
            "en_US": "Yes",
            "ru_RU": "Да"
        },
        "no": {
            "en_US": "No",
            "ru_RU": "Нет"
        },
        "your_private_sticker": {
            "en_US": "Your private sticker:",
            "ru_RU": "Ваш приватный стикер:"
        },
        "this_sticker_is_private": {
            "en_US": "This sticker is already private. Good!",
            "ru_RU": "Этот стикер уже приватный. Отлично!"
        },
        "there_was_an_exception": {
            "en_US": "There was an exception while making sticker private. Try to send this sticker again or /cancel",
            "ru_RU": "Произошла ошибка при анонимизации стикера. Попробуйте отправить этот стикер ещё раз или /cancel"
        },
        "privacy_choose_only_yes_or_no": {
            "en_US": "The answer have to be either yes or no. Resend your answer please.",
            "ru_RU": "Ответ должен быть либо \"yes\", либо \"no\". Отправьте ответ ещё раз."
        },
        "send_keywords": {
            "en_US": "Now send keywords of this sticker, message-by-message. They can be words or emojis. When you're "
                     "ready, /finish",
            "ru_RU": "Отправьте ключевые слова стикера отдельными сообщениями. Это могут быть слова или эмодзи. Когда "
                     "будете готовы, /finish"
        },
        "no_send_keywords": {
            "en_US": "Send us textual keywords.",
            "ru_RU": "Отправьте текстовые ключевые слова."
        },
        "send_more_keywords": {
            "en_US": "Okay! Write some more, or /finish",
            "ru_RU": "Отлично! Отправьте ещё, или /finish"
        },
        "send_position_of_sticker_to_insert": {
            "en_US": "Send the position the sticker will be inserted into from 1 to $0$. All of the stickers after "
                     "position you entered will be shifted to the right including that sticker which was in this "
                     "position previously. To cancel, /cancel",
            "ru_RU": "Напишите позицию, на которую вставите стикер, от 1 до $0$. Все стикеры после этой позиции будут "
                     "сдвинуты направо, включая тот стикер, который был на этой позиции. Отменить действие - /cancel"
        },
        "start_position": {
            "en_US": "To the start",
            "ru_RU": "В начало"
        },
        "end_position": {
            "en_US": "To the end",
            "ru_RU": "В конец"
        },
        "write_a_number": {
            "en_US": "No, write a number.",
            "ru_RU": "Нет, напишите число."
        },
        "write_a_positive_number_or_zero": {
            "en_US": "No, write a positive number or zero.",
            "ru_RU": "Нет, напишите положительное число или ноль."
        },
        "write_a_number_from_sth_to_sth": {
            "en_US": "No, write a number between $0$ and $1$.",
            "ru_RU": "Нет, напишите число от $0$ до $1$."
        },
        "done_adding_sticker": {
            "en_US": "Done! Try to use sticker via typing @$0$ in any chat.",
            "ru_RU": "Готово! Попробуйте отправить стикер, написав @$0$ в любом чате."
        }
    },

    "movesticker": {
        "send_position_of_sticker": {
            "en_US": "Send the position the sticker will be moved into from 1 to $0$. To cancel, /cancel",
            "ru_RU": "Напишите позицию, на которую передвинете стикер, от 1 до $0$. Отменить действие - /cancel"
        },
        "write_a_number": {
            "en_US": "No, write a number.",
            "ru_RU": "Нет, напишите число."
        },
        "write_a_positive_number_or_zero": {
            "en_US": "No, write a positive number or zero.",
            "ru_RU": "Нет, напишите положительное число или ноль."
        },
        "write_a_number_from_sth_to_sth": {
            "en_US": "No, write a number between $0$ and $1$.",
            "ru_RU": "Нет, напишите число от $0$ до $1$."
        },
        "done": {
            "en_US": "Done!",
            "ru_RU": "Готово!"
        },
    },

    "deletesticker": {
        "this_action_is_irreversible": {
            "en_US": "Are you really sure? Deleting sticker is irreversible\! To "
                     "confirm, please send `I totally want to delete sticker\.` To cancel, /cancel",
            "ru_RU": "Вы уверены? Удаление стикера необратимо\! Чтобы "
                     "продолжить, отправьте `Да, я точно хочу удалить стикер\.` Отменить действие \- /cancel"
        },
        "i_am_totally_sure": {
            "en_US": "I totally want to delete sticker.",
            "ru_RU": "Да, я точно хочу удалить стикер."
        },
        "you_typed_that_message_incorrectly": {
            "en_US": "You typed that message incorrectly. Try again or /cancel",
            "ru_RU": "Вы написали это сообщение неправильно. Попробуйте снова или /cancel"
        },
        "sticker_was_deleted": {
            "en_US": "Sticker was deleted. /help",
            "ru_RU": "Стикер удалён. /help"
        },
    },

    "getstickerkeywords": {
        "keywords_of_sticker_are": {
            "en_US": "Keywords of this sticker:\n\n$0$",
            "ru_RU": "Ключевые слова стикера:\n\n$0$"
        },
    },

    "resetstickerkeywords": {
        "send_keywords": {
            "en_US": "Now send keywords of this sticker, message-by-message. They can be words or emojis. When you're "
                     "ready, /finish",
            "ru_RU": "Отправьте ключевые слова стикера отдельными сообщениями. Это могут быть слова или эмодзи. Когда "
                     "будете готовы, /finish"
        },
        "no_send_keywords": {
            "en_US": "Send us textual keywords.",
            "ru_RU": "Отправьте текстовые ключевые слова."
        },
        "send_more_keywords": {
            "en_US": "Okay! Write some more, or /finish",
            "ru_RU": "Отлично! Отправьте ещё, или /finish"
        },
        "done": {
            "en_US": "Done!",
            "ru_RU": "Готово!"
        },
    },
}


def l10n(code: str, lang: str, attrs=None) -> str:
    if attrs is None:
        attrs = []
    try:
        # 1. find the translation
        translations = texts
        for piece in code.split("."):
            translations = translations[piece]

        try:
            translation = translations[lang]
        except:
            print(f"No {lang} translation for {code}")
            translation = translations["en_US"]

        # 2. replace all attrs of translation
        for i in range(len(attrs)):
            translation = translation.replace(f"${i}$", str(attrs[i]))

        return translation
    except:
        print(f"No {code} translation")
        return code
