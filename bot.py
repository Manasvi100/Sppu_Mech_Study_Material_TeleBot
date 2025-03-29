from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup  # type: ignore
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes  # type: ignore

TOKEN = "7461766688:AAEbW-foFMOxN6iR5ZqBX55e3TkmyZbklb0"

SUBJECTS = {
    "SE_SEM3": ["Solid Mechanics", "Solid Modeling and Drafting", "Engineering Thermodynamics","Engineering Materials and Metallurgy","Electrical and Electronics Engineering "],
    "SE_SEM4": ["Engineering Mathematics - III ", "Kinematics of Machinery ", " Applied Thermodynamics","Fluid Mechanics","Manufacturing Processes","Machine Shop"],
    "TE_SEM5": ["Numerical & Statistical Methods", "Heat & Mass Transfer", "Design of Machine Elements","Mechatronics","Advanced Forming & Joining Processes","Machining Science & Technology"],
    "TE_SEM6": ["Artificial Intelligence &Machine Learning", "Computer Aided Engineering ", "Design of Transmission Systems","Composite Materials ","Surface Engineering"],
    "BE_SEM7": ["Heating Ventilation Air-Conditioning and Refrigeration", "Dynamics of Machinery ","Turbomachinery","Automobile Design ","Design of Heat Transfer Equipments","Modern Machining Processes ","Industrial Engineering","Internet of Things","Computational Fluid Dynamics","Product Design and Development","Experimental Methods in Thermal Engineering ","Additive Manufacturing","Operations Research","Augmented Reality and Virtual Reality "],
    "BE_SEM8": ["Computer Integrated Manufacturing ", "Energy Engineering","Quality and Reliability Engineering ","Energy Audit  and Management","Manufacturing Systems and Simulation","Engineering Economics and Financial Management","Organizational Informatics ","Computational Multi Body Dynamics","Process Equipment Design","Renewable Energy Technologies","Automation and  Robotics","Industrial Psychology and Organizational Behavior","Electrical and Hybrid Vehicle"]
}

SYLLABUS_LINKS = {
    "SE_SEM3": "https://drive.google.com/file/d/1ahcujj4-8mn15Dow43bLBCXxoRbpe0JE/view?usp=drive_link",
    "SE_SEM4": "https://drive.google.com/file/d/1jp62KlhwRAhmrfiJNxJBOqMjpuegNXPr/view?usp=drive_link",
    "TE_SEM5": "https://drive.google.com/file/d/12K1ZplGsYrNYVvdFXvKwiYIVU6bgoaIj/view?usp=drive_link",
    "TE_SEM6": "https://drive.google.com/file/d/10iChux1qBVmaQRWnkEtvkjlQ3umNePDn/view?usp=drive_link",
    "BE_SEM7": "https://drive.google.com/file/d/1T3qYn3gohwNRqU9zc3vRprwe2GFHzeCa/view?usp=drive_link",
    "BE_SEM8": "https://drive.google.com/file/d/1tKPaTahlYlvmQChY0hrzUlBQB5rFggje/view?usp=drive_link"
}

QUESTION_PAPERS = {
    "SE_SEM3": {
        "Solid Mechanics": "https://drive.google.com/file/d/1bFnza8vW0erI-WXr0796EMel4PJWkTHS/view?usp=drive_link",
        "Solid Modeling and Drafting": "https://drive.google.com/file/d/136940ZL4gbxv9iiPpWUqsDUYnn07GjXV/view?usp=drive_link",
        "Engineering Thermodynamics": "https://drive.google.com/file/d/136_ipXWynu8WEq6jRcuGtQuPSiw6tt0X/view?usp=drive_link",
        "Engineering Materials and Metallurgy": "https://drive.google.com/file/d/13Gz-tqRJAFfHW0JTcNwMVTGiIUbreu86/view?usp=drive_link",
        "Electrical and Electronics Engineering ": "https://drive.google.com/file/d/136dvvW8JsJHA8oPFlGMjAa4t8LBud3A-/view?usp=drive_link",
    },
    
    "SE_SEM4": {
        "Engineering Mathematics - III ": "https://drive.google.com/file/d/13-62B1zVzRy8M1n8d_ALQRPSVCTkWmwY/view?usp=drive_link",
        "Kinematics of Machinery ": "https://drive.google.com/file/d/12yRcyHBGAGP1AK7CQC4HYFELOQ-mgqWw/view?usp=drive_link", 
       "Applied Thermodynamics": "https://drive.google.com/file/d/13-wpQSSryM6OhdqA4hvf4Q4a_2mQY2Rs/view?usp=drive_link",
        "Fluid Mechanics": "https://drive.google.com/file/d/130B7QdikD8GM5H89rQ3FUjYRflKQZ_k8/view?usp=drive_link",
        "Manufacturing Processes": "https://drive.google.com/file/d/130lnEuRQEmM0KnyJs9Z_UmDmneVnnGWr/view?usp=drive_link",
        
    },
    
    "TE_SEM5": {
        "Numerical & Statistical Methods": "https://drive.google.com/file/d/12lJ-Xepqp9b7vXPYZjkJ7KblbjV4HySv/view?usp=drive_link", 
        "Heat & Mass Transfer": "https://drive.google.com/file/d/12pSZ9vHLomaasfP4wlQCfwGR4GCk77Z9/view?usp=drive_link",
        "Design of Machine Elements": "https://drive.google.com/file/d/12rMKBEVFWhyCn14C4JmP1cu4J2REeopj/view?usp=drive_link",
        "Mechatronics": "https://drive.google.com/file/d/12dv5Lo2tWTwGz9UVILN1V5HNyb-z5sTK/view?usp=drive_link",
        "Machining Science & Technology": "https://drive.google.com/file/d/12eqSffyGfE_b-BQmZZasn1FgC3t8CGYC/view?usp=drive_link",
    },
    
    "TE_SEM6": {
        
        "Artificial Intelligence &Machine Learning": "https://drive.google.com/file/d/11wS6JR00jE3d506-yMcrO2SYdl4KfpgW/view?usp=drive_link", 
        "Computer Aided Engineering ": "https://drive.google.com/file/d/11e9C-_hYBHMBqR3T-m7Xhvkl6fr7bWt-/view?usp=drive_link", 
        "Design of Transmission Systems": "https://drive.google.com/file/d/11e_ehcwctgnR7TFk1ONgP0KyUAAhaF9y/view?usp=drive_link",
        "Composite Materials ": "https://drive.google.com/file/d/11f4bLc3OsKuKs5MG2p-uiNyv3JzasbsC/view?usp=drive_link",
        "Surface Engineering": "https://drive.google.com/file/d/11fICjC6hKYFmlLZYnfzWwvDC2ThWftBf/view?usp=drive_link",
        
    },
    
    "BE_SEM7": {
       
       "Heating Ventilation Air-Conditioning and Refrigeration":"https://drive.google.com/file/d/10pmrIuCn-VhkhBNmbl8n_NgTRlvA6pV7/view?usp=drive_link", 
       "Dynamics of Machinery ": "https://drive.google.com/file/d/10tauQkVgrXtXdSBHMRYzswkDxAsbUDsa/view?usp=drive_link",
       "Turbomachinery": "https://drive.google.com/file/d/110xdgeZSqkKxggAuBrrIZRdIbAnrw4j3/view?usp=drive_link",
       "Automobile Design": "https://drive.google.com/file/d/11KLpHkkeWKjg5IqPjX_iZIfkfOjMGLvw/view?usp=drive_link",
       "Modern Machining Processes ": "https://drive.google.com/file/d/11N4uw9fmsjSK2K2km9EbT94COAmKNsuG/view?usp=drive_link",
       "Industrial Engineering": "https://drive.google.com/file/d/11OF8bZai_paxVsXgrBf_WHWK2LiZS6Wz/view?usp=drive_link",
       "Product Design and Development": "https://drive.google.com/file/d/11PmqaVXKgwQlCZT4PUbEkzOmXTY1sdeh/view?usp=drive_link",
       "Operations Research": "https://drive.google.com/file/d/11aBo6SupEMrYI7NpBz_SRol1Tc_dIVsD/view?usp=drive_link",
       
    },
    
    "BE_SEM8": {
        
        "Computer Integrated Manufacturing ": "https://drive.google.com/file/d/1-C8sOyJDvX_VaKxhwrVnqPavKID3OJxd/view?usp=drive_link", 
        "Energy Engineering": "https://drive.google.com/file/d/10NOVGK4Aewuq122WdpC514jwA_fNNgdX/view?usp=drive_link",
        "Quality and Reliability Engineering ": "https://drive.google.com/file/d/10WeMO0-YAen4XgkJuh6f03aL9-wqZqAI/view?usp=drive_link",
        "Energy Audit  and Management": "https://drive.google.com/file/d/10Zuj3o7rDft_iAr-jMoxGttN1Zpfi9Go/view?usp=drive_link",
        "Process Equipment Design": "https://drive.google.com/file/d/10dUfNNAXjFIdOaTTcMKXkBH8XOFnNHLX/view?usp=drive_link",
        "Renewable Energy Technologies": "https://drive.google.com/file/d/10f61lXPubVa2wxVzfHtqXlKCPdF7NtCG/view?usp=drive_link",
        "Electrical and Hybrid Vehicle": "https://drive.google.com/file/d/10fcuP-Tc_kX2J9ZMrEjCV9M6pHDv5Lvl/view?usp=drive_link",
        
    },
   
}

NOTES={
   
   "SE_SEM3": {
        "Solid Mechanics": "https://drive.google.com/file/d/1bFnza8vW0erI-WXr0796EMel4PJWkTHS/view?usp=drive_link",
        "Solid Modeling and Drafting": "https://drive.google.com/file/d/136940ZL4gbxv9iiPpWUqsDUYnn07GjXV/view?usp=drive_link",
        "Engineering Thermodynamics": "https://drive.google.com/file/d/136_ipXWynu8WEq6jRcuGtQuPSiw6tt0X/view?usp=drive_link",
        "Engineering Materials and Metallurgy": "https://drive.google.com/file/d/13Gz-tqRJAFfHW0JTcNwMVTGiIUbreu86/view?usp=drive_link",
        "Electrical and Electronics Engineering ": "https://drive.google.com/file/d/136dvvW8JsJHA8oPFlGMjAa4t8LBud3A-/view?usp=drive_link",
    },
   
    
    
    
    
}



async def show_year_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Second Year (SE)", callback_data='SE')],
        [InlineKeyboardButton("Third Year (TE)", callback_data='TE')],
        [InlineKeyboardButton("Final Year (BE)", callback_data='BE')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_message = """✨ Welcome, Team SPPU Mechanical Engineering! ✨


📚 *Presenting: SPPU Mechanical Study Bot* 📚

Stay updated & learn easily with our resources!

========================

🔗 *SPPU Mechanical Group Links:*  
📄 *Telegram channel for notes:*  
https://t.me/sppusemech23

💬 *Telegram group for doubts & discussions:*  
https://t.me/sppupuneuniversity

========================

👤 *Admin Contact:*  

• Telegram:  [@mech_nivednikam_dpu](https://t.me/mech_nivednikam_dpu)

• Instagram: [nikam_nived_12](https://www.instagram.com/nikam_nived_12?igsh=MW94d21tY2FqYWd6eA==)

========================

✅ *Please select your Year to continue:*
"""

    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def show_sem_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, year):
    keyboard = []

    if year == 'SE':
        keyboard = [
            [InlineKeyboardButton("Semester 3", callback_data=f'{year}_SEM3')],
            [InlineKeyboardButton("Semester 4", callback_data=f'{year}_SEM4')],
            [InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_YEAR')]
        ]
    elif year == 'TE':
        keyboard = [
            [InlineKeyboardButton("Semester 5", callback_data=f'{year}_SEM5')],
            [InlineKeyboardButton("Semester 6", callback_data=f'{year}_SEM6')],
            [InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_YEAR')]
        ]
    elif year == 'BE':
        keyboard = [
            [InlineKeyboardButton("Semester 7", callback_data=f'{year}_SEM7')],
            [InlineKeyboardButton("Semester 8", callback_data=f'{year}_SEM8')],
            [InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_YEAR')]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.edit_message_text(
        text=f"✅ You selected {year}. Now select your Semester:",
        reply_markup=reply_markup
    )


async def show_syllabus_subject_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    year = context.user_data['year']
    sem = context.user_data['semester']
    keyboard = [
        [InlineKeyboardButton("Syllabus", callback_data='SYLLABUS')],
        [InlineKeyboardButton("Subjects", callback_data='SUBJECTS')],
        [InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_SEM')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.edit_message_text(
        text=f"✅ You selected {year} {sem}. Now choose an option:",
        reply_markup=reply_markup
    )


async def show_subject_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    year = context.user_data['year']
    sem = context.user_data['semester']
    key = f"{year}_{sem}"
    subjects = SUBJECTS.get(key, [])

    keyboard = [
        [InlineKeyboardButton(subj, callback_data=f"SUBJECT_{subj}")]
        for subj in subjects
    ]
    keyboard.append([InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_SYLLABUS_SUBJECT')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.edit_message_text(
        text="📚 Choose your subject:",
        reply_markup=reply_markup
    )


async def show_material_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subject = context.user_data['subject']
    keyboard = [
        [InlineKeyboardButton("📄 Question papers", callback_data='NOTES_PAPERS')],
        [InlineKeyboardButton("📚 Books(Any Publication /Decode/Easy)", callback_data='BOOKS_PAPERS')],
        [InlineKeyboardButton("❗📄 Notes +imp question +question bank& micro", callback_data='IMP_QUE')],
        [InlineKeyboardButton("🔙 Back", callback_data='BACK_TO_SUBJECTS')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.edit_message_text(
        text=f"📌 Selected Subject: {subject}\nChoose what you want:",
        reply_markup=reply_markup
    )


async def button_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ['SE', 'TE', 'BE']:
        context.user_data['year'] = data
        await show_sem_menu(update, context, data)
        return

    if data == 'BACK_TO_YEAR':
        await query.edit_message_text("🔙 Going back to Year selection...")
        await show_year_menu(update, context)
        return

    if data == 'BACK_TO_SEM':
        year = context.user_data['year']
        await show_sem_menu(update, context, year)
        return

    if data == 'BACK_TO_SYLLABUS_SUBJECT':
        await show_syllabus_subject_menu(update, context)
        return

    if data == 'BACK_TO_SUBJECTS':
        await show_subject_menu(update, context)
        return

    if '_SEM' in data:
        year, sem = data.split('_')
        context.user_data['year'] = year
        context.user_data['semester'] = sem
        await show_syllabus_subject_menu(update, context)
        return

    if data == 'SYLLABUS':
        year = context.user_data['year']
    sem = context.user_data['semester']
    key = f"{year}_{sem}"
    syllabus_link = SYLLABUS_LINKS.get(key)

    if syllabus_link:
        await query.edit_message_text(
            text=f"📄 Here is the syllabus for {year} {sem}:\n\n{syllabus_link}"
        )
    else:
        await query.edit_message_text(
            text=f"❗ Syllabus file not available for {year} {sem}."
        )
    return


    if data == 'SUBJECTS':
        await show_subject_menu(update, context)
        return

    if data.startswith('SUBJECT_'):
        subject = data.replace('SUBJECT_', '')
        context.user_data['subject'] = subject
        await show_material_options(update, context)
        return

    if data == 'NOTES_PAPERS':
        year = context.user_data['year']
    sem = context.user_data['semester']
    subject = context.user_data['subject']

    key = f"{year}_{sem}"
    file_link = QUESTION_PAPERS.get(key, {}).get(subject)

    if file_link:
        await query.edit_message_text(
            text=f"📄 Here are the Question Papers for {subject} ({year} {sem}):\n{file_link}"
        )
    else:
        await query.edit_message_text(
            text=f"❗ Question Papers for {subject} ({year} {sem}) are not available."
        )
    return



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    greetings = ["hi", "hello", "hey", "first year", "second year", "third year", "final year"]
    year = context.user_data.get('year')
    sem = context.user_data.get('semester')

    if not year or not sem:
        if any(word in query for word in greetings):
            await show_year_menu(update, context)
            return
        else:
            await update.message.reply_text(
                "❗ Please select your Year first by typing 'Hi' or 'Hello'."
            )


def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", show_year_menu))
    app.add_handler(CallbackQueryHandler(button_selected))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
