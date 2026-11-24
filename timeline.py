# SEP350 Presentation Workflow — Graph Databases & Social Network Analysis
# Team: Son, Eugene (Yevhenii), Zarlasht | Deadline: Tue Dec 1, 2026

TEAM = ["Son", "Eugene", "Zarlasht"]

timeline = {

    "Tue Nov 24": {                       # TODAY: kickoff
        "tasks": [
            "read Presentation Topics & Instructions (time limit, slide count, rubric)",
            "agree on outline in group chat",
            "assign sections -> 2 per person",
            "create shared slide deck (Google Slides / PPT)",
        ],
        "done_when": "everyone knows their sections",
    },

    "Wed Nov 25": {                       # research
        "tasks": [
            "each person researches own sections",
            "collect sources (keep links for References slide)",
            "Son: build graph vs SQL example (friends-of-friends query)",
        ],
        "done_when": "bullet notes + sources for every section",
    },

    "Thu Nov 26": {                       # draft slides
        "tasks": [
            "turn notes into slides (max ~5 bullets each)",
            "add diagrams: nodes/edges, SQL JOIN vs Cypher",
        ],
        "done_when": "rough draft of ALL slides in deck",
    },

    "Fri Nov 27": {                       
        "tasks": [
            "light day: review teammates' slides, leave comments",
        ],
    },

    "Sat Nov 28": {                       # merge + polish
        "tasks": [
            "unify design (fonts, colors, layout)",
            "fix flow + transitions between speakers",
            "write speaker notes",
            "FIRST full practice run (call or in person) + time it",
        ],
        "done_when": "deck is 95% final",
    },

    "Sun Nov 29": {                       # MillionRose shift
        "tasks": [
            "solo: rehearse own part 2-3x",
        ],
    },

    "Mon Nov 30": {                       # final check
        "tasks": [
            "SECOND full run-through, check time limit",
            "prep Q&A: 'Why not just use SQL?', 'When NOT to use graph DB?'",
            "submit / upload deck if required",
            "backup: PDF on USB + email + Drive",
        ],
        "freeze": True,                   # no new content after today
    },

    "Tue Dec 1": {                        # PRESENT
        "tasks": [
            "arrive early, test laptop/projector",
            "present",
            "complete Peer Review - Presentations on Blackboard",
        ],
    },
}

outline = [
    ("Intro + What is a Graph DB",              "Speaker A"),
    ("Nodes, Edges, Properties",                "Speaker A"),
    ("Graph DB vs Relational (JOIN vs Cypher)", "Speaker B"),
    ("Neo4j + Cypher basics",                   "Speaker B"),
    ("Social Network Analysis use cases",       "Speaker C"),
    ("Real examples, Pros/Cons, Conclusion",    "Speaker C"),
]

# after Dec 1 -> switch to Assignment 2 (due Tue Dec 8, 11:59 PM)


if __name__ == "__main__":
    print("=== SEP350 Presentation Timeline ===\n")
    for day, info in timeline.items():
        print(f"[{day}]")
        for task in info["tasks"]:
            print(f"  - {task}")
        if "done_when" in info:
            print(f"  done when: {info['done_when']}")
        if info.get("freeze"):
            print("  FREEZE: no new content after today")
        print()

    print("=== Outline ===")
    for section, speaker in outline:
        print(f"  {speaker}: {section}")