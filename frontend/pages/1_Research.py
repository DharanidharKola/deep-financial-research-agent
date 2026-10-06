import sys
from pathlib import Path

ROOT = Path(
    __file__
).resolve().parents[2]

sys.path.append(
    str(ROOT)
)

import streamlit as st
import pandas as pd
import plotly.express as px

from backend.graph.workflow import (
    graph
)

st.set_page_config(
    page_title="Research",
    layout="wide"
)

st.title(
    "🔎 Financial Research Agent"
)

query = st.text_area(
    "Research Query",
    height=120,
    placeholder="Analyze Indian Pharma sector outlook"
)

#sector = st.selectbox(
#    "Sector",
#    [
#        "IT",
#        "Pharma"
#    ]
#)

if st.button(
    "Generate Research",
    use_container_width=True
):

    if not query:

        st.warning(
            "Please enter a research query."
        )

    else:

        state = {

            "query": query,

 #           "sector": sector,

            "approved": True,

            "search_history": [],

            "findings": [],

            "financial_metrics": {},

            "rag_context": "",

            "source_documents": [],

            "analysis": "",

            "final_report": ""

        }

        with st.spinner(
            "Running Multi-Agent Financial Research..."
        ):

            result = graph.invoke(
                state
            )
        

        st.session_state["report"] = result.get(
            "final_report",
            ""
        )

        st.session_state["sources"] = result.get(
            "source_documents",
            []
        )

        st.session_state["metrics"] = result.get(
            "financial_metrics",
            {}
        )

        st.session_state["report_path"] = result.get(
            "report_path",
            ""
        )

        metrics = result.get(
            "financial_metrics",
            {}
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Companies",
            len(metrics)
        )

        col2.metric(
            "Sources",
            len(
                result.get(
                    "source_documents",
                    []
                )
            )
        )

        col3.metric(
            "Research Steps",
            len(
                result.get(
                    "search_history",
                    []
                )
            )
        )

        st.markdown("---")

        rows = []

        for company, data in metrics.items():

            rows.append({

                "Company":
                company,

                "Market Cap":
                data.get(
                    "market_cap"
                ),

                "Revenue":
                data.get(
                    "revenue"
                ),

                "PE Ratio":
                data.get(
                    "pe_ratio"
                ),

                "Profit Margin (%)":
                round(
                    float(data.get("profit_margin") or 0) * 100,
                    2
                )

            })

        if rows:

            df = pd.DataFrame(
                rows
            )

            st.subheader(
                "Financial Metrics"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader(
                "Revenue Comparison"
            )

            fig = px.bar(
                df,
                x="Company",
                y="Revenue"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.subheader(
                "PE Ratio Comparison"
            )

            fig2 = px.bar(
                df,
                x="Company",
                y="PE Ratio"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        st.subheader(
            "Annual Reports Used"
        )

        for source in result.get(
            "source_documents",
            []
        ):

            st.write(
                f"📄 {source['source']}"
            )

        st.subheader(
            "Research Report"
        )

        st.markdown(
            result.get(
                "final_report",
                ""
            )
        )