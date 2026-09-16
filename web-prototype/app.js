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
const query=new URLSearchParams(location.search);
const mode=query.get('choices');
const choiceSet=mode==='long'?longChoices:(mode==='3'?threeChoices:twoChoices);
if(query.get('rtl')==='1')document.documentElement.dir='rtl';

function render(){
  resources.forEach(k=>$(k).textContent=state[k]);
  $('turn').textContent=String(state.turn).padStart(3,'0');
  renderChoices();
}

function renderChoices(){
  const root=$('choices');
  root.classList.toggle('choice-count-3',choiceSet.length===3);
  root.replaceChildren();
  choiceSet.forEach(choice=>{
    const button=document.createElement('button');
    button.className='choice';
    button.dataset.choice=choice.id;
    button.type='button';
    button.innerHTML=`<span class="choice-kicker">${choice.kicker}</span><strong>${choice.title}</strong><span class="choice-support">${choice.support}</span><span class="choice-state" aria-hidden="true"></span>`;
    button.addEventListener('click',()=>choose(choice.id));
    root.appendChild(button);
  });
}

function choose(id){
  if(state.chosen)return;
  const selected=document.querySelector(`[data-choice="${id}"]`);
  if(!selected)return;
  state.chosen=true;
  document.querySelectorAll('.choice').forEach(button=>{
    button.disabled=true;
    button.classList.add('resolving');
    button.setAttribute('aria-disabled','true');
  });
  selected.classList.add('resolved');
  selected.querySelector('.choice-state').textContent='SELECTED';
  selected.setAttribute('aria-label',`${selected.querySelector('strong').textContent}. Selected.`);
  $('consequenceText').textContent='Decision recorded in the visual prototype. Gameplay effects belong to GameSession, not this UI layer.';
  $('consequence').hidden=false;
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
  panel.scrollIntoView({behavior:'smooth',block:'nearest'});
}));

render();
