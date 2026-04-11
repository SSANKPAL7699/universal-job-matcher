# Universal Skills Database
# Covers 15 fields with 300+ skills
# This is the brain of the Universal Job Matcher

FIELDS = {

    # ── TECHNOLOGY ────────────────────────────────────────────
    "Software Engineering": {
        "keywords": [
            "software", "developer", "engineer", "programming",
            "coding", "backend", "frontend", "fullstack", "computer science"
        ],
        "skills": {
            "languages": [
                "python", "java", "javascript", "typescript", "kotlin",
                "swift", "rust", "scala", "php", "ruby", "bash", "golang",
                "html", "css", "sql", "abap", "c++", "c#"
            ],
            "frameworks": [
                "fastapi", "flask", "django", "react", "react native",
                "angular", "vue", "nodejs", "spring boot", "express",
                "graphql", "rest api", "microservices", "bootstrap"
            ],
            "databases": [
                "postgresql", "mysql", "mongodb", "redis", "sqlite",
                "dynamodb", "cassandra", "elasticsearch", "firebase",
                "supabase", "sql server", "oracle", "sap hana"
            ],
            "devops": [
                "docker", "kubernetes", "aws", "azure", "gcp",
                "github actions", "jenkins", "terraform", "ansible",
                "nginx", "linux", "ci/cd", "git", "github"
            ],
        },
        "tips": {
            "missing_languages": "Add the specific programming languages from the JD to your skills section.",
            "missing_frameworks": "Highlight relevant frameworks in your project descriptions.",
            "missing_devops": "Consider adding cloud/DevOps projects to your GitHub.",
            "general": "Quantify your impact — e.g. 'reduced load time by 40%' beats 'improved performance'."
        }
    },

    # ── DATA ──────────────────────────────────────────────────
    "Data Science & Analytics": {
        "keywords": [
            "data scientist", "data analyst", "data engineer", "analytics",
            "machine learning", "artificial intelligence", "business intelligence",
            "data", "insights", "statistical", "ml engineer"
        ],
        "skills": {
            "languages": [
                "python", "r", "sql", "scala", "julia"
            ],
            "ml_ai": [
                "machine learning", "deep learning", "nlp", "computer vision",
                "scikit-learn", "tensorflow", "pytorch", "keras", "xgboost",
                "lightgbm", "random forest", "neural network", "llm",
                "hugging face", "transformers", "bert", "feature engineering",
                "model deployment", "mlflow", "regression", "classification",
                "clustering", "a/b testing", "statistical analysis"
            ],
            "data_tools": [
                "pandas", "numpy", "matplotlib", "seaborn", "plotly",
                "tableau", "power bi", "looker", "dbt", "airflow",
                "spark", "hadoop", "kafka", "snowflake", "bigquery",
                "redshift", "databricks", "jupyter", "google colab"
            ],
            "databases": [
                "postgresql", "mysql", "mongodb", "bigquery", "snowflake",
                "redshift", "elasticsearch", "dynamodb"
            ],
        },
        "tips": {
            "missing_ml_ai": "Add ML projects with measurable outcomes — accuracy %, dataset size, business impact.",
            "missing_data_tools": "Tableau and Power BI are in high demand — consider getting certified.",
            "general": "Include a Kaggle profile or GitHub with notebooks showing your analysis work."
        }
    },

    # ── MARKETING ─────────────────────────────────────────────
    "Marketing": {
        "keywords": [
            "marketing", "brand", "campaign", "digital marketing", "content",
            "seo", "social media", "growth", "demand generation", "cmо"
        ],
        "skills": {
            "digital_marketing": [
                "seo", "sem", "google ads", "facebook ads", "instagram ads",
                "tiktok ads", "linkedin ads", "ppc", "display advertising",
                "programmatic advertising", "affiliate marketing",
                "email marketing", "content marketing", "inbound marketing",
                "growth hacking", "conversion rate optimization", "cro"
            ],
            "analytics": [
                "google analytics", "google tag manager", "mixpanel",
                "amplitude", "hotjar", "semrush", "ahrefs", "moz",
                "hubspot", "marketo", "salesforce marketing cloud",
                "klaviyo", "mailchimp", "a/b testing"
            ],
            "content": [
                "copywriting", "content strategy", "social media management",
                "brand strategy", "market research", "competitive analysis",
                "influencer marketing", "public relations", "pr",
                "video marketing", "podcast marketing", "storytelling"
            ],
            "tools": [
                "hubspot", "salesforce", "marketo", "canva", "figma",
                "hootsuite", "buffer", "sprout social", "wordpress",
                "shopify", "webflow", "adobe creative suite"
            ],
        },
        "tips": {
            "missing_digital_marketing": "Add specific ad platforms you've used with ROI or ROAS metrics.",
            "missing_analytics": "Google Analytics certification is free and highly valued.",
            "general": "Quantify everything — 'grew organic traffic by 150%' is far stronger than 'managed SEO'."
        }
    },

    # ── FINANCE ───────────────────────────────────────────────
    "Finance": {
        "keywords": [
            "finance", "financial", "investment", "banking", "accounting",
            "analyst", "portfolio", "equity", "trading", "cfa", "cpa",
            "fintech", "treasury", "audit", "tax"
        ],
        "skills": {
            "financial_skills": [
                "financial modeling", "valuation", "dcf", "lbo",
                "mergers and acquisitions", "private equity", "venture capital",
                "investment banking", "equity research", "portfolio management",
                "risk management", "derivatives", "fixed income",
                "financial analysis", "budgeting", "forecasting",
                "variance analysis", "p&l management"
            ],
            "accounting": [
                "gaap", "ifrs", "accounting", "bookkeeping", "tax",
                "audit", "compliance", "financial reporting",
                "accounts payable", "accounts receivable", "reconciliation"
            ],
            "tools": [
                "excel", "bloomberg", "factset", "capital iq", "quickbooks",
                "sap", "oracle financials", "tableau", "power bi",
                "python", "sql", "vba", "matlab"
            ],
        },
        "tips": {
            "missing_financial_skills": "Add specific deal sizes or portfolio values you've worked with.",
            "missing_tools": "Bloomberg certification and advanced Excel modeling are highly valued.",
            "general": "CFA or CPA certifications significantly boost your profile for finance roles."
        }
    },

    # ── DESIGN ────────────────────────────────────────────────
    "Design": {
        "keywords": [
            "designer", "ux", "ui", "product design", "graphic design",
            "visual design", "interaction design", "user experience",
            "user interface", "creative", "design thinking"
        ],
        "skills": {
            "design_tools": [
                "figma", "sketch", "adobe xd", "invision", "zeplin",
                "photoshop", "illustrator", "after effects", "premiere pro",
                "indesign", "canva", "framer", "principle"
            ],
            "ux_skills": [
                "ux design", "ui design", "user research", "wireframing",
                "prototyping", "usability testing", "information architecture",
                "design systems", "accessibility", "wcag", "heuristic evaluation",
                "journey mapping", "persona creation", "a/b testing"
            ],
            "soft_skills": [
                "typography", "color theory", "layout", "branding",
                "visual hierarchy", "responsive design", "motion design",
                "design thinking", "storytelling", "presentation"
            ],
        },
        "tips": {
            "missing_design_tools": "Add a portfolio link — design roles require seeing your work.",
            "missing_ux_skills": "Include case studies showing your design process, not just final outputs.",
            "general": "Behance or Dribbble portfolio is essential for design roles."
        }
    },

    # ── SALES ─────────────────────────────────────────────────
    "Sales": {
        "keywords": [
            "sales", "account executive", "business development", "revenue",
            "quota", "pipeline", "closing", "b2b", "b2c", "saas sales",
            "enterprise sales", "inside sales", "account manager"
        ],
        "skills": {
            "sales_skills": [
                "b2b sales", "b2c sales", "saas sales", "enterprise sales",
                "inside sales", "outside sales", "cold calling", "prospecting",
                "lead generation", "pipeline management", "account management",
                "negotiation", "closing", "upselling", "cross selling",
                "business development", "revenue growth", "quota attainment"
            ],
            "tools": [
                "salesforce", "hubspot", "outreach", "salesloft", "zoominfo",
                "linkedin sales navigator", "gong", "chorus", "apollo",
                "pipedrive", "close", "zoho crm"
            ],
            "methodologies": [
                "meddic", "spin selling", "challenger sale", "solution selling",
                "value selling", "sandler", "consultative selling"
            ],
        },
        "tips": {
            "missing_sales_skills": "Always include quota attainment % — e.g. '125% of quota consistently'.",
            "missing_tools": "Salesforce CRM experience is required for most enterprise sales roles.",
            "general": "Numbers close deals and get interviews — every bullet needs a metric."
        }
    },

    # ── HEALTHCARE ────────────────────────────────────────────
    "Healthcare": {
        "keywords": [
            "healthcare", "medical", "clinical", "nurse", "physician",
            "patient", "hospital", "health", "pharmaceutical", "biotech",
            "public health", "mental health", "therapy"
        ],
        "skills": {
            "clinical": [
                "patient care", "clinical trials", "diagnosis", "treatment",
                "nursing", "pharmacology", "medical coding", "icd-10",
                "cpt codes", "hipaa", "fda", "clinical research",
                "medical writing", "telemedicine", "ehr"
            ],
            "systems": [
                "epic", "cerner", "meditech", "allscripts", "athenahealth",
                "nextgen", "practice fusion", "eclinicalworks"
            ],
            "certifications": [
                "rn", "md", "np", "pa", "cna", "lpn", "cma",
                "bls", "acls", "pals", "cpr", "hipaa compliance"
            ],
        },
        "tips": {
            "missing_clinical": "Highlight patient outcomes and quality metrics in your experience.",
            "missing_systems": "EHR system experience (Epic, Cerner) is highly valued.",
            "general": "Include any certifications, licenses, and continuing education prominently."
        }
    },

    # ── OPERATIONS ────────────────────────────────────────────
    "Operations": {
        "keywords": [
            "operations", "project manager", "program manager", "supply chain",
            "logistics", "process improvement", "business operations",
            "chief of staff", "strategy", "consulting"
        ],
        "skills": {
            "project_management": [
                "project management", "program management", "agile", "scrum",
                "kanban", "waterfall", "pmp", "prince2", "jira", "asana",
                "monday.com", "notion", "confluence", "trello"
            ],
            "operations": [
                "supply chain", "logistics", "procurement", "vendor management",
                "lean", "six sigma", "process improvement", "kpi", "okr",
                "business analysis", "requirements gathering", "stakeholder management",
                "change management", "risk management", "budgeting"
            ],
            "tools": [
                "excel", "tableau", "power bi", "sql", "salesforce",
                "sap", "oracle", "netsuite", "workday", "servicenow"
            ],
        },
        "tips": {
            "missing_project_management": "PMP or Agile certifications significantly boost operations roles.",
            "missing_operations": "Quantify process improvements — 'reduced costs by 20%' is powerful.",
            "general": "Show cross-functional leadership — operations is about influencing without authority."
        }
    },

    # ── LEGAL ─────────────────────────────────────────────────
    "Legal": {
        "keywords": [
            "lawyer", "attorney", "legal", "counsel", "paralegal",
            "law", "litigation", "corporate law", "compliance", "regulatory"
        ],
        "skills": {
            "legal_skills": [
                "contract law", "litigation", "corporate law", "intellectual property",
                "mergers and acquisitions", "employment law", "real estate law",
                "criminal law", "family law", "immigration law",
                "legal research", "legal writing", "due diligence",
                "regulatory compliance", "gdpr", "ccpa", "hipaa compliance"
            ],
            "tools": [
                "westlaw", "lexisnexis", "bloomberg law", "pacer",
                "clio", "mycase", "docusign", "contract management"
            ],
        },
        "tips": {
            "missing_legal_skills": "Specify the areas of law you've practiced — generalist is less valuable.",
            "missing_tools": "Westlaw and LexisNexis proficiency is expected for research roles.",
            "general": "Bar admission state(s) and JD from ABA-accredited school should be prominent."
        }
    },

    # ── HR ────────────────────────────────────────────────────
    "Human Resources": {
        "keywords": [
            "human resources", "hr", "recruiter", "talent acquisition",
            "people operations", "hrbp", "compensation", "benefits",
            "learning and development", "organizational development"
        ],
        "skills": {
            "hr_skills": [
                "talent acquisition", "recruiting", "sourcing", "onboarding",
                "performance management", "compensation and benefits",
                "employee relations", "hrbp", "learning and development",
                "organizational development", "workforce planning",
                "diversity equity inclusion", "dei", "culture"
            ],
            "tools": [
                "workday", "successfactors", "bamboohr", "greenhouse",
                "lever", "jobvite", "linkedin recruiter", "indeed",
                "adp", "paychex", "ceridian", "servicenow hr"
            ],
        },
        "tips": {
            "missing_hr_skills": "Add metrics — time-to-hire, offer acceptance rate, retention rate.",
            "missing_tools": "ATS experience (Greenhouse, Lever, Workday) is required for most HR roles.",
            "general": "SHRM-CP or PHR certification demonstrates HR competency."
        }
    },
}

# ── Build flat skills list for matching ───────────────────────────────────────
ALL_SKILLS = []
for field_name, field_data in FIELDS.items():
    for category, skills in field_data["skills"].items():
        for skill in skills:
            ALL_SKILLS.append({
                "skill": skill,
                "category": category,
                "field": field_name
            })

# ── Aliases — shorthand to full form ─────────────────────────────────────────
ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "k8s": "kubernetes",
    "gcp": "google cloud",
    "tf": "tensorflow",
    "js": "javascript",
    "ts": "typescript",
    "py": "python",
    "postgres": "postgresql",
    "mongo": "mongodb",
    "sklearn": "scikit-learn",
    "golang": "golang",
    "go": "golang",
    "node": "nodejs",
    "bi": "power bi",
    "sf": "salesforce",
    "ux": "ux design",
    "ui": "ui design",
    "seo": "seo",
    "sem": "sem",
    "ppc": "ppc",
    "cro": "conversion rate optimization",
    "m&a": "mergers and acquisitions",
    "pe": "private equity",
    "vc": "venture capital",
}