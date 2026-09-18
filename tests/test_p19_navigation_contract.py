from pathlib import Path


SURFACE = Path(__file__).parents[1] / "web-preview" / "design-navigation-p19-premium.html"


def test_p19_navigation_surface_contract():
    html = SURFACE.read_text(encoding="utf-8")
    assert 'viewport-fit=cover' in html
    assert 'aria-labelledby="navigation-title"' in html
    assert 'aria-describedby="navigation-context"' in html
    assert 'aria-current="page"' in html
    assert html.count('class="item') == 6
    assert 'min-height:48px' in html
    assert 'min-width:48px' in html
    assert 'focus-visible' in html
    assert 'prefers-reduced-motion:reduce' in html
    assert '@media(max-width:620px)' in html
    assert 'html[dir=rtl]' in html
    assert 'env(safe-area-inset-top)' in html
    assert 'env(safe-area-inset-bottom)' in html
    assert 'overflow-wrap:anywhere' in html
    assert 'Current Journey' in html
    assert 'People & Relationships' in html
    assert 'Threads of Truth' in html
    assert 'Kingdom Chronicle' in html
    assert 'New Reign' in html
    assert 'Settings & Access' in html
