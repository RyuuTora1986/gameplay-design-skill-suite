const stageData = [
  {
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
    title: "Coding Handoff Compiler",
    body:
      "Compiles the locked gameplay package into scene, UI, object, state, variable, and event structures that downstream spec and coding agents can consume directly.",
    points: [
      "bridges design language into runtime shape",
      "defines placeholder strategy and prototype acceptance",
      "reduces redesign burden on implementation agents",
    ],
  },
];

const revealItems = document.querySelectorAll("[data-reveal]");
const stageTitle = document.getElementById("stage-title");
const stageBody = document.getElementById("stage-body");
const stagePoints = document.getElementById("stage-points");
const stageNodes = document.querySelectorAll(".stage-node");
const stageCard = document.querySelector(".stage-card");

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

function setStage(index) {
  const stage = stageData[index];
  if (!stage) return;

  stageTitle.textContent = stage.title;
  stageBody.textContent = stage.body;
  stagePoints.innerHTML = stage.points.map((point) => `<li>${point}</li>`).join("");

  stageNodes.forEach((node) => {
    node.classList.toggle("active", Number(node.dataset.stage) === index);
  });
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

setStage(0);

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
