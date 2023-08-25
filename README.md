Project Overview:

In this project, Melbo aims to design a highly secure yet simple Physical Unclonable Function (PUF) utilizing a Conditional Delay Unit (CDU) approach. The CDU takes a select bit and a signal as inputs, and based on the select bit, either relays the input signal with no delay (select bit = 0) or introduces a secret delay of p microseconds (select bit = 1). Melbo's goal is to create a robust PUF by chaining multiple CDUs together, where select bits serve as challenges and the total delay becomes the response. However, to enhance security, Melbo introduces dummy CDUs that do not affect the response, making the PUF more challenging to break.

The project involves implementing a Sparse CDU PUF with D = 2048 CDUs, out of which S = 512 are active. The challenge is to learn a linear model that accurately predicts the response of the PUF using the provided training data. The approach includes techniques such as Naive, Relaxation, and Projected Gradient Descent to develop sparse linear models. The evaluation criteria encompass the speed of the training method, the Euclidean distance between true and learned models, mean absolute error on test data, and the accuracy of discovering the active CDUs.

The project's main tasks are as follows:
1. Mathematical Derivation: Show mathematically how a sparse CDU PUF can be broken by a sparse linear model. Derive the mappings and constraints.
2. Code Implementation: Develop a sparse linear model using the numpy library, with a focus on methods to solve the least squares problem, LASSO, and Projected Gradient Descent.
3. Method Selection and Comparison: Experiment with various methods and explain the choice of the preferred method. Describe experiences with alternative techniques.
4. Hyperparameter Tuning: Describe how optimal hyperparameter values were chosen for the selected method.

The project aims to demonstrate the ability to create an effective sparse linear model for predicting the responses of the Sparse CDU PUF, enhancing security and accuracy.
