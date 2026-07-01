import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title(
    "📄 Saved Reports"
)

if "report" not in st.session_state:

    st.info(
        "No report generated yet."
    )

else:

    tab1, tab2, tab3 = st.tabs(
        [
            "Report",
            "Sources",
            "Financial Metrics"
        ]
    )

    with tab1:

        st.markdown(
            st.session_state.get(
                "report",
                ""
            )
        )

    with tab2:

        sources = st.session_state.get(
            "sources",
            []
        )

        if sources:

            for source in sources:

                st.write(
                    f"📄 {source['source']}"
                )

        else:

            st.info(
                "No source documents found."
            )

    with tab3:

        metrics = st.session_state.get(
            "metrics",
            {}
        )

        if metrics:

            st.json(
                metrics
            )

        else:

            st.info(
                "No financial metrics available."
            )

    st.markdown("---")

    pdf_path = st.session_state.get(
        "report_path",
        ""
    )

    st.write(
        f"PDF Path: {pdf_path}"
    )

    if pdf_path:

        pdf_file = Path(
            pdf_path
        )

        if pdf_file.exists():

            pdf_bytes = pdf_file.read_bytes()

            st.success(
                "PDF report ready."
            )

            st.download_button(

                label=
                "📥 Download PDF Report",

                data=
                pdf_bytes,

                file_name=
                pdf_file.name,

                mime=
                "application/pdf",

                use_container_width=True

            )

        else:

            st.error(
                f"PDF file not found: {pdf_path}"
            )

    else:

        st.warning(
            "No PDF path available."
        )