import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

BG     = '#0d1117'; CARD   = '#161b22'; GREEN  = '#2ea043'
BLUE   = '#58a6ff'; ORANGE = '#f0883e'; PURPLE = '#bc8cff'
RED    = '#ff7b72'; YELLOW = '#e3b341'; WHITE  = '#e6edf3'
GRAY   = '#8b949e'; TEAL   = '#39d353'; PINK   = '#f778ba'

OUT = os.path.dirname(os.path.abspath(__file__))

def bg(fig, axes):
    fig.patch.set_facecolor(BG)
    for ax in (axes if hasattr(axes, '__iter__') else [axes]):
        ax.set_facecolor(BG)
        for s in ax.spines.values(): s.set_visible(False)
        ax.set_xticks([]); ax.set_yticks([])

def box(ax, cx, cy, w, h, fc, label, sub=None, fs=11,
        tc=WHITE, ec=None, lw=1.5, radius=0.05, bold=True):
    ec = ec or fc
    p = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                       boxstyle=f'round,pad={radius}',
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
    ax.add_patch(p)
    dy = 0.013 if sub else 0
    ax.text(cx, cy+dy, label, ha='center', va='center', fontsize=fs,
            color=tc, fontweight='bold' if bold else 'normal', zorder=4)
    if sub:
        ax.text(cx, cy-0.055, sub, ha='center', va='center',
                fontsize=7.5, color=GRAY, zorder=4)

def line(ax, x1,y1,x2,y2, col, lw=1.8, dash=False):
    ls = (0,(5,4)) if dash else '-'
    ax.plot([x1,x2],[y1,y2], color=col, lw=lw, linestyle=ls, zorder=1, alpha=0.9)

def arr(ax, x1,y1,x2,y2, col, lw=2):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color=col, lw=lw,
                                connectionstyle='arc3,rad=0'), zorder=4)

# ── IMAGE 1: JUnit5 Mind Map ─────────────────────────────────────────────────
def junit5_mindmap():
    fig, ax = plt.subplots(figsize=(20, 12))
    bg(fig, ax)
    ax.set_xlim(0,20); ax.set_ylim(0,12)

    ax.text(10, 11.5, 'JUnit 5  --  Day 1 Mind Map',
            ha='center', fontsize=20, color=GREEN, fontweight='bold')
    ax.text(10, 11.05,'1 July 2026  |  Author: Vishnu Vardhan',
            ha='center', fontsize=10, color=GRAY)

    # centre
    box(ax, 10, 5.8, 2.6, 0.95, GREEN, 'JUnit 5', 'Testing Framework',
        fs=14, tc='#0d1117')

    branches = [
        (3.5,  9.2,  BLUE,   '@Test\nAnnotation',   'marks method as test'),
        (10,   9.4,  ORANGE, 'Architecture',        'Platform+Jupiter+Vintage'),
        (16.5, 9.2,  PURPLE, 'Assertions',          'assertEquals, assertTrue...'),
        (2.5,  5.8,  TEAL,   'JUnit 4\nvs JUnit 5', '@Before vs @BeforeEach'),
        (17.5, 5.8,  PINK,   'Parameterized\nTests','@ParameterizedTest'),
        (3.5,  2.4,  YELLOW, 'Lifecycle\nHooks',    '@BeforeEach @AfterEach'),
        (10,   2.0,  RED,    'Manual vs\nUnit Test', 'if/else vs framework'),
        (16.5, 2.4,  BLUE,   'Maven/Gradle\nSetup', 'pom.xml dependency'),
    ]
    for bx,by,col,lbl,sub in branches:
        line(ax, 10,5.8, bx,by, col)
        box(ax, bx,by, 3.0,0.95, CARD, lbl, sub,
            fs=10, tc=col, ec=col, lw=1.5, radius=0.07)

    # sub-nodes
    subs = [
        (1.5,10.3, BLUE,  'org.junit.jupiter.api'),
        (4.5,10.3, BLUE,  'no public needed'),
        (7.5, 10.4,ORANGE,'Jupiter'),
        (10,  10.4,ORANGE,'Platform'),
        (12.5,10.4,ORANGE,'Vintage'),
        (15,  10.3,PURPLE,'assertEquals'),
        (17.5,10.3,PURPLE,'assertThrows'),
        (0.8, 4.0, TEAL,  '@Ignore vs @Disabled'),
        (0.8, 3.2, TEAL,  '@RunWith vs @ExtendWith'),
        (18.5,4.0, PINK,  '@ValueSource'),
        (18.5,3.2, PINK,  '@CsvSource'),
        (2.2, 1.2, YELLOW,'@BeforeAll'),
        (4.8, 1.2, YELLOW,'@AfterAll'),
        (8.5, 0.9, RED,   'Manual: if/else'),
        (11.5,0.9, RED,   'JUnit: assertions'),
    ]
    for sx,sy,col,lbl in subs:
        ax.plot(sx,sy,'o', color=col, markersize=6, zorder=3)
        ax.text(sx,sy-0.22, lbl, ha='center', va='top', fontsize=7.5, color=col)

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-MindMap.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── IMAGE 2: JUnit 5 Architecture ────────────────────────────────────────────
def junit5_architecture():
    fig, ax = plt.subplots(figsize=(16, 9))
    bg(fig, ax)
    ax.set_xlim(0,16); ax.set_ylim(0,9)

    ax.text(8, 8.6, 'JUnit 5 Architecture', ha='center',
            fontsize=17, color=GREEN, fontweight='bold')
    ax.text(8, 8.2, 'JUnit 5 is NOT just JUnit 4 + new features -- it is a brand new architecture',
            ha='center', fontsize=10, color=GRAY)

    # top: JUnit 5 banner
    box(ax, 8, 7.2, 5.5, 0.75, GREEN, 'JUnit 5', fs=14, tc='#0d1117')

    # 3 modules
    modules = [
        (2.8, 5.4, BLUE,   'JUnit Platform',
         'Foundation layer\nLaunches tests on JVM\nIntegrates with Maven/Gradle/IDEs'),
        (8.0, 5.4, ORANGE, 'JUnit Jupiter',
         'New JUnit 5 API\nAll new annotations\n@Test @BeforeEach @AfterEach\nassertions & extensions'),
        (13.2,5.4, PURPLE, 'JUnit Vintage',
         'Backward compatibility\nRuns JUnit 3 and 4 tests\nOld projects still work'),
    ]
    for mx,my,col,title,desc in modules:
        arr(ax, 8,6.82, mx,my+0.45, col)
        mod_bg = FancyBboxPatch((mx-2.4, my-1.5), 4.8, 2.2,
                                boxstyle='round,pad=0.08',
                                facecolor=CARD, edgecolor=col, lw=2)
        ax.add_patch(mod_bg)
        ax.text(mx, my+0.62, title, ha='center', fontsize=11,
                color=col, fontweight='bold')
        for i,ln in enumerate(desc.split('\n')):
            ax.text(mx, my+0.18-i*0.42, ln, ha='center', fontsize=8.5, color=WHITE)

    # maven/gradle → platform
    box(ax, 3.0, 2.4, 2.5, 0.65, CARD, 'Maven', 'mvn test',
        fs=10, tc=RED, ec=RED, lw=1.5)
    box(ax, 6.5, 2.4, 2.5, 0.65, CARD, 'Gradle', 'gradle test',
        fs=10, tc=YELLOW, ec=YELLOW, lw=1.5)
    box(ax, 10.0,2.4, 2.5, 0.65, CARD, 'IntelliJ', 'IDE runner',
        fs=10, tc=BLUE, ec=BLUE, lw=1.5)
    box(ax, 13.5,2.4, 2.5, 0.65, CARD, 'VS Code', 'IDE runner',
        fs=10, tc=GROOVY if 'GROOVY' in dir() else TEAL, ec=TEAL, lw=1.5)

    for tx in [3.0, 6.5, 10.0, 13.5]:
        arr(ax, tx, 2.72, 2.8 if tx < 8 else 13.2, 4.3, GRAY, lw=1.2)

    # note box
    note = FancyBboxPatch((0.4, 0.2), 15.2, 1.0,
                          boxstyle='round,pad=0.08',
                          facecolor=CARD, edgecolor=ORANGE, lw=1.2)
    ax.add_patch(note)
    ax.text(8, 0.85, 'JUnit Platform is the foundation that launches tests.',
            ha='center', fontsize=10, color=WHITE)
    ax.text(8, 0.45, 'Jupiter contains all the new annotations and assertion methods used in JUnit 5.',
            ha='center', fontsize=10, color=ORANGE)

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-Architecture.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── IMAGE 3: JUnit 4 vs JUnit 5 ──────────────────────────────────────────────
def junit4_vs_junit5():
    fig, ax = plt.subplots(figsize=(18, 13))
    bg(fig, ax)
    ax.set_xlim(0,18); ax.set_ylim(0,13)

    ax.text(9, 12.6, 'JUnit 4  vs  JUnit 5  --  Complete Comparison',
            ha='center', fontsize=17, color=WHITE, fontweight='bold')

    # headers
    box(ax, 4.0, 11.7, 6.5, 0.75, RED,   'JUnit 4', fs=14, tc=WHITE)
    box(ax, 14.0,11.7, 6.5, 0.75, GREEN, 'JUnit 5', fs=14, tc='#0d1117')
    ax.text(9, 11.7, 'VS', ha='center', va='center', fontsize=18,
            color=WHITE, fontweight='black')

    rows = [
        ('Modules',       'Single JAR',                  '3 modules: Platform + Jupiter + Vintage'),
        ('Package',       'org.junit',                   'org.junit.jupiter.api'),
        ('Before each',   '@Before',                     '@BeforeEach'),
        ('After each',    '@After',                      '@AfterEach'),
        ('Before all',    '@BeforeClass (static,public)','@BeforeAll  (static, any visibility)'),
        ('After all',     '@AfterClass  (static,public)','@AfterAll   (static, any visibility)'),
        ('Skip test',     '@Ignore',                     '@Disabled'),
        ('Extension',     '@RunWith(Runner.class)',       '@ExtendWith(Extension.class)'),
        ('Visibility',    'Methods MUST be public',       'Methods can be package-private'),
        ('Custom names',  'Not available',               '@DisplayName("friendly name")'),
        ('Group tests',   'Not available',               '@Nested  (inner test classes)'),
        ('Multi-input',   '@RunWith(Parameterized)',      '@ParameterizedTest + @ValueSource'),
        ('Exception test','try/catch pattern',            'assertThrows(Exception.class, ...)'),
        ('Group asserts', 'No assertAll()',               'assertAll() -- all run, all reported'),
    ]

    y0 = 10.85
    for i, (feature, j4, j5) in enumerate(rows):
        y = y0 - i * 0.72
        row_bg = '#1a1f29' if i % 2 == 0 else CARD
        p = FancyBboxPatch((0.2, y-0.28), 17.6, 0.58,
                           boxstyle='round,pad=0.02',
                           facecolor=row_bg, edgecolor='none', zorder=1)
        ax.add_patch(p)
        ax.text(1.8, y, feature, ha='center', va='center',
                fontsize=9, color=GRAY, fontweight='bold')
        ax.text(5.8, y, j4, ha='center', va='center',
                fontsize=8.8, color='#ff8888')
        ax.text(13.2,y, j5, ha='center', va='center',
                fontsize=8.8, color='#88ffbb')
        ax.axvline(x=9,   color='#30363d', lw=1,   ymin=0.02, ymax=0.98)
        ax.axvline(x=3.4, color='#30363d', lw=0.5, alpha=0.4)

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-JUnit4-vs-JUnit5.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── IMAGE 4: Manual Testing vs Unit Testing ───────────────────────────────────
def manual_vs_unit():
    fig, axes = plt.subplots(1, 2, figsize=(18, 10))
    bg(fig, axes)

    # ── LEFT: Manual Testing flow ──────────────────────────────
    ax = axes[0]
    ax.set_xlim(0,9); ax.set_ylim(0,10)
    ax.text(4.5, 9.7, 'Manual Testing  (Old Way)', ha='center',
            fontsize=13, color=RED, fontweight='bold')

    code_lines = [
        ("class Sol {",                    WHITE),
        ("  public int mult(int a,int b){", WHITE),
        ("    return a * b;",              TEAL),
        ("  }",                            WHITE),
        ("  public int div(int a,int b){",  WHITE),
        ("    return a / b;",              TEAL),
        ("  }",                            WHITE),
        ("}",                              WHITE),
        ("",                               WHITE),
        ("class Test {",                   WHITE),
        ("  public static void main(){",    WHITE),
        ("    Sol s = new Sol();",          BLUE),
        ("    int res = s.mult(5,6);",      ORANGE),
        ("    if(res == 30) {",             YELLOW),
        ('      S.O.P("Test Passed");',     GREEN),
        ("    } else {",                    YELLOW),
        ('      S.O.P("Test Failed");',     RED),
        ("    }",                           YELLOW),
        ("  }",                             WHITE),
        ("}",                               WHITE),
    ]
    code_bg = FancyBboxPatch((0.2,0.3),8.6,8.9,
                             boxstyle='round,pad=0.08',
                             facecolor='#0d1117', edgecolor=RED, lw=1.5)
    ax.add_patch(code_bg)
    for i,(ln,col) in enumerate(code_lines):
        ax.text(0.55, 9.0-i*0.42, ln, fontsize=8.5, color=col,
                family='monospace', va='center')

    # problems callout
    probs = ['No standard output', 'Write if/else manually every time',
             'Hard to manage 100s of tests', 'No automatic reports']
    for i,p in enumerate(probs):
        ax.text(0.5, 1.4-i*0.28, f'  {p}', fontsize=8, color='#ff8888')
    ax.text(0.5, 1.55, 'Problems:', fontsize=9, color=RED, fontweight='bold')

    # ── RIGHT: Unit Testing flow ────────────────────────────────
    ax2 = axes[1]
    ax2.set_xlim(0,9); ax2.set_ylim(0,10)
    ax2.text(4.5, 9.7, 'JUnit 5  Unit Testing  (Right Way)', ha='center',
             fontsize=13, color=GREEN, fontweight='bold')

    code2 = [
        ("import org.junit.jupiter.api.*;",          PURPLE),
        ("import static org.junit.jupiter.api",      PURPLE),
        ("        .Assertions.*;",                   PURPLE),
        ("",                                         WHITE),
        ("class SolTest {",                          WHITE),
        ("  Sol s = new Sol();",                     BLUE),
        ("",                                         WHITE),
        ("  @Test",                                  GREEN),
        ("  void testMultiply() {",                  WHITE),
        ("    assertEquals(30, s.mult(5, 6));",      TEAL),
        ("    // PASS -- no if/else needed!",         GRAY),
        ("  }",                                      WHITE),
        ("",                                         WHITE),
        ("  @Test",                                  GREEN),
        ("  void testDivide() {",                    WHITE),
        ("    assertEquals(2, s.div(4, 2));",        TEAL),
        ("  }",                                      WHITE),
        ("",                                         WHITE),
        ("  @Test",                                  GREEN),
        ("  void testDivByZero() {",                 WHITE),
        ("    assertThrows(",                         ORANGE),
        ("      ArithmeticException.class,",         ORANGE),
        ("      () -> s.div(10, 0));",               ORANGE),
        ("  }",                                      WHITE),
        ("}",                                        WHITE),
    ]
    code_bg2 = FancyBboxPatch((0.2,0.3),8.6,8.9,
                              boxstyle='round,pad=0.08',
                              facecolor='#0d1117', edgecolor=GREEN, lw=1.5)
    ax2.add_patch(code_bg2)
    for i,(ln,col) in enumerate(code2):
        ax2.text(0.45, 9.0-i*0.33, ln, fontsize=8.0, color=col,
                 family='monospace', va='center')

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-Manual-vs-Unit-Testing.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── IMAGE 5: All Assertions cheat sheet ──────────────────────────────────────
def assertions_cheatsheet():
    fig, ax = plt.subplots(figsize=(18, 13))
    bg(fig, ax)
    ax.set_xlim(0,18); ax.set_ylim(0,13)

    ax.text(9, 12.6, 'JUnit 5 -- Assertions Cheat Sheet',
            ha='center', fontsize=17, color=ORANGE, fontweight='bold')
    ax.text(9, 12.15,'Assertions = static methods to check actual vs expected result',
            ha='center', fontsize=10.5, color=GRAY)

    assertions = [
        (BLUE,   'assertEquals(expected, actual)',
                 'assertEquals(30, calc.mult(5,6));',
                 'Checks expected == actual  --  most common'),
        (GREEN,  'assertNotEquals(unexpected, actual)',
                 'assertNotEquals(10, calc.add(2,3));',
                 'Checks they are NOT equal'),
        (ORANGE, 'assertTrue(condition)',
                 'assertTrue(calc.isEven(4));',
                 'Checks condition is true'),
        (YELLOW, 'assertFalse(condition)',
                 'assertFalse(calc.isEven(7));',
                 'Checks condition is false'),
        (PURPLE, 'assertNull(object)',
                 'assertNull(userService.findById(999));',
                 'Checks object is null'),
        (PINK,   'assertNotNull(object)',
                 'assertNotNull(calc.greet("Vishnu"));',
                 'Checks object is not null'),
        (RED,    'assertThrows(Exception.class, () -> { })',
                 'assertThrows(ArithmeticException.class,\n   () -> calc.divide(10, 0));',
                 'Checks that exception IS thrown'),
        (TEAL,   'assertAll("label", () -> ..., () -> ...)',
                 'assertAll("calc",\n   () -> assertEquals(5, calc.add(2,3)),\n   () -> assertEquals(6, calc.multiply(2,3)));',
                 'Runs ALL assertions -- reports ALL failures at once'),
    ]

    for i, (col, name, code, desc) in enumerate(assertions):
        row = i
        y_base = 11.2 - row * 1.35
        row_bg = FancyBboxPatch((0.3, y_base-0.55), 17.4, 1.15,
                                boxstyle='round,pad=0.06',
                                facecolor=CARD, edgecolor=col, lw=1.2, zorder=1)
        ax.add_patch(row_bg)

        # method name
        ax.text(0.6,  y_base+0.3, name, fontsize=9, color=col,
                fontweight='bold', family='monospace', va='center')
        # description
        ax.text(0.6,  y_base-0.12, desc, fontsize=8.5, color=WHITE, va='center')
        # code
        code_bg = FancyBboxPatch((9.4, y_base-0.48), 8.2, 0.98,
                                 boxstyle='round,pad=0.04',
                                 facecolor='#0d1117', edgecolor=col, lw=0.8)
        ax.add_patch(code_bg)
        for j, cl in enumerate(code.split('\n')):
            ax.text(9.6, y_base+0.22-j*0.36, cl, fontsize=8.0,
                    color=TEAL, family='monospace', va='center')

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-Assertions-CheatSheet.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── IMAGE 6: Lifecycle annotations flow ──────────────────────────────────────
def lifecycle_flow():
    fig, ax = plt.subplots(figsize=(16, 9))
    bg(fig, ax)
    ax.set_xlim(0,16); ax.set_ylim(0,9)

    ax.text(8, 8.6, 'JUnit 5 -- Test Lifecycle Annotations',
            ha='center', fontsize=16, color=BLUE, fontweight='bold')

    # flow boxes
    steps = [
        (8,  7.4, GREEN,  '@BeforeAll',  'Runs ONCE before\nall tests in class\n(static method)'),
        (8,  5.8, BLUE,   '@BeforeEach', 'Runs before\nEVERY single test'),
        (8,  4.2, ORANGE, '@Test',       'Your actual\ntest method runs'),
        (8,  2.6, PURPLE, '@AfterEach',  'Runs after\nEVERY single test'),
        (8,  1.0, RED,    '@AfterAll',   'Runs ONCE after\nall tests in class\n(static method)'),
    ]
    for i,(x,y,col,name,desc) in enumerate(steps):
        step_bg = FancyBboxPatch((x-3.8, y-0.55), 7.6, 1.1,
                                 boxstyle='round,pad=0.08',
                                 facecolor=CARD, edgecolor=col, lw=2)
        ax.add_patch(step_bg)
        ax.text(x-2.2, y, name, ha='center', va='center',
                fontsize=12, color=col, fontweight='bold')
        ax.text(x+1.8, y, desc, ha='center', va='center',
                fontsize=8.5, color=WHITE)
        if i < len(steps)-1:
            arr(ax, x, y-0.55, x, steps[i+1][1]+0.55, col)

    # run count annotation
    ax.text(13.5, 5.8, 'Runs N times\n(once per test)', ha='center',
            fontsize=9, color=BLUE,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=CARD,
                      edgecolor=BLUE, lw=1))
    ax.annotate('', xy=(11.8, 5.8), xytext=(12.8, 5.8),
                arrowprops=dict(arrowstyle='<-', color=BLUE, lw=1.5))

    ax.text(13.5, 4.2, 'Runs N times\n(once per test)', ha='center',
            fontsize=9, color=ORANGE,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=CARD,
                      edgecolor=ORANGE, lw=1))
    ax.annotate('', xy=(11.8, 4.2), xytext=(12.8, 4.2),
                arrowprops=dict(arrowstyle='<-', color=ORANGE, lw=1.5))

    plt.tight_layout()
    path = os.path.join(OUT, 'Day-01-Lifecycle-Annotations.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ── run all ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    junit5_mindmap()
    junit5_architecture()
    junit4_vs_junit5()
    manual_vs_unit()
    assertions_cheatsheet()
    lifecycle_flow()
    print('\nAll JUnit 5 images generated successfully!')
