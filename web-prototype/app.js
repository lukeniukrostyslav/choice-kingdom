const state={turn:14,gold:62,trust:57,security:49,power:54,reputation:61,chosen:false};
const $=id=>document.getElementById(id);
const resources=['gold','trust','security','power','reputation'];
const twoChoices=[
  {id:'open',kicker:'EXAMINE THE EVIDENCE',title:'Open the ledger',support:'Trust the record and begin with the numbers.'},
  {id:'seal',kicker:'PROTECT THE CROWN',title:'Seal the ledger',support:'Keep the accusation inside the palace for now.'}
];
const threeChoices=[
  ...twoChoices,
  {id:'summon',kicker:'TEST THE ACCOUNT',title:'Summon the steward',support:'Ask for the Crown’s figures before you judge either record.'}
];
const longChoices=[
  {id:'open-long',kicker:'EXAMINE THE EVIDENCE',title:'Open the ledger and trace the grain reserve through the winter accounts',support:'Begin with the record itself, then compare each discrepancy against the Crown’s known shipments and market reports.'},
  {id:'seal-long',kicker:'PROTECT THE CROWN',title:'Seal the ledger until the palace can prepare a controlled inquiry',support:'Keep the accusation contained for now, giving the court time to establish who may safely examine the evidence.'},
  {id:'summon-long',kicker:'TEST THE ACCOUNT',title:'Summon the steward and demand both accounts before making a judgment',support:'Place the competing records in the same room and let the contradiction become visible without naming a culprit.'}
];
const longNarrative='Mara places the book before you without opening it. The figures inside do not match the Crown’s accounts for the grain reserve. If the discrepancy is real, someone has been moving provisions through the winter markets before the court was meant to know. The record is incomplete, the hour is late, and every person who touches it may become part of the story.';
const query=new URLSearchParams(location.search);
const mode=query.get('choices');
const choiceSet=mode==='long'?longChoices:(mode==='3'?threeChoices:twoChoices);
if(query.get('rtl')==='1')document.documentElement.dir='rtl';
if(query.get('font')==='large')document.documentElement.classList.add('large-type');
if(query.get('artwork')==='none')document.documentElement.classList.add('no-artwork');
if(query.get('narrative')==='long')document.documentElement.classList.add('long-narrative');
if(query.get('qa')==='states')document.documentElement.classList.add('state-qa');

function render(){
  resources.forEach(k=>$(k).textContent=state[k]);
  $('turn').textContent=String(state.turn).padStart(3,'0');
  if(query.get('narrative')==='long')$('narrative').textContent=longNarrative;
  renderChoices();
}

function choiceMarkup(choice,index,stateClass='',stateLabel=''){
  const button=document.createElement('button');
  button.className=`choice ${stateClass}`.trim();
  button.dataset.choice=choice.id;
  button.dataset.index=String(index+1);
  button.type='button';
  button.setAttribute('aria-pressed',stateClass==='resolved'||stateClass==='selected'?'true':'false');
  button.setAttribute('aria-label',`${index+1}. ${choice.title}. ${choice.support}`);
  if(stateClass==='disabled')button.disabled=true;
  if(stateClass==='resolving'||stateClass==='disabled')button.setAttribute('aria-disabled','true');
  button.innerHTML=`<span class="choice-kicker">${choice.kicker}</span><strong>${choice.title}</strong><span class="choice-support">${choice.support}</span><span class="choice-state" aria-hidden="true">${stateLabel}</span>`;
  return button;
}

function renderChoices(){
  const root=$('choices');
  root.classList.toggle('choice-count-3',choiceSet.length===3);
  root.setAttribute('aria-label',`${choiceSet.length} available decision${choiceSet.length===1?'':'s'}`);
  root.replaceChildren();
  choiceSet.forEach((choice,index)=>{
    const button=choiceMarkup(choice,index);
    button.addEventListener('click',()=>choose(choice.id));
    root.appendChild(button);
  });
  if(query.get('qa')==='states')renderStateQA(root);
}

function renderStateQA(root){
  const states=[
    ['idle','IDLE'],['focused','FOCUS'],['pressed','PRESSED'],['resolving','RESOLVING'],['resolved','SELECTED'],['disabled','DISABLED']
  ];
  root.classList.add('qa-state-grid');
  root.setAttribute('aria-label','Choice state visual QA matrix');
  root.replaceChildren();
  states.forEach(([stateClass,label],index)=>{
    const choice=choiceSet[index%choiceSet.length];
    const card=choiceMarkup(choice,index,stateClass,label);
    card.setAttribute('tabindex',stateClass==='focused'?'0':'-1');
    if(stateClass==='pressed')card.setAttribute('aria-pressed','true');
    if(stateClass==='focused')card.classList.add('qa-focused');
    if(stateClass==='pressed')card.classList.add('qa-pressed');
    root.appendChild(card);
  });
  $('consequence').hidden=false;
  $('consequenceText').textContent='Design QA fixture: every decision state is shown together. This fixture does not execute gameplay.';
  $('choices').setAttribute('aria-busy','false');
}

function choose(id){
  if(state.chosen)return;
  const selected=document.querySelector(`[data-choice="${CSS.escape(id)}"]`);
  if(!selected)return;
  state.chosen=true;
  const buttons=[...document.querySelectorAll('.choice')];
  buttons.forEach(button=>{
    button.disabled=true;
    button.classList.add('resolving');
    button.setAttribute('aria-disabled','true');
  });
  selected.classList.remove('resolving');
  selected.classList.add('selected');
  selected.setAttribute('aria-pressed','true');
  selected.setAttribute('aria-label',`${selected.querySelector('strong').textContent}. Selected. Resolving decision.`);
  selected.querySelector('.choice-state').textContent='RESOLVING';
  $('choices').setAttribute('aria-busy','true');
  $('consequence').hidden=false;
  $('consequence').classList.remove('is-resolved');
  $('consequenceText').textContent='Recording this decision…';

  window.setTimeout(()=>{
    selected.classList.remove('selected');
    selected.classList.add('resolved');
    selected.querySelector('.choice-state').textContent='SELECTED';
    selected.setAttribute('aria-label',`${selected.querySelector('strong').textContent}. Selected. Decision recorded.`);
    $('consequenceText').textContent='Decision recorded in the visual prototype. Gameplay effects belong to GameSession, not this UI layer.';
    $('consequence').classList.add('is-resolved');
    $('choices').setAttribute('aria-busy','false');
  },180);
}

const panel=$('panel');
const panels={
  realm:`<h2>The Realm</h2><p>The kingdom is stable enough to breathe, but several pressures are beginning to overlap.</p><div class="stat-grid">${resources.map(k=>`<div class="stat"><small>${k.toUpperCase()}</small><b>${state[k]}</b></div>`).join('')}</div><div class="panel-note"><strong>Pressure centers</strong><span>Crown · Commons · Houses · Guilds · Border</span></div>`,
  history:`<h2>Royal History</h2><p>Decisions remain visible here as part of the reign, not as a score.</p><div class="history-entry"><small>TURN 014 · NORTH RECORD ROOM</small><strong>The Winter Ledger</strong><span>Mara · Crown records · Investigation begins</span></div>`,
  characters:`<h2>People of the Crown</h2><p>Relationships are remembered through people, language and history—not a heart meter.</p><div class="history-entry"><small>ROYAL ACCOUNTING</small><strong>Mara</strong><span>Keeper of the Crown's accounts · awaiting your answer</span></div>`,
  factions:`<h2>Factions</h2><p>Political constituencies are presented through their interests, pressures and unresolved concerns—not morality meters.</p><div class="history-entry"><small>GUILD · CURRENT CONCERN</small><strong>Winter market resilience</strong><span>Pressure, recent decisions and unresolved issues belong here when authored by the campaign.</span></div>`
};

document.querySelectorAll('.nav-item').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('.nav-item').forEach(b=>{b.classList.remove('active');b.removeAttribute('aria-current')});
  button.classList.add('active');
  button.setAttribute('aria-current','page');
  const name=button.dataset.panel;
  if(name==='event'){panel.hidden=true;return;}
  panel.innerHTML=panels[name];
  panel.hidden=false;
  panel.setAttribute('tabindex','-1');
  panel.focus({preventScroll:true});
  panel.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'nearest'});
}));

render();
