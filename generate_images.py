import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import os

# ── colour palette ──────────────────────────────────────────────────────────
BG      = '#0d1117'
CARD    = '#161b22'
GREEN   = '#02b875'
BLUE    = '#58a6ff'
ORANGE  = '#f0883e'
PURPLE  = '#7f52ff'
GROOVY  = '#4298b8'
RED     = '#e94560'
YELLOW  = '#ffd700'
WHITE   = '#e6edf3'
GRAY    = '#8b949e'

def set_dark_bg(fig, ax_list):
    fig.patch.set_facecolor(BG)
    for ax in ax_list:
        ax.set_facecolor(BG)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

def rounded_box(ax, cx, cy, w, h, color, label, sublabel=None,
                fontsize=11, radius=0.04, text_color=WHITE, bold=True):
    box = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                         boxstyle=f"round,pad={radius}",
                         facecolor=color, edgecolor=color,
                         linewidth=1.5, zorder=3)
    ax.add_patch(box)
    dy = 0.012 if sublabel else 0
    weight = 'bold' if bold else 'normal'
    ax.text(cx, cy + dy, label, ha='center', va='center',
            fontsize=fontsize, color=text_color, fontweight=weight, zorder=4)
    if sublabel:
        ax.text(cx, cy - 0.055, sublabel, ha='center', va='center',
                fontsize=7.5, color=GRAY, zorder=4)

def draw_line(ax, x1, y1, x2, y2, color, lw=1.8, alpha=0.9, dash=False):
    ls = (0, (5, 4)) if dash else '-'
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw,
            alpha=alpha, linestyle=ls, zorder=1)

def arrow(ax, x1, y1, x2, y2, color, lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, connectionstyle='arc3,rad=0'))

OUT = os.path.dirname(os.path.abspath(__file__))
MAVEN_DIR  = os.path.join(OUT, 'maven')
GRADLE_DIR = os.path.join(OUT, 'gradle')
os.makedirs(MAVEN_DIR,  exist_ok=True)
os.makedirs(GRADLE_DIR, exist_ok=True)

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 1 — Maven Day-1 Mind Map
# ════════════════════════════════════════════════════════════════════════════
def maven_mindmap():
    fig, ax = plt.subplots(figsize=(18, 11))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 18); ax.set_ylim(0, 11)

    ax.text(9, 10.5, 'MAVEN  --  Day 1 Mind Map',
            ha='center', va='center', fontsize=18, color=GREEN,
            fontweight='bold')
    ax.text(9, 10.1, '30 June 2026  |  Author: Vishnu Vardhan',
            ha='center', va='center', fontsize=10, color=GRAY)

    # centre node
    rounded_box(ax, 9, 5.5, 2.2, 0.85, RED, 'MAVEN', 'Build Automation Tool',
                fontsize=14)

    branches = [
        (4.5, 8.5,   BLUE,   'Build\nLifecycle',     'compile→test→package'),
        (13.5, 8.5,  ORANGE, 'Project\nStructure',   'src/main·src/test·pom.xml'),
        (1.5, 5.5,   PURPLE, 'Repositories',         'Local·Central·Remote'),
        (16.5, 5.5,  BLUE,   'POM File',             'GroupId·ArtifactId·Version'),
        (4.5, 2.5,   ORANGE, 'Goals',                'clean·compile·test·package'),
        (13.5, 2.5,  GREEN,  'Dep vs Plugin',        'dependencies·build/plugins'),
    ]
    for bx, by, col, lbl, sub in branches:
        draw_line(ax, 9, 5.5, bx, by, col)
        rounded_box(ax, bx, by, 2.6, 0.95, CARD, lbl, sub,
                    fontsize=10, radius=0.06, text_color=col)

    # sub-nodes
    sub_nodes = [
        (2.5, 9.5,  BLUE,   'compile'),
        (4.5, 9.7,  BLUE,   'test'),
        (6.5, 9.5,  BLUE,   'package/deploy'),
        (0.6, 7.0,  PURPLE, '~/.m2/repo'),
        (0.6, 4.0,  PURPLE, 'repo1.maven.org'),
        (15.5, 7.0, BLUE,   'SNAPSHOT'),
        (15.5, 4.2, BLUE,   'RELEASE'),
        (2.2, 1.2,  ORANGE, 'mvn clean'),
        (4.8, 1.2,  ORANGE, 'mvn package'),
        (12.2,1.2,  GREEN,  '<dependencies>'),
        (14.8,1.2,  GREEN,  '<build><plugins>'),
    ]
    for sx, sy, col, lbl in sub_nodes:
        ax.plot(sx, sy, 'o', color=col, markersize=7, zorder=3)
        ax.text(sx, sy - 0.22, lbl, ha='center', va='top',
                fontsize=7.5, color=col)

    plt.tight_layout()
    path = os.path.join(MAVEN_DIR, 'Day-01-MindMap.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 2 — Maven Build Lifecycle Flow
# ════════════════════════════════════════════════════════════════════════════
def maven_lifecycle():
    fig, ax = plt.subplots(figsize=(18, 6))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 18); ax.set_ylim(0, 6)

    ax.text(9, 5.6, 'Maven Build Lifecycle — Default Phase Flow',
            ha='center', fontsize=16, color=RED, fontweight='bold')

    phases = [
        (1.4, 3.0, GREEN,  'validate',  'checks\nproject'),
        (3.6, 3.0, BLUE,   'compile',   '.java →\n.class'),
        (5.8, 3.0, ORANGE, 'test',      'JUnit\ntests'),
        (8.0, 3.0, PURPLE, 'package',   'creates\nJAR/WAR'),
        (10.2,3.0, GROOVY, 'verify',    'integration\ntests'),
        (12.4,3.0, RED,    'install',   'copy to\n~/.m2'),
        (14.6,3.0, YELLOW, 'deploy',    'upload to\nremote'),
    ]
    for i, (x, y, col, name, desc) in enumerate(phases):
        rounded_box(ax, x, y, 1.8, 1.1, col, name, desc,
                    fontsize=10, text_color='#0d1117')
        if i < len(phases) - 1:
            arrow(ax, x + 0.9, y, phases[i+1][0] - 0.9, y, WHITE)

    # labels above
    ax.text(9, 1.4, 'mvn package  =  validate + compile + test + package  (runs ALL previous phases)',
            ha='center', fontsize=11, color=GRAY,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=CARD, edgecolor=GREEN, lw=1.2))

    # clean + site
    rounded_box(ax, 3,  0.7, 2.2, 0.6, CARD, 'clean lifecycle',
                'mvn clean  →  deletes target/', fontsize=9,
                text_color=ORANGE, radius=0.05)
    rounded_box(ax, 14, 0.7, 2.2, 0.6, CARD, 'site lifecycle',
                'mvn site  →  generates docs', fontsize=9,
                text_color=GROOVY, radius=0.05)

    plt.tight_layout()
    path = os.path.join(MAVEN_DIR, 'Day-01-Build-Lifecycle.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 3 — Maven Repositories Flow
# ════════════════════════════════════════════════════════════════════════════
def maven_repos():
    fig, ax = plt.subplots(figsize=(14, 9))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 14); ax.set_ylim(0, 9)

    ax.text(7, 8.6, 'Maven Repository Flow',
            ha='center', fontsize=16, color=GREEN, fontweight='bold')

    # boxes
    rounded_box(ax, 7,   7.2, 3.2, 0.9,  BLUE,   'Maven App',
                'your project  (pom.xml)', fontsize=12)
    rounded_box(ax, 7,   5.0, 3.2, 0.9,  PURPLE, 'Local Repository',
                '~/.m2/repository  (your machine)', fontsize=11)
    rounded_box(ax, 3,   2.6, 3.2, 0.9,  GREEN,  'Maven Central',
                'repo1.maven.org  (online)', fontsize=11)
    rounded_box(ax, 11,  2.6, 3.2, 0.9,  ORANGE, 'Remote Repository',
                'Company / Private server', fontsize=11)

    # arrows
    arrow(ax, 7, 6.75, 7, 5.45, WHITE)
    ax.text(7.15, 6.1, '1. needs dependency', fontsize=9, color=GRAY)

    # found / not found split
    arrow(ax, 5.4, 5.0, 3.0, 3.05, GREEN)
    ax.text(3.5, 4.2, 'NOT FOUND\ndownload', fontsize=9, color=GREEN,
            ha='center')

    arrow(ax, 3.0, 3.05, 5.4, 5.0, GROOVY)
    ax.text(4.1, 3.85, 'save to\nlocal', fontsize=8, color=GROOVY,
            ha='center')

    ax.annotate('', xy=(8.8, 5.0), xytext=(9.6, 5.0),
                arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(9.9, 5.1, 'Remote\ncheck', fontsize=8, color=ORANGE)

    # found checkmark
    ax.text(5.2, 5.5, 'FOUND!\nuse directly (fast)', fontsize=9,
            color=YELLOW, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=CARD, edgecolor=YELLOW))

    # first-time vs next-time note
    ax.text(7, 1.1,
            '1st time: App → Local (miss) → Central (download) → Local (cache)\n'
            'Next time: App → Local (hit — fast!) — no internet needed!',
            ha='center', fontsize=10, color=GRAY,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD,
                      edgecolor=GREEN, lw=1.2))

    plt.tight_layout()
    path = os.path.join(MAVEN_DIR, 'Day-01-Repositories.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 4 — Gradle Day-1 Mind Map
# ════════════════════════════════════════════════════════════════════════════
def gradle_mindmap():
    fig, ax = plt.subplots(figsize=(18, 11))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 18); ax.set_ylim(0, 11)

    ax.text(9, 10.5, 'GRADLE  --  Day 1 Mind Map',
            ha='center', fontsize=18, color=GREEN, fontweight='bold')
    ax.text(9, 10.1, '1 July 2026  |  Author: Vishnu Vardhan',
            ha='center', fontsize=10, color=GRAY)

    # centre
    rounded_box(ax, 9, 5.5, 2.4, 0.9, GREEN, 'GRADLE', 'Build Tool',
                fontsize=14, text_color='#0d1117')

    branches = [
        (4.0, 8.5,  BLUE,   'What is\nGradle?',        'open-source · fast'),
        (14.0,8.5,  ORANGE, 'Gradle vs\nMaven',        'faster · flexible'),
        (1.5, 5.5,  GROOVY, 'Groovy DSL',              'build.gradle'),
        (16.5,5.5,  PURPLE, 'Kotlin DSL',              'build.gradle.kts'),
        (4.0, 2.5,  RED,    'Project\nStructure',      'src · build · wrapper'),
        (14.0,2.5,  YELLOW, 'Gradle\nWrapper',         'gradlew.bat · no install'),
    ]
    for bx, by, col, lbl, sub in branches:
        draw_line(ax, 9, 5.5, bx, by, col)
        rounded_box(ax, bx, by, 2.8, 0.95, CARD, lbl, sub,
                    fontsize=10, radius=0.06, text_color=col)

    # sub-nodes
    subs = [
        (2.0, 9.6,  BLUE,   'Java·Kotlin·Groovy'),
        (5.5, 9.6,  BLUE,   'Scala·C++·Swift'),
        (12.2,9.6,  ORANGE, 'Incremental Build'),
        (15.8,9.6,  ORANGE, 'Android default'),
        (0.5, 7.0,  GROOVY, "'single quotes'"),
        (0.5, 4.2,  GROOVY, 'no parens'),
        (16.5,7.0,  PURPLE, '"double quotes"'),
        (16.5,4.2,  PURPLE, 'parens required'),
        (2.5, 1.2,  RED,    'build.gradle'),
        (5.2, 1.2,  RED,    'src/main/java'),
        (12.5,1.2,  YELLOW, 'gradlew.bat'),
        (15.0,1.2,  YELLOW, 'wrapper.properties'),
    ]
    for sx, sy, col, lbl in subs:
        ax.plot(sx, sy, 'o', color=col, markersize=7, zorder=3)
        ax.text(sx, sy - 0.22, lbl, ha='center', va='top',
                fontsize=7.5, color=col)

    plt.tight_layout()
    path = os.path.join(GRADLE_DIR, 'Day-01-MindMap.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 5 — Gradle vs Maven Comparison
# ════════════════════════════════════════════════════════════════════════════
def gradle_vs_maven():
    fig, ax = plt.subplots(figsize=(16, 10))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 16); ax.set_ylim(0, 10)

    ax.text(8, 9.6, 'Maven  vs  Gradle — Full Comparison',
            ha='center', fontsize=16, color=WHITE, fontweight='bold')

    # column headers
    rounded_box(ax, 4,  8.8, 5.5, 0.7, RED,   'MAVEN', fontsize=14,
                text_color=WHITE)
    rounded_box(ax, 12, 8.8, 5.5, 0.7, GREEN, 'GRADLE', fontsize=14,
                text_color='#0d1117')
    ax.text(8, 8.8, 'VS', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='black')

    rows = [
        ('Config File',      'pom.xml  (XML)',             'build.gradle / build.gradle.kts'),
        ('Language',         'XML — markup only',          'Groovy or Kotlin DSL'),
        ('Performance',      'Slower',                 'Faster (Incremental Build)'),
        ('Flexibility',      'Fixed conventions',          'Highly customizable'),
        ('Supported Langs',  'Java, Spring Boot only',     'Java·Kotlin·Groovy·Scala·C++·Swift'),
        ('Industry Usage',   'Java Enterprise projects',   'Android + Modern projects'),
        ('Learning Curve',   'Easier (just XML)',          'Moderate (need DSL knowledge)'),
    ]
    y_start = 7.8
    for i, (feature, maven_val, gradle_val) in enumerate(rows):
        y = y_start - i * 0.95
        row_bg = '#1a1f29' if i % 2 == 0 else CARD
        bg = FancyBboxPatch((0.3, y - 0.35), 15.4, 0.75,
                            boxstyle='round,pad=0.02',
                            facecolor=row_bg, edgecolor='none', zorder=1)
        ax.add_patch(bg)
        ax.text(2.0, y + 0.02, feature, ha='center', va='center',
                fontsize=10, color=GRAY, fontweight='bold')
        ax.text(5.5, y + 0.02, maven_val, ha='center', va='center',
                fontsize=9.5, color='#ff8888')
        ax.text(11.8, y + 0.02, gradle_val, ha='center', va='center',
                fontsize=9.5, color='#88ffbb')
        ax.axvline(x=7.8, color='#30363d', lw=1, ymin=0.05, ymax=0.95)
        ax.axvline(x=3.6, color='#30363d', lw=0.6, alpha=0.5)

    # Incremental build visual
    ax.text(8, 0.7,
            'Incremental Build Example:  1000 files, 5 changed  →  '
            'Maven rebuilds ALL 1000 [X]   |   Gradle rebuilds ONLY 5 [OK]',
            ha='center', fontsize=10, color=GRAY,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=CARD,
                      edgecolor=GREEN, lw=1.2))

    plt.tight_layout()
    path = os.path.join(GRADLE_DIR, 'Day-01-Gradle-vs-Maven.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 6 — Groovy DSL vs Kotlin DSL
# ════════════════════════════════════════════════════════════════════════════
def groovy_vs_kotlin():
    fig, ax = plt.subplots(figsize=(18, 12))
    set_dark_bg(fig, [ax])
    ax.set_xlim(0, 18); ax.set_ylim(0, 12)

    ax.text(9, 11.6, 'Groovy DSL  vs  Kotlin DSL',
            ha='center', fontsize=18, color=WHITE, fontweight='bold')
    ax.text(9, 11.2, 'Two ways to write your Gradle build script',
            ha='center', fontsize=11, color=GRAY)

    # --- left panel: Groovy ---
    groovy_bg = FancyBboxPatch((0.3, 0.3), 7.9, 10.5,
                               boxstyle='round,pad=0.1',
                               facecolor='#0f1f2e', edgecolor=GROOVY, lw=2)
    ax.add_patch(groovy_bg)
    ax.text(4.5, 9.7, 'GROOVY DSL', ha='center', fontsize=14,
            color=GROOVY, fontweight='bold')
    ax.text(4.25, 10.15, 'File: build.gradle', ha='center', fontsize=10, color=GRAY)

    groovy_props = [
        ('Dynamic typing',         '— flexible, less strict'),
        ("'single quotes' strings",'— for dependency coords'),
        ('No parentheses needed',  '— shorter syntax'),
        ('Older projects',         '— widely used in legacy code'),
        ('Less IDE auto-complete', '— editor gives basic hints'),
        ('Beginner friendly',      '— easier to start with'),
    ]
    for i, (k, v) in enumerate(groovy_props):
        y = 9.4 - i * 0.62
        ax.text(0.9, y, f'•  {k}', fontsize=9.5, color=GROOVY, va='center')
        ax.text(5.0, y, v,         fontsize=9,   color=GRAY,   va='center')

    # code block Groovy
    code_g = [
        "// build.gradle  (Groovy DSL)",
        "plugins {",
        "    id 'java'",
        "    id 'org.springframework.boot'",
        "       version '3.1.0'",
        "}",
        "",
        "dependencies {",
        "    implementation",
        "      'org.springframework.boot:",
        "       spring-boot-starter:3.1.0'",
        "    testImplementation",
        "      'junit:junit:4.13.2'",
        "}",
    ]
    code_bg = FancyBboxPatch((0.5, 0.5), 7.4, 5.0,
                             boxstyle='round,pad=0.1',
                             facecolor='#0d1117', edgecolor=GROOVY, lw=1)
    ax.add_patch(code_bg)
    for i, line in enumerate(code_g):
        color = GROOVY if line.startswith('//') else (
                ORANGE if any(k in line for k in ['plugins','dependencies','id ','implementation','testImpl']) else
                GREEN  if line.strip().startswith(("'org","'junit")) else WHITE)
        ax.text(0.75, 5.3 - i * 0.33, line, fontsize=7.8,
                color=color, family='monospace', va='center')

    # --- right panel: Kotlin ---
    kotlin_bg = FancyBboxPatch((9.8, 0.3), 7.9, 10.5,
                               boxstyle='round,pad=0.1',
                               facecolor='#130f2a', edgecolor=PURPLE, lw=2)
    ax.add_patch(kotlin_bg)
    ax.text(13.75, 10.55, 'KOTLIN DSL', ha='center', fontsize=14,
            color=PURPLE, fontweight='bold')
    ax.text(13.75, 10.15, 'File: build.gradle.kts', ha='center',
            fontsize=10, color=GRAY)

    kotlin_props = [
        ('Static typing',           '— strict, catches errors early'),
        ('"double quotes" strings', '— required in Kotlin'),
        ('Parentheses required',    '— more explicit syntax'),
        ('Modern projects',         '— new/team projects prefer this'),
        ('Full IDE auto-complete',  '— best editor support [OK]'),
        ('Better for large teams',  '— clear, readable code'),
    ]
    for i, (k, v) in enumerate(kotlin_props):
        y = 9.4 - i * 0.62
        ax.text(10.3, y, f'•  {k}', fontsize=9.5, color=PURPLE, va='center')
        ax.text(14.4, y, v,          fontsize=9,   color=GRAY,   va='center')

    code_k = [
        "// build.gradle.kts  (Kotlin DSL)",
        "plugins {",
        '    java',
        '    id("org.springframework.boot")',
        '       version "3.1.0"',
        "}",
        "",
        "dependencies {",
        '    implementation(',
        '      "org.springframework.boot:',
        '       spring-boot-starter:3.1.0")',
        '    testImplementation(',
        '      "junit:junit:4.13.2")',
        "}",
    ]
    code_bg2 = FancyBboxPatch((10.0, 0.5), 7.4, 5.0,
                              boxstyle='round,pad=0.1',
                              facecolor='#0d1117', edgecolor=PURPLE, lw=1)
    ax.add_patch(code_bg2)
    for i, line in enumerate(code_k):
        color = PURPLE if line.startswith('//') else (
                ORANGE if any(k in line for k in ['plugins','dependencies','id(','implementation','testImpl','java']) else
                GREEN  if line.strip().startswith(('"org','"junit')) else WHITE)
        ax.text(10.25, 5.3 - i * 0.33, line, fontsize=7.8,
                color=color, family='monospace', va='center')

    # VS badge in middle
    ax.text(9, 5.5, 'VS', ha='center', va='center',
            fontsize=22, color=WHITE, fontweight='black',
            bbox=dict(boxstyle='circle,pad=0.3', facecolor=RED, edgecolor=WHITE, lw=1.5))

    plt.tight_layout()
    path = os.path.join(GRADLE_DIR, 'Day-01-Groovy-vs-Kotlin.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 7 — Gradle Project Structure + Wrapper
# ════════════════════════════════════════════════════════════════════════════
def gradle_structure():
    fig, axes = plt.subplots(1, 2, figsize=(18, 10))
    set_dark_bg(fig, axes)

    # --- LEFT: Project Structure tree ---
    ax = axes[0]
    ax.set_xlim(0, 9); ax.set_ylim(0, 10)
    ax.text(4.5, 9.7, 'Gradle Project Structure', ha='center',
            fontsize=14, color=GREEN, fontweight='bold')

    tree = [
        (0.3, 'my-project/',               GREEN,  12, True),
        (0.8, '├── build.gradle',          BLUE,   10, False),
        (1.5, '│   (main build script)',   GRAY,    9, False),
        (0.8, '├── settings.gradle',       BLUE,   10, False),
        (1.5, '│   (project name)',        GRAY,    9, False),
        (0.8, '├── gradlew',              ORANGE,  10, False),
        (1.5, '│   (Linux/Mac script)',    GRAY,    9, False),
        (0.8, '├── gradlew.bat',          ORANGE,  10, False),
        (1.5, '│   (Windows script [OK])',GRAY,    9, False),
        (0.8, '├── gradle/wrapper/',      YELLOW,  10, False),
        (1.5, '│   (version info files)', GRAY,    9, False),
        (0.8, '├── src/',                 WHITE,   10, False),
        (1.3, '│   ├── main/java/',       GREEN,   10, False),
        (1.8, '│   │   (your code)',       GRAY,    9, False),
        (1.3, '│   ├── main/resources/',  GROOVY,  10, False),
        (1.8, '│   │   (configs, props)', GRAY,    9, False),
        (1.3, '│   └── test/java/',       PURPLE,  10, False),
        (1.8, '│       (unit tests)',      GRAY,    9, False),
        (0.8, '└── build/',               RED,     10, False),
        (1.5,  '    (auto-generated output)',GRAY,  9, False),
    ]
    for i, (indent, text, color, size, bold) in enumerate(tree):
        y = 9.1 - i * 0.43
        ax.text(indent, y, text, fontsize=size, color=color,
                fontweight='bold' if bold else 'normal', family='monospace')

    # --- RIGHT: Gradle Wrapper explanation ---
    ax2 = axes[1]
    ax2.set_xlim(0, 9); ax2.set_ylim(0, 10)
    ax2.text(4.5, 9.7, 'Gradle Wrapper Explained', ha='center',
             fontsize=14, color=YELLOW, fontweight='bold')

    # definition box
    def_box = FancyBboxPatch((0.3, 8.2), 8.4, 1.1,
                             boxstyle='round,pad=0.1',
                             facecolor=CARD, edgecolor=YELLOW, lw=1.5)
    ax2.add_patch(def_box)
    ax2.text(4.5, 8.85, 'Gradle Wrapper = scripts + small JAR files',
             ha='center', fontsize=10, color=YELLOW, fontweight='bold')
    ax2.text(4.5, 8.45, 'Run Gradle WITHOUT installing it on your machine',
             ha='center', fontsize=9.5, color=WHITE)

    # analogy
    ax2.text(4.5, 7.85, 'Analogy:', ha='center', fontsize=10, color=GRAY)
    ax2.text(4.5, 7.45,
             'Like a game that comes with its own launcher.\n'
             'You don\'t install anything — just run gradlew.bat!',
             ha='center', fontsize=9.5, color=WHITE, style='italic')

    # files
    ax2.text(0.5, 6.85, 'Wrapper files:', fontsize=10, color=ORANGE, fontweight='bold')
    files = [
        ('gradlew',                    'Shell script for Linux / Mac'),
        ('gradlew.bat',                'Batch script for Windows'),
        ('gradle-wrapper.jar',         'Downloads the right Gradle version'),
        ('gradle-wrapper.properties',  'Stores which version to use'),
    ]
    for i, (f, desc) in enumerate(files):
        y = 6.35 - i * 0.62
        ax2.text(0.7,  y, f,    fontsize=9.5, color=YELLOW, family='monospace')
        ax2.text(3.8,  y, desc, fontsize=9,   color=GRAY)

    # commands
    ax2.text(0.5, 3.85, 'Commands:', fontsize=10, color=GREEN, fontweight='bold')
    cmds = [
        ('Windows:',   'gradlew.bat build'),
        ('Windows:',   'gradlew.bat test'),
        ('Linux/Mac:', './gradlew build'),
        ('Linux/Mac:', './gradlew test'),
    ]
    for i, (sys, cmd) in enumerate(cmds):
        y = 3.35 - i * 0.58
        ax2.text(0.7, y, sys, fontsize=9,   color=GRAY)
        ax2.text(2.5, y, cmd, fontsize=9.5, color=GREEN, family='monospace')

    # without vs with wrapper
    ax2.text(0.5, 1.35, 'Without wrapper:', fontsize=9, color=RED)
    ax2.text(0.5, 0.95, 'Dev A: Gradle 7, Dev B: Gradle 8 → CONFLICT [X]',
             fontsize=8.5, color='#ff8888')
    ax2.text(0.5, 0.58, 'With wrapper:', fontsize=9, color=GREEN)
    ax2.text(0.5, 0.2,  'Everyone uses same version from wrapper.properties  [OK]',
             fontsize=8.5, color='#88ffbb')

    plt.suptitle('', y=0)
    plt.tight_layout()
    path = os.path.join(GRADLE_DIR, 'Day-01-Structure-and-Wrapper.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'Saved: {path}')


# ── run all ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    maven_mindmap()
    maven_lifecycle()
    maven_repos()
    gradle_mindmap()
    gradle_vs_maven()
    groovy_vs_kotlin()
    gradle_structure()
    print('\nAll images generated successfully!')
