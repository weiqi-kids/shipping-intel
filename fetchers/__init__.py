"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .cosco import CoscoFetcher
from .cssc import CsscFetcher
from .evergreen import EvergreenFetcher
from .hanwha_ocean import HanwhaOceanFetcher
from .hapag import HapagFetcher
from .hd_korea import HdKoreaFetcher
from .maersk import MaerskFetcher
from .samsung_heavy import SamsungHeavyFetcher
from .star_bulk import StarBulkFetcher
from .u_ming import UMingFetcher
from .wan_hai import WanHaiFetcher
from .wisdom import WisdomFetcher
from .yang_ming import YangMingFetcher
from .zim import ZimFetcher

FETCHERS = {
    "cosco": CoscoFetcher,
    "cssc": CsscFetcher,
    "evergreen": EvergreenFetcher,
    "hanwha_ocean": HanwhaOceanFetcher,
    "hapag": HapagFetcher,
    "hd_korea": HdKoreaFetcher,
    "maersk": MaerskFetcher,
    "samsung_heavy": SamsungHeavyFetcher,
    "star_bulk": StarBulkFetcher,
    "u_ming": UMingFetcher,
    "wan_hai": WanHaiFetcher,
    "wisdom": WisdomFetcher,
    "yang_ming": YangMingFetcher,
    "zim": ZimFetcher,
}
