from rest_framework import serializers

from .models import HeadlinerTable


class HeadlinerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HeadlinerTable
        fields = "__all__"

    def create(self, validated_data):
        try:
            lst_patio_code = validated_data['patio_code'].split(";")

            lst_price_old = _correct_price(validated_data['price_old'], len(lst_patio_code))
            lst_price_new = _correct_price(validated_data['price_old'], len(lst_patio_code))

            lst_budget = _correct_budget_and_plan(validated_data['budget'], len(lst_patio_code))
            lst_sales_plan = _correct_budget_and_plan(validated_data['sales_plan'], len(lst_patio_code))

            if validated_data['choice_input'] is False and len(lst_patio_code) > 1:
                raise TypeError

            if validated_data['choice_input'] is True:
                for index, element in enumerate(lst_patio_code):
                    validated_data['patio_code'] = element
                    validated_data['price_old'] = lst_price_old[index]
                    validated_data['price_new'] = lst_price_new[index]
                    validated_data['budget'] = lst_budget[index]
                    validated_data['sales_plan'] = lst_sales_plan[index]

                    if element != lst_patio_code[-1]:
                        HeadlinerTable.objects.create(**validated_data)

        except TypeError:
            print('Error')

        return HeadlinerTable.objects.create(**validated_data)


def _correct_price(data, num):
    return [data for i in range(num)] if data.find(";") == -1 else data.split(';')


def _correct_budget_and_plan(data, num):
    return [str(int(data) / num) for i in range(num)] if data.find(";") == -1 else data.split(';')