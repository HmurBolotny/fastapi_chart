import asyncio
from sqlalchemy import text, insert, select, update, func, cast, Integer, and_, sql, delete
from sqlalchemy.orm import aliased



from database import sync_engine, sync_session_factory, async_session_factory, Base
# from models import WorkersOrm, ResumesOrm, Workload, metadata_obj
from models import MarkCoefficient, MarkDescription, LaboratoryCoefficient, ImpokData, ImpokTrand
#передача любового объекта из  models отдает все метаданные и дет возможность создать все описанные в нем сущности
# если не передавать никакого объекта метаданные будут неопределены и таблици не будут созданы


def create_tables():
    sync_engine.echo = True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


class SyncOrm:
    @staticmethod
    def create_tables():
        sync_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

#написать функцию заполнения тестовыми данными имеет смысл перенести в отдельй файл
    @staticmethod
    def create_test_data():
         pass

    @staticmethod
    def mark_descr_insert(name_mark: str, description: str):
        """
        добавление  в базу марку стали
        """
        with sync_session_factory() as session:
            mark = MarkDescription(name_mark=name_mark, description=description)          # выполняется всегда
            session.add_all([mark])                                                 # список строк у добавлению
            session.commit()
    # проблема передачи только имени, требует второй параметр !!!!!!!!!!!!!

    @staticmethod
    def _mark_insert_many(**kwargs):
        pass

    @staticmethod
    def mark_descr_update(mark_id: int, name_mark: str | None, description: str | None):                #обновление по ид или по имени сделать??
        with sync_session_factory() as session:
            mark_description = session.get(MarkDescription, mark_id)
            mark_description.description = description
            mark_description.name_mark = name_mark
            session.commit()
    # как это реализовать через arg и kwarg?????
    # как реализовать поиск по имани с учетом возможных ошибок при написании


    @staticmethod
    def mark_descr_select():
        with sync_session_factory() as session:
            query = select(MarkDescription)         # SELECT * FROM MarkDescription
            result = session.execute(query)         # выполнить запрос результат записать в  result
            res = result.scalars().all()            # результат возвращяется в виде кортежа из одного объекта
            # тк используется модель MarkDescription его извлекаем scalars
            print(f"{res=}")
            return(res)
    #получение конкретных строк предпологается через relashinship

    @staticmethod
    def mark_coeff_insert(id_mark, coeff_1, coeff_2, coeff_3):
        with sync_session_factory() as session:
            mark_coeff = MarkCoefficient(id_mark=id_mark, coeff_1=coeff_1, coeff_2=coeff_2, coeff_3=coeff_3)  # выполняется всегда
            session.add_all([mark_coeff])  # список строк  у добавлению
            session.commit()

    @staticmethod
    def mark_coeff_update(id_mark, coeff_1, coeff_2, coeff_3):
        with sync_session_factory() as session:
            mark_coeff = session.get(MarkCoefficient, id_mark)
            mark_coeff.coeff_1 = coeff_1
            mark_coeff.coeff_2 = coeff_2
            mark_coeff.coeff_3 = coeff_3
            session.commit()
    # нужна функция для обновления одного конкретного значения?

    @staticmethod
    def mark_coeff_select():
        with sync_session_factory() as session:
            query = select(MarkCoefficient)
            result = session.execute(query)         # выполнить запрос результат записать в  result
            res = result.scalars().all()            # результат возвращяется в виде списка кортежей первым элементом
            # которого являются данные в виде моделей скалятр извлекает первый элемент кортежа
            print(f"{res=}")
            return(res)


    @staticmethod
    def mark_coeff_delete(id_mark):                     # а оно надо?
        with sync_session_factory() as session:
            query = delete(MarkCoefficient).where(MarkCoefficient.id_mark.in_([id_mark]))
            session.execute(query)

    @staticmethod
    def impok_trend_insert(id_roll, imp):        #через kwrg можно передать несколько строк  ли передавать их списком или кортежем
        # рзбить кортежи на составляющие
        with sync_session_factory() as session:
            impok_trend = ImpokTrand(id_roll=id_roll, imp=imp)  # если будет список нужно переделать через for
            session.add_all([impok_trend])  # список строк  у добавлению
            session.commit()

    @staticmethod
    def impok_trend_select(id_roll):
        with sync_session_factory() as session:
            query = select(ImpokTrand, id_roll)
            result = session.execute(query)         # выполнить запрос результат записать в  result
            res = result.scalars().all()
            print(f"{res=}")
            return(res)

    @staticmethod
    def lab_coeff_insert(id_roll, id_mark, imp_1, imp_2, imp_3):
        with sync_session_factory() as session:
            lab_coeff = LaboratoryCoefficient(id_roll=id_roll, id_mark=id_mark, imp_1=imp_1, imp_2=imp_2, imp_3=imp_3)
            # если будет список нужно переделать через for
            session.add_all([lab_coeff])  # список строк  у добавлению
            session.commit()

    @staticmethod
    def lab_coeff_select(id_roll):                        #выборка по марке тоже нужнаможно ли как-то в одно функции реализовать?
        with sync_session_factory() as session:
            query = select(LaboratoryCoefficient, id_roll)
            result = session.execute(query)  # выполнить запрос результат записать в  result
            res = result.scalars().all()
            print(f"{res=}")
            return (res)


    @staticmethod
    def lab_coeff_update(id_lab, id_roll, id_mark, imp_1, imp_2, imp_3):
        with sync_session_factory() as session:
            lab_coeff = session.get(LaboratoryCoefficient, id_lab)
            lab_coeff.id_roll = id_roll
            lab_coeff.id_mark = id_mark
            lab_coeff.imp_1 = imp_1
            lab_coeff.imp_2 = imp_2
            lab_coeff.imp_3 = imp_3
            session.commit()

    @staticmethod
    def lab_coeff_delete(id_lab):
        with sync_session_factory() as session:
            query = delete(LaboratoryCoefficient).where(LaboratoryCoefficient.id_lab.in_([id_lab]))
            session.execute(query)



# def sync_insert_data():
#     with sync_session_factory() as session:
#         worker_bobr = WorkersOrm(username='bobr')
#         worker_volk = WorkersOrm(username='volk')
#         session.add(worker_bobr)
#         session.add(worker_volk)
#         session.add_all([worker_volk, worker_bobr])
#         session.commit()
#
#
# async def async_insert_data():
#     async with async_session_factory() as session:
#         worker_bobr = WorkersOrm(username='bobr')
#         worker_volk = WorkersOrm(username='volk')
#         session.add(worker_bobr)
#         session.add(worker_volk)
#         session.add_all([worker_volk, worker_bobr])
#         await session.commit()
#
#
# class SyncOrm:
#     @staticmethod
#     def create_tables():
#         sync_engine.echo = True
#         Base.metadata.drop_all(sync_engine)
#         Base.metadata.create_all(sync_engine)
#         sync_engine.echo = True
#
#     @staticmethod
#     def insert_workers():
#         with sync_session_factory() as session:
#             worker_bobr = WorkersOrm(username='bobr')
#             worker_volk = WorkersOrm(username='volk')
#             session.add_all([worker_volk, worker_bobr])
#             session.flush()         #   обращение к дазе за id и тд не пишет в базу
#             session.expire_all()    #   сбрасывает все изменения в сессии  но выполняет запрсо к базе
#             session.refresh(worker_volk)        #обнавляет все данные из базы даных
#             session.commit()
#
#     @staticmethod
#     def select_workers():
#         with sync_session_factory() as session:
#             # worker_id = 1
#             # worker = session.get(WorkersOrm,worker_id)
#             query = select(WorkersOrm)
#             result = session.execute(query)
#             workers = result.scalars().all()
#             print(f"{workers=}")
#
#     @staticmethod
#     def update_workers(worker_id: int, new_username: str):
#         with sync_session_factory() as session:
#             worker = session.get(WorkersOrm, worker_id)
#             worker.username = new_username
#             session.commit()
#
#     @staticmethod
#     def insert_resumes():
#         with sync_session_factory() as session:
#             resume_jack_1 = ResumesOrm(
#                 title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
#             resume_jack_2 = ResumesOrm(
#                 title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
#             resume_michael_1 = ResumesOrm(
#                 title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
#             resume_michael_2 = ResumesOrm(
#                 title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
#             session.add_all([resume_jack_1, resume_jack_2,
#                              resume_michael_1, resume_michael_2])
#             session.commit()
#
#     @staticmethod
#     def select_resumes_avg_compensation(like_language: str = "Python"):
#         """
#         select workload,avg(compensation)::int as avg_compensation
#         from resumes
#         where title like'%Python%' and compensation >4 0000
#         group by workload
#         """
#         with sync_session_factory() as session:
#             query = (
#                 select(
#                     ResumesOrm.workload,
#                     cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compenstaion")
#                 )
#                 .select_from(ResumesOrm)
#                 .filter(and_(
#                     ResumesOrm.title.contains(like_language),
#                     ResumesOrm.compensation > 40000
#                 ))
#                 .group_by(ResumesOrm.workload)
#                 .having(cast(func.avg(ResumesOrm.compensation), Integer) > 70000)
#             )
#             print(query.compile(compile_kwargs={"literal_binds": True}))
#             res = session.execute(query)
#             result = res.all()
#             print(result)
#
#     @staticmethod
#     def insert_additional_resumes():
#         with sync_session_factory() as session:
#             workers = [
#                 {"username": "Artem"},  # id 3
#                 {"username": "Roman"},  # id 4
#                 {"username": "Petr"},   # id 5
#             ]
#             resumes = [
#                 {"title": "Python программист", "compensation": 60000, "workload": "fulltime", "worker_id": 3},
#                 {"title": "Machine Learning Engineer", "compensation": 70000, "workload": "parttime", "worker_id": 3},
#                 {"title": "Python Data Scientist", "compensation": 80000, "workload": "parttime", "worker_id": 4},
#                 {"title": "Python Analyst", "compensation": 90000, "workload": "fulltime", "worker_id": 4},
#                 {"title": "Python Junior Developer", "compensation": 100000, "workload": "fulltime", "worker_id": 5},
#             ]
#             insert_workers = insert(WorkersOrm).values(workers)
#             insert_resumes = insert(ResumesOrm).values(resumes)
#             session.execute(insert_workers)
#             session.execute(insert_resumes)
#             session.commit()
#
#     @staticmethod
#     def join_cte_subquery_window_func_my_version(like_language: str = "Python"):            #dont work
#         """
#         WITH helper2 AS (
#             SELECT *, compenstion-avg_workload_compensation AS compenstion_diff
#             FROM
#             (SELECT
#                 w.id,
#                 w.username,
#                 r.compensation,
#                 r.workload,
#                 avg(r.compensation) OVER (PARTITION BY workload):: int AS avg_workload_compensation
#             FROM resumes r
#             JOIN workers w ON r.worker_id = w.id) helper1
#         )
#         SELECT * FROM helper2
#         ORDER BY compensation_diff DESC;
#         """
#         with sync_session_factory() as session:
#             r = aliased(ResumesOrm)
#             w = aliased(WorkersOrm)
#             subq = (
#                 select(
#                     r,
#                     w,
#                     func.avg(r.compensation).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation")
#                 )
#                 .select_from(r)
#                 .join(r, r.worker_id == w.id).subquery("helper1")
#             )
#             cte = (
#                 select(
#                     subq.c.id,
#                     subq.c.username,
#                     subq.c.compensation,
#                     subq.c.workload,
#                     subq.c.avg_workload_compensation,
#                     (subq.c.compensation - subq.c.avg_workload_compensation).label("compensation_diff"),
#                 )
#                 .cte("helper2")
#             )
#             query = (
#                 select(cte)
#                 .order_by(cte.c.compensation_diff.desc())
#             )
#         res = session.execute(query)
#         result = res.all()
#         print(f"{result=}")
#         # print(query.compile(compile_kwargs={"literal_binds": True}))
#
#     @staticmethod
#     def join_cte_subquery_window_func():
#         """
#         WITH helper2 AS (
#             SELECT *, compensation-avg_workload_compensation AS compensation_diff
#             FROM
#             (SELECT
#                 w.id,
#                 w.username,
#                 r.compensation,
#                 r.workload,
#                 avg(r.compensation) OVER (PARTITION BY workload)::int AS avg_workload_compensation
#             FROM resumes r
#             JOIN workers w ON r.worker_id = w.id) helper1
#         )
#         SELECT * FROM helper2
#         ORDER BY compensation_diff DESC;
#         """
#         with sync_session_factory() as session:
#             r = aliased(ResumesOrm)
#             w = aliased(WorkersOrm)
#             subq = (
#                 select(
#                     r,
#                     w,
#                     func.avg(r.compensation).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation"),
#                 )
#                 # .select_from(r)
#                 .join(r, r.worker_id == w.id).subquery("helper1")
#             )
#             cte = (
#                 select(
#                     subq.c.worker_id,
#                     subq.c.username,
#                     subq.c.compensation,
#                     subq.c.workload,
#                     subq.c.avg_workload_compensation,
#                     (subq.c.compensation - subq.c.avg_workload_compensation).label("compensation_diff"),
#                 )
#                 .cte("helper2")
#             )
#             query = (
#                 select(cte)
#                 .order_by(cte.c.compensation_diff.desc())
#             )
#
#             res = session.execute(query)
#             result = res.all()
#             print(f"{len(result)=}. {result=}")
