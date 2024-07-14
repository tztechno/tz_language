{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "01fa7ecc",
   "metadata": {
    "papermill": {
     "duration": 0.006336,
     "end_time": "2024-07-14T06:32:11.375307",
     "exception": false,
     "start_time": "2024-07-14T06:32:11.368971",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# さまざまな意見についての Vader 感情分析"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2b49915",
   "metadata": {
    "papermill": {
     "duration": 0.004718,
     "end_time": "2024-07-14T06:32:11.385270",
     "exception": false,
     "start_time": "2024-07-14T06:32:11.380552",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# はじめに"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a0ddc42",
   "metadata": {
    "papermill": {
     "duration": 0.004651,
     "end_time": "2024-07-14T06:32:11.395020",
     "exception": false,
     "start_time": "2024-07-14T06:32:11.390369",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "東京都知事選が終わりましたが、候補者に対して賛否両論さまざまな意見が上がっています。今回、収取した意見について Vaderを用いた Sentiment 解析を行い、発言者をクラス分けできるかやってみました。\n",
    "\n",
    "VADER (Valence Aware Dictionary and sEntiment Reasoner) 感情分析は、ソーシャル メディアのテキストで表現された感情を分析するために設計された、語彙とルールに基づく感情分析ツールです。トレーニング済みなので、少ない数のデータに対しても学習無しで解析できます。"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94f5adb8",
   "metadata": {
    "papermill": {
     "duration": 0.004499,
     "end_time": "2024-07-14T06:32:11.405468",
     "exception": false,
     "start_time": "2024-07-14T06:32:11.400969",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 使用ライブラリ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f952470",
   "metadata": {
    "_kg_hide-output": true,
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:11.417881Z",
     "iopub.status.busy": "2024-07-14T06:32:11.417371Z",
     "iopub.status.idle": "2024-07-14T06:32:33.643515Z",
     "shell.execute_reply": "2024-07-14T06:32:33.642272Z"
    },
    "papermill": {
     "duration": 22.23717,
     "end_time": "2024-07-14T06:32:33.647461",
     "exception": false,
     "start_time": "2024-07-14T06:32:11.410291",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting googletrans==3.1.0a0\r\n",
      "  Downloading googletrans-3.1.0a0.tar.gz (19 kB)\r\n",
      "  Preparing metadata (setup.py) ... \u001b[?25l-\b \b\\\b \b|\b \bdone\r\n",
      "\u001b[?25hCollecting httpx==0.13.3 (from googletrans==3.1.0a0)\r\n",
      "  Downloading httpx-0.13.3-py3-none-any.whl.metadata (25 kB)\r\n",
      "Requirement already satisfied: certifi in /opt/conda/lib/python3.10/site-packages (from httpx==0.13.3->googletrans==3.1.0a0) (2024.7.4)\r\n",
      "Collecting hstspreload (from httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading hstspreload-2024.7.1-py3-none-any.whl.metadata (2.1 kB)\r\n",
      "Requirement already satisfied: sniffio in /opt/conda/lib/python3.10/site-packages (from httpx==0.13.3->googletrans==3.1.0a0) (1.3.0)\r\n",
      "Collecting chardet==3.* (from httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading chardet-3.0.4-py2.py3-none-any.whl.metadata (3.2 kB)\r\n",
      "Collecting idna==2.* (from httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading idna-2.10-py2.py3-none-any.whl.metadata (9.1 kB)\r\n",
      "Collecting rfc3986<2,>=1.3 (from httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading rfc3986-1.5.0-py2.py3-none-any.whl.metadata (6.5 kB)\r\n",
      "Collecting httpcore==0.9.* (from httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading httpcore-0.9.1-py3-none-any.whl.metadata (4.6 kB)\r\n",
      "Collecting h11<0.10,>=0.8 (from httpcore==0.9.*->httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading h11-0.9.0-py2.py3-none-any.whl.metadata (8.1 kB)\r\n",
      "Collecting h2==3.* (from httpcore==0.9.*->httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading h2-3.2.0-py2.py3-none-any.whl.metadata (32 kB)\r\n",
      "Collecting hyperframe<6,>=5.2.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading hyperframe-5.2.0-py2.py3-none-any.whl.metadata (7.2 kB)\r\n",
      "Collecting hpack<4,>=3.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==3.1.0a0)\r\n",
      "  Downloading hpack-3.0.0-py2.py3-none-any.whl.metadata (7.0 kB)\r\n",
      "Downloading httpx-0.13.3-py3-none-any.whl (55 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m55.1/55.1 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m133.4/133.4 kB\u001b[0m \u001b[31m5.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading httpcore-0.9.1-py3-none-any.whl (42 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m42.6/42.6 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading idna-2.10-py2.py3-none-any.whl (58 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.8/58.8 kB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading h2-3.2.0-py2.py3-none-any.whl (65 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m65.0/65.0 kB\u001b[0m \u001b[31m3.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading rfc3986-1.5.0-py2.py3-none-any.whl (31 kB)\r\n",
      "Downloading hstspreload-2024.7.1-py3-none-any.whl (1.2 MB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m38.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading h11-0.9.0-py2.py3-none-any.whl (53 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.6/53.6 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading hpack-3.0.0-py2.py3-none-any.whl (38 kB)\r\n",
      "Downloading hyperframe-5.2.0-py2.py3-none-any.whl (12 kB)\r\n",
      "Building wheels for collected packages: googletrans\r\n",
      "  Building wheel for googletrans (setup.py) ... \u001b[?25l-\b \b\\\b \b|\b \b/\b \bdone\r\n",
      "\u001b[?25h  Created wheel for googletrans: filename=googletrans-3.1.0a0-py3-none-any.whl size=16352 sha256=c365613070f73cff06a5f9e5e9bcc87d07804fb460604c49921236bfc1f5ea1d\r\n",
      "  Stored in directory: /root/.cache/pip/wheels/50/5d/3c/8477d0af4ca2b8b1308812c09f1930863caeebc762fe265a95\r\n",
      "Successfully built googletrans\r\n",
      "Installing collected packages: rfc3986, hyperframe, hpack, h11, chardet, idna, hstspreload, h2, httpcore, httpx, googletrans\r\n",
      "  Attempting uninstall: h11\r\n",
      "    Found existing installation: h11 0.14.0\r\n",
      "    Uninstalling h11-0.14.0:\r\n",
      "      Successfully uninstalled h11-0.14.0\r\n",
      "  Attempting uninstall: idna\r\n",
      "    Found existing installation: idna 3.6\r\n",
      "    Uninstalling idna-3.6:\r\n",
      "      Successfully uninstalled idna-3.6\r\n",
      "  Attempting uninstall: httpcore\r\n",
      "    Found existing installation: httpcore 1.0.5\r\n",
      "    Uninstalling httpcore-1.0.5:\r\n",
      "      Successfully uninstalled httpcore-1.0.5\r\n",
      "  Attempting uninstall: httpx\r\n",
      "    Found existing installation: httpx 0.27.0\r\n",
      "    Uninstalling httpx-0.27.0:\r\n",
      "      Successfully uninstalled httpx-0.27.0\r\n",
      "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\r\n",
      "tensorflow-decision-forests 1.8.1 requires wurlitzer, which is not installed.\r\n",
      "jupyterlab 4.2.3 requires httpx>=0.25.0, but you have httpx 0.13.3 which is incompatible.\r\n",
      "jupyterlab 4.2.3 requires jupyter-lsp>=2.0.0, but you have jupyter-lsp 1.5.1 which is incompatible.\r\n",
      "jupyterlab-lsp 5.1.0 requires jupyter-lsp>=2.0.0, but you have jupyter-lsp 1.5.1 which is incompatible.\r\n",
      "tensorflow 2.15.0 requires keras<2.16,>=2.15.0, but you have keras 3.4.1 which is incompatible.\r\n",
      "ydata-profiling 4.6.4 requires numpy<1.26,>=1.16.0, but you have numpy 1.26.4 which is incompatible.\u001b[0m\u001b[31m\r\n",
      "\u001b[0mSuccessfully installed chardet-3.0.4 googletrans-3.1.0a0 h11-0.9.0 h2-3.2.0 hpack-3.0.0 hstspreload-2024.7.1 httpcore-0.9.1 httpx-0.13.3 hyperframe-5.2.0 idna-2.10 rfc3986-1.5.0\r\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/nltk/twitter/__init__.py:20: UserWarning: The twython library has not been installed. Some functionality from the twitter package will not be available.\n",
      "  warnings.warn(\"The twython library has not been installed. \"\n"
     ]
    }
   ],
   "source": [
    "!pip install --upgrade googletrans==3.1.0a0\n",
    "\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from googletrans import Translator\n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer\n",
    "from sklearn.cluster import KMeans, AgglomerativeClustering"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04ef4f21",
   "metadata": {
    "papermill": {
     "duration": 0.008649,
     "end_time": "2024-07-14T06:32:33.668740",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.660091",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# データ収集"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7801bbb1",
   "metadata": {
    "papermill": {
     "duration": 0.008125,
     "end_time": "2024-07-14T06:32:33.685796",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.677671",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "I候補に対する意見をgeminiに問い合わせ収集しました。\n",
    "発言者の苗字は略します。\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1122aa6c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:33.703675Z",
     "iopub.status.busy": "2024-07-14T06:32:33.702636Z",
     "iopub.status.idle": "2024-07-14T06:32:33.710543Z",
     "shell.execute_reply": "2024-07-14T06:32:33.709474Z"
    },
    "papermill": {
     "duration": 0.019825,
     "end_time": "2024-07-14T06:32:33.713272",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.693447",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "japanese_sentences = [\n",
    "    (\"Shinjiro\",\"彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。\"),\n",
    "    (\"Ryuuki\",\"彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。\"),\n",
    "    (\"Mitsuru\",\"彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。\"),\n",
    "    (\"Ikkei\",\"彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。\"),\n",
    "    (\"Ikou\",\"彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。\"),\n",
    "    (\"Naoki\",\"彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。\"),\n",
    "    (\"Ichiro\",\"彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。\"),\n",
    "    (\"Yukio\",\"彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。\"),\n",
    "    (\"Chiharu\",\"彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。\"),\n",
    "    (\"Yuichiro\",\"彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。\"),\n",
    "    (\"Ruri\",\"彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判断が難しい。\"),\n",
    "    (\"Soichiro\",\"彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。\"),\n",
    "]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55024d6d",
   "metadata": {
    "papermill": {
     "duration": 0.007693,
     "end_time": "2024-07-14T06:32:33.733399",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.725706",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "英語に翻訳するので、日本語は英訳し易いように少し手を加えました。"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "442145ae",
   "metadata": {
    "papermill": {
     "duration": 0.007402,
     "end_time": "2024-07-14T06:32:33.749151",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.741749",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# VADER 解析"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63d0df5d",
   "metadata": {
    "papermill": {
     "duration": 0.008689,
     "end_time": "2024-07-14T06:32:33.765458",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.756769",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "\n",
    "\n",
    "極性スコア: VADER は、テキストごとに 4 つの感情スコアを提供します。\n",
    "\n",
    "肯定スコア (pos): 肯定的として分類されるテキストの割合。\n",
    "ネガティブ スコア (neg): ネガティブとして分類されるテキストの割合。\n",
    "ニュートラル スコア (neu): ニュートラルとして分類されるテキストの割合。\n",
    "複合スコア (comp): すべてのレキシコン評価の合計を計算し、-1 (最もネガティブ) から +1 (最もポジティブ) の間で正規化された集計正規化スコア。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4742ee7d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:33.782923Z",
     "iopub.status.busy": "2024-07-14T06:32:33.782517Z",
     "iopub.status.idle": "2024-07-14T06:32:34.652901Z",
     "shell.execute_reply": "2024-07-14T06:32:34.651728Z"
    },
    "papermill": {
     "duration": 0.881787,
     "end_time": "2024-07-14T06:32:34.655418",
     "exception": false,
     "start_time": "2024-07-14T06:32:33.773631",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Shinjiro\n",
      "Original: 彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。\n",
      "Translated: If a person full of vitality like him were to become Tokyo's governor, Tokyo would change dramatically. I have high hopes for him.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.703, 'pos': 0.297, 'compound': 0.765}\n",
      "\n",
      "Name: Ryuuki\n",
      "Original: 彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。\n",
      "Translated: He is a politician with free ideas. I'm looking forward to his future activities.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.784, 'pos': 0.216, 'compound': 0.5106}\n",
      "\n",
      "Name: Mitsuru\n",
      "Original: 彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。\n",
      "Translated: His statements sound like he's telling the truth with the intention of causing a firestorm. I think he has the courage that politicians need.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.704, 'pos': 0.296, 'compound': 0.7906}\n",
      "\n",
      "Name: Ikkei\n",
      "Original: 彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。\n",
      "Translated: He is a politician who speaks politics in easy-to-understand terms. He will gain the support of the people.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.711, 'pos': 0.289, 'compound': 0.7269}\n",
      "\n",
      "Name: Ikou\n",
      "Original: 彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。\n",
      "Translated: His pledge is not concrete. It should be supported by numbers and financial resources.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.85, 'pos': 0.15, 'compound': 0.3182}\n",
      "\n",
      "Name: Naoki\n",
      "Original: 彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。\n",
      "Translated: He seems to be more focused on performance than policy. I can't expect much from him as Tokyo governor.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.855, 'pos': 0.145, 'compound': 0.4391}\n",
      "\n",
      "Name: Ichiro\n",
      "Original: 彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。\n",
      "Translated: Since he has little experience as a politician, there are concerns about whether he will be able to fulfill the important role of Tokyo governor.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.824, 'pos': 0.176, 'compound': 0.5719}\n",
      "\n",
      "Name: Yukio\n",
      "Original: 彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。\n",
      "Translated: He lacks administrative experience and financial knowledge. There are doubts as to whether he has the necessary abilities to serve as Tokyo governor.\n",
      "Sentiment Score: {'neg': 0.087, 'neu': 0.833, 'pos': 0.079, 'compound': -0.0516}\n",
      "\n",
      "Name: Chiharu\n",
      "Original: 彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。\n",
      "Translated: He had an arrogant attitude, interrupting questions and not answering them.\n",
      "Sentiment Score: {'neg': 0.375, 'neu': 0.625, 'pos': 0.0, 'compound': -0.6597}\n",
      "\n",
      "Name: Yuichiro\n",
      "Original: 彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。\n",
      "Translated: His remarks spark important discussions toward the realization of a society that respects diversity.\n",
      "Sentiment Score: {'neg': 0.0, 'neu': 0.625, 'pos': 0.375, 'compound': 0.6124}\n",
      "\n",
      "Name: Ruri\n",
      "Original: 彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判断が難しい。\n",
      "Translated: While he is charismatic, he can also be arrogant and self-righteous. It is difficult to judge whether he is suitable as a politician.\n",
      "Sentiment Score: {'neg': 0.222, 'neu': 0.778, 'pos': 0.0, 'compound': -0.6908}\n",
      "\n",
      "Name: Soichiro\n",
      "Original: 彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。\n",
      "Translated: He cannot run politics with charisma alone. It is important for him to continue building up his track record.\n",
      "Sentiment Score: {'neg': 0.096, 'neu': 0.817, 'pos': 0.087, 'compound': -0.0516}\n",
      "\n"
     ]
    }
   ],
   "source": [
    "translator = Translator()\n",
    "vader_analyzer = SentimentIntensityAnalyzer()\n",
    "\n",
    "names=[]\n",
    "ja=[]\n",
    "en=[]\n",
    "pos=[]\n",
    "neu=[]\n",
    "neg=[]\n",
    "comp=[]\n",
    "for name,sentence in japanese_sentences:\n",
    "    translated_text = translator.translate(sentence, src='ja', dest='en').text\n",
    "    score = vader_analyzer.polarity_scores(translated_text)\n",
    "    names+=[name]\n",
    "    ja+=[sentence]\n",
    "    en+=[translated_text]\n",
    "    pos+=[score['pos']]\n",
    "    neu+=[score['neu']]\n",
    "    neg+=[score['neg']]\n",
    "    comp+=[score['compound']]\n",
    "\n",
    "    print(f\"Name: {name}\")\n",
    "    print(f\"Original: {sentence}\")\n",
    "    print(f\"Translated: {translated_text}\")\n",
    "    print(f\"Sentiment Score: {score}\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a21926ca",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:34.673290Z",
     "iopub.status.busy": "2024-07-14T06:32:34.672886Z",
     "iopub.status.idle": "2024-07-14T06:32:34.710515Z",
     "shell.execute_reply": "2024-07-14T06:32:34.709418Z"
    },
    "papermill": {
     "duration": 0.049532,
     "end_time": "2024-07-14T06:32:34.713032",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.663500",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>ja</th>\n",
       "      <th>en</th>\n",
       "      <th>positive</th>\n",
       "      <th>neutral</th>\n",
       "      <th>negative</th>\n",
       "      <th>comp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Shinjiro</td>\n",
       "      <td>彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。</td>\n",
       "      <td>If a person full of vitality like him were to ...</td>\n",
       "      <td>0.297</td>\n",
       "      <td>0.703</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ryuuki</td>\n",
       "      <td>彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。</td>\n",
       "      <td>He is a politician with free ideas. I'm lookin...</td>\n",
       "      <td>0.216</td>\n",
       "      <td>0.784</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.5106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mitsuru</td>\n",
       "      <td>彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。</td>\n",
       "      <td>His statements sound like he's telling the tru...</td>\n",
       "      <td>0.296</td>\n",
       "      <td>0.704</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7906</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ikkei</td>\n",
       "      <td>彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。</td>\n",
       "      <td>He is a politician who speaks politics in easy...</td>\n",
       "      <td>0.289</td>\n",
       "      <td>0.711</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7269</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ikou</td>\n",
       "      <td>彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。</td>\n",
       "      <td>His pledge is not concrete. It should be suppo...</td>\n",
       "      <td>0.150</td>\n",
       "      <td>0.850</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.3182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Naoki</td>\n",
       "      <td>彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。</td>\n",
       "      <td>He seems to be more focused on performance tha...</td>\n",
       "      <td>0.145</td>\n",
       "      <td>0.855</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.4391</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ichiro</td>\n",
       "      <td>彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。</td>\n",
       "      <td>Since he has little experience as a politician...</td>\n",
       "      <td>0.176</td>\n",
       "      <td>0.824</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.5719</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Yukio</td>\n",
       "      <td>彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。</td>\n",
       "      <td>He lacks administrative experience and financi...</td>\n",
       "      <td>0.079</td>\n",
       "      <td>0.833</td>\n",
       "      <td>0.087</td>\n",
       "      <td>-0.0516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Chiharu</td>\n",
       "      <td>彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。</td>\n",
       "      <td>He had an arrogant attitude, interrupting ques...</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.625</td>\n",
       "      <td>0.375</td>\n",
       "      <td>-0.6597</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Yuichiro</td>\n",
       "      <td>彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。</td>\n",
       "      <td>His remarks spark important discussions toward...</td>\n",
       "      <td>0.375</td>\n",
       "      <td>0.625</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.6124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ruri</td>\n",
       "      <td>彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判...</td>\n",
       "      <td>While he is charismatic, he can also be arroga...</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.778</td>\n",
       "      <td>0.222</td>\n",
       "      <td>-0.6908</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Soichiro</td>\n",
       "      <td>彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。</td>\n",
       "      <td>He cannot run politics with charisma alone. It...</td>\n",
       "      <td>0.087</td>\n",
       "      <td>0.817</td>\n",
       "      <td>0.096</td>\n",
       "      <td>-0.0516</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        name                                                 ja  \\\n",
       "0   Shinjiro    彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。   \n",
       "1     Ryuuki                      彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。   \n",
       "2    Mitsuru          彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。   \n",
       "3      Ikkei              彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。   \n",
       "4       Ikou                       彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。   \n",
       "5      Naoki            彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。   \n",
       "6     Ichiro             彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。   \n",
       "7      Yukio       彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。   \n",
       "8    Chiharu                    彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。   \n",
       "9   Yuichiro             彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。   \n",
       "10      Ruri  彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判...   \n",
       "11  Soichiro         彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。   \n",
       "\n",
       "                                                   en  positive  neutral  \\\n",
       "0   If a person full of vitality like him were to ...     0.297    0.703   \n",
       "1   He is a politician with free ideas. I'm lookin...     0.216    0.784   \n",
       "2   His statements sound like he's telling the tru...     0.296    0.704   \n",
       "3   He is a politician who speaks politics in easy...     0.289    0.711   \n",
       "4   His pledge is not concrete. It should be suppo...     0.150    0.850   \n",
       "5   He seems to be more focused on performance tha...     0.145    0.855   \n",
       "6   Since he has little experience as a politician...     0.176    0.824   \n",
       "7   He lacks administrative experience and financi...     0.079    0.833   \n",
       "8   He had an arrogant attitude, interrupting ques...     0.000    0.625   \n",
       "9   His remarks spark important discussions toward...     0.375    0.625   \n",
       "10  While he is charismatic, he can also be arroga...     0.000    0.778   \n",
       "11  He cannot run politics with charisma alone. It...     0.087    0.817   \n",
       "\n",
       "    negative    comp  \n",
       "0      0.000  0.7650  \n",
       "1      0.000  0.5106  \n",
       "2      0.000  0.7906  \n",
       "3      0.000  0.7269  \n",
       "4      0.000  0.3182  \n",
       "5      0.000  0.4391  \n",
       "6      0.000  0.5719  \n",
       "7      0.087 -0.0516  \n",
       "8      0.375 -0.6597  \n",
       "9      0.000  0.6124  \n",
       "10     0.222 -0.6908  \n",
       "11     0.096 -0.0516  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data=pd.DataFrame()\n",
    "data['name']=names\n",
    "data['ja']=ja\n",
    "data['en']=en\n",
    "data['positive']=pos\n",
    "data['neutral']=neu\n",
    "data['negative']=neg\n",
    "data['comp']=comp\n",
    "display(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26e5d79d",
   "metadata": {
    "papermill": {
     "duration": 0.008043,
     "end_time": "2024-07-14T06:32:34.729413",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.721370",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Agglomerativeクラスタリング"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "be6cc963",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:34.747695Z",
     "iopub.status.busy": "2024-07-14T06:32:34.747298Z",
     "iopub.status.idle": "2024-07-14T06:32:34.793015Z",
     "shell.execute_reply": "2024-07-14T06:32:34.791690Z"
    },
    "papermill": {
     "duration": 0.058287,
     "end_time": "2024-07-14T06:32:34.795953",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.737666",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/sklearn/cluster/_agglomerative.py:983: FutureWarning: Attribute `affinity` was deprecated in version 1.2 and will be removed in 1.4. Use `metric` instead\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>ja</th>\n",
       "      <th>en</th>\n",
       "      <th>positive</th>\n",
       "      <th>neutral</th>\n",
       "      <th>negative</th>\n",
       "      <th>comp</th>\n",
       "      <th>cluster</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Shinjiro</td>\n",
       "      <td>彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。</td>\n",
       "      <td>If a person full of vitality like him were to ...</td>\n",
       "      <td>0.297</td>\n",
       "      <td>0.703</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7650</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ryuuki</td>\n",
       "      <td>彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。</td>\n",
       "      <td>He is a politician with free ideas. I'm lookin...</td>\n",
       "      <td>0.216</td>\n",
       "      <td>0.784</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.5106</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mitsuru</td>\n",
       "      <td>彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。</td>\n",
       "      <td>His statements sound like he's telling the tru...</td>\n",
       "      <td>0.296</td>\n",
       "      <td>0.704</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7906</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ikkei</td>\n",
       "      <td>彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。</td>\n",
       "      <td>He is a politician who speaks politics in easy...</td>\n",
       "      <td>0.289</td>\n",
       "      <td>0.711</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.7269</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ikou</td>\n",
       "      <td>彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。</td>\n",
       "      <td>His pledge is not concrete. It should be suppo...</td>\n",
       "      <td>0.150</td>\n",
       "      <td>0.850</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.3182</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Naoki</td>\n",
       "      <td>彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。</td>\n",
       "      <td>He seems to be more focused on performance tha...</td>\n",
       "      <td>0.145</td>\n",
       "      <td>0.855</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.4391</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ichiro</td>\n",
       "      <td>彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。</td>\n",
       "      <td>Since he has little experience as a politician...</td>\n",
       "      <td>0.176</td>\n",
       "      <td>0.824</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.5719</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Yukio</td>\n",
       "      <td>彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。</td>\n",
       "      <td>He lacks administrative experience and financi...</td>\n",
       "      <td>0.079</td>\n",
       "      <td>0.833</td>\n",
       "      <td>0.087</td>\n",
       "      <td>-0.0516</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Chiharu</td>\n",
       "      <td>彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。</td>\n",
       "      <td>He had an arrogant attitude, interrupting ques...</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.625</td>\n",
       "      <td>0.375</td>\n",
       "      <td>-0.6597</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Yuichiro</td>\n",
       "      <td>彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。</td>\n",
       "      <td>His remarks spark important discussions toward...</td>\n",
       "      <td>0.375</td>\n",
       "      <td>0.625</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.6124</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ruri</td>\n",
       "      <td>彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判...</td>\n",
       "      <td>While he is charismatic, he can also be arroga...</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.778</td>\n",
       "      <td>0.222</td>\n",
       "      <td>-0.6908</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Soichiro</td>\n",
       "      <td>彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。</td>\n",
       "      <td>He cannot run politics with charisma alone. It...</td>\n",
       "      <td>0.087</td>\n",
       "      <td>0.817</td>\n",
       "      <td>0.096</td>\n",
       "      <td>-0.0516</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        name                                                 ja  \\\n",
       "0   Shinjiro    彼のようなバイタリティ溢れる人物が都知事になれば、東京は大きく変わるだろう。彼に期待している。   \n",
       "1     Ryuuki                      彼は、自由な発想を持つ政治家だ。彼の今後の活躍が楽しみだ。   \n",
       "2    Mitsuru          彼の発言は、炎上覚悟で本音を言っているように聞こえる。政治家に必要な勇気だと思う。   \n",
       "3      Ikkei              彼は、分かりやすい言葉で政治を語る政治家だ。彼は国民の支持を集めるだろう。   \n",
       "4       Ikou                       彼の公約は具体性がない。数字や財源の裏付けを示すべきだ。   \n",
       "5      Naoki            彼は政策よりもパフォーマンスに力を入れているようだ。都知事として期待できない。   \n",
       "6     Ichiro             彼は政治家としての経験が浅いため、都知事という大役を果たせるかどうか心配だ。   \n",
       "7      Yukio       彼は行政経験や財政知識が不足している。彼は都知事として必要な能力を備えているのか疑問だ。   \n",
       "8    Chiharu                    彼は質問を遮ったり、答えなかったりするなど、傲慢な態度だった。   \n",
       "9   Yuichiro             彼の発言は、多様性を尊重する社会の実現に向けた重要な議論を呼び起こすものだ。   \n",
       "10      Ruri  彼はカリスマ性がある一方で、傲慢で独りよがりな面もある。政治家としてふさわしい人物かどうか判...   \n",
       "11  Soichiro         彼はカリスマ性だけで政治を運営することはできない。実績を積み重ねていくことが重要だ。   \n",
       "\n",
       "                                                   en  positive  neutral  \\\n",
       "0   If a person full of vitality like him were to ...     0.297    0.703   \n",
       "1   He is a politician with free ideas. I'm lookin...     0.216    0.784   \n",
       "2   His statements sound like he's telling the tru...     0.296    0.704   \n",
       "3   He is a politician who speaks politics in easy...     0.289    0.711   \n",
       "4   His pledge is not concrete. It should be suppo...     0.150    0.850   \n",
       "5   He seems to be more focused on performance tha...     0.145    0.855   \n",
       "6   Since he has little experience as a politician...     0.176    0.824   \n",
       "7   He lacks administrative experience and financi...     0.079    0.833   \n",
       "8   He had an arrogant attitude, interrupting ques...     0.000    0.625   \n",
       "9   His remarks spark important discussions toward...     0.375    0.625   \n",
       "10  While he is charismatic, he can also be arroga...     0.000    0.778   \n",
       "11  He cannot run politics with charisma alone. It...     0.087    0.817   \n",
       "\n",
       "    negative    comp  cluster  \n",
       "0      0.000  0.7650        0  \n",
       "1      0.000  0.5106        4  \n",
       "2      0.000  0.7906        0  \n",
       "3      0.000  0.7269        0  \n",
       "4      0.000  0.3182        3  \n",
       "5      0.000  0.4391        3  \n",
       "6      0.000  0.5719        4  \n",
       "7      0.087 -0.0516        2  \n",
       "8      0.375 -0.6597        1  \n",
       "9      0.000  0.6124        0  \n",
       "10     0.222 -0.6908        1  \n",
       "11     0.096 -0.0516        2  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def doAgglomerative(X, nclust=2):\n",
    "    model = AgglomerativeClustering(n_clusters=nclust, affinity = 'euclidean', linkage = 'ward')\n",
    "    clust_labels = model.fit_predict(X)\n",
    "    return clust_labels\n",
    "\n",
    "clust_labels = doAgglomerative(data.iloc[:,3:],5)\n",
    "agglomerative = pd.DataFrame(clust_labels)\n",
    "data.insert((data.shape[1]),'cluster',agglomerative)\n",
    "display(data)\n",
    "df=data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "072420ff",
   "metadata": {
    "papermill": {
     "duration": 0.008374,
     "end_time": "2024-07-14T06:32:34.813071",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.804697",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "明確な肯定的な人、明確に否定的な人、それ以外に分けることを目的とした。nclust=3では上手くいかなかった。nclust=5にすることで、明確な肯定的な人、明確に否定的な人、のクラスターと取り出すことができた。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6ab99fce",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:34.832943Z",
     "iopub.status.busy": "2024-07-14T06:32:34.832545Z",
     "iopub.status.idle": "2024-07-14T06:32:34.847637Z",
     "shell.execute_reply": "2024-07-14T06:32:34.846507Z"
    },
    "papermill": {
     "duration": 0.028475,
     "end_time": "2024-07-14T06:32:34.850347",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.821872",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   cluster                                  name\n",
      "0        0  [Shinjiro, Mitsuru, Ikkei, Yuichiro]\n",
      "1        1                       [Chiharu, Ruri]\n",
      "2        2                     [Yukio, Soichiro]\n",
      "3        3                         [Ikou, Naoki]\n",
      "4        4                      [Ryuuki, Ichiro]\n"
     ]
    }
   ],
   "source": [
    "cluster = df.groupby('cluster')['name'].apply(list).reset_index()\n",
    "print(cluster)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "240f59a4",
   "metadata": {
    "papermill": {
     "duration": 0.008628,
     "end_time": "2024-07-14T06:32:34.867722",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.859094",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Compound Score (comp) と Neutral Score (neu):\n",
    "テキストの感情の強さと中立的な要素のバランスを確認できます。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "59d44ab1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:34.887671Z",
     "iopub.status.busy": "2024-07-14T06:32:34.886846Z",
     "iopub.status.idle": "2024-07-14T06:32:35.354908Z",
     "shell.execute_reply": "2024-07-14T06:32:35.353579Z"
    },
    "papermill": {
     "duration": 0.481201,
     "end_time": "2024-07-14T06:32:35.357770",
     "exception": false,
     "start_time": "2024-07-14T06:32:34.876569",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 800x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "plt.scatter(df['neutral'], df['comp'], c=df['cluster'], s=100, cmap='viridis', edgecolor='k', alpha=0.6)\n",
    "for i, txt in enumerate(df['name']):\n",
    "    plt.annotate(txt, (df['neutral'][i], df['comp'][i]), textcoords=\"offset points\", xytext=(0,5), ha='center')\n",
    "\n",
    "plt.xlabel('Neutral Values')\n",
    "plt.ylabel('Compound Values')\n",
    "plt.title('Agglomerative Clustering')\n",
    "plt.grid(True)\n",
    "plt.colorbar(label='Cluster')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1de89bbc",
   "metadata": {
    "papermill": {
     "duration": 0.009981,
     "end_time": "2024-07-14T06:32:35.379592",
     "exception": false,
     "start_time": "2024-07-14T06:32:35.369611",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Positive Score (pos) と Negative Score (neg):\n",
    "テキストの肯定的な側面と否定的な側面を比較できます。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d8a67d80",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-14T06:32:35.400642Z",
     "iopub.status.busy": "2024-07-14T06:32:35.400272Z",
     "iopub.status.idle": "2024-07-14T06:32:35.821368Z",
     "shell.execute_reply": "2024-07-14T06:32:35.820363Z"
    },
    "papermill": {
     "duration": 0.43488,
     "end_time": "2024-07-14T06:32:35.824144",
     "exception": false,
     "start_time": "2024-07-14T06:32:35.389264",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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BMnJybC0tISXlxd27tyJbt26ASi9m6e/vz/WrVuHcePGYezYsXBzc8OWLVvQrFmzqhoCAAapRERERKJRCBIo1FzXtCJtquOnn3565vm4uLhSZf3790f//v3Veh9NY5BKREREJJInl4wSs82aiBOniIiIiEjrMJNKREREJBJNLkFV0zCTSkRERERah5lUIiIiIpFowxJUuoKZVCIiIiLSOsykEhEREYmEz6SKh5lUIiIiItI6zKQSERERiUQBidqL71ekzZqIQSoRERGRSDhxSjy83U9EREREWoeZVCIiIiLRiD9xCjX0dj8zqURERESkdZhJJSIiIhKJ8N8hdps1ETOpRERERKR1mEklIiIiEokgSCCIvASV2O1VF8ykEhEREZHWYSaViIiISCSK/w6x26yJGKQSERERiYS3+8XD2/1EREREpHWYSSUiIiISiyApPsRuswZiJpWIiIiItA4zqUREREQi4cQp8TCTSkRERERah5lUIiIiIpEIkECAyLP7RW6vumAmlYiIiIi0DjOpRERERGIR/jvEbrMGYiaViIiIiLQOM6lEREREIlFAAoXIz5CK3V51wSCViIiISCxczF80vN1PRERERFqHmVQiIiIikQhC8SF2mzURM6lEREREpHWYSSUiIiISCVegEg8zqURERESkdbQiSF20aBGcnZ1hZGQEX19fHD16tNy6P/zwA9q3bw9ra2tYW1sjICCgVP3BgwdDIpGoHD169ND0MIiIiKiGK9kWVeyjJqryIHXDhg2IjIzEhAkTcPLkSTRv3hyBgYG4e/dumfXj4uIwaNAg7NmzB/Hx8XByckL37t1x+/ZtlXo9evRAcnKy8vjll19exnCIiIiISARVHqTOmTMH4eHhCAsLg4eHB5YsWQITExMsX768zPpr167Fhx9+CG9vb7i7u+PHH3+EQqFAbGysSj2ZTAa5XK48rK2tX8ZwiIiIqAYrmd0v9lETVenEqfz8fJw4cQJRUVHKMj09PQQEBCA+Pr5CbeTk5KCgoAA2NjYq5XFxcbCzs4O1tTW6dOmCqVOnolatWmW2kZeXh7y8POXrzMxMAEBBQQEKCgrUHdYzlbQndrvaiuPVbRyvbuN4dZsujlcbxqKJ2/M19XZ/lQap9+7dQ1FREezt7VXK7e3tkZiYWKE2Pv/8c9SpUwcBAQHKsh49eqBv375wcXHB1atX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",
      "text/plain": [
       "<Figure size 800x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "plt.scatter(df['positive'], df['negative'], c=df['cluster'], s=100, cmap='viridis', edgecolor='k', alpha=0.6)\n",
    "for i, txt in enumerate(df['name']):\n",
    "    plt.annotate(txt, (df['positive'][i], df['negative'][i]), textcoords=\"offset points\", xytext=(0,5), ha='center')\n",
    "\n",
    "plt.xlabel('Positive Values')\n",
    "plt.ylabel('Negative Values')\n",
    "plt.title('Agglomerative Clustering')\n",
    "plt.grid(True)\n",
    "plt.colorbar(label='Cluster')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9e28b00",
   "metadata": {
    "papermill": {
     "duration": 0.011057,
     "end_time": "2024-07-14T06:32:35.845616",
     "exception": false,
     "start_time": "2024-07-14T06:32:35.834559",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 30746,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 28.195362,
   "end_time": "2024-07-14T06:32:36.578670",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-07-14T06:32:08.383308",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
