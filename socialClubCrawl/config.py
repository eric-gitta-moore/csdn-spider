class Config:
    @staticmethod
    def getUserInfoUrl(user_name):
        return 'https://blog.csdn.net/{}'.format(user_name)

    @staticmethod
    def getRecommendUrl(page):
        return 'https://cms-api.csdn.net/v1/web_home/select_content?componentIds=www-blog-recommend'.format(page)
