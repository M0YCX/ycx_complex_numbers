# Scatter S-Parameters

## Conversion to Y-Parameters
> Source: IEEE Transactions on Microwave Theory and Techniques. Vol 42, No. 2 Feb 1994 [page 206]

$$
\begin{aligned}
Y_{11} &= \frac{(1-S_{11})(Z_{02}^{\ast}+S_{22} Z_{02})+S_{12} S_{21} Z_{02}}{(Z_{01}^{\ast}+S_{11} Z_{01})(Z_{02}^{\ast}+S_{22} Z_{02})-S_{12} S_{21} Z_{01} Z_{02}}\\
%
Y_{12} &= \frac{-2 S_{12} (R_{01} R_{02})^{1/2}}{(Z_{01}^{\ast}+S_{11} Z_{01})(Z_{02}^{\ast}+S_{22} Z_{02})-S_{12} S_{21} Z_{01} Z_{02}} \\
%
Y_{21} &= \frac{-2 S_{21} (R_{01} R_{02})^{1/2}}{(Z_{01}^{\ast}+S_{11} Z_{01})(Z_{02}^{\ast}+S_{22} Z_{02})-S_{12} S_{21} Z_{01} Z_{02}} \\
%
Y_{22} &= \frac{(Z_{01}^{\ast}+S_{11} Z_{01})(1-S_{22})+S_{12} S_{21} S_{01}}{(Z_{01}^{\ast}+S_{11} Z_{01})(Z_{02}^{\ast}+S_{22} Z_{02})-S_{12} S_{21} Z_{01} Z_{02}} \\
\end{aligned}
$$

Where:
* $Z_{01}$ is the complex normalised impedance of port 1 (e.g, $50+0j$),
* $Z_{02}$ is the complex normalised impedance of port 2 (e.g, $50+0j$),
* $Z_{01}^{\ast}$ is the complex __conjugate__ of $Z_{01}$
* $Z_{02}^{\ast}$ is the complex __conjugate__ of $Z_{02}$
* $R_{01}$ is the __real__ part of $Z_{01}$
* $R_{02}$ is the __real__ part of $Z_{02}$

## Conversion to Z-Parameters
> Source: IEEE Transactions on Microwave Theory and Techniques. Vol 42, No. 2 Feb 1994 [page 206]

$$
\begin{aligned}
Z_{11} &= \frac{(Z_{01}^{\ast}+S_{11} Z_{01})(1-S_{22})+S_{12} S_{21} Z_{01}}{(1-S_{11})(1-S_{22})- S_{12} S_{21}} \\
%
Z_{12} &= \frac{2 S_{12} (R_{01} R_{02})^{1/2}}{(1-S_{11})(1-S_{22})- S_{12} S_{21}} \\
%
Z_{21} &= \frac{2 S_{21} (R_{01} R_{02})^{1/2}}{(1-S_{11})(1-S_{22})- S_{12} S_{21}} \\
%
Z_{22} &= \frac{(1-S_{11})(Z_{02}^{\ast}+S_{22} Z_{02})+S_{12} S_{21} Z_{02}}{(1-S_{11})(1-S_{22})- S_{12} S_{21}} \\
%
\end{aligned}
$$

Where:
* $Z_{01}$ is the complex normalised impedance of port 1 (e.g, $50+0j$),
* $Z_{02}$ is the complex normalised impedance of port 2 (e.g, $50+0j$),
* $Z_{01}^{\ast}$ is the complex __conjugate__ of $Z_{01}$
* $Z_{02}^{\ast}$ is the complex __conjugate__ of $Z_{02}$
* $R_{01}$ is the __real__ part of $Z_{01}$
* $R_{02}$ is the __real__ part of $Z_{02}$