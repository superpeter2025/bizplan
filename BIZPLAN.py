import streamlit as st

# Initialize session state to track progress and user inputs
if "responses" not in st.session_state:
    st.session_state["responses"] = [""] * 4  # Store responses for 4 questions
if "completed_steps" not in st.session_state:
    st.session_state["completed_steps"] = 0  # Track how many questions have been answered

# Questions and keys
questions = [
    "Describe in detail (max 100 words) your product",
    "Describe in detail (max 100 words) your target market",
    "Price of your product",
    "Revenue target for the first year"
]
keys = ["product_description", "target_market", "price", "revenue_target"]

# Display each question progressively
for i in range(len(questions)):
    if i <= st.session_state["completed_steps"]:
        # Show the question and text input
        response = st.text_area(questions[i], max_chars=300, key=f"input_{i}") if i < 2 else st.text_input(questions[i], key=f"input_{i}")

        # Next button for each question
        if st.button(f"Next {i + 1}", key=f"next_{i}"):
            if response.strip():  # Ensure response is not empty
                st.session_state["responses"][i] = response
                st.session_state["completed_steps"] += 1
            else:
                st.warning("Please fill in the field before proceeding.")

# Submit button after all questions are answered
if st.session_state["completed_steps"] == len(questions):
    if st.button("Submit"):
        # Generate a 500-word business plan
        product_description = st.session_state["responses"][0]
        target_market = st.session_state["responses"][1]
        price = st.session_state["responses"][2]
        revenue_target = st.session_state["responses"][3]

        business_plan = f"""
        BUSINESS PLAN

        1. Executive Summary:
        Our product is described as follows:
        {product_description}

        Write below 5 characteristics:

        ...............................
        ...............................
        ...............................
        ...............................
        ...............................

        Now convert those 5 characteristics into 5 BENEFITS, which will enable you to sell better:

        ...............................
        ...............................
        ...............................
        ...............................
        ...............................

        2. Target Market:
        We aim to serve the following market:
        {target_market}

        Describe your target market in terms of:

        Age: ..............................
        Education level: ..............................
        Income: ..............................
        Geography: ..............................
        Benefits sought: ..............................
        Usage level: ..............................
        Values: ..............................
        Past purchasing behavior: ..............................
        Synchrographics: ..............................

        3. Pricing Strategy:
        The product is priced at {price}, providing value to our customers while remaining competitive in the market.

        Can you offer a FREE sample? Yes/No
        Can you offer a smaller version of your product for only $1 as a trial? Yes/No
        Can you offer a free trial for 7 days? Yes/No
        Can you offer a Launch Promotion at a heavily discounted price like 50% off? Yes/No
        Can you offer a 2 for 1 special?
        Can you charge a monthly subscription fee? Yes/No

        4. Revenue Goals:
        Our revenue target for the first year is {revenue_target}. This goal aligns with our marketing strategy and expected sales growth.

        How does it translate into a monthly revenue target? Ex. {revenue_target}/12
        How does it translate into a weekly revenue target? Ex. {revenue_target}/52
        How many customer would you need to acquire per week? Ex. ({revenue_target}/{price})/52
        How many leads would you need to acquire per week?
        How many impression would you need to make per week?

        5. Marketing and Sales Plan:
        To achieve our revenue target, we plan to implement a comprehensive marketing strategy, leveraging social media, email campaigns, and partnerships with influencers to reach our target audience.

        6. Operations Plan:
        Our focus is on ensuring a seamless supply chain and excellent customer service to drive satisfaction and repeat purchases.

        7. Financial Plan:
        With the price point of {price}, our target market size, and a solid marketing strategy, we aim to achieve our revenue target of {revenue_target} in the first year while maintaining healthy profit margins.

        8. Conclusion:
        This business plan outlines our roadmap for launching and growing our product in the market, driven by a clear understanding of our product, target audience, pricing, and revenue goals.

        """

        # Save business plan to a text file
        with open("business_plan.txt", "w") as f:
            f.write(business_plan.strip())

        st.success("Business plan generated successfully!")
        st.download_button(
            label="Download Business Plan",
            data=business_plan.strip(),
            file_name="business_plan.txt",
            mime="text/plain"
        )

        # Reset the state for new inputs
        st.session_state["responses"] = [""] * 4
        st.session_state["completed_steps"] = 0
