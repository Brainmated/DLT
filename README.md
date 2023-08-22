# DLT
*My training repository for deep learning algorithms. Hopefully here I will upload my training path in better understanding the early stages of deep learning with tools such as image classification algorithms, optical character recognition models and recommendation systems.

22/7/2023
-I have just started working with the MNIST dataset to get a grasp of the possibilities of OCR from the first step of image classification. My first lesson starts with the "GNT Learning" training video on Tensorflow and Keras. https://www.youtube.com/watch?v=eU0FFjYumCI&t=2005s
As of today, I upload my hands-on work which will be referred to from time to time to help me build a proper OCR application which will benefit individuals and organizations alike to translate hand-written texts to a digitized mean.

2/8/2023
-With the study material provided by Digital Humanities T.M. i've managed to get a better grasp of Optical Character Recognition as an applicability of machine learning. Through my research and tutorials provided by PyTesseract and the numpy library I've managed to work with image processing, attribute/metadata changes and character readings such as of the Polytonics(Greek). In /OCR I will beging developing more efficient classes which can help reduce distractions in reading text from older images, improve readability and remove unecessary bording to help read, distribute and index information faster and with greater accuracy.

18/8/2023
-I have extracted data from Eurostat in search of the energy consumption in the EU. With ecp.py I have tried to perform a calulcation of the squared root and the mean error to validate my predictions for the years 2022-2026. So far I have managed to plot the data that I have so far and train a model to make future predictions for up to 5 years using ARIMA and SARIMA respectfully. Even after plotting and graphing my findings, I need to update the code to make more valid predictions. In data/ you can find the test.csv that I have used to to extract the data. The ecp.py reads the .csv, asks for the user to select which country they would like to get the prediction from. In data/results/graphs you can find 4 of my graphs being results of my application, Greece, Italy, Spain and Germany. To note, MAE, RMSE and RAME need to be updated to have more appropriate results.

20/8/2023
-New model, gas emissions per EU country. Will be updated for better validation results. The latest model(emissions.py) will merge with the scraping performed in ecp.py to produce comparative results based on the energy consumption and total greenhouse gas emissions. Breakthrough imminent!

21/8/2023
-Classification exercise with Iris.csv @ classification/.

22/8/2023
-Forest Fire Predictions model. This is my current focus right now for a forecasting model using data from 2000 up to 2022. Results will be clearly experimental because not all features might be taken into account.
