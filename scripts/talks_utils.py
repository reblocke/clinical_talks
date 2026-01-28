from __future__ import annotations

import re

SECTION_ORDER = [
    ("Airway & Ventilation", "airway-ventilation"),
    ("Pulmonary & Sleep", "pulmonary-sleep"),
    ("Critical Care", "critical-care"),
    ("Cardiology & Vascular", "cardiology-vascular"),
    ("Renal & Metabolic", "renal-metabolic"),
    ("Infectious & Immune", "infectious-immune"),
    ("Procedures & Devices", "procedures-devices"),
    ("Environmental & Occupational", "environmental-occupational"),
    ("Education & Research", "education-research"),
    ("Presentations", "presentations"),
    ("Miscellaneous", "miscellaneous"),
]

SECTION_SLUGS = {name: slug for name, slug in SECTION_ORDER}

SECTION_KEYWORDS = {
    "Airway & Ventilation": [
        "ards",
        "basic-ventilator",
        "control-of-ventilation",
        "intubation",
        "mechanisms-of-hypoxia",
        "oxygen-delivery",
        "patient-ventilator",
        "proning",
        "pulmonary-mechanics",
        "respiratory-failure",
        "tracheostomy",
        "ventilator",
        "ventilatory-failure",
        "weaning",
        "extubation",
    ],
    "Pulmonary & Sleep": [
        "asthma",
        "bronchiectasis",
        "bronchiolitis",
        "copd",
        "cpet",
        "cteph",
        "ecac",
        "eosinophilic",
        "hypersensitivity",
        "ild",
        "lung-cancer",
        "lung-transplant",
        "pleural",
        "pulmonary-function",
        "pulmonary-hypertension",
        "pulmonary-medicine",
        "reflux",
        "sarcoidosis",
        "sleep",
    ],
    "Critical Care": [
        "acute-pancreatitis",
        "alcohol-withdrawal",
        "aspiration",
        "cirrhosis",
        "ecmo",
        "family-updates",
        "goals-of-care",
        "hematologic",
        "hyperglycemic",
        "lactic-acidosis",
        "obstetrical",
        "sedation",
        "shock",
        "toxicology",
        "vasopressors",
    ],
    "Cardiology & Vascular": [
        "acls",
        "acs",
        "atrial-fibrillation",
        "cardiogenic",
        "fick-equation",
        "pa-catheter",
        "pacemakers",
        "vte",
    ],
    "Renal & Metabolic": [
        "acid-base",
        "aki",
        "bmp",
        "diuresis",
        "electrolytes",
        "metabolism",
        "renal-replacement",
        "sodium-balance",
    ],
    "Infectious & Immune": [
        "anaphylaxis",
        "angioedema",
        "antibiotic",
        "fungal",
        "mrsa",
        "pneumonia",
    ],
    "Procedures & Devices": [
        "arterial-line",
        "bronchoscopy",
        "central-venous",
        "chest-tubes",
        "critical-care-echo",
        "line-complications",
        "pocus",
        "procedure-index",
        "ultrasound",
    ],
    "Environmental & Occupational": [
        "air-pollution",
        "breath-hold",
        "diving",
        "hyperbarics",
        "inhalational",
        "occupational",
        "pneumoconioses",
    ],
    "Education & Research": [
        "education",
        "evidence-based",
        "medical-education",
        "teaching",
        "research",
        "index",
    ],
}

ACRONYMS = {
    "acs",
    "acls",
    "aki",
    "ards",
    "af",
    "ai",
    "bmp",
    "copd",
    "cpet",
    "cteph",
    "cxr",
    "ecmo",
    "edac",
    "ecac",
    "gi",
    "hfpef",
    "icu",
    "ild",
    "im",
    "mrsa",
    "osa",
    "pft",
    "pfts",
    "pgr",
    "rip",
    "rrt",
    "sdb",
    "tcc",
    "vte",
}


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return cleaned.strip("-") or "untitled"


def title_case(text: str) -> str:
    words = re.split(r"\s+", text.strip())
    normalized = []
    for word in words:
        stripped = re.sub(r"[^A-Za-z0-9]", "", word)
        if not stripped:
            normalized.append(word)
            continue
        lower = stripped.lower()
        if lower in ACRONYMS:
            normalized.append(word.replace(stripped, lower.upper()))
        else:
            normalized.append(word.capitalize())
    return " ".join(normalized).strip()


def normalize_presentation_stem(stem: str) -> str:
    cleaned = stem.replace("_", " ")
    cleaned = re.sub(r"\[[^\]]+\]", "", cleaned)
    cleaned = re.sub(r"\([^)]*autosaved[^)]*\)", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bcopy\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bcompressed\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bdiscarded\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bfinal\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bdraft\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bautosaved\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\breadonly\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\bread-only\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\b\d{4}-\d{1,2}-\d{1,2}\b", "", cleaned)
    cleaned = re.sub(r"\b\d{1,2}-\d{1,2}-\d{2,4}\b", "", cleaned)
    cleaned = re.sub(r"\b\d{1,2}\s\d{1,2}\s\d{2,4}\b", "", cleaned)
    cleaned = re.sub(r"\b\d{1,2}-\d{1,2}\b", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -")
    return cleaned.strip() or stem


def guess_section(text: str, path_parts: list[str]) -> str:
    lowered = text.lower()
    if any(part.lower() == "presentations" for part in path_parts):
        return "Presentations"
    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            pattern = rf"\b{re.escape(keyword)}\b"
            if re.search(pattern, lowered):
                return section
    return "Miscellaneous"
