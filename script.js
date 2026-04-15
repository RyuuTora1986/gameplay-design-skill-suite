const stageData = {
  en: [
    {
      name: "Input Normalizer",
      short: "stabilize constraints",
      title: "Input Normalizer",
      body:
        "Converts fuzzy input into usable design constraints, target player, emotional goal, platform bounds, and production pressure before the rest of the pipeline starts pretending details are settled.",
      points: [
        "stops vague inspiration from leaking into later stages as fake certainty",
        "defines who the player is, what matters, and what must be avoided",
        "creates a shared constraint frame before loop design begins",
      ],
    },
    {
      name: "Fantasy Loop Designer",
      short: "lock the repeatable fun",
      title: "Fantasy Loop Designer",
      body:
        "Locks the player promise, identity fantasy, core action, and micro-to-long loop structure so the package has a real repeatable-fun hypothesis instead of genre wallpaper.",
      points: [
        "identifies the strongest repeatable action",
        "tests whether the promise still works without theme skin",
        "prevents reward-only loops from pretending they are gameplay depth",
      ],
    },
    {
      name: "Pacing And Structure",
      short: "build time-layer pressure",
      title: "Pacing And Structure",
      body:
        "Builds 5-second, 30-second, 3-minute, and 15-minute layers to prove the loop survives contact with real session flow, early highs, and replay pull.",
      points: [
        "forces timing discipline instead of hiding weak loops behind progression",
        "surfaces early frustration points while the scope is still cheap to change",
        "supports explicit loop-back if pacing reveals upstream weakness",
      ],
    },
    {
      name: "World And Narrative Weaver",
      short: "wrap identity around play",
      title: "World And Narrative Weaver",
      body:
        "Wraps the gameplay spine with world rule, conflict, and act pressure without letting lore become a substitute for readable player decisions.",
      points: [
        "narrative must change pressure, target, or reward expectation",
        "keeps worldbuilding in service of play, not in competition with it",
        "protects the pipeline from theme-first drift",
      ],
    },
    {
      name: "System Weaver And Scope Cutter",
      short: "keep what earns its cost",
      title: "System Weaver And Scope Cutter",
      body:
        "Maps core systems, secondary systems, resource flow, and first-version cuts so the package preserves the player promise without exploding production cost.",
      points: [
        "separates core from optional systems",
        "makes MVP keep / later / cut visible and defensible",
        "names cost-heavy danger zones before implementation begins",
      ],
    },
    {
      name: "Coding Handoff Compiler",
      short: "turn design into runtime shape",
      title: "Coding Handoff Compiler",
      body:
        "Compiles the locked gameplay package into scene, UI, object, state, variable, and event structures that downstream spec and coding agents can consume directly.",
      points: [
        "bridges design language into runtime shape",
        "defines placeholder strategy and prototype acceptance",
        "reduces redesign burden on implementation agents",
      ],
    },
  ],
  "zh-CN": [
    {
      name: "输入归一化",
      short: "先把约束钉死",
      title: "输入归一化",
      body:
        "把模糊灵感压成可执行约束，先锁目标玩家、情绪目标、平台边界和开发压力，再进入后续阶段，避免整条链路假装细节已经成立。",
      points: [
        "阻断“模糊想法”在后续阶段伪装成确定事实",
        "明确谁在玩、什么最重要、哪些方向必须避开",
        "在循环设计前先建立共享约束框架",
      ],
    },
    {
      name: "幻想循环设计",
      short: "锁住可重复乐趣",
      title: "幻想循环设计",
      body:
        "锁定玩家承诺、身份幻想、核心动作和短中长循环结构，让方案真正围绕可重复乐趣成立，而不是只靠题材皮肤撑场面。",
      points: [
        "找出最强的可重复动作",
        "验证去掉题材包装后承诺是否仍然成立",
        "防止纯奖励循环伪装成玩法深度",
      ],
    },
    {
      name: "节奏与结构",
      short: "建立时间层压力",
      title: "节奏与结构",
      body:
        "把 5 秒、30 秒、3 分钟、15 分钟这些时间层压出来，验证核心循环在真实会话流、早期爽点和再来一局动力下是否还能站住。",
      points: [
        "逼迫团队面对时序问题，而不是用成长系统掩盖弱循环",
        "在成本还低的时候暴露前期挫败点",
        "如果节奏暴露上游问题，允许显式回环返修",
      ],
    },
    {
      name: "世界观与叙事编织",
      short: "让叙事服务玩法",
      title: "世界观与叙事编织",
      body:
        "为玩法主干包上世界规则、冲突和章节推进，但不允许设定文本替代玩家决策，也不让 lore 抢走核心体验的位置。",
      points: [
        "叙事必须改变压力、目标或奖励预期",
        "世界观只能为玩法服务，不能和玩法争主角",
        "防止整条链路滑向“题材优先”",
      ],
    },
    {
      name: "系统编织与范围切割",
      short: "保留值回票价的部分",
      title: "系统编织与范围切割",
      body:
        "把核心系统、次级系统、资源流向和首版砍法一起钉住，既守住玩家承诺，也避免制作成本在中途失控。",
      points: [
        "把核心系统和可选系统明确拆开",
        "让 MVP 保留 / 后置 / 砍掉始终可见且可辩护",
        "在实现前就标出高成本危险区",
      ],
    },
    {
      name: "编码交接编译器",
      short: "翻译成运行时结构",
      title: "编码交接编译器",
      body:
        "把已锁定的玩法包编译成场景、UI、对象、状态、变量和事件结构，让下游策划文档与编码代理可以直接接手。",
      points: [
        "把设计语言翻译成运行时结构",
        "定义占位策略和原型验收标准",
        "降低实现阶段重新发明设计的负担",
      ],
    },
  ],
};

const copy = {
  en: {
    htmlLang: "en",
    title: "Gameplay Design Skill Suite",
    description:
      "A loud, orchestrator-first gameplay design workflow for Codex. Turn raw game ideas into validated gameplay packages and Chinese production-ready specs.",
    brandTagline: "orchestrator-first for Codex",
    nav: {
      pipeline: "Pipeline",
      caseStudy: "Case",
      offers: "Offers",
      faq: "FAQ",
    },
    repoDocs: "Repo Docs",
    hero: {
      eyebrow: "Gameplay design ops for chaos-resistant builders",
      outline: "CHAOS IN.",
      solid: "SPEC OUT.",
      summary:
        "A cartoon-loud, structure-heavy workflow that takes raw game concepts, locks direction, forces stage order, cuts scope early, and lands on a gameplay package your AI coding stack can actually continue from.",
      primary: "Open GitHub Repo",
      secondary: "See The Pipeline",
      signals: [
        "8 coordinated skills",
        "1 orchestrator-first entry",
        "validated gyro-battle example",
        "Chinese production-ready spec output",
      ],
      stageLabel: "Cover Art // Live Workflow",
      stickers: ["LOCK DIRECTION", "CUT SCOPE", "SHIP THE PACKAGE"],
      marquee: [
        "GAMEPLAY-DESIGN-ORCHESTRATOR",
        "FUN-SOURCE JUDGMENT",
        "PACING PRESSURE",
        "MVP KEEP / CUT",
        "CODING HANDOFF",
        "VALIDATED EXAMPLE",
      ],
    },
    pipeline: {
      kicker: "The pipeline is the product",
      title: "No random prompt soup. No stage skipping.",
      body:
        'The strongest selling point here is not "good writing." It is workflow ownership. One orchestrator. Ordered stages. Explicit loop-backs. Downstream-ready packaging.',
      summaryLabel: "Current highlighted stage",
    },
    caseStudy: {
      kicker: "Validated example",
      title: "Gyro-battle web game, from direction lock to full spec.",
      windowTitle: "gyro-battle/final-package",
      windowLines: [
        "chosen direction: Arena knock-out combat",
        "strongest promise: land one perfect hit and swing the round",
        "biggest scope risk: unreadable physics becomes random noise",
        "loop-back count: 2",
        "output: package + review notes + spec + task bundle",
        "validation: package passed / spec passed",
      ],
      tag: "Why this example matters",
      copyTitle: "It proves the workflow can survive contact with a real game concept.",
      copyBody:
        "The included gyro-battle sample is not just a pretty mockup. It shows candidate direction selection, pacing corrections, scope cuts, system indexes, prototype acceptance, and downstream chapter-level tasking.",
      bullets: [
        {
          title: "Candidate A vs B",
          body: "Arena combat won. Deep parts/economy lost for scope reasons.",
        },
        {
          title: "Revision pressure",
          body: "Pacing and system stages forced loop-backs before the spec layer.",
        },
        {
          title: "Downstream packaging",
          body: "The result carries scenes, UI, rules, tasks, QA, and delivery mapping.",
        },
      ],
    },
    compare: {
      kicker: "Positioning",
      title: "Built for design geeks, not prompt tourists.",
      badLabel: "Generic prompt packs",
      badList: [
        "start with vibes and genre labels",
        "no owner for stage order",
        "easy to bloat scope",
        "beautiful prose, weak handoff",
        "no proof beyond screenshots",
      ],
      goodLabel: "Gameplay Design Skill Suite",
      goodList: [
        "orchestrator owns the workflow",
        "downstream stages stay ordered",
        "MVP keep / cut stays visible",
        "coding handoff is part of the chain",
        "validators and example included",
      ],
    },
    offers: {
      kicker: "Commercial path",
      title: "Public showcase outside. Paid leverage inside.",
      body:
        "This repo is positioned as a source-available showcase, not a free-for-all open-source giveaway. The monetization logic is licensing plus enablement, not pretending this is already a SaaS.",
      cards: [
        {
          tier: "Starter Adaptation",
          price: "$490+",
          body: "For solo builders and consultants testing the workflow in a real project.",
          list: [
            "single-buyer commercial path",
            "basic onboarding pack",
            "one target adaptation pass",
          ],
        },
        {
          tier: "Team Enablement",
          price: "$2.4K+",
          body: "For small studios that want an internal AI-assisted pre-production pipeline.",
          list: [
            "team commercial license path",
            "terminology alignment",
            "custom example package",
          ],
        },
        {
          tier: "Custom Pipeline Build",
          price: "$8K+",
          body: "For studios and agencies that want genre-specific, branded, or white-label variants.",
          list: [
            "custom skill edits",
            "revised validators",
            "deployment and rollout support",
          ],
        },
      ],
    },
    faq: {
      kicker: "Sharp questions",
      title: "FAQ for people who actually care about workflow integrity.",
      items: [
        {
          q: "Is this open source?",
          a: "No. It is public for evaluation and discovery, but commercial reuse and redistribution are intentionally protected.",
        },
        {
          q: "Can I trigger the stage skills one by one?",
          a: "Normally, no. The correct operating model is orchestrator-first. Stage skills are designed as controlled internal steps.",
        },
        {
          q: "Does this automatically make a shippable game?",
          a: "No. It compresses pre-production ambiguity and produces stronger handoff materials. It does not replace implementation, tuning, or production judgment.",
        },
        {
          q: "Why is the final spec in Chinese?",
          a: "Because the current downstream production target is a Chinese execution format. The workflow logic itself is broader than the language target.",
        },
      ],
    },
    cta: {
      kicker: "Final CTA",
      title: "If your game-design workflow still feels like prompt roulette, fix the topology first.",
      body:
        "Clone the repo, inspect the example, validate the outputs, then package the suite into your own Codex runtime or studio workflow.",
      primary: "View Repository",
      secondary: "Read Commercial Offers",
    },
  },
  "zh-CN": {
    htmlLang: "zh-CN",
    title: "Gameplay Design Skill Suite | 中文",
    description:
      "一套面向 Codex 的 orchestrator-first 游戏设计工作流。把原始游戏想法压缩成经过验证的玩法包，并继续展开为中文生产级策划案。",
    brandTagline: "面向 Codex 的 orchestrator-first 工作流",
    nav: {
      pipeline: "流程",
      caseStudy: "案例",
      offers: "商业化",
      faq: "问答",
    },
    repoDocs: "仓库文档",
    hero: {
      eyebrow: "给不想靠运气做游戏设计的人",
      outline: "灵感进来。",
      solid: "规格出去。",
      summary:
        "这是一套张力很强、结构很硬的工作流。它把原始游戏概念先锁方向、强制阶段顺序、提前切范围，最后落成一份你的 AI 编码链路真能继续接手的玩法设计包。",
      primary: "打开 GitHub 仓库",
      secondary: "查看完整流程",
      signals: [
        "8 个协同技能",
        "1 个 orchestrator 总入口",
        "已验证 gyro-battle 示例",
        "输出中文生产级策划文档",
      ],
      stageLabel: "封面画面 // 实战工作流",
      stickers: ["先锁方向", "先切范围", "再交付玩法包"],
      marquee: [
        "玩法设计总控",
        "乐趣来源判断",
        "节奏压力校准",
        "MVP 保留 / 删减",
        "编码交接",
        "带验证示例",
      ],
    },
    pipeline: {
      kicker: "真正的产品是这条流程",
      title: "不是提示词大杂烩，也不是想跳哪步就跳哪步。",
      body:
        "这里最值钱的不是“写得好看”，而是流程所有权。一个 orchestrator。严格的阶段顺序。显式回环。可直接下游接手的打包结果。",
      summaryLabel: "当前高亮阶段",
    },
    caseStudy: {
      kicker: "已验证案例",
      title: "Gyro-battle 网页游戏：从方向锁定一路推到完整规格。",
      windowTitle: "gyro-battle/final-package",
      windowLines: [
        "选定方向：竞技场击飞对战",
        "最强承诺：一记完美命中就能扭转整局",
        "最大范围风险：物理反馈失控后会变成随机噪音",
        "回环修订次数：2",
        "产物：玩法包 + 复盘记录 + 完整规格 + 任务集",
        "验证状态：玩法包通过 / 规格通过",
      ],
      tag: "这个案例为什么重要",
      copyTitle: "它证明这条工作流能扛住真实游戏概念，而不是只会做展示页。",
      copyBody:
        "内置的 gyro-battle 样例不是漂亮截图而已。它完整展示了候选方向筛选、节奏修正、范围裁剪、系统索引、原型验收，以及下游章节级任务拆解。",
      bullets: [
        {
          title: "候选方向对决",
          body: "竞技场对战被保留，深度部件与经济系统因范围压力被砍掉。",
        },
        {
          title: "回环压力真实存在",
          body: "节奏与系统阶段在进入规格层之前就强制触发返工。",
        },
        {
          title: "下游交付完整",
          body: "最终结果携带场景、UI、规则、任务、QA 与交付映射。",
        },
      ],
    },
    compare: {
      kicker: "定位",
      title: "这是给真正在乎设计结构的人，不是给提示词游客的。",
      badLabel: "通用提示词包",
      badList: [
        "从题材和氛围词起步",
        "没有阶段顺序负责人",
        "范围膨胀非常容易",
        "文字很漂亮，交接很虚",
        "除了截图没有证明",
      ],
      goodLabel: "Gameplay Design Skill Suite",
      goodList: [
        "由 orchestrator 接管流程",
        "下游阶段顺序保持严格",
        "MVP 保留 / 删减全程可见",
        "编码交接是链路内建部分",
        "自带验证器与完整样例",
      ],
    },
    offers: {
      kicker: "商业路径",
      title: "外面是公开展示，里面才是收费杠杆。",
      body:
        "这个仓库的定位是 source-available 展示资产，不是随手送人的开源礼包。真正的变现逻辑是授权与落地赋能，而不是假装它已经是一款 SaaS。",
      cards: [
        {
          tier: "单人适配版",
          price: "$490+",
          body: "面向独立开发者和顾问，用于把这套流程第一次接到真实项目里。",
          list: [
            "单买家商业使用路径",
            "基础上手包",
            "一次目标项目适配",
          ],
        },
        {
          tier: "团队落地版",
          price: "$2.4K+",
          body: "面向小团队，希望把 AI 辅助前期策划流程真正放进内部生产线。",
          list: [
            "团队商业授权路径",
            "术语与流程对齐",
            "定制案例包",
          ],
        },
        {
          tier: "定制流程构建",
          price: "$8K+",
          body: "面向工作室与服务商，需要行业化、品牌化或白标版本时使用。",
          list: [
            "定制技能修改",
            "验证器重写",
            "部署与 rollout 支持",
          ],
        },
      ],
    },
    faq: {
      kicker: "尖锐问题",
      title: "给真正关心工作流完整性的人准备的 FAQ。",
      items: [
        {
          q: "这是开源的吗？",
          a: "不是。它对外公开是为了评估和发现，不是为了放开商业复用或二次分发。",
        },
        {
          q: "我能不能把中间阶段一个个单独触发？",
          a: "通常不行。正确操作模型是 orchestrator-first，中间阶段应被视为受控内部步骤。",
        },
        {
          q: "它会自动帮我做出可上线的游戏吗？",
          a: "不会。它解决的是前期模糊与交接质量问题，不替代实现、调优和真实制作判断。",
        },
        {
          q: "为什么最终规格是中文？",
          a: "因为当前下游生产目标就是中文执行文档格式，但整套工作流逻辑本身并不只服务中文场景。",
        },
      ],
    },
    cta: {
      kicker: "最后一步",
      title: "如果你的游戏设计流程还像抽提示词彩票，先修拓扑，再谈产出。",
      body:
        "先 clone 仓库，拆读案例，验证输出，再把这套技能链打包进你自己的 Codex 运行时或工作室流程里。",
      primary: "查看仓库",
      secondary: "阅读商业方案",
    },
  },
};

const revealItems = document.querySelectorAll("[data-reveal]");
const stageTitle = document.getElementById("stage-title");
const stageBody = document.getElementById("stage-body");
const stagePoints = document.getElementById("stage-points");
const stageNodes = document.querySelectorAll(".stage-node");
const stageCard = document.querySelector(".stage-card");
const languageButtons = document.querySelectorAll(".lang-chip");
const descriptionMeta = document.querySelector('meta[name="description"]');

let currentLang = localStorage.getItem("gds-lang") || "en";
let currentStageIndex = 0;

for (const item of revealItems) {
  const delay = item.dataset.delay;
  if (delay) {
    item.style.setProperty("--delay", `${delay}ms`);
  }
}

const revealObserver = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      }
    }
  },
  {
    threshold: 0.16,
  }
);

revealItems.forEach((item) => revealObserver.observe(item));

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) {
    node.textContent = value;
  }
}

function renderList(id, items) {
  const node = document.getElementById(id);
  if (!node) return;
  node.innerHTML = items.map((item) => `<li>${item}</li>`).join("");
}

function renderSpanStrip(id, items) {
  const node = document.getElementById(id);
  if (!node) return;
  node.innerHTML = items.map((item) => `<span>${item}</span>`).join("");
}

function renderParagraphs(id, lines) {
  const node = document.getElementById(id);
  if (!node) return;
  node.innerHTML = lines.map((line) => `<p>${line}</p>`).join("");
}

function renderCaseBullets(items) {
  const node = document.getElementById("case-bullets");
  if (!node) return;
  node.innerHTML = items
    .map(
      (item) =>
        `<div><strong>${item.title}</strong><span>${item.body}</span></div>`
    )
    .join("");
}

function updateStageNodeLabels(lang) {
  const stages = stageData[lang];
  stageNodes.forEach((node, index) => {
    const strong = node.querySelector("strong");
    const small = node.querySelector("small");
    if (!stages[index] || !strong || !small) return;
    strong.textContent = stages[index].name;
    small.textContent = stages[index].short;
  });
}

function setStage(index) {
  const stages = stageData[currentLang] || stageData.en;
  const stage = stages[index];
  if (!stage) return;

  currentStageIndex = index;
  stageTitle.textContent = stage.title;
  stageBody.textContent = stage.body;
  stagePoints.innerHTML = stage.points.map((point) => `<li>${point}</li>`).join("");

  stageNodes.forEach((node) => {
    node.classList.toggle("active", Number(node.dataset.stage) === index);
  });
}

function applyLanguage(lang) {
  const content = copy[lang] || copy.en;
  currentLang = content === copy[lang] ? lang : "en";

  document.documentElement.lang = content.htmlLang;
  document.title = content.title;
  if (descriptionMeta) {
    descriptionMeta.setAttribute("content", content.description);
  }

  setText("brand-tagline", content.brandTagline);
  setText("nav-pipeline", content.nav.pipeline);
  setText("nav-case", content.nav.caseStudy);
  setText("nav-offers", content.nav.offers);
  setText("nav-faq", content.nav.faq);
  setText("repo-docs-link", content.repoDocs);

  setText("hero-eyebrow", content.hero.eyebrow);
  setText("hero-outline", content.hero.outline);
  setText("hero-solid", content.hero.solid);
  setText("hero-summary", content.hero.summary);
  setText("hero-primary-link", content.hero.primary);
  setText("hero-secondary-link", content.hero.secondary);
  renderSpanStrip("signal-strip", content.hero.signals);
  setText("stage-card-label", content.hero.stageLabel);
  setText("sticker-1", content.hero.stickers[0]);
  setText("sticker-2", content.hero.stickers[1]);
  setText("sticker-3", content.hero.stickers[2]);

  const marqueeItems = [...content.hero.marquee, ...content.hero.marquee];
  renderSpanStrip("marquee-track", marqueeItems);

  setText("pipeline-kicker", content.pipeline.kicker);
  setText("pipeline-title", content.pipeline.title);
  setText("pipeline-body", content.pipeline.body);
  setText("stage-summary-label", content.pipeline.summaryLabel);

  setText("case-kicker", content.caseStudy.kicker);
  setText("case-title", content.caseStudy.title);
  setText("case-window-title", content.caseStudy.windowTitle);
  renderParagraphs("case-window-body", content.caseStudy.windowLines);
  setText("case-tag", content.caseStudy.tag);
  setText("case-copy-title", content.caseStudy.copyTitle);
  setText("case-copy-body", content.caseStudy.copyBody);
  renderCaseBullets(content.caseStudy.bullets);

  setText("compare-kicker", content.compare.kicker);
  setText("compare-title", content.compare.title);
  setText("compare-bad-label", content.compare.badLabel);
  renderList("compare-bad-list", content.compare.badList);
  setText("compare-good-label", content.compare.goodLabel);
  renderList("compare-good-list", content.compare.goodList);

  setText("offers-kicker", content.offers.kicker);
  setText("offers-title", content.offers.title);
  setText("offers-body", content.offers.body);
  content.offers.cards.forEach((card, index) => {
    const cardIndex = index + 1;
    setText(`offer-${cardIndex}-tier`, card.tier);
    setText(`offer-${cardIndex}-price`, card.price);
    setText(`offer-${cardIndex}-body`, card.body);
    renderList(`offer-${cardIndex}-list`, card.list);
  });

  setText("faq-kicker", content.faq.kicker);
  setText("faq-title", content.faq.title);
  content.faq.items.forEach((item, index) => {
    const faqIndex = index + 1;
    setText(`faq-${faqIndex}-q`, item.q);
    setText(`faq-${faqIndex}-a`, item.a);
  });

  setText("cta-kicker", content.cta.kicker);
  setText("cta-title", content.cta.title);
  setText("cta-body", content.cta.body);
  setText("cta-primary-link", content.cta.primary);
  setText("cta-secondary-link", content.cta.secondary);

  updateStageNodeLabels(currentLang);
  setStage(currentStageIndex);

  languageButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.lang === currentLang);
  });

  localStorage.setItem("gds-lang", currentLang);
}

stageNodes.forEach((node) => {
  node.addEventListener("mouseenter", () => {
    setStage(Number(node.dataset.stage));
  });

  node.addEventListener("focus", () => {
    setStage(Number(node.dataset.stage));
  });

  node.addEventListener("click", () => {
    setStage(Number(node.dataset.stage));
  });
});

languageButtons.forEach((button) => {
  button.addEventListener("click", () => {
    applyLanguage(button.dataset.lang);
  });
});

applyLanguage(currentLang);

if (stageCard) {
  window.addEventListener("pointermove", (event) => {
    const bounds = stageCard.getBoundingClientRect();
    const withinX = event.clientX >= bounds.left && event.clientX <= bounds.right;
    const withinY = event.clientY >= bounds.top && event.clientY <= bounds.bottom;

    if (!withinX || !withinY) {
      stageCard.style.transform = "";
      return;
    }

    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    stageCard.style.transform = `perspective(1200px) rotateX(${(-y * 6).toFixed(2)}deg) rotateY(${(x * 8).toFixed(2)}deg)`;
  });

  stageCard.addEventListener("mouseleave", () => {
    stageCard.style.transform = "";
  });
}
