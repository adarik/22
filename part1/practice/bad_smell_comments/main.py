# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move(self, field, x_param: int, y_param: int, direction, is_fly: bool, crawl: bool, speed=1):
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direction == 'DOWN':
                new_x = x_param
            elif direction == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direction == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direction == 'DOWN':
                new_y = y_param - speed
                new_x = x_param
            elif direction == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direction == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
