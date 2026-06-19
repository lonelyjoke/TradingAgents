from langchain_core.messages import HumanMessage, RemoveMessage

# Import tools from separate utility files
from tradingagents.agents.utils.core_stock_tools import (
    get_stock_data
)
from tradingagents.agents.utils.technical_indicators_tools import (
    get_indicators
)
from tradingagents.agents.utils.fundamental_data_tools import (
    get_fundamentals,
    get_balance_sheet,
    get_cashflow,
    get_commodity_context,
    get_compute_leasing_context,
    get_consumer_staples_context,
    get_dividend_defensive_context,
    get_earnings_model_context,
    get_financial_report_intelligence_context,
    get_income_statement,
    get_insurance_context,
    get_intraday_behavior_context,
    get_medical_device_context,
    get_metals_mining_context,
    get_optical_module_context,
    get_price_move_attribution_context,
    get_investor_interaction_context,
    get_policy_planning_context,
    get_web_fact_check_context,
    get_market_sector_risk,
    get_market_expectation_context,
    get_market_timing_context,
    get_relative_strength_context,
    get_management_capital_allocation_context,
    get_baijiu_context,
    get_biopharma_context,
    get_building_materials_context,
    get_software_context,
    get_peer_comparison,
    get_price_earnings_decomposition_context,
    get_shareholder_structure_context,
    get_supply_chain_comparison,
    get_shipping_context,
    get_thematic_catalyst_context,
    get_valuation_percentiles,
)
from tradingagents.agents.utils.news_data_tools import (
    get_company_events,
    get_news,
    get_insider_transactions,
    get_global_news
)


def get_language_instruction() -> str:
    """Return a prompt instruction for the configured output language.

    Returns empty string when English (default), so no extra tokens are used.
    Only applied to user-facing agents (analysts, portfolio manager).
    Internal debate agents stay in English for reasoning quality.
    """
    from tradingagents.dataflows.config import get_config
    lang = get_config().get("output_language", "English")
    if lang.strip().lower() == "english":
        return ""
    return (
        f" Write your entire response in {lang}. "
        "If the output language is Chinese, translate by meaning rather than word-for-word. "
        "Use fluent Chinese buy-side research phrasing and avoid awkward literal translations, "
        "machine-translation wording, or English sentence order. Preferred terms: translate "
        "`investment thesis`, `core thesis`, or `thesis` as `投资论点`, `核心投资假设`, "
        "`核心逻辑`, or `投资主线` depending on context; translate `falsification` as "
        "`证伪`, `验证/证伪条件`, or `风险触发条件`; translate `watch item` as "
        "`观察项` or `跟踪项`; translate `holder` as `已持有者`; translate `builder` "
        "as `准备建仓者` or `增配者`; translate `probability/payoff` as `胜率/赔率` "
        "or `概率收益比`; translate `expectation gap` as `预期差`; translate `core bet` "
        "as `核心判断` or `核心押注`. Do not use `论文` to describe a stock pitch, "
        "trading argument, investment case, or falsification framework unless the topic "
        "is literally an academic paper."
    )


def get_evidence_instruction() -> str:
    """Return anti-hallucination rules for numeric investment claims."""
    return (
        " Evidence discipline: any concrete number, percentage, price, inventory, "
        "capacity, production quota, product spread, or date-specific market claim "
        "must be grounded in the supplied tool outputs or analyst reports. If the "
        "supporting evidence is absent, explicitly label it as an unverified key "
        "assumption and do not present it as fact. Never invent commodity prices, "
        "inventory levels, product-price changes, or policy details."
        " Unit discipline: Tushare and filing numeric fields are usually raw CNY "
        "unless the context explicitly says 万元/亿元. Before writing market cap, "
        "profit, revenue, or cash-flow in 万元/亿元, convert and sanity-check the "
        "order of magnitude against the source table. If you estimate probabilities, "
        "target prices, regulatory penalty odds, asset haircuts, or liquidation values, "
        "label them as scenario assumptions unless a source explicitly provides them."
    )


def get_research_gap_instruction() -> str:
    """Return rules for handling missing but thesis-critical evidence."""
    return (
        " Research-gap discipline: when a thesis-critical driver is missing "
        "(for example product prices, product spreads, inventory, freight rates, "
        "policy details, capacity, order backlog, or utilization), do not let the "
        "analysis collapse into technical indicators or static PE/PB alone. Treat "
        "the missing driver as neutral for direction but material for confidence: "
        "explain why it matters, and build conditional scenarios from the evidence "
        "that is available. "
        "If the missing driver is essential to a bullish or bearish claim, cap "
        "conviction, label the conclusion as evidence-limited, and list the exact "
        "data that should be checked next. Missing data cannot be the decisive "
        "reason for Buy/Sell or Underweight/Sell unless independent verified "
        "evidence supports that direction. Hold/watch is appropriate when the "
        "same missing variable is decisive for both bull and bear cases and the "
        "verified evidence is genuinely mixed."
    )


def get_supply_demand_fallback_instruction() -> str:
    """Return rules for macro supply-demand analysis when micro data is unavailable."""
    return (
        " Supply-demand fallback: if micro data for a key product or route is "
        "unavailable, use macro supply-demand evidence instead, but keep it "
        "product-specific rather than generic. Discuss the product's traits "
        "(standardized vs non-standardized, storability, import/export exposure, "
        "policy sensitivity, substitution risk), upstream cost drivers, downstream "
        "demand industries, inventory or operating-rate proxies, capacity additions "
        "or shutdowns, and whether margins/spreads can be inferred from verified "
        "inputs. Clearly separate verified macro proxies from unverified micro "
        "prices. Do not say 'demand is improving' or 'supply is tight' unless you "
        "name the concrete channel, affected upstream/downstream link, and evidence "
        "strength."
    )


def get_web_fact_check_instruction() -> str:
    """Return rules for using web-searched high-frequency fact checks."""
    return (
        " Web fact-check discipline: use web-searched facts only for small, "
        "high-frequency variables that filings and Tushare do not cover well, "
        "such as baijiu wholesale prices, channel inventory, terminal discounts, "
        "product price changes, bank NIM/deposit-cost commentary, bank asset-quality "
        "updates, monthly sales clues, or local policy details. "
        "Keep the evidence hierarchy explicit: official filings/announcements "
        "> exchange Q&A > reputable news/search corroboration > market rumor. "
        "A single web result can create a watch item or research gap, but it "
        "cannot become a hard trading trigger unless multiple recent independent "
        "sources or an official source support it. Always preserve source date, "
        "source name, and whether the searched fact is verified, corroborated, "
        "conflicting, or unverified. For banks, do not use orders, sales volume, "
        "gross margin, channel inventory, or product-price searches as thesis "
        "evidence; route web checks to NIM/deposit cost, NPL/provision coverage, "
        "capital adequacy, fee income, wealth management, and rate-policy transmission."
    )


def get_baijiu_instruction() -> str:
    """Return rules for gated A-share baijiu/liquor analysis."""
    return (
        " Baijiu verification gate: only use baijiu-specific channel, wholesale-price, "
        "dealer-payment, and festival-demand logic when the supplied baijiu context "
        "says `Status: triggered`, or when official filings clearly show a baijiu "
        "business. When triggered, distinguish ex-factory price, guided retail price, "
        "wholesale/reference price, loose-bottle price, original-carton price, and "
        "terminal retail price. Contract liabilities must be interpreted with "
        "baijiu seasonality: same-quarter YoY and multi-year seasonal baselines "
        "matter more than a simple Q4-to-Q1 sequential drop. If core product "
        "wholesale price, channel inventory, or peer-basket evidence is missing, "
        "label it as a critical research gap and cap conviction. Do not make a "
        "firm relative-allocation claim for a baijiu stock if the peer basket "
        "failed, unless the conclusion is explicitly low-confidence."
    )


def get_compute_leasing_instruction() -> str:
    """Return rules for gated A-share compute-leasing analysis."""
    return (
        " Compute-leasing gate: only analyze an A-share target as a compute-leasing "
        "or AI-compute stock when the supplied compute-leasing context says "
        "`Status: triggered`, or when official filings/announcements/investor "
        "interaction in the prompt independently show a compute-leasing business. "
        "If the context says `Status: not_applicable`, do not inject GPU, IDC, "
        "AI-compute rental, or data-center valuation assumptions into the thesis. "
        "When triggered, separate legacy business value, verified compute-leasing "
        "business value, and unverified compute optionality. Require the asset "
        "gate (GPU/server model, quantity, delivery, ownership/financing lease, "
        "data-center/power/network/O&M status), contract gate (customer quality, "
        "contract term, pricing, minimum usage, related-party risk, collections), "
        "unit-economics gate (rent, utilization, electricity, rack, bandwidth, "
        "O&M, depreciation, financing cost, ROIC/payback), capex/funding gate, "
        "and transition-credibility gate before treating compute leasing as "
        "base-case valuation. If only weak mentions exist and those asset, "
        "contract, revenue, or unit-economics gates are not met, treat compute "
        "leasing as a rejected/insufficient-evidence optionality item rather "
        "than a standalone thesis driver. A-share compute-leasing facts are often hard to "
        "obtain; missing GPU counts, lease prices, utilization, customer identity, "
        "or power cost are research gaps, not neutral evidence. News-only or "
        "framework-agreement evidence can create a watch item, but not a hard "
        "valuation uplift."
    )


def get_dividend_defensive_instruction() -> str:
    """Return rules for gated defensive-dividend analysis."""
    return (
        " Defensive-dividend gate: only call an A-share target a defensive "
        "dividend asset when the supplied dividend defensive context says "
        "`Status: triggered` and the evidence supports stable dividends, "
        "profit/cash-flow or bank-capital coverage, non-declining industry "
        "logic, and valuation buffer. If the context says `Status: not_applicable`, "
        "do not force a red-chip/high-yield thesis. High dividend yield is only "
        "the starting hypothesis: explicitly test the dividend-trap path where "
        "profits shrink, FCF weakens, capital constraints bind, or the industry "
        "is structurally eroding, causing future dividends to fall. When the "
        "context supplies same-industry or cross-industry alternatives, compare "
        "the target against them and state whether the entered ticker is the "
        "best defensive expression, should be paired for diversification, or "
        "should be substituted by a higher-quality/lower-risk peer."
    )


def get_consumer_staples_instruction() -> str:
    """Return rules for gated A-share consumer staples / food-beverage analysis."""
    return (
        " Consumer-staples verification gate: only use food/beverage-specific "
        "channel, category, raw-material, distributor, and consumption-macro logic "
        "when the supplied consumer-staples context says `Status: triggered`, or "
        "when official filings independently prove a food, beverage, dairy, meat, "
        "condiment, frozen-food, prepared-dish, snack, or similar consumer-staples "
        "business. When triggered, classify the category first: frozen prepared "
        "food, meat processing, dairy, condiment, snacks, beverage, or general "
        "consumer staples. Do not stop at static PE/PB, dividend yield, or generic "
        "`consumption recovery`. Tie the thesis to the native variables: restaurant "
        "traffic or household demand, channel sell-through, distributor inventory, "
        "contract liabilities/advance receipts, inventory-to-revenue, receivables, "
        "gross margin, promotion intensity, raw-material proxies, cold-chain or "
        "logistics cost, product mix, and food-safety risk. For Anjoy/frozen-food "
        "names, explicitly test whether strong Q1 results are Spring Festival "
        "seasonality, distributor restocking after destocking, lower raw-material "
        "costs, high-margin core-category mix, prepared-dish ramp, or durable "
        "end-demand acceleration. Missing restaurant traffic, channel inventory, "
        "surimi/poultry/flour/oil cost, segment margin, or prepared-dish sell-"
        "through evidence is a research gap that caps conviction, not permission "
        "to write a generic consumer-stock thesis."
    )


def get_optical_module_instruction() -> str:
    """Return rules for gated A-share AI optical-module / datacom hardware analysis."""
    return (
        " AI optical-module gate: only use optical-module, AI datacom, 800G/1.6T, "
        "CPO/LPO, silicon-photonics, or hyperscaler-capex logic when the supplied "
        "optical-module context says `Status: triggered`, or when official filings "
        "independently prove an optical-communication / AI datacom hardware business. "
        "When triggered, start from supply-chain position rather than generic "
        "high-growth technology labeling: module integrator, optical component, "
        "connector, optical chip, telecom/device supplier, or technology-route "
        "optionality. Bridge downstream AI capex into company revenue through "
        "GPU/ASIC cluster buildout, switch upgrade, 400G/800G/1.6T migration, "
        "customer qualification, capacity, yield, shipment mix, and pricing. "
        "For Zhongji Innolight, Eoptolink, and similar names, explicitly test "
        "whether growth comes from 800G share gain, 1.6T ramp, overseas cloud "
        "orders, product mix, exchange rate, or temporary supply tightness. "
        "Revenue acceleration is investable only when gross margin, inventory/"
        "revenue, receivables/revenue, operating cash flow, customer concentration, "
        "and overseas exposure form a coherent delivery story. Missing customer, "
        "order, ASP, shipment, capacity, qualification, or 1.6T roadmap evidence "
        "is a research gap that caps conviction. Treat CPO/LPO/silicon photonics, "
        "export controls, tariffs, customer concentration, price erosion, and "
        "technology-route substitution as thesis-critical risks. Valuation must "
        "separate base-case earnings already implied by the current multiple from "
        "scenario value tied to future AI capex and technology optionality."
    )


def get_building_materials_instruction() -> str:
    """Return rules for gated A-share building-materials analysis."""
    return (
        " Building-materials gate: only use building-materials-specific logic "
        "when the supplied building-materials context says `Status: triggered`, "
        "or when official filings independently show cement, waterproofing, "
        "glass/fiberglass, gypsum-board, pipe, coating, ceramic-tile, hardware, "
        "wood-panel, or other building-material operations. When triggered, "
        "use it as a discipline layer, not a replacement for the core memo. "
        "Anchor on company filings and management wording, then classify "
        "the industry stage and likely evolution path, and then use product ASP, "
        "regional demand, property-completion or infrastructure "
        "exposure, renovation/retail versus engineering channel mix, capacity "
        "and utilization, upstream energy/raw-material costs, inventory, "
        "receivables, impairment, cash collection, and maintenance capex. "
        "For cement/glass/fiberglass names, require price, inventory, cost, and "
        "utilization evidence before treating a cycle inflection as proven. For "
        "waterproofing/coating/pipe/hardware names, require channel health, "
        "receivable quality, impairment, and cash-collection evidence before "
        "calling revenue growth investable. For low-PB/high-dividend building "
        "material leaders, explicitly explain why book-value discount or dividend "
        "yield is not enough unless asset value, payout coverage, cash conversion, "
        "and capital-allocation proof all hold. Treat buyback/dividend analysis "
        "as shareholder-return, safety-margin, and controlling-shareholder-attitude "
        "evidence, but do not let it crowd out operating evidence from filings "
        "or the industry-cycle interpretation. Add a dedicated building-materials "
        "verdict only when it changes rating, valuation, sizing, or action; "
        "otherwise integrate the relevant points into the business, valuation, "
        "or risk discussion. If the context says "
        "`Status: not_applicable`, do not inject cement/property-completion "
        "logic unless other primary evidence proves relevance."
    )


def get_biopharma_instruction() -> str:
    """Return rules for gated A-share biopharma / pharma-services analysis."""
    return (
        " Biopharma verification gate: only use biopharma-specific clinical, "
        "regulatory, reimbursement, pipeline, or CRO/CDMO order-cycle logic when "
        "the supplied biopharma context says `Status: triggered`, or when "
        "official filings independently show an innovative-drug, biotech, "
        "pharma, or pharma-services business. When triggered, separate approved "
        "commercial assets, label expansion, late-stage pipeline, early pipeline, "
        "BD/licensing economics, and cash runway before valuation. Commercialized "
        "products can support base earnings only when label, sales, reimbursement, "
        "and competitive evidence exists; clinical pipeline should use "
        "risk-adjusted NPV or scenario optionality, not a simple PE/PB shortcut. "
        "Require official evidence from filings/IR, ClinicalTrials.gov or CDE "
        "trial registration, CDE/NMPA/FDA/EMA decisions and labels, NRDL or "
        "procurement/pricing records, and conference/paper readouts before "
        "treating a catalyst as hard. For Phase I/II assets, small single-arm "
        "data, or immature endpoints, cap base-case valuation credit and label "
        "the thesis as evidence-limited. For CRO/CDMO/pharma-services companies "
        "such as WuXi AppTec, analyze order backlog, customer funding, project "
        "conversion, capacity utilization, capex returns, geopolitical risk, and "
        "FCF rather than valuing them like drug-owner pipelines. Missing trial "
        "IDs, regulatory status, product sales, reimbursement/pricing, endpoint "
        "quality, or cash-runway data is a critical research gap, not permission "
        "to invent clinical or commercial numbers."
    )


def get_software_instruction() -> str:
    """Return rules for gated A-share software / SaaS analysis."""
    return (
        " Software verification gate: only use software/SaaS-specific ARR, ARPU, "
        "paid-user, renewal, churn, NRR/GRR, seat, project-delivery, or "
        "AI-monetization logic when the supplied software context says "
        "`Status: triggered`, or when official filings independently show a "
        "software, SaaS, financial IT, cybersecurity, industrial software, AI "
        "software, or hardware-plus-service business. When triggered, first "
        "classify the revenue model and sales motion: product-led subscription, "
        "enterprise-seat SaaS, project implementation, financial IT, industrial "
        "software, cybersecurity appliance plus subscription, cloud/IDC hybrid, "
        "or hardware plus service. Do not call all software companies SaaS. "
        "For subscription models, require paid users, ARPU, conversion, renewal, "
        "billing duration, contract-liability conversion, churn, and preferably "
        "ARR/MRR or NRR/GRR before assigning a SaaS-like multiple. For project "
        "software, require order backlog, implementation/acceptance timing, "
        "receivables, collection, and project gross margin. AI features are not "
        "AI revenue: require paid AI users, attach rate, AI ARPU uplift, pricing, "
        "and compute/cloud cost before putting AI into base-case earnings. "
        "Broad A-share `software service` peer screens are only a starting point; "
        "model-label peers before making relative allocation claims. Missing "
        "ARR, ARPU, paid-user, renewal, churn, segment margin, or contract-"
        "liability-structure evidence is a critical research gap and should cap "
        "conviction rather than be filled by narrative."
    )


def get_insurance_instruction() -> str:
    """Return rules for gated A-share insurance analysis."""
    return (
        " Insurance verification gate: only use insurance-specific NBV, EV, "
        "P/EV, solvency, agent, bancassurance, persistency, surrender, CSM/NCSM, "
        "investment-yield, and P&C COR logic when the supplied insurance context "
        "says `Status: triggered`, or when official filings independently prove "
        "a material insurance business. When triggered, treat PE/PB as cross-checks "
        "rather than the whole valuation. For life/health insurance, start from "
        "new-business value growth, NBV margin, channel productivity, EV growth, "
        "CSM/NCSM movement, and liability-cost versus investment-yield spread. "
        "For P&C insurance, separate premium growth from underwriting profitability "
        "through COR, loss ratio, expense ratio, catastrophe exposure, and auto "
        "pricing. For integrated insurers with banking or technology subsidiaries, "
        "split the case into insurance core, bank subsidiary, asset-management / "
        "technology optionality, and capital-return policy; do not let a bank "
        "subsidiary make the whole company read like a pure bank. Dividends and "
        "buybacks require solvency, capital generation, and regulatory-capital "
        "support. Hidden investee holdings or IPO optionality belong in SOTP or "
        "scenario value unless ownership, fair value, exit timing, lock-up, tax, "
        "and double-counting checks are available. Missing NBV, EV, solvency, "
        "investment-yield, COR, or channel-quality evidence is a critical research "
        "gap and should cap conviction. For insurance or high-dividend defensive "
        "candidates, do not let one-quarter net profit, non-recurring profit, or "
        "operating cash flow mechanically drive the rating; use those as warning "
        "signals only after checking NBV/EV, OPAT or core operating profit, CSM/NCSM, "
        "investment-yield spread, solvency, payout coverage, and P&C COR. The "
        "operating cash-flow signal must be described precisely: a sharp OCF "
        "deterioration is a hard negative cash-flow signal with unresolved "
        "attribution, not a soft concern and not standalone proof of franchise "
        "impairment until NBV, EV, OPAT, solvency, investment spread, dividend "
        "capacity, and P&C underwriting evidence confirm or refute the damage. "
        "valuation bridge must show at least P/EV or EV growth, NBV multiple, "
        "PB-ROE, dividend yield/payout sustainability, and SOTP for bank, asset-"
        "management, technology, or holding-company discount buckets. If current "
        "EV is unavailable, use the latest annual EV only as a stale base and "
        "label it explicitly; do not pretend a missing current-period EV has "
        "been verified. Every dividend claim must reconcile interim dividend, "
        "final dividend, full-year DPS, payout ratio, ex-date/cutoff period when "
        "available, and dividend-yield price base; conflicting dividend-per-share "
        "figures must be flagged instead of averaged. Any SOTP bridge must show "
        "the formula for each bucket, such as operating metric times multiple or "
        "listed-market value times ownership stake, plus per-share conversion, "
        "holding-company discount, and double-counting checks. If the stock "
        "has low PB and a meaningful dividend yield but NBV/OPAT evidence is still "
        "missing or mixed, prefer a relative-allocation stance such as Hold or "
        "Underweight-as-relative-low-weight/watch rather than a high-conviction "
        "absolute Sell; reserve stronger Underweight/Sell language for verified "
        "NBV deterioration, OPAT/core-profit decline, solvency pressure, dividend "
        "coverage weakening, investment spread compression, COR deterioration, or "
        "a clearly superior peer substitute. For Overweight on an insurance or "
        "defensive-dividend name with unresolved OCF, EV, solvency, or dividend "
        "coverage gaps, qualify the stance as staged/cautious Overweight in the "
        "text, keep sizing below full target until the named disclosure verifies "
        "the thesis, and reconcile why the clean rating is still positive. "
        "Scenario probabilities, if used, must be labeled as subjective PM "
        "weights or underwriting assumptions, not facts. Peer comparison must "
        "state whether the target is a cleaner insurer, higher-beta recovery/SOTP "
        "expression, better dividend sleeve, or inferior substitute versus true "
        "operating peers such as life insurers, P&C insurers, and integrated "
        "financial groups. A generic peer screen built only from PE, PB, ROE, "
        "dividend yield, and one-quarter profit growth is not enough to prove a "
        "superior insurance substitute. Before using peer superiority to drive "
        "Underweight/Sell, compare the peer on the same insurance-native drivers: "
        "NBV growth, NBV margin, EV or P/EV, OCF/cash-quality trend, solvency, "
        "investment spread, payout coverage, channel mix, and P&C COR where "
        "applicable. If those peer-native checks are missing, cap the conclusion "
        "at Hold or relative low-weight/watch and say the peer switch is a "
        "hypothesis, not a verified reason to reduce the target. Always state "
        "whether the conclusion "
        "is about absolute downside, insurance-sector relative allocation, or "
        "defensive-basket suitability."
    )


def get_medical_device_instruction() -> str:
    """Return rules for gated A-share medical-device analysis."""
    return (
        " Medical-device verification gate: only use medical-device-specific "
        "installed-base, tender/procurement, VBP, reagent pull-through, "
        "registration, overseas-channel, service attach-rate, and device "
        "replacement-cycle logic when the supplied medical-device context says "
        "`Status: triggered`, or when official filings independently prove a "
        "material medical equipment, IVD, reagent/consumables, or high-value "
        "device business. When triggered, separate capital equipment, IVD "
        "closed-loop analyzers plus reagents, consumables/procedure volume, "
        "service revenue, overseas expansion, and policy/procurement impact "
        "before valuation. For equipment companies, require installed base, "
        "replacement cycle, tender cadence, delivery/acceptance, service attach "
        "rate, and hospital capex evidence. For IVD, require analyzer installed "
        "base, tests per machine, reagent menu breadth, reagent gross margin, "
        "and lab automation pull-through before calling revenue recurring. For "
        "consumables and high-value devices, test procedure/testing volume, VBP "
        "price reset, hospital access, product approval, and price-volume offset. "
        "For overseas growth, require registration status such as NMPA/FDA/CE or "
        "local equivalents, distributor quality, localization, channel inventory, "
        "service network, FX, and tariff exposure. Do not value a device company "
        "like an innovative-drug pipeline unless it owns drug-like clinical asset "
        "economics. If the context includes a Medical-Device Evidence Gate Matrix "
        "or Company-Specific Follow-Up Questions, the final PM memo must explicitly "
        "answer each thesis-critical gate or carry it into Evidence Gaps, sizing, "
        "and the dated verification calendar. Missing installed-base, tender, VBP, "
        "registration, overseas channel, receivable, cash-flow, or reagent "
        "pull-through evidence is a critical research gap and should cap conviction."
    )


def get_metals_mining_instruction() -> str:
    """Return rules for gated A-share metals/mining analysis."""
    return (
        " Metals/mining verification gate: only use metals/mining-specific reserve, "
        "grade, equity-output, AISC/unit-cost, mine-life, project-ramp, hedging, "
        "inventory, capex, NAV/SOTP, and cycle-trough logic when the supplied "
        "metals/mining context says `Status: triggered`, or when official filings "
        "independently prove a material mining, smelting, refining, or metal-resource "
        "business. When triggered, do not stop at commodity-price direction or PE TTM. "
        "Separate mine asset quality, realized selling price versus exchange proxy, "
        "volume, cost curve, FX, sustaining capex, smelting/trading contribution, "
        "working capital, derivatives, leverage, and project execution. Domestic "
        "exchange futures can be used as timely proxies only when the source/date/unit "
        "is shown; COMEX/LME/LBMA or licensed spot benchmarks should be treated as "
        "cross-checks unless explicitly fetched. Build valuation through bull/base/bear "
        "metal-price sensitivity and, for diversified miners, mine/metal SOTP or NAV. "
        "A sell-side-depth metals memo must be organized around: cycle and price deck, "
        "asset/production table, reserve/grade/mine-life evidence, cost curve and "
        "AISC/cash-cost bridge, mining versus smelting/refining/trading profit pools, "
        "NAV/SOTP with optionality separated from base value, commodity-price "
        "sensitivity table, balance-sheet survival, and a dated verification calendar. "
        "If these tables cannot be filled from evidence, state the gap and cap the "
        "rating conviction rather than replacing them with a generic PE paragraph. "
        "Missing reserve, grade, equity-output, AISC, project-ramp, hedging, or NAV "
        "evidence is a critical research gap and should cap conviction. Missing "
        "thesis-critical metals data is neutral for direction: it can prevent a "
        "high-conviction Buy or Sell, but it cannot prove deterioration or improvement "
        "by itself. "
        "For nonferrous metals such as aluminum, copper, zinc, nickel, lithium, "
        "silver, and gold, split the conclusion into four layers before the final "
        "rating: Industry Cycle View, Company Expression View, Valuation/Odds View, "
        "and Tactical Attribution View. A high-prosperity metal cycle with supply "
        "constraints, low TTM/forward PE, profit release, operating cash-flow release, "
        "or dividend support must not be collapsed into Underweight solely because "
        "PB is high, EPS percentile is high, or one-quarter working-capital items "
        "look weaker. Treat PE-low/PB-high as a live fork: it can be a peak-earnings "
        "trap, or it can be an ROE re-rating path if supply discipline, margin, "
        "cash conversion, and payout are durable. To issue Underweight/Sell in that "
        "setup, explicitly answer the strongest bull case and prove at least one "
        "hard path: metal-price/profit-center downshift, company cash-cycle "
        "deterioration beyond seasonality, materially superior peer expression, "
        "or valuation already pricing the favorable scenario. One-quarter receivables, "
        "contract liabilities, inventory, or impairment direction can cap conviction, "
        "but cannot be decisive without seasonality, aging, peer comparison, and "
        "cash-conversion evidence. For aluminum names, explicitly bridge supply "
        "ceiling/capacity policy, LME-SHFE or domestic-overseas price gaps, alumina "
        "and power costs, property drag, grid/PV/EV/lightweighting demand, exports, "
        "and inflation/liquidity beta. If alumina, power, or anode cost evidence is "
        "missing, treat the gap as neutral for direction and cap conviction; do not "
        "call profit deterioration, margin collapse, or `perfect scenario priced` "
        "unless independent verified cost, spread, segment-margin, cash-flow, or "
        "peer-opportunity evidence supports it. AI or robotics demand should be treated as "
        "indirect optionality unless aluminum-volume linkage is quantified."
    )


def get_price_move_attribution_instruction() -> str:
    """Return rules for short-horizon sharp-move attribution."""
    return (
        " Price-move attribution discipline: when a stock has a sharp short-horizon "
        "move, separate market beta, same-industry or same-metal equity moves, "
        "cross-metal equity moves, mapped commodity futures moves, company events, "
        "valuation support, liquidity/turnover, and trend context before assigning "
        "a cause. Do not call a drop `emotionally undervalued` merely because the "
        "commodity did not fall. A stronger emotion-kill conclusion needs weak "
        "commodity explanation, no material company event, target residual worse "
        "than peers, credible valuation or NAV/PB support, and signs that forced "
        "selling is stabilizing. If copper, silver, lithium, or other metal equities "
        "behave differently from the target's metal basket, discuss that cross-metal "
        "residual explicitly."
    )


def get_derived_financial_metric_instruction() -> str:
    """Return rules for using calculated ratios when reported indicators are missing."""
    return (
        " Derived financial metric discipline: when ready-made indicators such "
        "as gross margin, operating margin, net margin, cash-conversion ratio, "
        "or debt ratio are missing, use explicitly labelled derived metrics "
        "calculated from the income statement, balance sheet, and cash-flow "
        "statement. Do not call derived metrics company-disclosed indicators. "
        "For interim A-share reports, remember that income and cash-flow fields "
        "may be period-to-date rather than standalone single-quarter figures. "
        "Use derived metrics to improve judgment, but explain their accounting "
        "limits when they materially affect the thesis. Also read forward-looking "
        "accounting signals from contract liabilities, advance receipts, contract "
        "assets, receivables, inventories, prepayments, payables, goodwill, net "
        "cash, and working capital. Interpret them by business model: contract "
        "liabilities can indicate order visibility for project or subscription "
        "businesses, but may be less meaningful for spot commodity sales; rising "
        "inventory can be proactive stocking in an upcycle or demand pressure in "
        "a downturn; rising receivables can mean growth or collection risk. Use "
        "these signals as evidence for future revenue/profit inference only when "
        "the accounting item, industry context, and cash-flow quality point in "
        "the same direction."
    )


def get_buy_side_accounting_radar_instruction() -> str:
    """Return a buy-side accounting checklist for forward-looking financial analysis."""
    return (
        " Buy-side accounting radar: read financial statements as reliable but "
        "lagging evidence. Organize accounting analysis around five questions. "
        "First, is revenue real: compare revenue growth with receivables, notes "
        "receivable, contract assets, cash received from customers, and operating "
        "cash flow. Second, is profit quality durable: inspect gross margin, "
        "operating margin, expense ratios, R&D intensity, finance costs, impairment "
        "losses, investment income, fair-value gains, non-operating gains, and "
        "deducted recurring profit if available. Third, are there forward-looking "
        "clues: read contract liabilities, advance receipts, inventories, "
        "prepayments, capex, construction in progress, and order/capacity signals "
        "in the context of the industry cycle. Fourth, can the balance sheet "
        "survive the cycle: check net cash/debt, short-term debt pressure, working "
        "capital, liquidity, goodwill, asset impairment risk, and cash conversion. "
        "Fifth, are shareholder returns aligned: consider dividend sustainability, "
        "buybacks, dilution, minority interests, and whether capital expenditure "
        "is creating future earnings or destroying returns. Do not list every "
        "item mechanically; highlight only the accounting signals that change "
        "the thesis, rating, or falsification conditions."
    )


def get_buy_side_thesis_instruction() -> str:
    """Return rules that make the framework more like a buy-side thesis memo."""
    return (
        " Buy-side thesis discipline: do not behave like a static fact checker. "
        "For every directional view, first state the core bet: what future variable "
        "the investor is actually underwriting. Then judge whether the boom-bust "
        "or business-cycle expectation can plausibly happen using verified data, "
        "proxy data, and bounded inference. Separate facts from inference, but do "
        "not default to Hold just because some data is missing. A direction can be "
        "valid when the probability/payoff is attractive and the thesis is "
        "falsifiable. Always discuss expectation gap: whether the market may have "
        "already priced the thesis, or whether there is a plausible mispricing. "
        "State catalyst path, falsification signals, conviction level, and position "
        "implication. Use Hold only when there is no clear tradable thesis, the "
        "expectation gap is weak, or probability/payoff is not attractive. If writing "
        "in Chinese, use idiomatic buy-side wording: thesis = 投资论点/核心投资假设/投资主线, "
        "not 论文; falsification = 证伪 or 验证/证伪条件; watch item = 观察项 or 跟踪项; "
        "probability/payoff = 胜率/赔率 or 概率收益比; expectation gap = 预期差."
    )


def get_buy_side_underwriting_modules_instruction() -> str:
    """Return reusable buy-side modules that raise the final memo standard."""
    return (
        " Buy-side underwriting modules: when writing the final research note, "
        "add the following modules when they are relevant to the company. These "
        "modules are generic, not ticker-specific; adapt the labels to the "
        "business model instead of forcing every module mechanically. "
        "(1) PM summary: in 5-8 lines, state rating, action, sizing, time horizon, "
        "core bet, why now, biggest risk, and the next verification date. "
        "(2) Key data check: reconcile the 6-10 most important numbers used in "
        "the memo, such as revenue, net profit, EPS, market cap, PE/PB, operating "
        "cash flow, contract liabilities/orders/backlog, capex, dividend, net debt, "
        "and any segment metric. If a number appears with conflicting signs, units, "
        "or periods across the debate, flag the conflict and use the source-backed "
        "figure rather than averaging narratives. "
        "(3) Expectation-gap evidence: prove what the market appears to believe "
        "with valuation percentile, price-EPS-multiple decomposition, consensus or "
        "sell-side expectations when supplied, institutional/holder behavior, "
        "technical price action, and investor-interaction question patterns. "
        "(4) Revenue/profit growth sustainability: state whether the company's "
        "revenue and profit growth can continue or ramp further, using the actual "
        "business model. Name the 3-6 drivers, mark each as verified, inferred, "
        "or missing, and list the operating or financial signals that would "
        "falsify the growth thesis. "
        "(5) Unit-economics bridge for any second curve, platform, service, new "
        "product, project, channel, or financing business: revenue/GMV/volume x "
        "take rate or ASP x gross margin/net margin x reinvestment or working "
        "capital. If take rate, margin, breakeven, utilization, customer retention, "
        "or loss rate is not disclosed, write 'not disclosed' and keep the business "
        "in scenario value rather than core valuation. "
        "(6) Project ramp or capacity/occupancy bridge: for new plants, mines, "
        "stores, malls, data centers, ships, property projects, or platforms, track "
        "capacity/area/users, utilization or occupancy, price/rent, ramp timetable, "
        "incremental margin, capex, ROIC/payback, and the source of demand. "
        "(7) Financing/listing/dilution scenario: for H-share/secondary listings, "
        "private placements, convertibles, debt refinancing, major capex funding, "
        "or asset sales, state bull/base/bear pricing or cost-of-capital scenarios, "
        "use of proceeds, dilution, ROE/FCF impact, and whether it creates an "
        "anchor or overhang. "
        "(8) Verification calendar: list the exact next disclosures or operating "
        "data that would make the analyst add, hold, trim, downgrade, or exit. "
        "(9) Safety price / defensive build anchor: include a standalone safety "
        "price or safety price band for slow accumulation by new builders, or "
        "explicitly say no reliable safety price can be set. When writing Chinese, "
        "title the section `## 安全价格区间 / 防御性建仓锚`. This is not a target "
        "price and not a stop-loss. For blue chips, mature value stocks, banks, "
        "cash-flow compounders, or defensive dividend names, anchor it in "
        "normalized low-cycle EPS/FCF, sustainable dividend yield, book value/PB "
        "and ROE, net cash or leverage, asset quality, cash conversion, payout "
        "capacity, and historical/peer valuation floors. For commodity/resource/"
        "cyclical names, anchor it in cycle-trough or stress-case earnings, "
        "conservative product prices, unit-cost resilience, balance-sheet survival, "
        "maintenance capex, and normalized PE/PB floors. Include the price band, "
        "valuation bridge, business conditions that must remain true, slow-build "
        "plan, and financial or operating deterioration that would invalidate the "
        "safety price. "
        "Do not make these modules stock-specific buzzwords: for a payment company "
        "the unit-economics bridge may be GMV x take rate x margin; for a landlord "
        "it may be area x occupancy x rent x margin; for a manufacturer it may be "
        "volume x ASP x gross margin; for a bank, use bank-native KPI bridges "
        "instead of gross-margin or contract-liability language."
    )


def get_focused_report_instruction() -> str:
    """Return rules for keeping reports concise and decision-relevant."""
    return (
        " Focus discipline: prioritize decision-relevant evidence over exhaustive "
        "data listing. Do not restate every financial line, every indicator, or "
        "every tool output. Keep the memo organized around thesis, key evidence, "
        "missing evidence, expectation gap, risk/reward, and next verification "
        "signals. Compress routine background unless it changes the rating."
    )


def get_fair_cycle_valuation_instruction() -> str:
    """Return fair calibration rules across valuation and cycle regimes."""
    return (
        " Fair cycle-valuation calibration: evaluate the stock through a neutral "
        "valuation x business-cycle lens. Do not mechanically reward cheapness, "
        "penalize low prosperity, reward high prosperity, or penalize high "
        "valuation. Classify the setup: low valuation/low prosperity, high "
        "valuation/high prosperity, low valuation/high prosperity, or high "
        "valuation/low prosperity. For low valuation/low prosperity names, ask "
        "whether pessimism is fully priced, whether the downturn is cyclical or "
        "structural, whether the company can survive the trough, and whether "
        "there are marginal improvement signals. For high prosperity/high "
        "valuation names, ask whether growth durability and earnings upgrades can "
        "digest valuation, whether crowding is excessive, and what happens if the "
        "cycle rolls over. For low valuation/high prosperity names, test whether "
        "the cheapness reflects overlooked opportunity or unsustainable earnings. "
        "For high valuation/low prosperity names, require clear future inflection "
        "or scarce growth to justify anything above Hold. The rating must follow "
        "expected value: probability, payoff, duration, balance-sheet resilience, "
        "and expectation gap."
    )


def get_material_catalyst_instruction() -> str:
    """Return rules for handling genuine thematic catalysts without chasing noise."""
    return (
        " Material-catalyst discipline: for A-share names, actively check whether "
        "there are company-specific themes that can genuinely affect cash flow, "
        "asset value, or valuation anchors, such as investee IPOs, asset listings, "
        "verified new-business commercialization, policy licenses, major signed "
        "orders, or capacity milestones. A theme may enter valuation only if it "
        "passes all four gates: (1) verifiable evidence from filings, exchange "
        "documents, official disclosures, or equivalent primary sources; "
        "(2) a clear economic transmission path to earnings, NAV, or valuation; "
        "(3) a trackable catalyst timetable or milestone; and (4) materiality "
        "large enough to matter for the listed company. Classify qualifying "
        "themes as asset-revaluation catalysts or business-realization catalysts. "
        "When mining annual or half-year reports for bull themes, reward themes "
        "with filing-backed monetization evidence such as orders, revenue, delivery, "
        "customers, commercialization, or capacity release; reject bare buzzwords "
        "that lack a disclosed economic bridge. Use a three-tier ladder: tier-1 "
        "hard catalysts may enter core valuation, tier-2 soft catalysts may support "
        "scenario upside or improve odds, and tier-3 narrative options from media "
        "association, concept linkage, or investor-interaction claims may receive "
        "only a small imagination premium until filings verify them. "
        "Use filing/news cross-validation rather than one-sided discovery: scan "
        "annual and half-year report text for candidate investees, assets, and "
        "new-business lines, then look for recent news catalysts; for any theme "
        "first discovered in news, require validation from annual or half-year "
        "report text before it may affect valuation. "
        "Keep economic hardness separate from evidence completeness: if a theme "
        "already has a real monetization or NAV bridge but fetched corroboration "
        "is still thin, label it as a latent hard catalyst / pending diligence "
        "instead of demoting it to pure narrative or pretending proof is complete. "
        "If a topic is only a market label, media narrative, vague interaction, "
        "or unsupported concept, keep it in a narrative-option watchlist rather "
        "than core valuation; it may support a small sentiment premium, but it "
        "must not drive the rating before harder evidence appears."
        " For A-share research, do not exclude non-fantastical low-confidence "
        "themes from discussion merely because they are not yet valuation-grade. "
        "Bring extracted themes into analysis, then interrogate them: source "
        "quality, plausibility, market imagination, catalyst path, evidence gaps, "
        "what would upgrade them, and what would falsify them. The discipline is "
        "rational debate and bounded weighting, not silence."
    )


def get_thematic_valuation_instruction() -> str:
    """Return rules for converting verified themes into valuation arguments."""
    return (
        " Thematic-valuation discipline: do not stop at naming a catalyst. "
        "For every verified theme, state the valuation bridge explicitly. "
        "For asset-revaluation themes, discuss ownership exposure, disclosed "
        "carrying or fair value, listed-company market-cap materiality, catalyst "
        "timing, realizability, dilution/lock-up/liquidity haircuts, and whether "
        "the correct treatment is SOTP/NAV uplift, qualitative optionality, or "
        "exclusion. For material primary investments or non-listed equity holdings, "
        "build a three-step NAV ladder: conservative value equals carrying value "
        "with liquidity/exit haircut, base value equals carrying value or latest "
        "financing/IPO reference with explicit discount, and upside value equals "
        "exit/IPO repricing multiplied by probability and lock-up/liquidity "
        "haircuts. Keep this NAV value separate from recurring operating earnings, "
        "but do not erase it as mere narrative when ownership value and a plausible "
        "exit path are disclosed. For business-realization themes, require disclosed revenue, "
        "profit, order, contract, or cash-flow evidence before allowing the theme "
        "into core valuation; otherwise keep it as scenario upside rather than "
        "base-case earnings. Bulls should quantify what the market may be "
        "underpricing; bears should test monetization, ownership, double-counting, "
        "timing, and materiality. Never let an attractive story enter valuation "
        "without saying exactly how much value it could add and what would make "
        "that bridge fail. Also distinguish a one-off asset from a repeatable "
        "capital-allocation capability: when filings show multiple successful "
        "investee realizations plus current verified optionality, discuss whether "
        "management's investing skill deserves a separate qualitative bull factor "
        "instead of burying each holding as an isolated footnote. Narrative "
        "options may still matter in A-shares, but they should be framed as low-weight "
        "imagination premium, not mistaken for earnings evidence."
    )


def get_peer_selection_instruction() -> str:
    """Return rules for deciding whether a same-industry peer is a better build candidate."""
    return (
        " Peer-selection discipline: every recommendation must answer the cross-sectional "
        "question, not just the single-name question. Compare the target with same-industry "
        "peers on valuation, profitability, growth, leverage, cash quality, shareholder "
        "return, and any industry-specific operating metrics available. State explicitly "
        "whether the target is the best build candidate in the sampled peer set, merely "
        "acceptable, or inferior to one or more alternatives. If another peer is better, "
        "name it, explain the concrete metrics and business reasons, and say whether that "
        "weakens the target to watch/underweight rather than build now. If no peer is clearly "
        "better, say why no superior alternative emerged; never treat a lower PE alone as "
        "proof of superiority. Use the competitor-analysis rows in the peer context as a "
        "shortlist for deeper work, then verify from financial reports whether the peers "
        "really compete with the target by product, customer, region, segment economics, "
        "cash conversion, and valuation bucket. If either company has an emerging or second-curve "
        "business, compare that segment separately instead of forcing one blended multiple."
    )


def get_supply_chain_selection_instruction() -> str:
    """Return rules for comparing different profit pools inside one industrial chain."""
    return (
        " Supply-chain-selection discipline: when a curated industrial-chain map is "
        "available, answer a second cross-sectional question after peer selection: "
        "is the target sitting in the best part of the chain to own now? Compare "
        "different chain positions on economics, scarcity, pricing power, earnings "
        "revision potential, valuation, and balance-sheet quality. State explicitly "
        "whether the better build opportunity lies in the target's own segment or "
        "in another profit pool of the same chain. If another segment is better, "
        "explain why the investor should consider rotating across the chain rather "
        "than merely switching names within one segment. Never force this verdict "
        "for industries whose value-chain map is not yet defined."
    )


def get_earnings_model_instruction() -> str:
    """Return rules for forcing every thesis through an earnings bridge."""
    return (
        " Earnings-model discipline: every investable thesis must pass through an "
        "earnings bridge. State which operating levers move revenue, which levers "
        "move margin, and how they flow into profit, cash generation, and finally "
        "valuation. Use bull/base/bear scenarios only when each case changes a "
        "specific modeled assumption such as volume, price, mix, utilization, "
        "gross margin, working capital, or financing cost. A catalyst that cannot "
        "be mapped to a modeled lever is not yet a valuation catalyst. Treat simple "
        "Q1/H1/Q3 annualization as a run-rate diagnostic only; when seasonality-adjusted "
        "earnings are available, use that estimate or explain why it is inappropriate. "
        "For commodity, resource, shipping, and other cyclical businesses, do not use "
        "PE TTM as the primary valuation anchor; build bull/base/bear forward or "
        "normalized earnings and then discuss the PE or EV/EBITDA implied by each case. "
        "For hog breeders, force the bridge through sales kilograms = hog output x "
        "average sale weight, unit spread = realized commodity-hog ASP - complete "
        "hog-breeding cost, and a hog-price sensitivity table for each material "
        "1 CNY/kg ASP or cost move."
    )


def get_market_expectation_instruction() -> str:
    """Return rules for separating business quality from what is already priced."""
    return (
        " Market-expectation discipline: always distinguish a good company from "
        "a good investment. Read the current quote as an implied bundle of "
        "assumptions about earnings power, sales scale, margin durability, and "
        "growth persistence. State explicitly whether the market appears to price "
        "recovery, stagnation, or deterioration, then identify the precise "
        "assumption where your view differs. Never call a stock cheap or expensive "
        "from PE/PB alone. When comparing the quote with interim earnings, distinguish "
        "simple-run-rate earnings from seasonality-adjusted earnings; do not build a "
        "full-year forecast by mechanically multiplying Q1 by four. For resource and "
        "other cyclical companies, treat PE TTM as a backward-looking snapshot and "
        "make forward/normalized earnings scenarios the main valuation test. For hog "
        "breeders, reverse-engineer the hog-price center already implied by the current "
        "market cap under reasonable normalized PE/PB bands before calling the stock "
        "cheap, expensive, or fairly priced."
    )


def get_price_earnings_decomposition_instruction() -> str:
    """Return rules for reading current price through historical EPS and PE drivers."""
    return (
        " Price-EPS-PE decomposition discipline: explain the stock's current quote "
        "through two separate engines: earnings support and valuation multiple. "
        "Use the historical close / PE TTM EPS proxy to ask whether past and current "
        "price levels were supported by higher EPS, higher PE, or both. Do not treat "
        "the proxy as reported EPS; use it as a market-consistent bridge from price "
        "history to expectation. Bulls should prefer earnings-led or credible "
        "double-engine setups. Bears should challenge multiple-led reratings when "
        "EPS support is flat, falling, or already cyclical-peak. The Portfolio "
        "Manager should fold this into the valuation/cycle setup rather than make "
        "it a standalone checklist: say whether today's price is earnings-supported, "
        "multiple-supported, double-engine, or fragile."
    )


def get_investor_interaction_instruction() -> str:
    """Return rules for turning official investor Q&A into investable evidence."""
    return (
        " Investor-interaction discipline: when official exchange-platform Q&A "
        "is available, do not treat it only as a source of themes. Read it on "
        "three layers: (1) what investors repeatedly ask about, which reveals "
        "the market's live concern map; (2) how management answers, separating "
        "substantive, directional-but-unquantified, non-committal, and "
        "unanswered replies; and (3) whether the answer pattern strengthens or "
        "weakens management credibility, disclosure quality, or catalyst "
        "visibility. Repeated questioning with weak answers is itself evidence "
        "of unresolved uncertainty; substantive answers can improve confidence "
        "but remain weaker than filings or announcements. If investors repeatedly "
        "ask about a possible new business or asset bucket, such as compute "
        "leasing, data-center, network-engineering, or large subsidiary asset "
        "movements, explicitly discuss it as an unverified operating-asset clue "
        "or diligence gap; do not silently drop it merely because management "
        "gave a boilerplate answer."
    )


def get_policy_planning_instruction() -> str:
    """Return rules for using official policy plans in investment debate."""
    return (
        " Policy-planning discipline: when national plans or other official "
        "policy files are available, use them to judge strategic priority, "
        "future market expansion, and the likely durability of industry demand. "
        "Separate three layers: policy direction, industry TAM, and "
        "company-specific monetization. Bulls may use policy support to raise "
        "confidence in demand slope when the company has a credible transmission "
        "path into orders, pricing, capacity, or asset value. Bears should test "
        "whether the policy only grows industry volume, benefits competitors "
        "more, or remains too distant from the company's actual earnings bridge. "
        "Policy support can strengthen optionality and scenario weight, but it "
        "must not substitute for contracts, revenue, or cash-flow proof."
    )


def get_three_layer_conclusion_instruction() -> str:
    """Return rules for splitting the final verdict into three different questions."""
    return (
        " Three-layer conclusion discipline: keep three questions separate in the "
        "final verdict. Company quality asks whether the business is good. Current "
        "odds ask whether today's price offers attractive expected value. Relative "
        "allocation asks whether this is the best place to deploy capital versus "
        "same-industry peers and alternative chain positions. A stock may score "
        "well on one layer and poorly on another; do not collapse them into a "
        "single undifferentiated opinion."
    )


def get_management_capital_allocation_instruction() -> str:
    """Return rules for judging stewardship with hard evidence."""
    return (
        " Management-and-capital-allocation discipline: judge stewardship from "
        "hard signals before praise. Use capital returns, buybacks, dividends, "
        "financing, acquisitions, capex, leverage, goodwill, and later ROIC / "
        "cash-flow outcomes to decide whether management compounds value, merely "
        "grows assets, or dilutes owners. For companies that repeatedly seed, "
        "hold, and exit minority investments, also test whether realized gains "
        "plus the current pipeline demonstrate a repeatable first-level investing "
        "capability rather than one lucky mark-to-market. Treat management quality as a synthesis "
        "variable: hard evidence can support or weaken the case, but a single "
        "title, speech, or compensation table is never enough by itself."
    )


def get_shareholder_structure_instruction() -> str:
    """Return rules for reading ownership and chip signals without overfitting them."""
    return (
        " Shareholder-structure discipline: use top holders, float holders, holder "
        "count, insider increases/decreases, pledge ratio, repurchases, and unlock "
        "schedule to refine supply-demand and governance risk. Explain whether "
        "ownership is stabilizing, crowded, or becoming a supply overhang. Distinguish "
        "a historical sell-down that has already executed from a still-live future "
        "overhang; after an event has landed, require separate evidence before "
        "reusing it as a forward-looking bearish driver. Do not let chip signals override the business thesis unless size, timing, "
        "and materiality are clear."
    )


def get_filing_intelligence_instruction() -> str:
    """Return rules for using business evidence buried inside filings."""
    return (
        " Filing-intelligence discipline: read quarterly, half-year, and annual "
        "reports as business documents, not only as sources of the three statements. "
        "Use the filing context in fifteen passes: (1) filing reading coverage audit, "
        "(2) internal filing quality modules, (3) pre-debate underwriting questions, "
        "(4) paragraph reading pack, (5) industry reading pack, "
        "(6) statement table reading pack, (7) filing note reading pack, "
        "(8) financial relationship reading pack, (9) filing textual signals, "
        "(10) business model map, (11) segment economics pack, "
        "(12) business segment valuation map, (13) growth vector map, "
        "(14) material filing findings, and (15) report-to-report bridge. "
        "If the coverage audit is partial, weak, or failed, state the confidence downgrade "
        "before making any filing-backed claim. "
        "The internal filing quality modules are the report-internal buy-side review layer: "
        "accounting reconciliation, segment economics depth, footnote radar, cash-flow "
        "quality, capex/CIP return bridge, MD&A text change, non-recurring profit quality, "
        "balance-sheet forward signals, shareholder-return authenticity, and disclosure "
        "quality. Integrate those findings into the PM Summary, Investment Thesis, valuation, "
        "risk, and verification calendar; do not leave them as a detached checklist. "
        "The pre-debate underwriting questions are the company-specific buy-side agenda "
        "created before the bull/bear debate: answer how the business makes money, what "
        "protects the moat, what drives growth, whether second curves are monetized, "
        "whether earnings convert to cash, how segments should be valued, and which risks "
        "can change equity value. Bulls and bears must debate these questions directly; "
        "the PM should integrate the useful answers into the business-model primer and "
        "core thesis instead of pasting the whole table. "
        "The paragraph reading pack "
        "is the closest thing to actually reading the report: answer its "
        "paragraph-level questions before collapsing the company into ratios. "
        "The industry reading pack is the specialist layer: use it to decide "
        "which operating questions matter most for this company's business model "
        "before interpreting valuation or sentiment. "
        "The statement table reading pack is the hard-accounting layer: use it to test "
        "contract liabilities, receivables, inventory, prepayments, capex, investment assets, "
        "operating cash flow, and impairment. The filing note reading pack is the footnote layer: "
        "use it to surface customer concentration, related parties, guarantees, litigation, "
        "provisioning assumptions, and capitalization choices that may not appear in headline ratios. "
        "The financial relationship reading pack is the integrative layer: use it to explain "
        "how revenue, margin, cash conversion, and balance-sheet demands fit together before "
        "forming a thesis. "
        "The filing textual signals layer reads management wording: proof-backed claims, "
        "implementation language, soft strategy language, risk upgrades, and abnormal silence. "
        "Use it to decide whether a theme is being proven, softened, or avoided; keep a concise "
        "module in the manager report when it changes the thesis. "
        "The filing insight distillation layer is the buy-side memo layer: use it to transform "
        "filing snippets into a small number of central arguments about the core business engine, "
        "second growth curve, quality of growth, monetization gap, capital allocation, and tail "
        "risks. The final manager report should synthesize these as a company thesis rather than "
        "scatter them across many isolated bullet points. "
        "For companies with rich product lines or geographies, the segment economics pack is mandatory: "
        "use annual and half-year product/geography/channel revenue, cost, gross margin, and growth-rate "
        "splits to explain company introduction, bull observations, bear observations, and valuation bridges. "
        "If this segment pack is unavailable or header-only, name that as a research gap before discussing mix. "
        "The business segment valuation map is mandatory for unfamiliar companies: first identify the "
        "core revenue engine from filings, then split mature core businesses, emerging second curves, "
        "geographies, and channels into separate valuation buckets. Mature disclosed businesses may use "
        "normalized earnings, FCF yield, EV/EBITDA, PE, or peer-relative multiples; emerging businesses "
        "belong in SOTP or scenario valuation until segment revenue, margin, asset intensity, utilization, "
        "customer quality, and cash conversion are proven. Never apply one blended multiple before explaining "
        "why a split valuation is unnecessary. "
        "Actively use filing-derived evidence on orders, backlog, customers, "
        "commercialization, prices, margins, capacity, capex, overseas expansion, "
        "R&D, receivables, inventory, cash collection, guarantees, litigation, "
        "impairment, and related-party risk. Bulls should use quantified filing "
        "evidence to support visibility, moat, monetization, and inflection. Bears "
        "should use the same filings to challenge margin durability, working-capital "
        "quality, capital intensity, customer concentration, governance, and tail "
        "risk. Use quarterly reports to test short-cycle confirmation, half-year "
        "reports to judge trend formation and segment mix, and annual reports to "
        "judge business model, capital allocation, and long-cycle risk. Distinguish "
        "audited or quantified disclosures from management narrative, prefer the "
        "latest report when facts evolve, and explain what changed across reports "
        "when that matters. When the filing context contains a core discussion promotion queue, "
        "use it as the bridge from reading to investing: core items belong in the bull/bear debate, "
        "supporting items reinforce or weaken an existing thesis, scenario items belong in "
        "upside/downside cases, and watch items stay out of base-case valuation until upgraded. "
        "Treat unanswered filing questions as explicit research gaps rather than neutral evidence; "
        "if the thesis depends on one, reduce conviction or state what disclosure would close it. "
        "When the filing context contains material findings such "
        "as signed long-term agreements, named customers, capacity-to-demand bridges, "
        "or commercialization milestones, discuss them explicitly in the core thesis "
        "instead of leaving them as background color. Quarterly reports should be "
        "used as short-cycle proof or disproof, half-year reports as structural "
        "confirmation, and annual reports as the base text for business-model and "
        "second-curve understanding. When a paragraph-level filing read contradicts "
        "a surface-level ratio read, surface the contradiction rather than hiding it. "
        "Cross-input synthesis rule: do not discuss filings, policy, investor "
        "interactions, thematic catalysts, peers, and market expectations as "
        "separate silos. Use filing evidence as the anchor, then ask whether each "
        "external input upgrades, weakens, or merely decorates the relevant "
        "industry reading lens. Policy should widen or narrow TAM, interactions "
        "should confirm or challenge execution, thematic catalysts should be "
        "classified by filing-backed monetization, peers should test relative "
        "quality, and market expectations should tell you whether the filing "
        "insight is already priced. If the filing context says report extraction "
        "was unavailable or no readable report text was retrieved, explicitly "
        "downgrade confidence, say that the system did not complete a deep filing "
        "read, and do not claim second-curve, business-model, or filing-backed "
        "catalyst conclusions from that missing layer."
    )


def get_question_led_debate_instruction() -> str:
    """Return rules that force the debate to start from skeptical questions."""
    return (
        " Question-led debate discipline: when Thesis Question Context or "
        "Financial-report intelligence contains Pre-Debate Underwriting "
        "Questions, treat them as the live research agenda rather than a "
        "background appendix. Prefer the Thesis Question Context when present, "
        "because it merges company archetype, sector-native KPIs, forecast "
        "drivers, quality-audit gaps, peers, and verification signals into one "
        "company-specific interrogation list. Preserve the same question IDs or "
        "short labels across the bull case, bear case, Research Manager ruling, "
        "and Portfolio Manager memo so the debate does not talk past itself. "
        "Before writing a directional story, select the 4-7 questions that can "
        "actually change rating, valuation, sizing, or the next verification "
        "action. For each question, keep the full loop: "
        "initial skeptical prior, bull evidence, bear evidence, evidence verdict, "
        "earnings or valuation impact, position-size impact, and next "
        "verification or falsification item. The opening bull turn should answer "
        "the agenda before broader optimism; the opening bear turn should attack "
        "the same agenda before broader objections. Research Manager and PM "
        "outputs should include a compact question-led audit table when the "
        "agenda is supplied. Do not paste the upstream table mechanically; "
        "rewrite it as an investment committee issue log. If a thesis-critical "
        "question remains unanswered, make it an explicit research gap and cap "
        "conviction, SOTP credit, or position size instead of hiding the gap."
    )


def build_instrument_context(ticker: str) -> str:
    """Describe the exact instrument so agents preserve exchange-qualified tickers."""
    return (
        f"The instrument to analyze is `{ticker}`. "
        "Use this exact ticker in every tool call, report, and recommendation, "
        "preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`)."
    )

def create_msg_delete():
    def delete_messages(state):
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]

        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]

        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")

        return {"messages": removal_operations + [placeholder]}

    return delete_messages


        
