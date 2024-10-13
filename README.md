# Topsis-for-Pretrained-Models

# Sports Text Summarization Evaluation

## Overview

It evaluates pre-trained models for summarizing sports articles using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method. It provides a framework for assessing the performance of different summarization models based on various parameters.

## Objectives

- To assess the performance of different pre-trained summarization models in the domain of sports.
- To implement the TOPSIS method for ranking the models based on their summarization quality.
- To visualize the results for easy comparison of model performance.

## Parameters Evaluated

The following parameters are used to evaluate the models:

1. **ROUGE Score**: Measures the overlap of n-grams between the generated summary and a reference summary (maximize).
2. **Compression Ratio**: Ratio of the summary length to the original text length (maximize).
3. **Execution Time**: Time taken by the model to generate the summary (minimize).
4. **Fluency**: Measures how naturally the summary reads (maximize).
5. **F1-Score**: Balances precision and recall in summarizing sports events (maximize).

## Methodology

1. **Data Collection**: Collect performance metrics for various summarization models applied to sports articles.
2. **TOPSIS Calculation**: Implement the TOPSIS method to rank models based on the defined parameters.
3. **Visualization**: Use matplotlib to create visual representations of the models' performance based on their TOPSIS scores.

## Requirements

To run the code, make sure you have the following libraries installed:

- `numpy`
- `matplotlib`

You can install them using pip:

```bash
pip install numpy matplotlib
