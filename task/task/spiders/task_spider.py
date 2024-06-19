import scrapy
from re import sub, search
import json


class TaskSpider(scrapy.Spider):
    name = "task"

    def start_requests(self):
        url = "https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = sub("\n", "", response.xpath("//h1/text()").get())
        price = sub(
            r"[a-zA-Z\n ]",
            "",
            response.xpath("//span[@class='value']/text()").get()
        )
        colour = response.xpath("//div[contains(@class,'colour-picker')]/@data-colorname").get()
        size_pre = response.xpath("//select[contains(@class,'select-size')]//option[position()>1]/text()").getall()
        size = [sub(r'-(.*)|\n', "", i) for i in size_pre]
        score_count_pre = response.xpath("//script[contains(text(), 'reviewCount')]/text()").get()
        reviews_count = search('"reviewCount":"(.*?)"', score_count_pre).group(1)
        reviews_score = search('"ratingValue":"(.*?)"', score_count_pre).group(1)

        with open("task.json", "w") as file:
            json.dump({
                "name": str(name),
                "price": float(price),
                "colour": str(colour),
                "size": size,
                "reviews_count": int(reviews_count),
                "reviews_score": float(reviews_score)
            }, file)
