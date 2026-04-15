const stageData = {
  en: [
    {
      name: "Input Normalizer",
      short: "lock constraints",
      title: "Input Normalizer",
      body:
        "Turns rough ideas into clear constraints, target player, emotional goal, platform limits, and production boundaries before the rest of the pipeline begins.",
      points: [
        "defines player, platform, scope, and key constraints",
        "creates a stable design frame before loop design starts",
        "reduces ambiguity for every downstream stage",
      ],
    },
    {
      name: "Fantasy Loop Designer",
      short: "define the core loop",
      title: "Fantasy Loop Designer",
      body:
        "Defines the player promise, identity fantasy, core action, and repeatable loop so the package is built around a clear gameplay hypothesis.",
      points: [
        "identifies the strongest repeatable action",
        "locks the player promise early",
        "keeps the design centered on playable value",
      ],
    },
    {
      name: "Pacing And Structure",
      short: "build session flow",
      title: "Pacing And Structure",
      body:
        "Builds the short, medium, and long session layers that make the loop readable in real play instead of only on paper.",
      points: [
        "tests the loop across real session lengths",
        "surfaces early frustration before implementation cost rises",
        "supports explicit loop-backs when pacing reveals weakness",
      ],
    },
    {
      name: "World And Narrative Weaver",
      short: "wrap play with context",
      title: "World And Narrative Weaver",
      body:
        "Adds world rules, conflict, and narrative pressure around the gameplay spine without replacing gameplay clarity with lore.",
      points: [
        "keeps worldbuilding in service of play",
        "uses narrative to change pressure and player meaning",
        "helps the package stay coherent across design layers",
      ],
    },
    {
      name: "System Weaver And Scope Cutter",
      short: "control scope",
      title: "System Weaver And Scope Cutter",
      body:
        "Maps core systems, secondary systems, resource flow, and first-version cuts so the project stays aligned with the player promise and production reality.",
      points: [
        "separates core systems from optional systems",
        "makes MVP keep / later / cut visible",
        "names production-heavy risk areas early",
      ],
    },
    {
      name: "Coding Handoff Compiler",
      short: "prepare implementation",
      title: "Coding Handoff Compiler",
      body:
        "Compiles the locked gameplay package into scene, UI, object, state, variable, and event structures that downstream spec and coding agents can use directly.",
      points: [
        "bridges design language into runtime structure",
        "defines prototype acceptance and placeholder strategy",
        "reduces redesign pressure during implementation",
      ],
    },
  ],
  "zh-CN": [
    {
      name: "输入归一化",
      short: "锁定约束",
      title: "输入归一化",
      body:
        "把模糊想法整理成清晰约束、目标玩家、情绪目标、平台限制和制作边界，为后续阶段建立稳定起点。",
      points: [
        "明确玩家、平台、范围和关键约束",
        "在循环设计前先统一设计边界",
        "减少后续阶段的理解偏差",
      ],
    },
    {
      name: "幻想循环设计",
      short: "定义核心循环",
      title: "幻想循环设计",
      body:
        "定义玩家承诺、身份幻想、核心动作和可重复循环，让方案围绕明确的玩法假设展开。",
      points: [
        "找出最强的可重复动作",
        "尽早锁定玩家承诺",
        "让设计持续围绕可玩价值展开",
      ],
    },
    {
      name: "节奏与结构",
      short: "建立会话流",
      title: "节奏与结构",
      body:
        "建立短中长会话层的节奏结构，验证核心循环在真实游玩流程里是否成立，而不是只停留在纸面上。",
      points: [
        "按真实会话长度验证循环",
        "在实现成本升高前暴露前期问题",
        "当节奏暴露弱点时支持显式回环修正",
      ],
    },
    {
      name: "世界观与叙事编织",
      short: "给玩法加语境",
      title: "世界观与叙事编织",
      body:
        "用世界规则、冲突和叙事压力包裹玩法主干，同时保持玩法判断的清晰度。",
      points: [
        "让世界观服务玩法，而不是替代玩法",
        "用叙事改变压力、目标和意义",
        "让设计包在不同层面保持一致",
      ],
    },
    {
      name: "系统编织与范围裁剪",
      short: "控制范围",
      title: "系统编织与范围裁剪",
      body:
        "规划核心系统、次级系统、资源流和首版裁剪方案，让项目同时对齐玩家价值和制作现实。",
      points: [
        "区分核心系统和可选系统",
        "让 MVP keep / later / cut 始终可见",
        "提前标出高成本风险区",
      ],
    },
    {
      name: "编码交接编译器",
      short: "准备实现结构",
      title: "编码交接编译器",
      body:
        "把已锁定的玩法包编译成场景、UI、对象、状态、变量和事件结构，让下游规格与编码代理可以直接接手。",
      points: [
        "把设计语言转换成运行时结构",
        "定义原型验收与占位策略",
        "降低实现阶段的返工压力",
      ],
    },
  ],
};

const copy = {
  en: {
    htmlLang: "en",
    title: "Gameplay Design Skill Suite",
    description:
      "An orchestrator-first gameplay design workflow for Codex. Turn raw game ideas into validated gameplay packages, Chinese production-ready specs, execution plans, and a runner-driven execution path.",
    brandTagline: "orchestrator-first for Codex",
    nav: {
      pipeline: "Pipeline",
      caseStudy: "Case",
      offers: "Offers",
      faq: "FAQ",
    },
    repoDocs: "Repo Docs",
    hero: {
      eyebrow: "Structured gameplay design for builders who need clear execution",
      outline: "IDEA IN.",
      solid: "SYSTEM OUT.",
      summary:
        "A structured workflow that takes raw game concepts, locks direction, keeps stages ordered, controls scope, and lands on a gameplay package your AI coding stack can continue from.",
      primary: "Open GitHub Repo",
      secondary: "See The Pipeline",
      signals: [
        "10 coordinated skills",
        "1 orchestrator-first entry",
        "validated gyro-battle example",
        "spec, plan, runner, and adapter path",
      ],
      stageLabel: "Workflow Overview",
      stickers: ["LOCK DIRECTION", "CONTROL SCOPE", "HAND OFF CLEANLY"],
      marquee: [
        "GAMEPLAY-DESIGN-ORCHESTRATOR",
        "LOOP DESIGN",
        "PACING STRUCTURE",
        "MVP KEEP / CUT",
        "EXECUTION PLAN",
        "WORKER ADAPTER",
      ],
    },
    pipeline: {
      kicker: "The pipeline is the product",
      title: "One controlled chain from idea to execution handoff.",
      body:
        "The value is not just better output. It is workflow ownership: one orchestrator, ordered stages, explicit loop-backs, spec expansion, execution-plan compilation, and runner-managed task coordination.",
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
        "output: package + review notes + spec + execution plan",
        "validation: package passed / spec passed / plan passed / runner path checked",
      ],
      tag: "Why this example matters",
      copyTitle: "It shows the workflow holding up under a real game concept.",
      copyBody:
        "The included gyro-battle sample is a full example, not just a teaser. It covers direction choice, pacing revision, scope control, system indexes, prototype acceptance, and downstream implementation mapping.",
      bullets: [
        {
          title: "Direction choice",
          body: "Arena combat won. Deeper parts and economy layers were removed for first-version scope control.",
        },
        {
          title: "Revision pressure",
          body: "Pacing and system stages forced loop-backs before the spec layer, keeping the package honest.",
        },
        {
          title: "Downstream packaging",
          body: "The result includes scenes, UI, rules, tasks, QA, delivery mapping, and an agent-executable task graph.",
        },
      ],
    },
    compare: {
      kicker: "Positioning",
      title: "Built for teams and operators who need a repeatable workflow.",
      badLabel: "Generic prompt packs",
      badList: [
        "start with theme and genre labels",
        "no owner for stage order",
        "scope expands too early",
        "good prose, weak handoff",
        "little proof beyond screenshots",
      ],
      goodLabel: "Gameplay Design Skill Suite",
      goodList: [
        "orchestrator owns the workflow",
        "downstream stages stay ordered",
        "MVP keep / cut stays visible",
        "coding handoff is part of the chain",
        "spec, execution-plan, runner, and adapter checks included",
      ],
    },
    offers: {
      kicker: "Commercial path",
      title: "Public showcase outside. Paid workflow leverage inside.",
      body:
        "This repo is positioned as a source-available showcase with a commercial path for teams that want onboarding, adaptation, and internal rollout support.",
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
      kicker: "FAQ",
      title: "Questions about product scope and workflow usage.",
      items: [
        {
          q: "Is this open source?",
          a: "No. It is public for evaluation and discovery, but commercial reuse and redistribution are protected.",
        },
        {
          q: "Can I trigger the stage skills one by one?",
          a: "Normally, no. The intended operating model is orchestrator-first, with stage skills used as controlled internal steps.",
        },
        {
          q: "Does this automatically produce a shippable game?",
          a: "No. It improves design structure, handoff quality, and execution readiness. It does not replace implementation, tuning, or production judgment.",
        },
        {
          q: "Why is the final spec in Chinese?",
          a: "Because the current downstream production target is a Chinese execution format. The workflow logic can still support broader use cases.",
        },
      ],
    },
    cta: {
      kicker: "Next Step",
      title: "Review the example, validate the outputs, and adapt the workflow to your own production stack.",
      body:
        "Use the repository as a practical reference for orchestrator-first gameplay design, execution planning, and worker-facing handoff.",
      primary: "View Repository",
      secondary: "Read Commercial Offers",
    },
  },
  "zh-CN": {
    htmlLang: "zh-CN",
    title: "Gameplay Design Skill Suite | 中文",
    description:
      "一套面向 Codex 的 orchestrator-first 游戏设计工作流。把原始游戏想法整理为经过验证的玩法包、中文生产级规格书、execution plan，以及 runner 与 worker adapter 执行路径。",
    brandTagline: "面向 Codex 的 orchestrator-first 工作流",
    nav: {
      pipeline: "流程",
      caseStudy: "案例",
      offers: "商业化",
      faq: "问答",
    },
    repoDocs: "仓库文档",
    hero: {
      eyebrow: "适合需要清晰执行路径的游戏设计团队与独立开发者",
      outline: "想法进来。",
      solid: "系统出去。",
      summary:
        "这是一套结构化工作流。它把原始游戏概念先锁方向、再控范围、再出设计包，最后继续落到规格书、execution plan、runner 和 worker adapter 执行路径。",
      primary: "打开 GitHub 仓库",
      secondary: "查看完整流程",
      signals: [
        "10 个协同技能",
        "1 个 orchestrator 总入口",
        "已验证 gyro-battle 示例",
        "规格、计划、runner 与 adapter 路径",
      ],
      stageLabel: "工作流概览",
      stickers: ["先锁方向", "控制范围", "清晰交接"],
      marquee: [
        "玩法设计总控",
        "循环设计",
        "节奏结构",
        "MVP 保留 / 裁剪",
        "执行计划",
        "WORKER ADAPTER",
      ],
    },
    pipeline: {
      kicker: "真正的产品是这条流程",
      title: "从想法到执行交接的一条受控链路。",
      body:
        "它的价值不只是输出更完整，而是流程被真正接管：一个 orchestrator、固定阶段顺序、显式 loop-back、规格扩展、execution plan 编译，以及 runner 管理的任务协调。",
      summaryLabel: "当前高亮阶段",
    },
    caseStudy: {
      kicker: "验证样例",
      title: "Gyro-battle 网页游戏：从方向锁定一路推进到完整规格。",
      windowTitle: "gyro-battle/final-package",
      windowLines: [
        "选定方向：竞技场击飞对抗",
        "核心承诺：一次精准命中就能改变回合走势",
        "最大范围风险：物理反馈失控后会变成随机噪音",
        "loop-back 次数：2",
        "输出：玩法包 + 复盘记录 + 规格书 + 执行计划",
        "验证状态：package 通过 / spec 通过 / plan 通过 / runner 路径已检查",
      ],
      tag: "这个案例为什么重要",
      copyTitle: "它证明这条工作流可以承受真实游戏概念，而不是只适合展示。",
      copyBody:
        "仓库附带的 gyro-battle 样例是完整案例，不是只供展示的片段。它覆盖方向选择、节奏修正、范围控制、系统索引、原型验收，以及下游实现映射。",
      bullets: [
        {
          title: "方向选择",
          body: "竞技场对抗被保留，更深的部件与经济层因为首版范围控制被移除。",
        },
        {
          title: "修正压力",
          body: "节奏层和系统层在进入规格层之前就触发了回环修正。",
        },
        {
          title: "下游交接",
          body: "最终产物包含场景、UI、规则、任务、QA、交付映射，以及 agent 可执行任务图。",
        },
      ],
    },
    compare: {
      kicker: "定位",
      title: "为需要可重复流程的团队和设计运营者而做。",
      badLabel: "通用 prompt 包",
      badList: [
        "从题材和风格标签开始",
        "没有阶段顺序负责人",
        "范围过早膨胀",
        "文案好看但交接弱",
        "除了截图几乎没有证明",
      ],
      goodLabel: "Gameplay Design Skill Suite",
      goodList: [
        "由 orchestrator 接管流程",
        "下游阶段保持有序",
        "MVP 保留 / 裁剪始终可见",
        "编码交接是链路内建部分",
        "附带 spec、execution plan、runner 和 adapter 校验",
      ],
    },
    offers: {
      kicker: "商业路径",
      title: "对外是公开展示，对内是可收费的工作流能力。",
      body:
        "这个仓库的定位是 source-available 展示资产，同时保留面向团队的适配、培训与落地支持空间。",
      cards: [
        {
          tier: "单人适配",
          price: "$490+",
          body: "适合独立开发者和顾问，把这套流程第一次接到真实项目里。",
          list: [
            "单买家商业使用路径",
            "基础上手包",
            "一次目标项目适配",
          ],
        },
        {
          tier: "团队落地",
          price: "$2.4K+",
          body: "适合小团队把 AI 辅助前期策划流程放入内部生产线。",
          list: [
            "团队商业授权路径",
            "术语与流程对齐",
            "定制案例包",
          ],
        },
        {
          tier: "定制流程构建",
          price: "$8K+",
          body: "适合工作室与服务商构建行业化、品牌化或白标版本。",
          list: [
            "定制技能修改",
            "验证器调整",
            "部署与 rollout 支持",
          ],
        },
      ],
    },
    faq: {
      kicker: "FAQ",
      title: "关于产品边界与使用方式的常见问题。",
      items: [
        {
          q: "这是开源的吗？",
          a: "不是。它对外公开是为了评估和发现，但商业复用与二次分发受保护。",
        },
        {
          q: "我能不能把中间阶段一个个单独触发？",
          a: "通常不建议。标准使用方式是 orchestrator-first，中间阶段更适合作为受控内部步骤。",
        },
        {
          q: "它会自动产出可上线游戏吗？",
          a: "不会。它提升的是设计结构、交接质量和执行准备度，不替代实现、调优和制作判断。",
        },
        {
          q: "为什么最终规格是中文？",
          a: "因为当前下游生产目标是中文执行格式，但这套流程逻辑本身并不限于中文场景。",
        },
      ],
    },
    cta: {
      kicker: "下一步",
      title: "先查看案例、跑通验证，再把这条流程接到你的生产栈里。",
      body:
        "把这个仓库当作 orchestrator-first 游戏设计、执行计划和 worker 交接的实践参考。",
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
