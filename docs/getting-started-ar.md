# البدء باستخدام OpenSelfHosting Skills

تضم هذه المكتبة مهارات قابلة لإعادة الاستخدام لوكلاء الذكاء الاصطناعي: فهم المشاريع، تصحيح الأخطاء، مراجعة الكود والأمان، الاختبارات، التوثيق، وتجهيز الإصدارات. تعتمد المهارات على تنسيق `SKILL.md` المفتوح، لكن طريقة التثبيت والمسارات تختلف حسب الوكيل.

## التثبيت

تأكد من توفر Node.js وnpm/npx، ثم نفّذ من مجلد المشروع:

```bash
# عرض المهارات المتاحة
npx skills add OpenSelfHosting/skills --list

# تثبيت مهارة تصحيح الأخطاء
npx skills add OpenSelfHosting/skills --skill systematic-debugging

# تثبيت مهارة مراجعة الكود لوكيل محدد يدعمه CLI
npx skills add OpenSelfHosting/skills --skill code-review --agent claude-code

# تثبيت عام للمستخدم، بحسب دعم الأداة
npx skills add OpenSelfHosting/skills --skill codebase-onboarding -g
```

راجع `npx skills add --help` لمعرفة خيارات إصدار CLI الذي تستخدمه. إذا لم يكن المستودع منشورًا بعد على GitHub، استبدل `OpenSelfHosting/skills` باسم المالك والمستودع الفعليين بعد النشر.

## اختيار المهارة

- `codebase-onboarding`: تعرّف على مشروع غير مألوف قبل تعديله.
- `systematic-debugging`: أعد إنتاج الخطأ، وابحث عن السبب الجذري، ثم تحقق من الإصلاح.
- `code-review`: راجع التغييرات بحثًا عن عيوب فعلية ومخاطر مهمة.
- `test-driven-changes`: اربط تغييرات السلوك باختبارات مفيدة.
- `ci-failure-triage`: حلّل فشل CI/CD.
- `security-review`: راجع الأمن بشكل دفاعي.
- `dependency-health`: افحص تحديثات التبعيات ومخاطرها.
- `database-migration-review`: راجع تغييرات قاعدة البيانات والترحيلات.
- `api-contract-review`: راجع توافق واجهات API وعقودها.
- `docs-maintenance`: حدّث التوثيق استنادًا إلى الكود الفعلي.
- `pull-request-prep`: جهّز طلب دمج واضحًا وقابلًا للمراجعة.
- `release-readiness`: قيّم جاهزية الإصدار ومخاطره.
- `skill-authoring`: أنشئ مهارات جديدة واختبرها.
- `research-with-sources`: أنجز بحثًا مدعومًا بمصادر موثوقة.

## قبل الاستخدام

المهارات إرشادات لوكيل الذكاء الاصطناعي وليست ضمانًا للصحة أو بديلًا عن الاختبارات. راجع التعليمات والسكربتات قبل تثبيتها، ولا تمنح الوكيل صلاحيات لا يحتاجها. المهارات لا توفر أدوات غير موجودة في الوكيل نفسه ولا تتجاوز صلاحياته أو سياسات السلامة.

للمساهمة، ابدأ من [دليل المساهمة](../CONTRIBUTING.md) و[دليل إنشاء المهارات](skill-authoring-guide.md).
