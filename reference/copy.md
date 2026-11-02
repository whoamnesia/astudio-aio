# Words

Copy is the first design decision: a headline that needs four lines cannot be rescued by typography, and a page of
slogans cannot be rescued by layout. Write the page as plain text before markup. Reply and write in the language of
the user's brief and audience (Russian sites get Russian copy with Russian typography - typography.md §7).

## Contents
1. Write the argument first
2. The two-line headline (character budget)
3. Headline shapes that work
4. Supporting line, body, buttons, navigation
5. Proof without inventing it
6. Persuasion frameworks (for landing pages and ads)
7. UX writing (product UI) - English and Russian
8. Things that read as generated

## 1. The argument
Answer in one line each: who is reading and what do they know; what this is, said the way its maker would tell a
friend; the single thing they should believe after one screen; what proves it; what they do next. Then list the page
as claims with proof, one per section:
```
1. It is a three-legged oak stool, made to order.          -> the stool, large
2. Each seat is cut from one board, so the grain is yours. -> three close-ups
3. It takes six weeks and you can follow it.               -> the stages, photographed
4. It costs 240 € and the maker delivers it.               -> price, button
```
A section with no claim is filler - delete it. The order of the argument is the order of the page.

## 2. The two-line headline
Every headline fits in **two lines or fewer at every width** (hero and section headings).
`chars per line ≈ line width ÷ (font size × k)`; k ≈ 0.40 condensed, 0.50 most faces at display size, 0.58 wide/caps.

| Where | Width | Size | Per line | Two-line budget |
|---|---|---|---|---|
| Phone 390 | 350px | 44px | ~16 | ~32 chars |
| Phone 390 | 350px | 34px | ~21 | ~42 chars |
| Tablet 768 | 690px | 64px | ~22 | ~44 chars |
| Desktop half width | 620px | 72px | ~17 | ~34 chars |
| Desktop 12-col | 1100px | 104px | ~21 | ~42 chars |
So ~32 characters (4-6 words) survives everywhere at a confident size; Russian needs ~10-15% fewer. Past that you are
writing a sentence - move the rest into the supporting line. Never fix a long headline only by shrinking it; author
the break (`<br>` + `text-wrap: balance`) and check the phone. Section headings: 2-5 words. A large statement
(manifesto line, quote) is a `<p>`/`<blockquote>` at ≤ 36px desktop / 24px phone, ≤ ~25 words.

## 3. Headline shapes
- **The name** set very large, with a one-line description beside it (studios, restaurants, hotels, people).
- **What it is**: "Furniture for small rooms." / «Мебель для маленьких кухонь».
- **The claim** a competitor could not sign: "Your bank won't do this."
- **The instruction**: verb first, short. "Understand your money."
- **The place or moment**: "Lisbon, since 1984."
Avoid: the mad-lib ("The AI-powered platform for modern teams"); tricolons; "not just X, it's Y"; "X, reimagined";
"Welcome to"; a question nobody asked; a headline that needs its colon; one styled word. Sentence case.

## 4. Supporting line, body, buttons
- **Supporting line:** one sentence, ≤ ~22 words, directly under the headline, saying concretely what it is and for
  whom - visible with the headline, never delayed by animation.
- **Body:** short paragraphs, specific nouns and real numbers ("ships in a week", not "fast delivery"; "38 seats", not
  "intimate"). If a competitor could print a sentence unchanged, sharpen or cut it. "If deleting 30% improves it,
  keep deleting."
- **Buttons:** name the action or the thing, 1-3 words: "Book a table", "See the plans", "Download for Mac". The
  primary action keeps one name everywhere (the button that says "Publish" produces a toast "Published"). One primary
  per screen; secondary is a text link. At most one arrow glyph, on the primary, if any.
- **Navigation:** wordmark, ≤ 5 single-noun links, one action.
- **Full content:** every section the visitor came for delivers it completely (the whole menu with prices, each room
  with its rate, every speaker). Thin sections are the commonest reason a clean page loses to a busier one. Where the
  brief leaves gaps, write plausible sample details and list them for the client to confirm.

## 5. Proof without inventing it
Never invent customers, named quotes, press logos, user counts, ratings, benchmarks or awards. When no proof is
supplied use what is true by construction: show the thing large; explain how it works specifically; use facts from the
brief (price, place, year, materials, what is included); a real guarantee/trial the business offers. If a testimonial
section is explicitly required and none exist, build it with plainly fictional sample content and flag it in the
report for replacement - never real names or companies.

## 6. Persuasion frameworks (landing pages, ads, CTAs)
- **Awareness stage (Schwartz)** decides the message, not the product: *unaware* → lead with the situation/story;
  *problem-aware* → name the pain precisely, then the way out; *solution-aware* → why this approach beats the others;
  *product-aware* → proof, specifics, risk reversal; *most aware* → the offer and the button. Wrong stage = dead ad.
- **Structures:** PAS (problem → agitate → solve), AIDA (attention → interest → desire → action), BAB (before → after →
  bridge), FAB (feature → advantage → benefit), 4U headline test (useful, urgent, unique, ultra-specific).
- **Angles to test** (generate several per brief, each a different reason to care): pain, desire/outcome, proof,
  identity ("for people who…"), contrarian, mechanism (how it works), urgency/scarcity (only if real), price/value.
- **Objections** (price, time, trust, complexity, past failures) get answered where they arise: FAQ of real questions,
  comparison, guarantee, a specific number.
- **Persuade-page checklist:** one named primary action, nothing competing above the fold, repeated at the close;
  proof beside each claim (or the claim is cut / marked `[needs proof]`); a real risk reversal (free plan, trial, no
  card, cancel anytime, refund) only if the business offers it; index/noindex decided (ad-only pages noindex; indexed
  pages get a real title/description and FAQPage JSON-LD for a real FAQ).

## 7. UX writing (product UI)
Words make the interface easier to understand and use - they are design content, not decoration.
- Write from the user's perspective in plain language: a user manages *notifications*, not *webhook config*.
- Active voice; controls say exactly what happens ("Save changes", not "Submit"). Destructive actions name the object
  ("Delete project") and the consequence; confirmation dialogs name the object again.
- Errors: what happened + why (if useful) + what to do. Never blame, never vague, never apologise theatrically.
  "File is too large. Maximum 25 MB." Different errors get different headlines.
- Empty states: what this space is for + the first action. Loading states end with an ellipsis: "Saving…".
- One term per concept across all screens. Numerals for counts ("8 deployments").
- **Russian UI:** buttons are infinitive verbs - Сохранить, Отправить, Удалить проект; cancel is always «Отмена»
  (not «Отменить» - that is undo); Скачать (download) vs Загрузить (upload); Войти / Выйти / Зарегистрироваться;
  «Подробнее» only as a secondary link. Errors: «Не удалось сохранить файл. Проверьте подключение», «Укажите email»,
  «Файл слишком большой. Максимум — 25 МБ». Prefer «Мои заказы» style. Avoid канцелярит: «осуществить» → «сделать»,
  «произвести оплату» → «оплатить», «в настоящее время» → «сейчас», «данный» → «этот», «является» → dash or rephrase.

## 8. Things that read as generated
Genre verbs/adjectives (unlock, supercharge, seamless, elevate, effortless, cutting-edge, all-in-one); RU штампы
(инновационный, уникальное решение, индивидуальный подход, широкий спектр); labels pretending to be editorial
("Field notes", "Our philosophy"); furniture text (coordinates, "Est. 2024", "Scroll to explore", middle-dot strings,
"Available for work ●"); the em dash as a habit; captions that narrate the design; "Step 1 / Phase 02" labels; three
parallel items everywhere (use the number the content has).
