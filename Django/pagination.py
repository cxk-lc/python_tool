from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, current_page_num: int, all_page_data,
                 data_num_per_page: int = 10, pagination_length: int = 10):
        self.current_page_num = current_page_num  # 当前页数
        self.data = all_page_data  # 需要分页显示的数据列表
        self.data_num_per_page = data_num_per_page  # 每页显示的数据数量
        self.pagination_length = pagination_length  # 分页器的长度

        self.__a_label_disable = 'style="pointer-events: none;"'

    def pagination_data(self):
        """
        当前页需要显示的数据
        """
        current_page_data = \
            self.data[(self.current_page_num - 1) * self.data_num_per_page:
                      self.current_page_num * self.data_num_per_page]
        # 当前页面数据下标为：[(当前页数-1) * 每页数据数, 当前页数 * 每页数据数]
        return current_page_data

    def __endpoint_pagination(self, half_pagination_length, page_num):
        """
        计算分页器端点页面
        """
        if self.current_page_num <= half_pagination_length:
            pagination_left = 1
        else:
            pagination_left = self.current_page_num - half_pagination_length

        if self.current_page_num + half_pagination_length >= page_num:
            pagination_right = page_num
        else:
            pagination_right = self.current_page_num + half_pagination_length
        return pagination_left, pagination_right

    def __splice_page(self, total_page_num):
        """
        拼接当前分页器显示的页码
        """

        # 计算当前页前后的可选页面
        half_pagination_length, remainder_pagination_length = divmod(
            self.pagination_length, 2)

        pagination_left, pagination_right = self.__endpoint_pagination(
            half_pagination_length, total_page_num)

        # 分页器长度得到具体显示的页面列表
        page_num_list = list(range(pagination_left, pagination_right + 1))
        print(page_num_list)

        # 拼接
        pagination_label = ''

        for num in page_num_list:
            if num == self.current_page_num:
                page_label = f'<li><a href="#">{num}</a></li>'
            else:
                page_label = f'<li><a href="?page={num}">{num}</a></li>'
            pagination_label += page_label

        pagination_label = \
            self.__home_page() + self.__previous_page() + pagination_label + \
            self.__next_page(total_page_num) + self.__end_page(total_page_num)

        pagination_label = f'<ul class="pagination">{pagination_label}</ul>'

        return pagination_label

    def __previous_page(self):
        if self.current_page_num > 1:
            page_num = self.current_page_num - 1
        else:
            page_num = 1
        previous_page_label = \
            f'<li><a href="?page={page_num}" aria-label="Previous">' \
            f'<span aria-hidden="true">&laquo;</span></a></li>'
        return previous_page_label

    def __next_page(self, total_page_num):
        if self.current_page_num < total_page_num:
            page_num = self.current_page_num + 1
        else:
            page_num = total_page_num
        next_page_label = \
            f'<li><a href="?page={page_num}" aria-label="Next">' \
            f'<span aria-hidden="true">&raquo;</span></a></li>'
        return next_page_label

    def __home_page(self):
        if self.current_page_num == 1:
            home_page_label = \
                f'<li><a href="?page=1" {self.__a_label_disable}>' \
                f'<span>首页</span></a></li>'
        else:
            home_page_label = \
                f'<li><a href="?page=1"><span>首页</span></a></li>'
        return home_page_label

    def __end_page(self, total_page_num):
        if self.current_page_num == total_page_num:
            end_page_label = \
                f'<li><a href="?page={total_page_num}" ' \
                f'{self.__a_label_disable}><span>末页</span></a></li>'
        else:
            end_page_label = \
                f'<li><a href="?page={total_page_num}">' \
                f'<span>末页</span></a></li>'
        return end_page_label

    def pagination(self):
        page_quotient, page_remainder = divmod(len(self.data),
                                               self.data_num_per_page)
        # 计算数据总数除以每页显示的数据数量得到的商和余数

        if page_remainder:
            # 有余数，页数等于商+1
            total_page_num = page_quotient + 1
        else:
            # 否则，页数等于商
            total_page_num = page_quotient

        pagination_label = self.__splice_page(total_page_num)

        return mark_safe(pagination_label)


if __name__ == '__main__':
    page = Pagination(5, list(range(500)))

    page_label = page.pagination()
    page_data = page.pagination_data()

    print(page_label)
    print(page_data)
