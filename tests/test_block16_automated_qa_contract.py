from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TESTS = (
    'tests/test_runtime_state.py', 'tests/test_authored_choice_execution.py',
    'tests/test_presentation_runtime.py', 'tests/test_presentation_bridge.py',
    'tests/test_scenario_final_gate.py', 'tests/test_replay_meta_runtime.py',
    'tests/test_block10_localization.py', 'tests/test_block11_accessibility_contract.py',
    'tests/test_block12_responsive_contract.py', 'tests/test_block14_motion_audio_haptics_contract.py',
    'tests/test_block15_visual_regression_contract.py',
)
def test_block16_required_regression_suite_is_present():
    missing = [p for p in REQUIRED_TESTS if not (ROOT / p).is_file()]
    assert not missing, f'Missing required automated QA tests: {missing}'
def test_block16_qa_workflow_exists():
    workflow = ROOT / '.github/workflows/block16-automated-qa.yml'
    assert workflow.is_file()
    text = workflow.read_text(encoding='utf-8')
    for required in ('compileall', 'pytest', 'upload-artifact', 'junit'):
        assert required in text
