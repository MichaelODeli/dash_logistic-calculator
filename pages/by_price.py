from dash import (
    dcc,
    html,
    Input,
    Output,
    callback,
    register_page,
    State,
    Input,
    Output,
    no_update,
    ALL,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from datetime import datetime
from dash_extensions import Purify

register_page(
    __name__, path="/by_price", icon="fa-solid:home", name="Цена | Логист. калькулятор"
)

allow_save_data_in_fields = False


def make_styles(labels, tr_list, style):
    """
    Стилизация только тех элементов, метки которых перечислены в списке labels. У остальных элементов стилизация будет сброшена.
    """
    styles_list = []
    for selected_tr in tr_list:
        label = selected_tr["type"][-1] + str(selected_tr["index"])
        if label in labels:
            styles_list.append(style)
        else:
            styles_list.append(None)
    return [styles_list]


def get_tablerow_with_input(parameter_id=None, value_name=None):
    global allow_save_data_in_fields
    label_type = parameter_id[0]
    label_id = parameter_id[1:]
    return html.Tr(
        [
            html.Td(dcc.Markdown(value_name), style={"text-align": "left"}),
            html.Td(
                dbc.Input(
                    placeholder=f"Введите {parameter_id}",
                    id={"type": f"price-{label_type}", "index": int(label_id)},
                    type="number",
                    persistence=allow_save_data_in_fields,
                )
            ),
        ],
        id={"type": f"tr-{label_type}", "index": int(label_id)},
        style={'vertical-align': 'middle'}
    )


def layout():
    # return html.A("Раздел не готов. Перейдите к расчетам по времени.", href="/by_time")
    values_div = dmc.Stack(
        [
            html.H3("Исходные данные"),
            html.Div(
                [
                    dbc.ButtonGroup(
                        [
                            dbc.InputGroupText(
                                'Выберите параметр для расчета: ',
                                style={
                                    'border-radius': 'var(--bs-border-radius) 0px 0px var(--bs-border-radius)', 'background-color': 'var(--bs-btn-bg)'},
                                    class_name='border border-primary fw-medium'
                            ),
                            dbc.Button("P1", id="toggle_hover_P1", outline=True, color="primary"),
                            dbc.Button("P2", id="toggle_hover_P2", outline=True, color="primary"),
                            dbc.Button("P4", id="toggle_hover_P4", outline=True, color="primary"),
                            dbc.Button("B1", id="toggle_hover_B1", outline=True, color="primary"),
                            dbc.Button("B2", id="toggle_hover_B2", outline=True, color="primary"),
                            dbc.Button("Убрать подсветку", id="toggle_hover_off", outline=True, color="primary"), 
                        ]
                    ),
                    dmc.Space(h=10),
                    html.Table(
                        html.Tbody(
                            [
                                get_tablerow_with_input("S1", "Площадь склада"),

                                html.Tr(dcc.Markdown("**Основные расходы**")),
                                get_tablerow_with_input("F1", "Фонд оплаты труда"),
                                get_tablerow_with_input("F2", "Расходы на подбор персонала"),
                                get_tablerow_with_input("F3", "Расходы на доставку персонала"),
                                get_tablerow_with_input("F4", "Связь и Интернет"),
                                get_tablerow_with_input("F5", "Расходы на обслуж. офисной техники"),
                                get_tablerow_with_input("F6", "Расходы на экспл. офисных помещений"),
                                get_tablerow_with_input("F7", "Канцелярские товары"),
                                get_tablerow_with_input("F8", "Прочие расходы"),
                                get_tablerow_with_input("F9", "ФОТ водителя ПТМ"),
                                get_tablerow_with_input("F10", "ФОТ кладовщика"),
                                get_tablerow_with_input("F11", "ФОТ приемосдатчика"),
                                get_tablerow_with_input("F12", "ФОТ грузчика"),

                                html.Tr(dcc.Markdown("**Расходы на аренду и эксплуатацию**")),
                                get_tablerow_with_input("R1", "Расходы на аренду 1 кв.м площади"),
                                get_tablerow_with_input("R2", "Коммунальные платежи на 1 кв.м"),
                                get_tablerow_with_input("R3", "Прочие расходы на экспл. и содержание склада"),
                                get_tablerow_with_input("R4", "Расходы на экспл. ПРО"),
                                get_tablerow_with_input("R5", "Расходы на экспл. тележек и погрузчиков"),
                                get_tablerow_with_input("R6", "Расходы на экспл. штабелеров"),
                                get_tablerow_with_input("R7", "ТО и прочие расходы на экспл."),

                                html.Tr(dcc.Markdown("**Амортизация**")),
                                get_tablerow_with_input("A1", "Срок амортизации стеллажей в мес."),
                                get_tablerow_with_input("A2", "Срок амортизации прочего скл. оборудования в мес."),
                                get_tablerow_with_input("A3", "Срок амортизации погрузчиков в мес."),
                                get_tablerow_with_input("A4", "Срок амортизации тележек в мес."),
                                get_tablerow_with_input("A5", "Срок амортизации штабелеров в мес."),

                                html.Tr(dcc.Markdown("**Расходы на эксплуатацию**")),
                                get_tablerow_with_input("C1", "Стоимость стеллажей"),
                                get_tablerow_with_input("C2", "Обслуживание стеллажей"),
                                get_tablerow_with_input("C3", "Стоимость прочего скл. оборудования"),
                                get_tablerow_with_input("C4", "Прочие расходы на эксплуатацию"),
                                get_tablerow_with_input("C5", "Стоимость погрузчиков"),
                                get_tablerow_with_input("C6", "Стоимость тележек"),
                                get_tablerow_with_input("C7", "Стоимость штабелеров"),

                                html.Tr(dcc.Markdown("**Дополнительные количественные характеристики**")),
                                get_tablerow_with_input("N1", "Кол-во водителей ПТМ"),
                                get_tablerow_with_input("N2", "Кол-во кладовщиков"),
                                get_tablerow_with_input("N3", "Кол-во приемосдатчиков"),
                                get_tablerow_with_input("N4", "Кол-во грузчиков"),

                                html.Tr(dcc.Markdown("**Расходники**")),
                                get_tablerow_with_input("M1", "Расходники и упаковка"),

                                html.Tr(dcc.Markdown("**Стоимости, согласованные с клиентом**")),
                                get_tablerow_with_input("P3", "Стоимость хранения"),
                                get_tablerow_with_input("P5", "Стоимость приемки одного паллета"),

                                html.Tr(dcc.Markdown("**Кол-во паллет**")),
                                get_tablerow_with_input("T1", "Поступивших на склад в теч. месяца"),
                                get_tablerow_with_input("T2", "Отправившихся со склада в теч. месяца"),
                            ]
                        ),
                        className='table table-borderless'
                    ),
                    dmc.Space(h=10),
                    html.Center(dbc.Button('Выполнить расчет', color='primary', outline=True, id='btn-calc-price', style={'width': '30%'}, size='lg'))
                ],
                className="input-block",
            ),
        ],
        align="center",
        spacing="xl",
    )

    calc_div = dmc.Stack(
        [
            html.H3("Результаты расчетов"),
            html.Div(
                dmc.Stack(
                    [
                        html.Div(id='what-will-be-calculated'),
                        html.Div(id='price-calc-results')
                    ]
                ),
                className="input-block", style={"height": "200px"}),
        ],
        align="center",
        spacing="xl",
    )

    return dmc.Grid(
        [
            dcc.Store('selected_calc_mode'),
            dmc.Col(span="auto", className="block-col hide-it"),
            dmc.Col(html.Div(values_div), span=5, className="block-col"),
            dmc.Col(html.Div(calc_div), span=5, className="block-col"),
            dmc.Col(span="auto", className="block-col hide-it"),
        ]
    )


# for tests
@callback(
    [
        Output("selected_calc_mode", "data"),
        Output("toggle_hover_P1", "n_clicks"),
        Output("toggle_hover_P2", "n_clicks"),
        Output("toggle_hover_P4", "n_clicks"),
        Output("toggle_hover_B1", "n_clicks"),
        Output("toggle_hover_B2", "n_clicks"),
        Output("toggle_hover_off", "n_clicks"),
        Output({"type": "tr-R", "index": ALL}, "className"),
        Output({"type": "tr-A", "index": ALL}, "className"),
        Output({"type": "tr-C", "index": ALL}, "className"),
        Output({"type": "tr-F", "index": ALL}, "className"),
        Output({"type": "tr-S", "index": ALL}, "className"),
        Output({"type": "tr-N", "index": ALL}, "className"),
        Output({"type": "tr-M", "index": ALL}, "className"),
        Output({"type": "tr-P", "index": ALL}, "className"),
        Output({"type": "tr-T", "index": ALL}, "className"),
    ],
    [
        Input("toggle_hover_P1", "n_clicks"),
        Input("toggle_hover_P2", "n_clicks"),
        Input("toggle_hover_P4", "n_clicks"),
        Input("toggle_hover_B1", "n_clicks"),
        Input("toggle_hover_B2", "n_clicks"),
        Input("toggle_hover_off", "n_clicks"),
    ],
    [
        State({"type": "tr-R", "index": ALL}, "id"),
        State({"type": "tr-A", "index": ALL}, "id"),
        State({"type": "tr-C", "index": ALL}, "id"),
        State({"type": "tr-F", "index": ALL}, "id"),
        State({"type": "tr-S", "index": ALL}, "id"),
        State({"type": "tr-N", "index": ALL}, "id"),
        State({"type": "tr-M", "index": ALL}, "id"),
        State({"type": "tr-P", "index": ALL}, "id"),
        State({"type": "tr-T", "index": ALL}, "id"),
    ],
    prevent_initial_call=True,
)
def color_row(
    toggle_hover_P1,
    toggle_hover_P2,
    toggle_hover_P4,
    toggle_hover_B1,
    toggle_hover_B2,
    toggle_hover_off,
    tr_R,
    tr_A,
    tr_C,
    tr_F,
    tr_S,
    tr_N,
    tr_M,
    tr_P,
    tr_T,
):
    # style = {"background-color": "var(--bs-yellow)"}
    style = 'table-primary'
    if toggle_hover_P1 is not None:
        return (
            ['P1']
            + [None]*6
            + make_styles(["R1", "R2", "R3"], tr_R, style)
            + make_styles(["A1", "A2"], tr_A, style)
            + make_styles(["C1", "C2", "C3", "C4"], tr_C, style)
            + make_styles([], tr_F, style)
            + make_styles(['S1'], tr_S, style)
            + make_styles([], tr_N, style)
            + make_styles([], tr_M, style)
            + make_styles([], tr_P, style)
            + make_styles([], tr_T, style)
        )
    elif toggle_hover_P2 is not None:
        return (
            ['P2']
            + [None]*6
            + make_styles(["R1", "R2", "R3"], tr_R, style)
            + make_styles(["A1", "A2"], tr_A, style)
            + make_styles(["C1", "C2", "C3", "C4"], tr_C, style)
            + make_styles(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'], tr_F, style)
            + make_styles(['S1'], tr_S, style)
            + make_styles([], tr_N, style)
            + make_styles([], tr_M, style)
            + make_styles([], tr_P, style)
            + make_styles([], tr_T, style)
        )
    elif toggle_hover_P4 is not None:
        return (
            ['P4']
            + [None]*6
            + make_styles(["R4", "R5", "R6", 'R7'], tr_R, style)
            + make_styles(["A3", "A4", "A5"], tr_A, style)
            + make_styles(["C5", "C6", "C7"], tr_C, style)
            + make_styles(['F9', 'F10', 'F11', 'F12'], tr_F, style)
            + make_styles([], tr_S, style)
            + make_styles(['N1', 'N2', 'N3', 'N4'], tr_N, style)
            + make_styles(['M1'], tr_M, style)
            + make_styles([], tr_P, style)
            + make_styles(['T1', 'T2'], tr_T, style)
        )
    elif toggle_hover_B1 is not None:
        return (
            ['B1']
            + [None]*6
            + make_styles(["R1", "R2", "R3"], tr_R, style)
            + make_styles(["A1", "A2"], tr_A, style)
            + make_styles(["C1", "C2", "C3", "C4"], tr_C, style)
            + make_styles(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'], tr_F, style)
            + make_styles(['S1'], tr_S, style)
            + make_styles([], tr_N, style)
            + make_styles([], tr_M, style)
            + make_styles(['P3'], tr_P, style)
            + make_styles([], tr_T, style)
        )
    elif toggle_hover_B2 is not None:
        return (
            ['B2']
            + [None]*6
            + make_styles(["R4", "R5", "R6", 'R7'], tr_R, style)
            + make_styles(["A3", "A4", "A5"], tr_A, style)
            + make_styles(["C5", "C6", "C7"], tr_C, style)
            + make_styles(['F9', 'F10', 'F11', 'F12'], tr_F, style)
            + make_styles([], tr_S, style)
            + make_styles(['N1', 'N2', 'N3', 'N4'], tr_N, style)
            + make_styles(['M1'], tr_M, style)
            + make_styles(['P5'], tr_P, style)
            + make_styles(['T1', 'T2'], tr_T, style)
        )
    else:
        return (
            [None]
            + [None]*6
            + [[None] * len(tr_R)]
            + [[None] * len(tr_A)]
            + [[None] * len(tr_C)]
            + [[None] * len(tr_F)]
            + [[None] * len(tr_S)]
            + [[None] * len(tr_N)]
            + [[None] * len(tr_M)]
            + [[None] * len(tr_P)]
            + [[None] * len(tr_T)]
        )


@callback(
    Output('price-calc-results', 'children'),
    Input('btn-calc-price', 'n_clicks'),
    [
        State({"type": "tr-R", "index": ALL}, "value"),
        State({"type": "tr-A", "index": ALL}, "value"),
        State({"type": "tr-C", "index": ALL}, "value"),
        State({"type": "tr-F", "index": ALL}, "value"),
        State({"type": "tr-S", "index": ALL}, "value"),
        State({"type": "tr-N", "index": ALL}, "value"),
        State({"type": "tr-M", "index": ALL}, "value"),
        State({"type": "tr-P", "index": ALL}, "value"),
        State({"type": "tr-T", "index": ALL}, "value"),
        State('selected_calc_mode', 'data')
    ],
    prevent_initial_call=True,
)
def make_price_calc(
    n_clicks, 
    tr_R, 
    tr_A, 
    tr_C, 
    tr_F, 
    tr_S, 
    tr_N, 
    tr_M, 
    tr_P, 
    tr_T,
    selected_calc_mode
):
    return f"{selected_calc_mode} not implemented"
