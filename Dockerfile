FROM amazonlinux

RUN yum update -y
RUN yum install python3 -y
RUN yum install git -y

RUN git clone https://github.com/chaudhary4sachin/api_gui_unit_testing_fw.git
RUN cd api_gui_unit_testing_fw && pip3 install -r requirements.txt
RUN cd api_gui_unit_testing_fw && python3 tests/api/suite.py