# FazendaTech - Programming Challenge

## 04 - Generative AI

This challenge is designed to test your knowledge of Generative AI. Given the fact LLMs are becoming more and more popular, we want to test your knowledge and creativity on how to use them effectively.

There are no right or wrong answers here, so try to be as creative as you can. It's your chance to make an impression!

Here we provide 3 different problems for you to solve. You can choose to solve all of them or just a few. For the sake of not making this challenge too long, we recommend you solve at least 2 problems. Make sure to read all of them first, and pick the ones you feel will better demonstrate your problem solving skills.

> [!IMPORTANT]
> All problems involve creating a LLM Agent prompt. You can use any LLM Agent you want, you'll be evaluated on the quality of the prompt and the adjustments you make to it, not necessarily on the output of the LLM. We recommend using the free versions of [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/), or [Gemini](https://gemini.google.com/), but feel free to use any other LLM chat interface you're comfortable with.

> [!IMPORTANT]
> Make sure to document the process you followed to create the prompt and the adjustments you made to it (and why you made them). Providing just the final prompt you created will not be enough to understand how you approached the problem. Consider also providing a "share link" to the chat conversation with your solutions, but this is not mandatory.

### Problem 01 - Prompt Management and Adjustments

Describe a situation in which a LLM Agent needs to interact with a user that wants to generate a NF-e (Nota Fiscal Eletrônica). Create a prompt that asks the user for the necessary information to generate the NF-e, and adjust it to improve the Agent's accuracy and efficiency.

#### Your Task

1. Select at least a few NF-e fields, but don't go overboard. Around 5 fields should be good enough.
2. Create the prompt that asks the user for the necessary information to generate the NF-e.
3. The LLM Agent's output should include the parsed user input in JSON format, which could hypothetically be used to call an API to issue the NF-e.

### Problem 02 - Data Extraction and Analysis

> [!NOTE]
> This problem requires using a LLM chat interface that allows you to upload files. Some LLMs provide this feature on their free version, so make sure you're able to test this before starting the problem.

You are provided a DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) in PDF format. The DANFE is a simplified version of the NF-e, and it contains some of the  information from the NF-e (which is in XML format) in a more human-readable format.

Given the provided DANFE ([sample-danfe.pdf](./sample-danfe.pdf), from a non-production environment NF-e), create a prompt extracts the necessary information from the DANFE, and provides a plain text summary of the information extracted, and a JSON output that could be used to issue a similar NF-e.

#### Your task

1. Create a prompt that extracts the necessary information from the DANFE.
2. The LLM Agent's output should include a plain text summary of the information extracted, and a JSON output that could be used to issue a similar NF-e.

### Problem 03 - Information Summarization

The Brazilian tax system is complex, and many people are unsure about how to calculate taxes. Create a prompt that helps a farmer understand it. It should explain, in non-technical terms, which taxes are usually paid when selling agricultural products, when they DON'T need to be paid, and what they're used for (e.g., social security, country's infrastructure, etc.).

#### Your Task

1. Create a prompt that helps a farmer understand which taxes are usually paid when selling agricultural products.
2. Keep in mind the farmer is not a tax expert, so the explanation should be simple and straightforward.
3. Consider a user flow in which the farmer asks questions about specific taxes (ICMS, PIS/COFINS, etc.).
