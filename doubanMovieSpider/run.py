from scrapy import cmdline


name = 'douban_movie_top250'
cmd = 'scrapy crawl {0} -o douban.csv'.format(name)
cmdline.execute(cmd.split())