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
const query=new URLSearchParams(location.search);
const choiceSet=query.get('choices')==='3'?threeChoices:twoChoices;
const rtl=query.get('rtl')==='1';
if(rtl)document.documentElement.dir='rtl';
function render(){resources.forEach(k=>$(k).textContent=state[k]);$('turn').textContent=String(state.turn).padStart(3,'0');renderChoices()}
function renderChoices(){
  const root=$('choices');root.classList.toggle('choice-count-3',choiceSet.length===3);root.replaceChildren();
  choiceSet.forEach(choice=>{
    const button=document.createElement('button');button.className='choice';button.dataset.choice=choice.id;button.type='button';
    button.innerHTML=`<span class="choice-kicker">${choice.kicker}</span><strong>${choice.title}</strong><span>${choice.support}</span>`;
    button.addEventListener('click',()=>choose(choice.id));root.appendChild(button);
  });
}
function choose(kind){
  if(state.chosen)return;state.chosen=true;
  document.querySelectorAll('.choice').forEach(b=>{b.classList.add('disabled');b.setAttribute('aria-disabled','true')});
  const selected=document.querySelector(`[data-choice="${kind}"]`);if(!selected)return;
  selected.classList.remove('disabled');selected.classList.add('resolved');
  if(kind==='open'){state.trust+=4;state.reputation+=2;$('consequenceText').textContent='The evidence enters the royal record. Mara knows you chose to look.'}
  else if(kind==='seal'){state.security+=3;state.trust-=2;$('consequenceText').textContent='The ledger is sealed. The Crown keeps its silence—for now.'}
  else {$('consequenceText').textContent='The steward is summoned. Two accounts will now have to answer to each other.'}
  render();$('consequence').hidden=false;
}
const panel=$('panel');
const panels={
 realm:`<h2>The Realm</h2><p>The kingdom is stable enough to breathe, but several pressures are beginning to overlap.</p><div class="stat-grid">${resources.map(k=>`<div class="stat"><small>${k.toUpperCase()}</small><b>${state[k]}</b></div>`).join('')}</div>`,
 history:`<h2>Royal History</h2><p>Decisions remain visible here as part of the reign, not as a score.</p><div class="history-entry"><small>TURN 014 · NORTH RECORD ROOM</small><strong>The Winter Ledger</strong><span>Mara · Crown records · Investigation begins</span></div>`,
 characters:`<h2>People of the Crown</h2><p>Relationships are remembered through people, language and history—not a heart meter.</p><div class="history-entry"><small>ROYAL ACCOUNTING</small><strong>Mara</strong><span>Keeper of the Crown's accounts · awaiting your answer</span></div>`
};
document.querySelectorAll('.nav-item').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.nav-item').forEach(b=>{b.classList.remove('active');b.removeAttribute('aria-current')});button.classList.add('active');button.setAttribute('aria-current','page');const name=button.dataset.panel;if(name==='event'){panel.hidden=true;return}panel.innerHTML=panels[name];panel.hidden=false;panel.scrollIntoView({behavior:'smooth',block:'nearest'})}));
render();
