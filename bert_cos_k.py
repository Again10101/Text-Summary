# -*- coding: utf-8 -*-
import re

import jieba
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def preprocess_word(text):
    sentences = []
    text = re.sub(r'[^\w\s]', '', text)
    words = jieba.cut(text, cut_all=False)
    for w in words:
        sentences.append(w)
    print(len(sentences))
    return sentences
def top_k_sentences(text, k=3):
    # 加载中文词向量模型
    model = SentenceTransformer('bert-base-chinese')
    # 获取句子列表
    sentences = preprocess_word(text)
    # 计算句子向量
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
    # 计算句子相似度矩阵之前添加以下代码
    sentence_embeddings = sentence_embeddings.cpu().numpy()
    # 计算句子相似度矩阵
    similarity_matrix = cosine_similarity(sentence_embeddings, sentence_embeddings)
    print(similarity_matrix)
    # # 计算句子权重
    # sentence_weights = similarity_matrix.sum(axis=1)
    # print(sentence_weights)
    # print(sentence_weights.argsort())
    # # 获取排名前 k 的句子
    # top_indices = sentence_weights.argsort()[-k:][::-1]
    # # 输出排名前 k 的句子及其权重
    # for index in top_indices:
    #     print(f"句子：{sentences[index]}，权重：{sentence_weights[index]}")

# 测试文本
text = "3月26日,一辆宝马轿车从长春市“名仕山庄”驶出。这个别墅区,被称为一汽的“厂长楼”。中央巡视组在巡视意见中曾对其“点名”。新京报记者涂重航摄3月15日,全国人大代表、一汽集团董事长徐建一开完两会后,被中纪委带走调查。自2011年以来,国家审计署进驻审计后,一汽多名中高层领导落马,有的已被判刑。去年,中央巡视组进驻一汽开展调查,查出一汽集团存在党风廉政建设责任落实不够到位、执行“三重一大”制度不力、顶风违纪和整改工作不力、汽车销售和资源配置领域腐败多发等4大问题。这4大问题件件指向一汽集团的高层负责人。据一汽退休干部透露,徐建一在任集团董事长以来,一汽高层享乐之风严重,一些老干部不断举报现任管理层奢靡腐败。部分老干部对现状不满有一汽内部职工称,前些年,常有老干部在一汽集团大楼前,放着高音喇叭指责现任管理层。今年两会期间,全国人大代表、一汽集团董事长徐建一有些反常。在代表团组审议会上,坐在主席台上的他几乎没有和旁边的吉林省领导说过话。一位曾被其三次拒绝采访的记者回忆,两会期间,徐建一表情总是很严肃。面对采访,他显得很烦躁。3月15日,全国人代会刚结束,徐建一在金台饭店被带走。当日下午,中纪委网站宣布,“中国第一汽车集团公司董事长、党委书记徐建一涉嫌严重违纪违法,目前正接受组织调查。”生于1953年的徐建一与中国一汽同龄。作为一汽的子弟,徐建一除了2003到2007年外调入吉林省任职外,其他时间均在一汽生活、工作。2008年,徐建一成为这家央企的掌舵者。他提出的“施政目标”是带领一汽集团发展自主品牌和整体上市。在被中纪委带走调查前,徐建一主政一汽七年间,不仅未能完成“施政目标”,一汽的市场地位也在不断下滑。这个成绩令一汽人倍感失望。一位接触一汽高层的人士称,长期以来,一汽人都有一种荣誉感、优越感。近几年,公司之间收入差距拉大,干群之间待遇差距也不断加大,也导致那些从建厂开始,一家三代在一汽工作的人对现状不满,特别是一些老干部因为待遇问题,不断向有关方面举报现任管理层奢靡腐败。有一汽内部职工称,前些年,常有老干部坐着轮椅,佩戴着勋章在一汽集团大楼前,放着高音喇叭指责现任管理层存在问题。“这些老干部们对一汽感情很深,现在的失落感也很强。”2011年审计曾发现问题业内有说法称,国内要开设一家一汽大众的4S店,没有1000万元以上打点,根本批不下来。2011年,一汽集团谋取整体上市。国家审计署进驻一汽开展审计,发现巨额资金亏空漏洞。随后,中央巡视组进驻一汽开展调查,相关线索交由中纪委吉林办事处调查。2012年,一汽大众公司原销售公司副总经理静国松接受调查。静国松曾掌握一汽大众汽车指标分配、一汽大众实验车、参展车外销等权力。随着静国松案的深入,一汽大众原销售公司总经理周勇江、原副总经理石涛也被调查。据了解,周勇江、静国松、石涛等人已于去年开庭审理,周勇江被判15年,静国松、石涛被判无期徒刑。三人主要涉嫌4S店的权力寻租腐败以及实验车低价销售存在的腐败问题。据一汽内部人士透露,静国松案发后,一汽大众4S店权力寻租腐败被曝光。由于受到市场追捧,业内有说法称,国内要开设一家一汽大众的4S店,没有1000万元以上打点,根本批不下来,甚至用钱打点也解决不了问题。据业内人士介绍,在汽车经销行业中,奥迪4S店是含金量最高的,一家投资上亿元的4S店,甚至能实现当年即盈利。有汽车经销商在谈及奥迪4S店时表示,“不是有钱就能开的,你的关系得足够有撼动力。”除了开设4S店外,能拿到热销车配置指标也需要打点。据内部人士介绍,长年以来,长春一汽周围住着各地经销商,他们不惜重金行贿一汽领导,希望拿到车辆配置资源。这些热销车型一旦配置下来,如一汽大众的迈腾、速腾、一汽奥迪系列车型等,上市后往往加价销售,谋取暴利。据媒体报道,长春一4S店一位业务员,一年销售奥迪1000多辆。这位名为姜丹丹的VIP业务员被曝与一汽高层有关联,涉嫌通过一汽高层拿到奥迪车配置资源,通过4S店洗钱。在周勇江的二审判决中显示,周勇江为蒋某等人开设4S店提供便利,收受贿赂合计约达1500万元。经过2012年的审计、巡视调查,一汽大众爆出上百名管理层被叫去接受调查。2013年一汽60周年大庆,也显得冷冷清清。据内部人士透露,2012年的审计风暴后,一汽集团董事长徐建一多次前往北京活动,最终将案件范围锁定在一汽大众公司,被调查的人员当中,基本没有涉及集团高层,仅限于一汽大众销售公司的范围。“这种长期存在的4S店寻租,一汽集团高层能独善其身?”3月25日,一汽内部一位退休干部称,静国松仅为一汽大众公司下属销售公司副总经理,他的上面到一汽集团还有四个层级的领导。巡视组意见直指领导班子巡视意见中提到,一汽领导干部存在享乐思想、履职担当不够、自主发展滞后的问题。2014年7月29日至8月29日,中央巡视组进驻一汽集团开展调查。原本已告一段落的静国松、周勇江案继续发酵。当年8月26日,中纪委发出公告,根据巡视组发现的问题线索,吉林省检察机关对一汽大众汽车有限公司原副总经理兼销售公司总经理李武、一汽大众汽车有限公司奥迪销售事业部副总经理周纯涉嫌严重违法问题进行立案调查。有消息人士称,李武、周纯与静国松、周勇江等人同在一汽大众销售公司共事过,他们被抓,是静国松、周勇江案深入查处的结果。除了针对一汽大众销售领域系列腐败案继续查处之外,中央巡视组针对一汽提出四条巡视意见,措施严厉,矛头直指在任的一汽集团高层领导。2014年10月29日下午,中纪委网站公布了中央巡视组对一汽集团的审查意见反馈。中央第十三巡视组组长朱保成指出,巡视组在一汽集团发现的问题主要是:党风廉政建设责任落实不够到位,执行“三重一大”制度不力,顶风违纪问题时有发生,对2011年巡视发现问题整改不力,汽车销售、资源配置领域腐败问题多发。巡视意见中提到,一汽班子成员“一岗双责”流于形式,案件查处不力,领导干部存在享乐思想、履职担当不够、自主发展滞后的问题。一退休干部称,这些问题的指向性很强,均是针对一汽集团的领导班子来的。这位人士称,徐建一在任集团董事长以来,一汽高层享乐之风很严重,引起职工们不满。另外一个突出的问题就是,2002年集团为历任高管修建净月别墅,原本已在一汽分得跃层“厂长楼”的高管们,又分得一套别墅。有内部人士透露,徐建一在2007年回一汽任职后,在净月开发区也分得一套别墅,但他对别墅样式不满,遂推倒重盖,耗费数百万元公款。针对这片别墅区,中央巡视组也专门指出,一汽顶风违纪,对之前查处的问题整改工作不力。特别是2002年未经班子集体决策违规挪用公款2340万在净月开发区购买土地建131栋别墅没追责。3月26日,记者在长春市净月开发区看到,这片名为“名仕山庄”的别墅区,每栋别墅三层、四层不等,每栋约在500平方米左右。据周围的居民称,这片别墅被称为一汽的“厂长楼”,除了一汽高管居住外,还有个别吉林省前任领导干部入住。为特定关系人谋取利益据内部人士透露,一汽一位前任领导的子女、儿媳等,都在一汽下属公司主要岗位任职。中央巡视组还重点点明一汽集团存在的汽车销售、资源配置领域腐败多发问题。其中包括,部分领导干部插手4S店审批,直接参股或拥有4S店,为特定关系人谋取利益。另外还包括,领导身边工作人员利用紧俏车型谋利,帮助他人协调购买紧俏车型。在中央巡视组的通报会上,朱保成指出,已将一些领导干部人员的问题线索,按有关规定转中央纪委、中央组织部及有关部门处理。据一位接近巡视组的人士称,2014年中央巡视组查出的问题已超出吉林省纪检部门调查范围,一些线索由中纪委直接调查。据内部人士透露,很多老干部对目前用人选人方面,特别是领导干部的子女安插进重要的岗位的现象很不满。这位人士举例称,一位一汽前任领导的子女、儿媳等,都在一汽下属公司主要岗位任职。其中一位女子,在一汽大众任公关负责人,每年掌握数十亿元的资金。另外,一些一汽领导干部直接插手采购业务,还有一些领导干部的亲属从事零配件生产经营,从一汽集团谋取利益。据了解,有内部举报称,一汽有高层从内部拿出零配件到全国各地倒卖,原本价值2000元的大众CC配件,到地方经销商手中就达5000多元。对于上述问题,中央巡视组也一一指明追查。特别提到有领导亲属参与供货、一些领导干部参与私人物流企业经营,承包一汽集团汽车运送等业务。另外,每年一汽的广告费用大概有数十亿元。中央巡视组特别指出,一汽集团一些领导干部虚设广告业务量、年底突击支付问题突出。今年1月9日,吉林省检察院宣布,依法对一汽集团原副总经理安德武(正厅级)涉嫌受贿犯罪决定逮捕。今年67岁的安德武已退休7年,2008年退休前曾担任一汽集团副总经理、一汽马自达销售公司董事长等职务。据内部人士透露,安德武系是目前除徐建一外,一汽集团被抓的最高级别领导。安德武被查与其在一汽马自达销售公司期间的数十亿元广告费开支有关。针对巨额广告费腐败,去年11月4日,一汽大众内部下发文件,即日起取消北京海辰恒业传媒广告公司等19家广告、公关类公司的一汽大众供应商资格,停止一切尚未启动的业务。据了解,上述一汽大众公关部负责人已于去年被调查,至今尚未露面。工业用地变为房地产项目据长春市当地人士称,长春几乎一半以上房地产项目都有一汽的影子,或参股,或直接开发。一汽贪腐窝案当中,涉及房地产开发领域的问题也特别突出。据了解,一汽下属公司在全国各地以园区名义圈地现象问题严重。在这一轮巡视当中,中央巡视组指出一汽一些园区投资大、产能过剩、重复建设等问题。为此,一汽取消了轿车公司三工厂项目、天津夏利公司空港开发区整车和动力总成新工厂项目、铸造公司一铸厂搬迁项目二期等项目。据内部人士透露,一汽股份公司旗下13家企业,几乎每家都有自己的土地资源。一汽集团的房地产项目在长春当地亦占有相当的优势。据长春市当地人士称,长春几乎一半以上房地产项目都有一汽的影子,或参股,或直接开发。3月25日,一位接触一汽高层的人士称,除了一汽内部开发的红旗家园、红旗嘉园等小区属于工业用地外,一汽这些年在长春的项目很多都是以工业用地先审批,而后再违规操作变成房地产开发项目。而这些项目很多属于一汽下属公司开发,利益牵扯到一汽高层很多人。另外,在国内其他地方,一汽分公司的工业园区也存在类似情况。据公开资料显示,2006年12月,从未涉足汽车行业的四川明君集团以增资扩股方式注资2.4亿元一汽集团优质资产——一汽川专。2009年,一汽川专搬离其位于成都市二环路东湖片区核心地段的原厂址,腾出约300亩土地。其后,明君集团宣布将在这一地块上打造集五星级酒店、甲级写字楼、商务休闲区、高端品质住宅、多样化金融商业集群等为一体的高端城市综合体。另外,明君集团又收购一汽集团位于长春的一汽华凯和一汽宏鼎两个企业。两个厂区皆位于长春市主城区,土地面积达20多万平方米。两家工厂已启动整体搬迁,原址土地现在都成为了明君旗下房地产企业成都中港置业的优质土地储备。据四川在线报道,汇源通信董事、明君集团创始人徐明君因涉嫌贿赂犯罪自去年12月22日起被监视居住。据了解,在徐明君产业中,汽车和房地产占据着绝对支柱地位。而这两项业务均与一汽集团有着千丝万缕的联系。□新京报记者涂重航长春报道(原标题:一汽反腐:从审计风暴到巡视调查)"


# 选择排名前 2 的句子
top_k_sentences(text, k=10)
