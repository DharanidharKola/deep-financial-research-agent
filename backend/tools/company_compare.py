def compare_pe_ratios(
    metrics
):

    comparison = []

    for company, data in metrics.items():

        comparison.append({

            "company":
                company,

            "pe":
                data.get(
                    "pe_ratio"
                )
        })

    comparison.sort(

        key=lambda x:
        x["pe"] or 0,

        reverse=True
    )

    return comparison