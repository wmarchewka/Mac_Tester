
�k�X�  �               @   s6   d  d l  m Z m Z m Z Gd d �  d e � Z d S)�    )�QtCore�QtGui�	QtWidgetsc               @   s(   e  Z d  Z d d �  Z d d �  Z d S)�Ui_MainWindowc             C   s�  | j  d � | j d d � t j | � |  _ |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d	 � t j |  j � |  _
 |  j
 j t j	 d d
 d d � � |  j
 j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d  � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d! � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d" � t j |  j � |  _ |  j j t j	 d d d d � � |  j j  d# � t j |  j � |  _ |  j j t j	 d d
 d d � � |  j j  d$ � t j |  j � |  _ |  j j t j	 d d
 d d � � |  j j  d% � t j |  j � |  _ |  j j t j	 d d
 d d � � |  j j  d& � | j |  j � t j | � |  _ |  j j t j	 d' d' d d( � � |  j j  d) � | j |  j � t j | � |  _  |  j  j  d* � | j! t j" j# |  j  � t j$ | � |  _% |  j% j  d+ � | j& |  j% � |  j' | � t j( j) | � d  S),N�
MainWindowi   i�  �centralWidget�<   �P   �   �   �	pbLed1_ON�n   �
pbLed1_OFF��   �2   �   �cbTFP3ComPort��   �   �G   �   �lblTFP3ComPorti�  �[   �lblCycloneComPortir  �cbCycloneComPorti  �cbScannerComPorti  �lblScannerComPort�   �lblModbusComPort�cbModbusComPort�
pbProgTFP3�pbProgCyclone�pbReadScanner�pbSendTelnet�pbDoPing�pbGetADCr   �   �menuBar�mainToolBar�	statusBar)*�setObjectName�resizer   ZQWidgetr   �QPushButtonr   �setGeometryr   ZQRectr   �	QComboBoxr   �QLabelr   r   r   r   r   r   r   r    r!   r"   r#   r$   r%   ZsetCentralWidgetZQMenuBarr'   Z
setMenuBarZQToolBarr(   Z
addToolBarZQtZTopToolBarAreaZ
QStatusBarr)   ZsetStatusBar�retranslateUiZQMetaObjectZconnectSlotsByName)�selfr   � r2   �L/Users/waltermarchewka/Desktop/FixturesProject/Mac_Tester/mainwindow_auto.py�setupUi   s�    """""""""""""""""zUi_MainWindow.setupUic             C   sR  t  j j } | j | d d � � |  j j | d d � � |  j j | d d � � |  j j | d d � � |  j j | d d � � |  j	 j | d d � � |  j
 j | d d � � |  j j | d d � � |  j j | d d	 � � |  j j | d d
 � � |  j j | d d � � |  j j | d d � � |  j j | d d � � d  S)Nr   zLED1 ONzLED1 OFFzTFP3 Com PortzCyclone Com PortzScanner Com PortzModbus Com Portz
PROG TFP3 zPROG CYCLONEzREAD SCANNERZTELNETzDo PINGzGET ADC)r   ZQCoreApplication�	translate�setWindowTitler   ZsetTextr   r   r   r   r   r    r!   r"   r#   r$   r%   )r1   r   Z
_translater2   r2   r3   r0   P   s    zUi_MainWindow.retranslateUiN)�__name__�
__module__�__qualname__r4   r0   r2   r2   r2   r3   r      s   Dr   N)�PyQt5r   r   r   �objectr   r2   r2   r2   r3   �<module>	   s   