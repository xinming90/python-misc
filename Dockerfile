FROM python:2.7.10

MAINTAINER xinming90 <panxinming90@gmail.com>

RUN pip install pytest -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

WORKDIR /python-misc

CMD ["py.test", "-sv"]
