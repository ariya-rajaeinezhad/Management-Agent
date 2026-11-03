export const translations = {
    fa: {
        // Header
        title: 'عامل هوشمند مدیریت',
        subtitle: 'تحلیل موضوعات مدیریتی بر اساس چهار وظیفه اصلی مدیریت',

        // Tabs
        tab_new: '✨ گزارش جدید',
        tab_history: '📚 آرشیو گزارش‌ها',

        // Topic Input
        input_label: '🎯 موضوع مدیریتی خود را وارد کنید:',
        input_placeholder: 'مثلاً: برنامه‌ریزی برای راه‌اندازی یک کافی‌شاپ دانشجویی...',
        char_count: 'کاراکتر',
        generate_btn: '✨ تولید گزارش مدیریتی',
        examples: '💡 مثال‌های پیشنهادی:',

        // Loading
        loading_title: 'در حال تولید گزارش...',
        loading_step1: 'در حال ترجمه موضوع به انگلیسی...',
        loading_step2: 'در حال تحلیل مدیریتی با چهار وظیفه اصلی...',
        loading_step3: 'در حال ترجمه و ساختاردهی گزارش نهایی...',
        loading_note: 'این فرآیند معمولاً ۱۰ تا ۳۰ ثانیه طول می‌کشد',

        // Report
        report_label: '📊 گزارش مدیریتی',
        show_english: 'نمایش تحلیل انگلیسی',
        new_topic: '← موضوع جدید',
        download_md: '📥 دانلود Markdown',
        edit_title: 'ویرایش عنوان',
        save: 'ذخیره',
        cancel: 'انصراف',

        // Report Sections
        exec_summary: '📋 خلاصه مدیریتی',
        section1: 'تعریف مسئله',
        section2: 'مفروضات و محدودیت‌ها',
        section3: 'برنامه‌ریزی (Planning)',
        section4: 'سازماندهی (Organizing)',
        section5: 'هدایت و اجرا (Leading)',
        section6: 'کنترل و ارزیابی (Controlling)',
        section7: 'شاخص‌های کلیدی عملکرد',
        section8: 'ریسک‌ها و راهکارهای مقابله',
        section9: 'پیشنهادات نهایی',
        section10: 'نتیجه‌گیری',

        // History
        history_title: '📚 آرشیو گزارش‌های شما',
        history_empty: 'آرشیو خالی است',
        history_empty_desc: 'هنوز گزارشی تولید نکرده‌اید. به تب «گزارش جدید» بروید و اولین گزارش خود را بسازید!',
        view: '👁️ مشاهده',
        delete: '🗑️ حذف',
        confirm_delete: '✓ حذف',
        cancel_delete: 'انصراف',
        created: '📅 ایجاد',
        updated: '✏️ ویرایش',

        // English Analysis
        english_analysis: '🇬🇧 تحلیل داخلی به انگلیسی',
        translated_topic: 'موضوع ترجمه شده',
        structured_analysis: 'تحلیل ساختاریافته (JSON)',

        // Footer
        footer: 'پروژه درس اصول مدیریت',

        // Examples
        example1: 'برنامه‌ریزی برای راه‌اندازی یک کافی‌شاپ دانشجویی در دانشگاه',
        example2: 'مدیریت یک تیم نرم‌افزاری دورکار با ۱۰ نفر عضو',
        example3: 'راه‌اندازی یک استارتاپ فناوری با بودجه محدود',
    },

    en: {
        // Header
        title: 'AI Management Agent',
        subtitle: 'Analyzing management topics through the four fundamental functions',

        // Tabs
        tab_new: '✨ New Report',
        tab_history: '📚 Report Archive',

        // Topic Input
        input_label: '🎯 Enter your management topic:',
        input_placeholder: 'e.g., Planning to launch a student café at university...',
        char_count: 'characters',
        generate_btn: '✨ Generate Management Report',
        examples: '💡 Suggested examples:',

        // Loading
        loading_title: 'Generating report...',
        loading_step1: 'Processing your topic...',
        loading_step2: 'Analyzing with 4 management functions...',
        loading_step3: 'Structuring the final report...',
        loading_note: 'This usually takes 10-30 seconds',

        // Report
        report_label: '📊 Management Report',
        show_english: 'Show English analysis',
        new_topic: '← New Topic',
        download_md: '📥 Download Markdown',
        edit_title: 'Edit Title',
        save: 'Save',
        cancel: 'Cancel',

        // Report Sections
        exec_summary: '📋 Executive Summary',
        section1: 'Problem Definition',
        section2: 'Assumptions & Constraints',
        section3: 'Planning',
        section4: 'Organizing',
        section5: 'Leading & Execution',
        section6: 'Controlling & Evaluation',
        section7: 'Key Performance Indicators',
        section8: 'Risks & Mitigation Strategies',
        section9: 'Final Recommendations',
        section10: 'Conclusion',

        // History
        history_title: '📚 Your Report Archive',
        history_empty: 'Archive is empty',
        history_empty_desc: "You haven't generated any reports yet. Go to 'New Report' and create your first one!",
        view: '👁️ View',
        delete: '🗑️ Delete',
        confirm_delete: '✓ Delete',
        cancel_delete: 'Cancel',
        created: '📅 Created',
        updated: '✏️ Updated',

        // English Analysis
        english_analysis: '🇬🇧 English Internal Analysis',
        translated_topic: 'TRANSLATED TOPIC',
        structured_analysis: 'STRUCTURED ANALYSIS (JSON)',

        // Footer
        footer: 'Management Principles Course Project',

        // Examples
        example1: 'Planning to launch a student café at the university',
        example2: 'Managing a remote software team with 10 members',
        example3: 'Launching a tech startup with limited budget',
    }
};

export const t = (key, lang) => {
    return translations[lang]?.[key] || translations.fa[key] || key;
};