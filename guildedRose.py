class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()

    def update_item(self):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            item.higher()
        else:
            item.lower()
                    
    def higher(self):
        if item.check_quality_name():
                item.quality = item.quality - 1
    def lower(self):
        item.quality()
        item.name()
        item.conjure()
        item.sell()

    def decrease_quality(self):
        item.quality = item.quality - 1

    def increase_quality(self):
        item.quality = item.quality + 1

    def check_quality_name(self):
        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            return True
        return False

    def check_high_sell(self):
        if item.sell_in < 11 and item.quality < 50:
            return True
        return False
    
    def check_low_sell(self):
        if item.sell_in < 6 and item.quality < 50:
            return True
        return False
    
    def higher_quality_name_check(self):
        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            return True
        return False
    
def check_which_sell(self):
    if item.check_high_sell():
        item.increase_quality()
    if item.check_low_sell():
        item.increase_quality()

    def quality(self):
        if item.quality < 50:
            item.quality = item.quality + 1
            item.if_backstage()

    def if_backstage(self):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
             item.check_which_sell()

    def name(self):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def sell(self):
        if item.sell_in < 0:
            item.not_aged_brei()

    def not_aged_brei(self):
        if item.name != "Aged Brie":
            item.name_quality_method()

    def name_quality_method(self):
        if item.name != "Aged Brie":
            item.not_backstage()
        else:
            if item.quality < 50:
                 item.quality = item.quality + 1

    def not_backstage(self):
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
           item.quality_check()

    def quality_check(self):
        if item.higher_quality_name_check():
            item.decrease_quality()
        else:
            item.quality = 0
            
    def conjure(self):
        if name == "Conjured Mana Cake":
            decrease_quality
            decrease_quality
            if sell_in < 0:
                decrease_quality
                decrease_quality

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
