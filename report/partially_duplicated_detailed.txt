Found 63 partially duplicated files:

Partially similar files found. First length 288, Second length 289,  The files are 99% identicalThe files differ in 2 lines:
	./resources/european/web/src/utils/index.js
	./resources/asia/ui/src/utils/index.js
	Unique lines in first:

	Unique lines in second:
		144	| };
		267	| console.debug('identityData api ', identityData);


Partially similar files found. First length 408, Second length 401,  The files are 99% identicalThe files differ in 3 lines:
	./resources/european/web/src/assets/css/index.less
	./resources/asia/ui/src/assets/css/index.less
	Unique lines in first:
		42	| .hover-primary {
		46	| color: #4318FF!important;
		47	| text-decoration-line: underline;

	Unique lines in second:


Partially similar files found. First length 269, Second length 269,  The files are 99% identicalThe files differ in 1 lines:
	./resources/european/service/src/parachain/staking/base/controller/staking-base-controller.ts
	./resources/asia/service/src/parachain/staking/base/controller/staking-base-controller.ts
	Unique lines in first:
		155	| return this.proxyService(request).getMaxCollatorsPerRound(request);

	Unique lines in second:
		155	| return this.proxyService(request).getMaxCollatorsPerRound(request.chainId);


Partially similar files found. First length 92, Second length 92,  The files are 97% identicalThe files differ in 2 lines:
	./resources/european/service/package.json
	./resources/asia/service/package.json
	Unique lines in first:
		1	| "name": "cumulon-protocol-portal-service",

	Unique lines in second:
		0	| {
		1	| "name": "go-staking-portal-service",


Partially similar files found. First length 27, Second length 27,  The files are 96% identicalThe files differ in 1 lines:
	./resources/european/web/src/api/platform.js
	./resources/asia/ui/src/api/platform.js
	Unique lines in first:

	Unique lines in second:
		17	| };


Partially similar files found. First length 587, Second length 581,  The files are 96% identicalThe files differ in 11 lines:
	./resources/european/web/src/views/home/index.vue
	./resources/asia/ui/src/views/home/index.vue
	Unique lines in first:
		12	| Support {{ supportChainList.map((v) => v.chainId).join("; ") }}
		56	| v-if="$store.getters.polkadotWalletTransformAddress"
		73	| :content="$store.getters.polkadotWalletTransformAddress"
		77	| $store.getters.polkadotWalletTransformAddress
		85	| @click="
		86	| $utils.copy($store.getters.polkadotWalletTransformAddress)
		87	| "
		116	| {{ sv.free == undefined ? "--" : $utils.roundNumber(sv.free) }}
		216	| watch: {
		217	| "$store.state.global.metamaskWallet": {},
		221	| console.log('111',this.$store.state.global.supportChainList);

	Unique lines in second:
		12	| Support Litentry; manta; moonriver; moonbeam; bifrost
		21	| <div
		56	| v-if="$store.state.global.polkadotWallet.address"
		73	| :content="$store.state.global.polkadotWallet.address"
		77	| $store.state.global.polkadotWallet.address
		85	| @click="$utils.copy($store.state.global.polkadotWallet.address)"
		114	| {{ sv.free == undefined ? "--" : sv.free }}
		207	| };
		273	| img {


Partially similar files found. First length 62, Second length 62,  The files are 96% identicalThe files differ in 1 lines:
	./resources/european/service/src/common/interceptor/HttpCacheInterceptor.ts
	./resources/asia/service/src/common/interceptor/HttpCacheInterceptor.ts
	Unique lines in first:
		39	| if (!key || ttlValueOrFactory === null || ttlValueOrFactory === 0) {

	Unique lines in second:
		39	| if (!key) {


Partially similar files found. First length 442, Second length 430,  The files are 95% identicalThe files differ in 14 lines:
	./resources/european/service/src/parachain/staking/base/service/staking-base-service.ts
	./resources/asia/service/src/parachain/staking/base/service/staking-base-service.ts
	Unique lines in first:
		35	| import { StakingRequest } from "src/viewModel/staking/StakingRequest";
		118	| const where: any = {
		121	| if (request.collator && request.collator.length) {
		122	| where.collator = request.collator;
		124	| if (request.roundindex ) {
		125	| where.realroundindex = request.roundindex;
		128	| where,
		144	| const where: any = {
		145	| account: request.delegatorAccount
		147	| if (request.actionType) {
		148	| where.actiontype = request.actionType
		465	| async getMaxCollatorsPerRound(request: StakingRequest): Promise<number> {
		466	| let record = await DbManager.get(request).cnhRepository.findOne({
		474	| let record = await DbManager.get(request).chainStateRepository.findOne({});

	Unique lines in second:
		453	| async getMaxCollatorsPerRound(chainId: string): Promise<number> {
		454	| let record = await DbManager.get(chainId).cnhRepository.findOne({
		462	| let record = await DbManager.get(chainId).chainStateRepository.findOne({});


Partially similar files found. First length 67, Second length 64,  The files are 95% identicalThe files differ in 2 lines:
	./resources/european/service/src/common/entity/StakingPortalStat/StatDelegator.entity.ts
	./resources/asia/service/src/common/entity/StakingModule/StatDelegator.entity.ts
	Unique lines in first:
		8	| @PrimaryColumn({name: 'chain_id'})
		9	| chainId: string;

	Unique lines in second:


Partially similar files found. First length 31, Second length 31,  The files are 94% identicalThe files differ in 1 lines:
	./resources/european/web/src/main.ts
	./resources/asia/ui/src/main.js
	Unique lines in first:
		21	| (window as any).localforage = localforage;

	Unique lines in second:
		21	| window.localforage = localforage;


Partially similar files found. First length 139, Second length 139,  The files are 94% identicalThe files differ in 5 lines:
	./resources/european/web/src/views/collatorDetail/RewardTable.vue
	./resources/asia/ui/src/views/collatorDetail/RewardTable.vue
	Unique lines in first:
		20	| <el-table-column label="Timestamp" min-width="160">

	Unique lines in second:
		8	| />
		13	| />
		20	| <el-table-column label="Timestamp" min-width="120">
		52	| };
		72	| };


Partially similar files found. First length 106, Second length 96,  The files are 90% identicalThe files differ in 7 lines:
	./resources/european/web/src/router/index.js
	./resources/asia/ui/src/router/index.js
	Unique lines in first:
		54	| title: 'Summary'
		55	| // title: 'Web3Go Staking'
		99	| router.beforeEach(async (to, from, next) => {
		100	| if (to.name !== 'home' && !store.state.global.currentChain.network) {
		101	| next({
		102	| name: 'home'
		104	| return;

	Unique lines in second:
		24	| //     {
		53	| title: 'Web3Go Staking'


Partially similar files found. First length 24, Second length 24,  The files are 90% identicalThe files differ in 1 lines:
	./resources/european/service/src/main.ts
	./resources/asia/service/src/main.ts
	Unique lines in first:
		16	| .setTitle('cumulon-protocol-portal-service')

	Unique lines in second:
		16	| .setTitle('go-staking-portal-service')


Partially similar files found. First length 37, Second length 37,  The files are 89% identicalThe files differ in 2 lines:
	./resources/european/web/public/index.html
	./resources/asia/ui/public/index.html
	Unique lines in first:
		8	| <link rel="icon" href="<%= BASE_URL %>favicon2.ico">
		12	| <script src="./config.js"></script>

	Unique lines in second:
		8	| <link rel="icon" href="<%= BASE_URL %>favicon.ico">
		12	| <script src="config.js"></script>


Partially similar files found. First length 17, Second length 17,  The files are 89% identicalThe files differ in 1 lines:
	./resources/european/service/src/parachain/staking/portal/staking-home.module.ts
	./resources/asia/service/src/parachain/staking/portal/staking-home.module.ts
	Unique lines in first:
		12	| max: 500

	Unique lines in second:
		12	| ttl: 15,


Partially similar files found. First length 548, Second length 489,  The files are 88% identicalThe files differ in 30 lines:
	./resources/european/web/src/views/Layout/index.vue
	./resources/asia/ui/src/views/Layout/index.vue
	Unique lines in first:
		5	| <!-- <img class="icon" src="@/assets/images/home/Frame(1).png" alt="" />
		6	| -->
		7	| <img class="icon" src="@/assets/images/home/cumulon.png" alt="" />
		93	| position="bottom"
		96	| content="Please select chain first"
		118	| $store.state.global.currentChain.symbols && $route.name !== 'home'
		120	| class="token-wrap"
		122	| <div class="token">
		123	| Token：{{ $store.state.global.currentChain.symbols[0] }}
		136	| <div class="bt-right">
		137	| <div class="doc hover-item">
		138	| <img src="@/assets/images/home/doc.png" alt="" />
		143	| !$store.getters.polkadotWalletTransformAddress
		158	| v-if="$store.state.global.metamaskWallet.address"
		159	| class="circle"
		168	| v-if="$store.getters.polkadotWalletTransformAddress"
		169	| class="circle"
		194	| import ConnectWalletModal from "./ConnectWalletModal";
		248	| !this.$store.getters.polkadotWalletTransformAddress) ||
		285	| // padding: 49px 62px;
		371	| height: calc(100% - 427px);
		398	| .token-wrap {
		399	| padding: 40px 24px;
		436	| padding-left: 290px;
		455	| .bt-right {
		459	| .doc {
		460	| width: 56px;
		461	| height: 56px;
		463	| box-shadow: 4px 8px 40px 4px rgba(112, 144, 176, 0.08);
		469	| img{

	Unique lines in second:
		5	| <img class="icon" src="@/assets/images/home/Frame(1).png" alt="" />
		23	| />
		42	| <img
		45	| alt=""
		46	| />
		48	| <img
		51	| alt=""
		91	| position="rt"
		94	| content="Please select chain frist"
		127	| !$store.state.global.polkadotWallet.address
		141	| <div v-if="$store.state.global.metamaskWallet.address" class="circle">
		148	| <div v-if="$store.state.global.polkadotWallet.address" class="circle">
		171	| import ConnectWalletModal from "./ConnectWalletModal/index.vue";
		196	| };
		225	| !this.$store.state.global.polkadotWallet.address) ||
		262	| padding: 49px 62px;
		347	| height: calc(100% - 265px);
		395	| margin-left: 290px;


Partially similar files found. First length 174, Second length 161,  The files are 87% identicalThe files differ in 15 lines:
	./resources/european/web/src/views/delegatorDetail/ActionTable.vue
	./resources/asia/ui/src/views/delegatorDetail/ActionTable.vue
	Unique lines in first:
		4	| <el-table-column prop="state" label="Collator" min-width="120">
		10	| class="hover-item"
		11	| @click="goToCollatorDetail(scope.row.collator)"
		16	| <span
		17	| class="hover-primary"
		18	| style="margin-left: 8px"
		19	| @click="goToCollatorDetail(scope.row.collator)"
		20	| >{{
		24	| }}</span
		25	| >
		44	| <el-table-column label="Timestamp" min-width="160">
		88	| goToCollatorDetail(address) {
		89	| localStorage.setItem("routeParamsAddress", address);
		90	| this.$router.push({
		91	| name: "collatorDetail",

	Unique lines in second:
		4	| <el-table-column prop="state" label="Delegator" min-width="120">
		14	| <span style="margin-left: 8px">{{
		37	| <el-table-column label="Timestamp" min-width="120">


Partially similar files found. First length 178, Second length 165,  The files are 87% identicalThe files differ in 15 lines:
	./resources/european/web/src/views/delegatorDetail/RewardTable.vue
	./resources/asia/ui/src/views/delegatorDetail/RewardTable.vue
	Unique lines in first:
		4	| <el-table-column prop="state" label="Collator" min-width="120">
		10	| class="hover-item"
		11	| @click="goToCollatorDetail(scope.row.collator)"
		16	| <span
		17	| class="hover-primary"
		18	| style="margin-left: 8px"
		19	| @click="goToCollatorDetail(scope.row.collator)"
		20	| >{{
		24	| }}</span
		25	| >
		48	| <el-table-column label="Timestamp" min-width="160">
		91	| goToCollatorDetail(address) {
		92	| localStorage.setItem("routeParamsAddress", address);
		93	| this.$router.push({
		94	| name: "collatorDetail",

	Unique lines in second:
		4	| <el-table-column prop="state" label="Delegator" min-width="120">
		14	| <span style="margin-left: 8px">{{
		18	| }}</span>
		41	| <el-table-column label="Timestamp" min-width="120">
		78	| };


Partially similar files found. First length 199, Second length 185,  The files are 86% identicalThe files differ in 14 lines:
	./resources/european/web/src/views/collatorDetail/DelegatorTable.vue
	./resources/asia/ui/src/views/collatorDetail/DelegatorTable.vue
	Unique lines in first:
		32	| class="hover-item"
		33	| @click="goToDelegatorDetail(scope.row.owner)"
		38	| <span
		39	| class="hover-primary"
		40	| style="margin-left: 8px"
		41	| @click="goToDelegatorDetail(scope.row.owner)"
		42	| >{{
		46	| }}</span
		110	| methods: {
		111	| goToDelegatorDetail(address) {
		112	| localStorage.setItem("routeParamsAddress", address);
		113	| this.$router.push({
		114	| name: "delegatorDetail",
		115	| });

	Unique lines in second:
		36	| <span style="margin-left: 8px">{{
		40	| }}</span>
		64	| />
		101	| };
		103	| methods: {},
		104	| };


Partially similar files found. First length 88, Second length 88,  The files are 85% identicalThe files differ in 6 lines:
	./resources/european/web/src/utils/chain/chain.utils.ts
	./resources/asia/ui/src/utils/chain/chain.utils.ts
	Unique lines in first:
		9	| const accounts = ChainUtils.ss58transform(account, [network]);
		22	| const accounts = ChainUtils.ss58transform(account, []);
		37	| const keys = [];
		42	| const publicKeys = keyring.getPublicKeys();
		71	| const key = {
		90	| const v = parseInt(p.toString());

	Unique lines in second:
		9	| let accounts = ChainUtils.ss58transform(account, [network]);
		22	| let accounts = ChainUtils.ss58transform(account, []);
		37	| let keys = [];
		42	| let publicKeys = keyring.getPublicKeys();
		71	| let key = {
		90	| let v = parseInt(p.toString());


Partially similar files found. First length 49, Second length 46,  The files are 84% identicalThe files differ in 5 lines:
	./resources/european/service/src/parachain/staking/core/db/database.module.ts
	./resources/asia/service/src/parachain/staking/core/db/database.module.ts
	Unique lines in first:
		8	| import { GO_STAKING_STAT_DB_CONNECT_ALIAS, GO_STAKING_STAT_DB_PROVIDER } from "src/common/orm/database.provider.v2/portal";
		9	| import { GoStakingPortalDbRegister } from "./go-staking-portal-db-register";
		12	| providers: [GO_STAKING_STAT_DB_PROVIDER, GoStakingPortalDbRegister],
		18	| maxQueryExecutionTime: 4000,
		43	| // ChainConnectManager.register(chain.info.id, new ChainConnector(chain.info, chain.defaultValues));

	Unique lines in second:
		10	| providers: [],
		40	| ChainConnectManager.register(chain.info.id, new ChainConnector(chain.info, chain.defaultValues));


Partially similar files found. First length 14, Second length 12,  The files are 83% identicalThe files differ in 2 lines:
	./resources/european/service/src/viewModel/staking/DelegatorActionHistory.ts
	./resources/asia/service/src/viewModel/staking/DelegatorActionHistory.ts
	Unique lines in first:
		9	| @ApiProperty({ required: false })
		10	| actionType: string;

	Unique lines in second:


Partially similar files found. First length 155, Second length 99,  The files are 82% identicalThe files differ in 16 lines:
	./resources/european/web/src/api/staking/index.js
	./resources/asia/ui/src/api/staking/index.js
	Unique lines in first:
		79	| export function delegatorStatistics(data) {
		81	| url: '/parachain/staking/delegator/statistics',
		107	| export function getCollatorReward(data) {
		109	| url: '/parachain/staking/getCollatorReward',
		114	| export function delegatorInfo(data) {
		116	| url: '/parachain/staking/delegator/info',
		121	| export function getMaxNominatorsPerCollator(data) {
		123	| url: '/parachain/staking/getMaxNominatorsPerCollator',
		128	| export function timeMachineRewardsStat(data) {
		130	| url: '/parachain/staking/delegator/timeMachine/rewards/stat',
		135	| export function timeMachineStakingHis(data) {
		137	| url: '/parachain/staking/delegator/timeMachine/staking/his',
		142	| export function timeMachineActionSelect(data) {
		144	| url: '/parachain/staking/delegator/timeMachine/staking/action/info',
		149	| export function timeMachineRewardSelect(data) {
		151	| url: '/parachain/staking/delegator/timeMachine/staking/reward/info',

	Unique lines in second:


Partially similar files found. First length 716, Second length 630,  The files are 81% identicalThe files differ in 71 lines:
	./resources/european/web/src/views/leaderBoard/index.vue
	./resources/asia/ui/src/views/leaderBoard/index.vue
	Unique lines in first:
		59	| {{ $utils.roundNumber(latestBlockNumber, 0) }}
		131	| class="icon hover-item"
		132	| @click="goToCollatorDetail(v.collator)"
		141	| class="mt hover-primary"
		142	| @click="goToCollatorDetail(v.collator)"
		152	| <span :class="getSafeStatus(v)">{{
		153	| getSafeStatus(v)
		154	| }}</span>
		155	| <span v-if="ifStaked(v)" class="delegate"
		156	| >Delegated</span
		211	| class="icon hover-item"
		212	| @click="goToCollatorDetail(v.collator)"
		221	| class="mt hover-primary"
		222	| @click="goToCollatorDetail(v.collator)"
		232	| <span :class="getSafeStatus(v)">{{
		233	| getSafeStatus(v)
		235	| <span v-if="ifStaked(v)" class="delegate"
		236	| >Delegated</span
		250	| <Table
		251	| :getSafeStatus="getSafeStatus"
		252	| :ifStaked="ifStaked"
		253	| @updateMyStakeList="getMyStakeList"
		266	| homeMyStake,
		271	| import Table from "./Table";
		280	| timer: null,
		281	| myStakeList: [],
		308	| this.initPage();
		309	| this.timer = setInterval(() => {
		310	| this.initPage();
		311	| }, 5 * 60 * 1000);
		313	| unmounted() {
		314	| clearInterval(this.timer);
		316	| watch: {
		317	| "$store.state.global.currentChain"() {
		318	| this.initPage();
		320	| "$store.state.global.metamaskWallet"() {
		321	| this.getMyStakeList();
		323	| "$store.state.global.polkadotWallet"() {
		324	| this.getMyStakeList();
		328	| initPage() {
		329	| this.getMyStakeList();
		334	| this.getAprRankList();
		338	| goToCollatorDetail(address) {
		339	| localStorage.setItem("routeParamsAddress", address);
		340	| this.$router.push({
		341	| name: "collatorDetail",
		344	| getAprRankList() {
		349	| orderBys: [{ sort: "apr", order: "DESC" }],
		356	| ifStaked(v) {
		357	| if (this.myStakeList.find((sv) => sv.collator == v.collator)) {
		362	| getMyStakeList() {
		363	| if (!this.$store.getters.currentChainWalletAddress) {
		364	| this.myStakeList = [];
		365	| return;
		367	| homeMyStake({
		369	| accountId: this.$store.getters.currentChainWalletAddress,
		371	| this.myStakeList = d;
		374	| getSafeStatus(v) {
		376	| v.totalStakeRank <
		380	| return "Safe";
		381	| } else if (v.totalStakeRank > this.safeStateConfig.max) {
		382	| return "Pending";
		383	| } else {
		384	| return "Risk";
		439	| .Risk {
		442	| .Safe {
		445	| .Pending {
		446	| color: #10a7e4;
		650	| .Risk {
		653	| .Safe {
		656	| .Pending {

	Unique lines in second:
		4	| <img
		7	| alt=""
		8	| />
		13	| <img
		14	| class="icon"
		16	| alt=""
		30	| class="icon"
		36	| <div class="value">
		58	| <div class="value">{{ $utils.roundNumber(latestBlockNumber) }}</div>
		137	| <div class="mt">
		146	| <span v-if="ifSafe(v)">Safe</span>
		147	| <span v-else class="risk">Risk</span>
		148	| <span class="delegate">Delegated</span>
		210	| <div class="mt">
		219	| <span v-if="ifSafe(v)">Safe</span>
		220	| <span v-else class="risk">Risk</span>
		221	| <span class="delegate">Delegated</span>
		234	| <Table :ifSafe="ifSafe" />
		249	| import Table from "./Table.vue";
		281	| };
		292	| orderBys: [{ sort: "aprRank", order: "DESC" }],
		301	| ifSafe(v) {
		303	| v.totalStakeRank >=
		356	| };
		362	| .risk {


Partially similar files found. First length 243, Second length 229,  The files are 81% identicalThe files differ in 21 lines:
	./resources/european/service/src/common/chain/chain-connector.ts
	./resources/asia/service/src/common/chain/chain-connector.ts
	Unique lines in first:
		11	| protected BREAK_CHANGE_SPEC_VERSION = 0;
		12	| protected NEED_CONVERT_ACCOUNT_ADDR = true;
		14	| formatAccountAddr(addr) {
		15	| if (this.NEED_CONVERT_ACCOUNT_ADDR) {
		16	| return ChainUtils.ss58transform_simple(addr, this.network);
		18	| return addr;
		44	| roundInfo["totalIssuance"] = this.formatWithDecimals(data.toString());
		180	| protected wsProvider: WsProvider;
		182	| protected systemVersion: any;
		183	| protected readonly logger: W3Logger;
		190	| // TODO to introduce the round-robin algorithms for multi-endpoints
		199	| this.wsProvider = new WsProvider(typeof wssEndpoint === 'string' ? wssEndpoint : wssEndpoint.url);
		208	| this.logger.debug('connected:' + this.network.id);
		211	| this.logger.debug('disconnected:' + this.network.id);
		214	| this.logger.error('error:' + this.network.id);
		225	| private isWaiting4Retrying = false;
		229	| if (!isReady) {
		230	| if (this.isWaiting4Retrying) {
		231	| throw new Error(`${this.network.id} is re-connecting and has not ready yet`)
		233	| this.isWaiting4Retrying = true;
		245	| this.isWaiting4Retrying = false;

	Unique lines in second:
		11	| private BREAK_CHANGE_SPEC_VERSION = 0;
		14	| await this.checkReady();
		24	| await this.checkReady();
		31	| await this.checkReady();
		36	| let formatSymbolDecimals = new BigNumber('1e' + this.network.decimals[0])
		37	| let value = new BigNumber(data.toString()).div(formatSymbolDecimals).toNumber();
		38	| roundInfo["totalIssuance"] = value;
		44	| await this.checkReady();
		61	| await this.checkReady();
		88	| //
		175	| private wsProvider: WsProvider;
		177	| private systemVersion: any;
		178	| private logger: W3Logger;
		193	| this.wsProvider = new WsProvider(wssEndpoint);
		202	| this.logger.debug('connected:' + val);
		205	| this.logger.debug('disconnected:' + val);
		208	| this.logger.error('error:' + val);


Partially similar files found. First length 76, Second length 65,  The files are 80% identicalThe files differ in 9 lines:
	./resources/european/web/src/components/IdentityIcon/index.vue
	./resources/asia/ui/src/components/IdentityIcon/index.vue
	Unique lines in first:
		8	| <div v-if="ifSupportPolkadot">
		29	| network: {
		43	| computed: {
		44	| ifSupportPolkadot() {
		45	| const network =
		46	| this.network || this.$store.state.global.currentChain.network;
		47	| return this.$utils.ifSupportPolkadot(network);
		73	| .eth-icon {
		74	| border-radius: 50%;

	Unique lines in second:
		8	| <div
		9	| v-if="$utils.ifSupportPolkadot($store.state.global.currentChain.network)"
		10	| >


Partially similar files found. First length 14, Second length 13,  The files are 80% identicalThe files differ in 2 lines:
	./resources/european/service/src/parachain/staking/task/staking-task.module.ts
	./resources/asia/service/src/parachain/staking/task/staking-task.module.ts
	Unique lines in first:
		7	| import { StatDelegatorService } from "./service/delegator-service";
		12	| providers: [CollatorService, StatDelegatorService, StatDataSyncTask],

	Unique lines in second:
		11	| providers: [CollatorService, StatDataSyncTask],


Partially similar files found. First length 166, Second length 122,  The files are 79% identicalThe files differ in 25 lines:
	./resources/european/service/src/common/entity/StakingPortalStat/StatCollator.entity.ts
	./resources/asia/service/src/common/entity/StakingModule/StatCollator.entity.ts
	Unique lines in first:
		14	| @PrimaryColumn({name: 'chain_id'})
		15	| chainId: string;
		78	| @Column({ name: "current_block", type: "int", default: 0 })
		79	| currentBlock: number;
		143	| name: "min_rps",
		145	| type: "float8",
		147	| minRps: number;
		151	| name: "max_rps",
		153	| type: "float8",
		155	| maxRps: number;
		159	| name: "avg_rps",
		161	| type: "float8",
		163	| avgRps: number;
		165	| @ApiProperty({
		166	| description: 'rps in last 10rounds, the JSON format is [  {roundIndex: 0, rps: 0} ] '
		169	| name: 'rps_his',
		170	| type: "text",
		171	| default: '{}',
		173	| rpsHis: string;
		175	| @ApiProperty(
		176	| {description: 'RPS Volatility Score'}
		177	| )
		179	| name: "rps_score",
		181	| type: "float8",
		183	| rpsScore: number;

	Unique lines in second:


Partially similar files found. First length 74, Second length 63,  The files are 78% identicalThe files differ in 9 lines:
	./resources/european/service/src/parachain/staking/core/db/db-manager.ts
	./resources/asia/service/src/parachain/staking/core/db/db-manager.ts
	Unique lines in first:
		15	| import { StatCollator } from "src/common/entity/StakingPortalStat/StatCollator.entity";
		16	| import { StatNetwork } from "src/common/entity/StakingPortalStat/StatNetwork.entity";
		17	| import { StatDelegator } from "src/common/entity/StakingPortalStat/StatDelegator.entity";
		22	| static PORTAL: DbManager4Portal;
		33	| readonly nrdhRepository: Repository<NominatorRewardDetailHistory>
		48	| dbConnect.getRepository(NominatorRewardDetailHistory)
		54	| static registerStakingPortal(dbConnect: Connection) {
		55	| this.PORTAL = new DbManager4Portal(
		74	| class DbManager4Portal {

	Unique lines in second:
		15	| import { StatCollator } from "src/common/entity/StakingModule/StatCollator.entity";
		16	| import { StatNetwork } from "src/common/entity/StakingModule/StatNetwork.entity";
		17	| import { StatDelegator } from "src/common/entity/StakingModule/StatDelegator.entity";
		31	| readonly nrdhRepository: Repository<NominatorRewardDetailHistory>,
		49	| dbConnect.getRepository(NominatorRewardDetailHistory),


Partially similar files found. First length 60, Second length 59,  The files are 77% identicalThe files differ in 7 lines:
	./resources/european/service/src/parachain/staking/portal/controller/home-controller.ts
	./resources/asia/service/src/parachain/staking/portal/controller/home-controller.ts
	Unique lines in first:
		1	| // CacheTTL,
		5	| // UseInterceptors,
		8	| // import { HttpCacheInterceptor } from "src/common/interceptor/HttpCacheInterceptor";
		20	| import { StatNetwork } from "src/common/entity/StakingPortalStat/StatNetwork.entity";
		22	| // @UseInterceptors(HttpCacheInterceptor)
		59	| const networkStat = await this.proxyService({ chainId }).listNetworkStat(chainId);
		60	| networkStat && res.push(networkStat);

	Unique lines in second:
		1	| CacheTTL,
		5	| UseInterceptors,
		8	| import { HttpCacheInterceptor } from "src/common/interceptor/HttpCacheInterceptor";
		19	| import { StatNetwork } from "src/common/entity/StakingModule/StatNetwork.entity";
		22	| @UseInterceptors(HttpCacheInterceptor)
		55	| res.push(await this.proxyService({ chainId }).listNetworkStat(chainId));


Partially similar files found. First length 58, Second length 51,  The files are 76% identicalThe files differ in 11 lines:
	./resources/european/web/package.json
	./resources/asia/ui/package.json
	Unique lines in first:
		1	| "name": "cumulon-protocol-web",
		7	| "lint": "vue-cli-service lint",
		8	| "start": "vue-cli-service serve"
		26	| "vue-class-component": "^8.0.0-0",
		31	| "vuex": "^4.0.0-0",
		32	| "webpack": "^5.75.0"
		39	| "@typescript-eslint/eslint-plugin": "^5.4.0",
		40	| "@typescript-eslint/parser": "^5.4.0",
		44	| "@vue/cli-plugin-typescript": "^5.0.8",
		48	| "@vue/eslint-config-typescript": "^9.1.0",
		54	| "typescript": "~4.5.5",

	Unique lines in second:
		1	| "name": "GoStaking",
		5	| "start": "vue-cli-service serve",
		8	| "lint": "vue-cli-service lint"
		30	| "vuex": "^4.0.0-0"


Partially similar files found. First length 18, Second length 17,  The files are 75% identicalThe files differ in 3 lines:
	./resources/european/web/.eslintrc.js
	./resources/asia/ui/.eslintrc.js
	Unique lines in first:
		7	| 'eslint:recommended',
		8	| '@vue/typescript'
		11	| parser: '@typescript-eslint/parser'

	Unique lines in second:
		7	| 'eslint:recommended'
		10	| parser: 'babel-eslint'


Partially similar files found. First length 699, Second length 558,  The files are 75% identicalThe files differ in 119 lines:
	./resources/european/web/src/views/delegatorDetail/index.vue
	./resources/asia/ui/src/views/delegatorDetail/index.vue
	Unique lines in first:
		19	| <span> Round {{ roundInfo.current }}-Delegator Leaderboard</span>
		21	| @click="$router.push({ name: 'leaderBoard' })"
		27	| <a-spin style="width: 100%; min-height: 300px" :loading="rank1Loading">
		29	| <div class="collector-item" v-for="(v, i) in aprRankList" :key="i">
		31	| <IdentityWrap :address="v.collator">
		34	| class="headicon hover-item"
		35	| @click="goToCollatorDetail(v.collator)"
		37	| :address="v.collator"
		38	| :iconSize="90"
		42	| <a-tooltip :content="v.collator" placement="top">
		43	| <span
		44	| @click="goToCollatorDetail(v.collator)"
		45	| class="hover-primary address"
		47	| {{
		48	| identity.display
		49	| ? identity.display
		50	| : $utils.shorterAddress(v.collator)
		51	| }}
		52	| </span>
		55	| @click="$utils.copy(v.collator)"
		72	| class="delegator-item"
		73	| v-for="(sv, si) in v.children"
		74	| :key="si"
		76	| <img class="rank" :src="rankImgList[si]" alt="" />
		78	| <IdentityWrap :address="sv.delegator">
		81	| class="headicon hover-item"
		82	| @click="searchItem(sv.delegator)"
		84	| :address="sv.delegator"
		85	| :iconSize="48"
		87	| <a-tooltip :content="sv.delegator" placement="top">
		88	| <span
		89	| class="address hover-primary"
		90	| @click="searchItem(sv.delegator)"
		91	| >{{
		94	| : $utils.shorterAddress(sv.delegator)
		95	| }}</span
		101	| @click="$utils.copy(sv.delegator)"
		107	| <span class="percent">{{ figureStakePercent(sv, v) }}%</span>
		112	| </a-spin>
		124	| <div class="text">Sorry, no data found by Cumulon.</div>
		171	| <span> {{ $utils.roundNumber(totalBonded) }} </span>
		228	| import BigNumber from "bignumber.js";
		231	| import RewardTable from "./RewardTable";
		232	| import ActionTable from "./ActionTable";
		233	| import {
		234	| getDelegatorRewardStatistic,
		235	| getSafeStateConfig,
		236	| homeMyStake,
		237	| delegatorStatistics,
		238	| getCurrentRoundInfo,
		239	| collatorStatistics,
		240	| delegatorInfo,
		241	| } from "@/api/staking";
		251	| aprRankList: [],
		252	| totalBonded: null,
		253	| roundInfo: {
		254	| current: null,
		255	| first: null,
		256	| length: null,
		257	| totalIssuance: null,
		262	| inputValue: "",
		270	| rank1Loading: false,
		273	| created() {
		274	| this.initPage();
		275	| const address = localStorage.getItem("routeParamsAddress");
		276	| if (address) {
		277	| localStorage.removeItem("routeParamsAddress");
		278	| this.searchItem(address);
		281	| watch: {
		282	| "$store.state.global.currentChain"() {
		283	| this.initPage();
		287	| initPage() {
		289	| this.inputValue = "";
		290	| this.getRoundInfo();
		291	| this.getAprRankList();
		293	| goToCollatorDetail(address) {
		294	| localStorage.setItem("routeParamsAddress", address);
		295	| this.$router.push({
		296	| name: "collatorDetail",
		299	| searchItem(address) {
		300	| this.inputValue = address;
		301	| this.handleSearch();
		303	| figureStakePercent(sv, v) {
		304	| const result = new BigNumber(sv.stake)
		305	| .div(new BigNumber(v.delegatorStake))
		306	| .multipliedBy(100)
		307	| .toFormat(2);
		308	| return result;
		310	| getRoundInfo() {
		311	| getCurrentRoundInfo({
		313	| }).then((d) => {
		314	| this.roundInfo = d;
		317	| getAprRankList() {
		318	| this.rank1Loading = true;
		319	| collatorStatistics({
		320	| pageSize: 3,
		321	| pageIndex: 1,
		322	| orderBys: [{ sort: "totalStake", order: "DESC" }],
		325	| let collectorList = d.list;
		326	| const promiseArr = [];
		327	| for (const v of d.list) {
		328	| promiseArr.push(
		329	| delegatorStatistics({
		330	| pageSize: 3,
		331	| pageIndex: 1,
		332	| orderBys: [{ sort: "stake", order: "DESC" }],
		334	| collator: v.collator,
		335	| })
		336	| );
		338	| Promise.all(promiseArr).then((data) => {
		339	| this.rank1Loading = false;
		340	| collectorList.forEach((v, i) => {
		341	| v.children = data[i].list;
		343	| this.aprRankList = collectorList;
		370	| this.loading = true;
		375	| this.loading = false;
		378	| delegatorInfo({
		380	| delegator: this.inputValue,
		382	| this.totalBonded = d.totalBond;

	Unique lines in second:
		10	| />
		19	| <span> Round xxx-Delegator Leaderboard</span>
		20	| <img
		23	| alt=""
		24	| />
		27	| <div class="collector-item" v-for="(v, i) in 3" :key="i">
		29	| <img
		30	| class="headicon"
		31	| src="@/assets/images/moonbeam/moonbeam.png"
		32	| alt=""
		36	| <span class="address">0x1245…1470fs</span>
		51	| <div class="delegator-item" v-for="(v, i) in 3" :key="i">
		52	| <img class="rank" :src="rankImgList[i]" alt="" />
		55	| class="headicon"
		56	| src="@/assets/images/moonbeam/moonbeam.png"
		59	| <span class="address">0x1245…1470fs</span>
		66	| <span class="percent">79%</span>
		82	| <div class="text">Sorry, no data found by Web3go.</div>
		129	| <span> 39,024,467 </span>
		130	| <span class="unit">GLMR</span>
		186	| import RewardTable from "./RewardTable.vue";
		187	| import ActionTable from "./ActionTable.vue";
		188	| import { getDelegatorRewardStatistic } from "@/api/staking";
		201	| inputValue: "4Aoj2JtzjYRizRA2fMxg437gWbUmf5o951ZD11bY7YJSPeAY",
		211	| created() {},
		242	| // this.getBonded();
		309	| img {


Partially similar files found. First length 25, Second length 24,  The files are 74% identicalThe files differ in 4 lines:
	./resources/european/service/src/parachain/staking/staking-analysis.module.ts
	./resources/asia/service/src/parachain/staking/staking-analysis.module.ts
	Unique lines in first:
		9	| import { ChainConnectModule } from "./core/chain/chain-connect.module";
		15	| // max: 500
		18	| ChainConnectModule.forRoot(),
		21	| StakingTask2Module,

	Unique lines in second:
		14	| ttl: 15,
		15	| isGlobal: true,
		20	| StakingTask2Module


Partially similar files found. First length 587, Second length 492,  The files are 73% identicalThe files differ in 84 lines:
	./resources/european/web/src/views/Layout/ConnectWalletModal/index.vue
	./resources/asia/ui/src/views/Layout/ConnectWalletModal/index.vue
	Unique lines in first:
		47	| >Connect to stake on below chains</span
		50	| <div class="icon-list">
		52	| v-for="(v, i) in metamaskChainList"
		54	| :content="v.name"
		56	| <div class="il-circle">
		57	| <img :src="v.icon" alt="" />
		95	| $store.getters.polkadotWalletTransformAddress
		101	| v-if="$store.getters.polkadotWalletTransformAddress"
		110	| v-if="$store.getters.polkadotWalletTransformAddress"
		111	| :content="$store.getters.polkadotWalletTransformAddress"
		115	| $store.getters.polkadotWalletTransformAddress
		119	| <span v-else>Connect to stake on below chains</span>
		121	| <div class="icon-list">
		123	| v-for="(v, i) in polkadotChainList"
		125	| :content="v.name"
		127	| <div class="il-circle">
		134	| v-if="!$store.getters.polkadotWalletTransformAddress"
		186	| import { ethers, utils } from "ethers";
		205	| this.$store.getters.polkadotWalletTransformAddress ||
		210	| this.$eventBus.on(
		211	| "updateSupportWalletFreeBalance",
		212	| this.updateSupportWalletFreeBalance
		225	| this.$utils.ifSupportPolkadot(
		226	| this.$store.state.global.currentChain.network
		227	| ) &&
		228	| !this.$store.getters.polkadotWalletTransformAddress
		233	| !this.$utils.ifSupportPolkadot(
		234	| this.$store.state.global.currentChain.network
		235	| ) &&
		241	| metamaskChainList() {
		242	| return this.$store.state.global.supportChainList.filter(
		243	| (v) => !this.$utils.ifSupportPolkadot(v.network)
		246	| polkadotChainList() {
		247	| return this.$store.state.global.supportChainList.filter((v) =>
		248	| this.$utils.ifSupportPolkadot(v.network)
		254	| return v.address == this.$store.getters.polkadotWalletTransformAddress;
		261	| const address = this.$store.getters.polkadotWalletTransformAddress;
		270	| let free = 0;
		272	| const _free = accountInfo.data.free.toString(10);
		273	| const miscFrozen = accountInfo.data.miscFrozen.toString(10);
		274	| free = BigNumber(_free - miscFrozen).dividedBy(
		275	| new BigNumber("1e" + parachainObj.decimals[0])
		278	| let copySupportChainList = JSON.parse(
		281	| const findIndex = copySupportChainList.findIndex(
		282	| (sv) => sv.network == parachainObj.network
		284	| copySupportChainList[findIndex].free = free;
		285	| this.$store.commit("changeSupportChainList", copySupportChainList);
		292	| // const provider = new ethers.providers.Web3Provider(window.ethereum);
		293	| let provider;
		294	| if (parachainObj.wssEndpoints[0].includes("wss://")) {
		295	| provider = new ethers.providers.WebSocketProvider(
		296	| parachainObj.wssEndpoints[0]
		299	| provider = new ethers.providers.JsonRpcProvider(
		300	| parachainObj.wssEndpoints[0]
		304	| const _free = ethers.utils.formatUnits(b, parachainObj.decimals[0]);
		305	| const free = new BigNumber(_free);
		306	| // const free = b
		307	| //   .dividedBy(new BigNumber("1e" + parachainObj.decimals[0]))
		308	| //   .toFixed(2);
		309	| let copySupportChainList = JSON.parse(
		312	| const findIndex = copySupportChainList.findIndex(
		313	| (sv) => sv.network == parachainObj.network
		315	| copySupportChainList[findIndex].free = free;
		316	| this.$store.commit("changeSupportChainList", copySupportChainList);
		318	| updateSupportWalletFreeBalance() {
		322	| newsupportChainList.forEach((v) => {
		323	| v.free = undefined;
		329	| this.getMetamaskBalance(v);
		331	| this.getPolkadotBalance(v);
		343	| address: utils.getAddress(accs[0]),
		456	| padding: 10px;
		460	| margin-bottom: 30px;
		461	| width: 40px;
		496	| .icon-list {
		497	| margin-top: 6px;
		500	| .il-circle {
		501	| width: 20px;
		502	| height: 20px;
		504	| border: 1px solid #d9d9d9;
		505	| background: white;
		509	| & + .il-circle {
		510	| margin-left: -4px;
		513	| max-width: 16px;
		514	| max-height: 16px;

	Unique lines in second:
		21	| <img
		24	| alt=""
		25	| />
		47	| >Connect to check your stake on Moonbeam, Moonriver</span
		74	| <img
		77	| alt=""
		78	| />
		84	| $store.state.global.polkadotWallet.address
		90	| v-if="$store.state.global.polkadotWallet.address"
		99	| v-if="$store.state.global.polkadotWallet.address"
		100	| :content="$store.state.global.polkadotWallet.address"
		104	| $store.state.global.polkadotWallet.address
		108	| <span v-else>Connect to check your stake on Litentry</span>
		112	| v-if="!$store.state.global.polkadotWallet.address"
		164	| import { ethers } from "ethers";
		179	| };
		183	| this.$store.state.global.polkadotWallet.address ||
		199	| this.$utils.ifSupportPolkadot(this.$store.state.global.currentChain.network) &&
		200	| !this.$store.state.global.polkadotWallet.address
		205	| !this.$utils.ifSupportPolkadot(this.$store.state.global.currentChain.network) &&
		214	| return v.address == this.$store.state.global.polkadotWallet.address;
		221	| const address = this.$store.state.global.polkadotWallet.address;
		223	| return 0;
		231	| let free = accountInfo.data.free.toString(10);
		232	| return BigNumber(free)
		233	| .dividedBy(new BigNumber("1e" + parachainObj.decimals[0]))
		234	| .toFixed(2);
		245	| const balance = ethers.utils.formatEther(b);
		246	| return BigNumber(balance)
		247	| .dividedBy(new BigNumber("1e" + parachainObj.decimals[0]))
		248	| .toFixed(2);
		250	| async updateSupportWalletFreeBalance() {
		256	| v.free = await this.getMetamaskBalance(v);
		258	| v.free = await this.getPolkadotBalance(v);
		271	| address: accs[0],
		344	| justify-content: center;
		381	| border-radius: 90px;
		383	| padding: 7px;
		387	| width: 46px;
		388	| height: 46px;
		390	| border-radius: 39px;
		393	| justify-content: center;


Partially similar files found. First length 781, Second length 596,  The files are 73% identicalThe files differ in 131 lines:
	./resources/european/web/src/views/collatorDetail/index.vue
	./resources/asia/ui/src/views/collatorDetail/index.vue
	Unique lines in first:
		18	| <span> Round {{ roundInfo.current }}-Collator Leaderboard</span>
		20	| @click="$router.push({ name: 'leaderBoard' })"
		26	| <a-spin style="width: 100%; min-height: 300px" :loading="rank1Loading">
		28	| <div class="item" v-for="(v, i) in aprRankList" :key="i">
		31	| <img class="num" :src="rankImgList[i]" alt="" />
		33	| <IdentityWrap :address="v.collator">
		34	| <template #default="{ identity }">
		35	| <IdentityIcon
		36	| class="icon hover-item"
		37	| :identity="identity"
		38	| :address="v.collator"
		39	| :iconSize="48"
		40	| @click="searchItem(v.collator)"
		41	| ></IdentityIcon>
		42	| <a-tooltip :content="v.collator" placement="top">
		43	| <div
		44	| class="address hover-primary"
		45	| @click="searchItem(v.collator)"
		46	| >
		47	| {{
		48	| identity.display
		49	| ? identity.display
		50	| : $utils.shorterAddress(v.collator)
		51	| }}
		53	| </a-tooltip>
		55	| </IdentityWrap>
		57	| @click="$utils.copy(v.collator)"
		64	| <span :class="getSafeStatus(v)">{{
		65	| getSafeStatus(v)
		67	| <span v-if="ifStaked(v)" class="delegated">Delegated</span>
		72	| <span class="percent">{{ $utils.roundNumber(v.apr) }}%</span>
		75	| @click="searchItem(v.collator)"
		83	| </a-spin>
		90	| <div class="text">Sorry, no data found by Cumulon.</div>
		102	| <span class="text">{{ collectorRank }}</span>
		198	| import DelegatorTable from "./DelegatorTable";
		199	| import RewardTable from "./RewardTable";
		200	| import ActionTable from "./ActionTable";
		204	| getCurrentRoundInfo,
		205	| collatorStatistics,
		206	| getSafeStateConfig,
		207	| homeMyStake,
		210	| import IdentityWrap from "@/components/IdentityWrap";
		211	| import IdentityIcon from "@/components/IdentityIcon";
		217	| IdentityWrap,
		218	| IdentityIcon,
		222	| collectorRank: null,
		223	| myStakeList: [],
		224	| // {"max":64,"collatorSafeStateThreshold":0.9}
		225	| safeStateConfig: {},
		226	| roundInfo: {
		227	| current: null,
		228	| first: null,
		229	| length: null,
		230	| totalIssuance: null,
		233	| inputValue: "",
		250	| rank1Loading: false,
		251	| aprRankList: [],
		254	| created() {
		255	| this.initPage();
		256	| const address = localStorage.getItem("routeParamsAddress");
		257	| if (address) {
		258	| localStorage.removeItem("routeParamsAddress");
		259	| this.searchItem(address);
		262	| watch: {
		263	| "$store.state.global.currentChain"() {
		264	| this.initPage();
		266	| "$store.state.global.metamaskWallet"() {
		267	| this.getMyStakeList();
		269	| "$store.state.global.polkadotWallet"() {
		270	| this.getMyStakeList();
		274	| initPage() {
		276	| this.inputValue = "";
		277	| this.getRoundInfo();
		278	| this.getAprRankList();
		279	| this.getMyStakeList();
		280	| this.getSafeStateConfig();
		282	| getCollatorRank() {
		283	| collatorStatistics({
		284	| pageSize: 10,
		285	| pageIndex: 1,
		286	| orderBys: [],
		288	| collator: this.inputValue,
		290	| if (d.list.length) {
		291	| this.collectorRank = d.list[0].totalStakeRank;
		295	| searchItem(address) {
		296	| this.inputValue = address;
		297	| this.handleSearch();
		299	| getSafeStateConfig() {
		300	| getSafeStateConfig({
		303	| this.safeStateConfig = d;
		306	| getMyStakeList() {
		307	| if (!this.$store.getters.currentChainWalletAddress) {
		308	| this.myStakeList = [];
		309	| return;
		311	| homeMyStake({
		313	| accountId: this.$store.getters.currentChainWalletAddress,
		315	| this.myStakeList = d;
		318	| ifStaked(v) {
		319	| if (this.myStakeList.find((sv) => sv.collator == v.collator)) {
		320	| return true;
		324	| getSafeStatus(v) {
		325	| if (
		326	| v.totalStakeRank <
		327	| this.safeStateConfig.max *
		328	| this.safeStateConfig.collatorSafeStateThreshold
		329	| ) {
		330	| return "Safe";
		331	| } else if (v.totalStakeRank > this.safeStateConfig.max) {
		332	| return "Pending";
		333	| } else {
		334	| return "Risk";
		337	| getAprRankList() {
		338	| this.rank1Loading = true;
		339	| collatorStatistics({
		340	| pageSize: 5,
		342	| orderBys: [{ sort: "totalStake", order: "DESC" }],
		345	| this.rank1Loading = false;
		346	| this.aprRankList = d.list;
		349	| getRoundInfo() {
		350	| getCurrentRoundInfo({
		353	| this.roundInfo = d;
		420	| this.getCollatorRank();
		587	| .Safe {
		601	| .Risk {
		613	| color: #e31a1a;
		614	| background: rgba(227, 26, 26, 0.1);
		616	| .Pending {
		628	| color: #10a7e4;
		629	| background: rgba(16, 167, 228, 0.1);
		680	| // margin-left: 63px;

	Unique lines in second:
		10	| />
		18	| <span> Round xxx-Collator Leaderboard</span>
		19	| <img
		22	| alt=""
		23	| />
		26	| <div class="item" v-for="(v, i) in rankImgList" :key="i">
		29	| <img class="num" :src="v" alt="" />
		31	| <img class="icon" src="@/assets/images/home/Group7(1).png" alt="" />
		32	| <span class="address">0x1245…1470fs</span>
		33	| <img
		36	| alt=""
		40	| <div class="safe">Safe</div>
		41	| <div class="delegated">Delegated</div>
		46	| <span class="percent">12.78%</span>
		62	| <div class="text">Sorry, no data found by Web3go.</div>
		74	| <span class="text">1800</span>
		91	| }}</span>
		170	| import DelegatorTable from "./DelegatorTable.vue";
		171	| import RewardTable from "./RewardTable.vue";
		172	| import ActionTable from "./ActionTable.vue";
		188	| inputValue: "49d8PJE2QUMqoQugP5m2xL76hp4usgxE4KnGBvFnDnQNLk8a",
		205	| };
		207	| created() {},
		229	| .toFixed(2);
		266	| };
		436	| .safe {
		496	| margin-left: 63px;


Partially similar files found. First length 265, Second length 220,  The files are 73% identicalThe files differ in 41 lines:
	./resources/european/web/src/views/myStake/StakingCollators/index.vue
	./resources/asia/ui/src/views/myStake/StakingCollators/index.vue
	Unique lines in first:
		9	| <div class="num">{{ roundInfo.current }}</div>
		16	| <div class="num">{{ $utils.roundNumber(latestBlockNumber, 0) }}</div>
		23	| <div class="num">
		24	| <span class="color">{{ latestBlockNumber - roundInfo.first }}</span
		25	| >/{{ roundInfo.length }}
		30	| <Table
		31	| :refreshTopPage="refreshTopPage"
		32	| :roundInfo="roundInfo"
		33	| :latestBlockNumber="latestBlockNumber"
		34	| />
		39	| import { getCurrentRoundInfo, getLatestBlockNumber } from "@/api/staking";
		40	| import Table from "./Table";
		45	| props: ["refreshTopPage"],
		47	| return {
		48	| latestBlockNumber: null,
		49	| roundInfo: {
		50	| current: null,
		51	| first: null,
		52	| length: null,
		53	| totalIssuance: null,
		57	| created() {
		58	| this.initPage();
		60	| watch: {
		61	| "$store.state.global.currentChain"() {
		62	| this.initPage();
		65	| methods: {
		66	| initPage() {
		67	| this.getLatestBlockNumber();
		68	| this.getRoundInfo();
		70	| getLatestBlockNumber() {
		71	| getLatestBlockNumber({
		72	| chainId: this.$store.state.global.currentChain.id,
		73	| }).then((d) => {
		74	| this.latestBlockNumber = d;
		75	| });
		77	| getRoundInfo() {
		78	| getCurrentRoundInfo({
		79	| chainId: this.$store.state.global.currentChain.id,
		80	| }).then((d) => {
		81	| this.roundInfo = d;
		82	| });

	Unique lines in second:
		9	| <div class="num">235</div>
		16	| <div class="num">235</div>
		23	| <div class="num"><span class="color">300</span>/1800</div>
		27	| <Table />
		32	| import Table from "./Table.vue";
		38	| return {};


Partially similar files found. First length 13, Second length 13,  The files are 69% identicalThe files differ in 2 lines:
	./resources/european/service/ecosystem.config.js
	./resources/asia/service/ecosystem.config.js
	Unique lines in first:
		2	| name: "20055-cumulon-protocol-portal-service",
		3	| script: "main.js",

	Unique lines in second:
		2	| name: "go-staking-portal-service",
		3	| script: "dist/main.js",


Partially similar files found. First length 35, Second length 34,  The files are 69% identicalThe files differ in 8 lines:
	./resources/european/service/src/common/chain/chain-network.ts
	./resources/asia/service/src/common/chain/chain-network.ts
	Unique lines in first:
		15	| // external= false(default) is indicating that it can be exposed to the frontend
		16	| wssEndpoints: Array<{external:Boolean, url: string}|string>;

	Unique lines in second:
		6	| info: {
		15	| wssEndpoints: Array<string>;
		18	| defaultValues: {
		24	| type: "postgres",
		26	| port: 5432,
		27	| username: "postgres",
		29	| synchronize: false,
		30	| logging: false,


Partially similar files found. First length 11, Second length 10,  The files are 67% identicalThe files differ in 2 lines:
	./resources/european/service/src/viewModel/staking/portal/StatDelegatorPageRequest.ts
	./resources/asia/service/src/viewModel/staking/portal/StatDelegatorPageRequest.ts
	Unique lines in first:
		8	| description: 'if specified it to the true, data will return the total for pagination',
		9	| default: false

	Unique lines in second:
		8	| description: 'if specified it to the true, data will return the total for pagination'


Partially similar files found. First length 30, Second length 22,  The files are 67% identicalThe files differ in 8 lines:
	./resources/european/service/src/parachain/staking/core/register/staking-register-controller.ts
	./resources/asia/service/src/parachain/staking/core/register/staking-register-controller.ts
	Unique lines in first:
		14	| private supports;
		24	| if (!this.supports) {
		25	| this.supports = parachainNetworks.map((it) => {
		26	| const info = JSON.parse(JSON.stringify(it.info)); // deep copy
		27	| info.wssEndpoints = info.wssEndpoints.filter( it => !it.external);
		28	| return info;
		29	| });
		31	| return this.supports;

	Unique lines in second:
		20	| return parachainNetworks.map((it) => it.info);


Partially similar files found. First length 603, Second length 362,  The files are 66% identicalThe files differ in 163 lines:
	./resources/european/web/src/components/DelegateDrawer/index.vue
	./resources/asia/ui/src/components/DelegateDrawer/index.vue
	Unique lines in first:
		20	| <div v-if="minBond" class="drawer-main">
		23	| <IdentityWrap :address="address">
		24	| <template #default="{ identity }">
		25	| <IdentityIcon
		26	| :iconSize="56"
		27	| :identity="identity"
		28	| :address="address"
		29	| ></IdentityIcon>
		32	| <a-tooltip :content="address" placement="top">
		33	| <span class="value">{{
		34	| identity.display
		35	| ? identity.display
		36	| : $utils.shorterAddress(address)
		38	| </a-tooltip>
		41	| </IdentityWrap>
		46	| <span> {{ $utils.roundNumber(alreadyStaked) }} </span>
		47	| <span class="unit"
		48	| >&nbsp;{{ $store.state.global.currentChain.symbols[0] }}</span
		66	| <div v-if="!isDelegateMore" class="min-bond-tip">
		67	| The minimum delegation amount is
		68	| <span class="blue">{{ $utils.roundNumber(minBond) }}</span>
		69	| {{ $store.state.global.currentChain.symbols[0] }}
		71	| <div class="free-tip">
		72	| The available token amount is
		73	| <span class="blue">{{ $utils.roundNumber(chainFree) }}</span>
		74	| {{ $store.state.global.currentChain.symbols[0] }}
		91	| import { homeMyStake, collatorStatistics } from "@/api/staking";
		95	| import IdentityWrap from "@/components/IdentityWrap";
		96	| import IdentityIcon from "@/components/IdentityIcon";
		97	| import moonbeamContractAbi from "@/utils/moonbeamContractAbi";
		98	| import { ethers } from "ethers";
		101	| components: {
		102	| IdentityWrap,
		103	| IdentityIcon,
		107	| alreadyStaked: 0,
		108	| minBond: "",
		115	| myStakeList: [],
		127	| computed: {
		128	| chainFree() {
		129	| const arr = this.$store.state.global.supportChainList;
		130	| const find = arr.find(
		131	| (v) => v.network == this.$store.state.global.currentChain.network
		133	| if (find) {
		134	| return find.free;
		136	| return "";
		140	| async figureRevokeStatus(address) {
		141	| let res = [];
		142	| try {
		143	| res = (
		144	| await this.apiPromise.query.parachainStaking.delegationScheduledRequests(
		145	| address
		147	| ).toHuman();
		148	| } catch (e) {
		149	| console.warn("encountered errors while fetching the revoking status");
		151	| const matched = res.filter(
		152	| (it) =>
		153	| it.whenExecutable &&
		154	| it.delegator === this.$store.getters.currentChainWalletAddress
		156	| if (!matched.length) {
		157	| return "TO_REVOKE";
		159	| return "other";
		170	| getMyStakeList() {
		171	| if (!this.$store.getters.currentChainWalletAddress) {
		172	| this.myStakeList = [];
		175	| homeMyStake({
		176	| chainId: this.$store.state.global.currentChain.id,
		177	| accountId: this.$store.getters.currentChainWalletAddress,
		178	| }).then((d) => {
		179	| this.myStakeList = d;
		180	| const find = d.find((v) => v.collator == this.address);
		181	| if (find) {
		182	| this.isDelegateMore = true;
		184	| this.alreadyStaked = find.myStake;
		186	| this.isDelegateMore = false;
		188	| this.alreadyStaked = 0;
		192	| async init(address) {
		193	| const status = await this.figureRevokeStatus(address);
		194	| if (status !== "TO_REVOKE") {
		195	| this.$message.error("You are unstaking this collator, you need to go to my stake page to cancel unstake before delegate.");
		199	| this.minBond = null;
		200	| this.address = address;
		201	| collatorStatistics({
		202	| pageSize: 10,
		203	| pageIndex: 1,
		204	| orderBys: [],
		205	| chainId: this.$store.state.global.currentChain.id,
		206	| collator: address,
		207	| }).then((d) => {
		208	| if (d.list.length) {
		209	| const minbond = d.list[0].minBond;
		210	| if (parseInt(minbond) == minbond) {
		211	| this.minBond = minbond;
		213	| this.minBond = Math.ceil(minbond * 100) / 100;
		215	| this.getMyStakeList();
		219	| async delegateByMetamask() {
		220	| // const provider = new ethers.providers.WebSocketProvider(
		221	| //   this.$store.state.global.currentChain.wssEndpoints[0]
		222	| // );
		223	| // const provider = new ethers.providers.JsonRpcProvider(
		224	| //   "https://rpc.api.moonbeam.network"
		225	| // );
		226	| // const signer = provider.getSigner();
		227	| if (this.$store.state.global.currentChain.network == "moonbeam") {
		228	| await ethereum.request({
		229	| method: "wallet_addEthereumChain",
		230	| params: [
		231	| {
		232	| chainId: "0x504",
		233	| chainName: "Moonbeam",
		234	| rpcUrls: ["https://rpc.api.moonbeam.network"],
		235	| nativeCurrency: {
		236	| name: "GLMR",
		237	| symbol: "GLMR",
		238	| decimals: 18,
		240	| blockExplorerUrls: ["https://moonbeam.moonscan.io"],
		242	| ],
		244	| } else if (this.$store.state.global.currentChain.network == "moonriver") {
		245	| await ethereum.request({
		246	| method: "wallet_addEthereumChain",
		247	| params: [
		249	| chainId: "0x505",
		250	| chainName: "Moonriver",
		251	| rpcUrls: ["https://rpc.api.moonriver.moonbeam.network"],
		252	| nativeCurrency: {
		253	| name: "MOVR",
		254	| symbol: "MOVR",
		255	| decimals: 18,
		257	| blockExplorerUrls: ["https://moonriver.moonscan.io"],
		259	| ],
		262	| const provider = new ethers.providers.Web3Provider(window.ethereum);
		263	| await provider.send("eth_requestAccounts", []);
		264	| const signer = provider.getSigner();
		265	| console.log("Account:", await signer.getAddress());
		266	| const contract = new ethers.Contract(
		267	| "0x0000000000000000000000000000000000000800",
		268	| moonbeamContractAbi,
		269	| signer
		273	| let delegateTx;
		274	| try {
		275	| delegateTx = await contract.delegator_bond_more(
		279	| } catch (error) {
		282	| delegateTx.wait().then((receipt) => {
		283	| if (receipt && receipt.status == 1) {
		287	| this.$eventBus.emit("updateSupportWalletFreeBalance");
		296	| const delegationCount = await contract.candidate_delegation_count(
		299	| const myDelegationCount = await contract.candidate_delegation_count(
		302	| let delegateTx;
		304	| delegateTx = await contract.delegate(
		313	| delegateTx.wait().then((receipt) => {
		314	| if (receipt && receipt.status == 1) {
		318	| this.$eventBus.emit("updateSupportWalletFreeBalance");
		338	| if (this.num > this.chainFree) {
		339	| this.$message.error("You don't have enough tokens");
		346	| if (
		347	| !this.$utils.ifSupportPolkadot(
		348	| this.$store.state.global.currentChain.network
		350	| ) {
		351	| this.delegateByMetamask();
		370	| this.$eventBus.emit("updateSupportWalletFreeBalance");
		425	| this.$eventBus.emit("updateSupportWalletFreeBalance");
		473	| .identity-icon {
		588	| .free-tip {
		589	| margin-top: 20px;

	Unique lines in second:
		20	| <div class="drawer-main">
		23	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		26	| <div class="value">Jetblue-125</div>
		32	| <span> 1790 </span>
		33	| <span class="unit">{{
		34	| $store.state.global.currentChain.symbols[0]
		52	| <div class="min-bond-tip">
		53	| The minimum delegation amount is <span class="blue">xx</span> GLMR
		77	| minBond: 50,
		106	| init(row, isMore) {
		108	| this.address = row.address;
		109	| if (isMore) {
		114	| this.isDelegateMore = isMore;
		228	| img {


Partially similar files found. First length 62, Second length 64,  The files are 65% identicalThe files differ in 12 lines:
	./resources/european/service/src/parachain/staking/portal/service/stat-collator-service.ts
	./resources/asia/service/src/parachain/staking/portal/service/stat-collator-service.ts
	Unique lines in first:
		15	| const chainPresetValues = ChainConnectManager.get(request).defaultValues;
		18	| collatorSafeStateThreshold: chainPresetValues.collatorSafeStateThreshold,
		26	| if (it.sort && it.sort !== "myStake") {
		31	| const where = {
		32	| chainId: request.chainId
		33	| } as any;
		45	| const rawData = await DbManager.PORTAL.statDelegatorRepository.query(
		46	| `SELECT DISTINCT collator  FROM stat_delegator  WHERE chain_id='${request.chainId}'	AND delegator = '${request.delegator}' LIMIT ${take} OFFSET ${skip}`
		47	| // `SELECT DISTINCT collator  FROM stat_delegator  WHERE	delegator LIKE'%${request.delegator}%' LIMIT ${take} OFFSET ${skip}`
		57	| return await DbManager.PORTAL.statCollatorRepository[method]({

	Unique lines in second:
		1	| import { skip } from "rxjs/operators";
		2	| import { StatCollator } from "src/common/entity/StakingModule/StatCollator.entity";
		19	| collatorSafeStateThreshold:
		20	| ChainConnectManager.get(request).defaultValues
		21	| .collatorSafeStateThreshold,
		29	| if (it.sort) {
		34	| const where = {} as any;
		46	| const rawData = await DbManager.get(
		47	| request
		48	| ).statDelegatorRepository.query(
		49	| `SELECT DISTINCT collator  FROM stat_delegator  WHERE	delegator LIKE'%${request.delegator}%' LIMIT ${take} OFFSET ${skip}`
		59	| return await DbManager.get(request).statCollatorRepository[method]({


Partially similar files found. First length 1462, Second length 1051,  The files are 64% identicalThe files differ in 323 lines:
	./resources/european/web/src/views/leaderBoard/Table.vue
	./resources/asia/ui/src/views/leaderBoard/Table.vue
	Unique lines in first:
		1	| <a-spin style="width: 100%" :loading="loading">
		3	| <el-table
		4	| :data="tableData"
		5	| ref="table"
		6	| @expand-change="handleExpand"
		7	| @sort-change="tableSortChange"
		11	| <!-- <p>State: {{ scope.row.state }}</p> -->
		18	| <v-chart class="chart" :option="getRowChartOption(scope.row)" />
		23	| <span class="text">Top3 Delegators (staked amount%)</span>
		25	| <div
		26	| v-if="top3DelegatorDataMap[scope.row.collator]"
		27	| class="rank"
		29	| <div
		30	| v-for="(v, i) in top3DelegatorDataMap[scope.row.collator]"
		31	| :key="i"
		32	| class="item"
		51	| <IdentityWrap :address="v.delegator">
		56	| @click="goToDelegatorDetail(v.delegator)"
		58	| :address="v.delegator"
		59	| :iconSize="40"
		62	| <a-tooltip :content="v.delegator" placement="top">
		63	| <div
		64	| class="address hover-primary"
		65	| @click="goToDelegatorDetail(v.delegator)"
		70	| : $utils.shorterAddress(v.delegator)
		76	| <div class="percent">
		77	| {{ figureStakePercent(v, scope.row) }}%
		88	| <span class="text">Collator </span>
		89	| <a-tooltip content="Rank by total stake">
		100	| <span class="text" :class="'color' + scope.row.totalStakeRank">{{
		101	| getIndex(scope.row.totalStakeRank)
		106	| class="icon hover-item"
		107	| @click="goToCollatorDetail(scope.row.collator)"
		114	| <div
		115	| class="top hover-primary"
		116	| @click="goToCollatorDetail(scope.row.collator)"
		126	| <span :class="getSafeStatus(scope.row)">{{
		127	| getSafeStatus(scope.row)
		129	| <span v-if="ifStaked(scope.row)" class="delegated"
		130	| >Delegated</span
		143	| sortable="custom"
		150	| <span class="text"
		151	| >{{ $utils.roundNumber(scope.row[v.prop]) }}%</span
		161	| sortable="custom"
		167	| <a-tooltip>
		169	| <div v-if="v.name == 'Avg Blocks'">
		170	| number of blocks which has been rewarded in past 10
		171	| rounds( round {{ startRoundIndex }} -
		172	| {{ endRoundIndex }} ).
		174	| <div v-else-if="v.name == 'Current Blocks'">
		175	| Blocks produced in the current round
		176	| {{ endRoundIndex }}.
		178	| <div v-else v-html="v.tip"></div>
		189	| <span class="text">{{
		190	| scope.row[v.prop] === null || scope.row[v.prop] === undefined
		191	| ? "-"
		192	| : $utils.roundNumber(scope.row[v.prop])
		198	| sortable="custom"
		205	| <span class="text">{{
		206	| scope.row[v.prop] === null
		207	| ? ""
		208	| : $utils.roundNumber(scope.row[v.prop])
		280	| @change="getTableData"
		307	| <a-spin
		308	| style="width: 100%; min-height: 300px"
		309	| :loading="!currentRow.collator"
		311	| <div v-if="currentRow.collator" class="drawer-main">
		314	| <IdentityWrap :address="currentRow.collator">
		318	| :address="currentRow.collator"
		319	| :iconSize="56"
		323	| <a-tooltip
		324	| :content="currentRow.collator"
		325	| placement="top"
		327	| <div class="value">
		331	| : $utils.shorterAddress(currentRow.collator)
		341	| <div class="value">{{ currentRow.totalStakeRank }}</div>
		344	| <span class="tag" :class="getSafeStatus(currentRow)">{{
		345	| getSafeStatus(currentRow)
		347	| <div v-if="ifStaked(currentRow)" class="tag yellow">
		348	| Delegated
		375	| <div
		376	| class="blue-line"
		378	| width: getSumulatePercent(currentRow),
		379	| }"
		380	| ></div>
		381	| <div
		382	| class="g-split"
		383	| :style="{ left: getSumulatePercent(currentRow) }"
		384	| ></div>
		385	| <div
		386	| class="popover"
		387	| :style="{ left: getSumulatePercent(currentRow) }"
		391	| <div class="nowrap">
		392	| Rank {{ getSimulateRank(currentRow) }}
		394	| <div>Stake {{ inputValue }}</div>
		400	| <div class="rank">Rank {{ maxNominator }}</div>
		401	| <div class="stake">
		402	| Stake
		404	| getSingleNominatorStakeByRank(currentRow, maxNominator)
		410	| Rank {{ parseInt(maxNominator * 0.9) }}
		412	| <div class="stake">
		413	| Stake
		415	| getSingleNominatorStakeByRank(
		416	| currentRow,
		417	| parseInt(maxNominator * 0.9)
		424	| Rank {{ parseInt(maxNominator * 0.5) }}
		426	| <div class="stake">
		427	| Stake
		429	| getSingleNominatorStakeByRank(
		430	| currentRow,
		431	| parseInt(maxNominator * 0.5)
		438	| <div class="stake">
		439	| Stake
		440	| {{ getSingleNominatorStakeByRank(currentRow, 1) }}
		452	| <span class="num">{{
		453	| getBoundaryReward1(currentRow)
		455	| <span class="unit">{{
		465	| getBoundaryReward2(currentRow)
		467	| <span class="unit">{{
		480	| </a-spin>
		483	| <DelegateDrawer @success="delegateSuccess" ref="DelegateDrawerRef" />
		489	| import { BigNumber } from "bignumber.js";
		490	| import {
		491	| collatorStatistics,
		492	| getCurrentRoundInfo,
		493	| getCollatorReward,
		494	| delegatorStatistics,
		495	| getMaxNominatorsPerCollator,
		496	| } from "@/api/staking";
		503	| props: ["getSafeStatus", "ifStaked"],
		519	| { name: "Delegator Stake", prop: "delegatorStake", "min-width": "160" },
		520	| { name: "Self Stake", prop: "selfStake", "min-width": "140" },
		523	| prop: "myStake",
		529	| prop: "avgBlockIn10R",
		535	| prop: "currentBlock",
		541	| { name: "Latest Rewards", prop: "latestReward", "min-width": "160" },
		543	| name: "Avg RPS",
		544	| prop: "avgRps",
		546	| tip: "Average rewards per stake.<br/>1. Use data of latest 10 rounds,<br/>2. Get a list of RPS: total rewards of each round / total stake of each round<br/>3. Calculate mean of the list to get Avg RPS",
		549	| name: "Min RPS",
		550	| prop: "minRps",
		552	| tip: "Minimum rewards per stake.<br/>1. Use data of latest 10 rounds,<br/> 2. Get a list of RPS: total rewards of each round / total stake of each round<br/>3. Find the minium of the list",
		555	| name: "Max RPS",
		556	| prop: "maxRps",
		558	| tip: "Maximum rewards per stake.<br/>1. Use data of latest 10 rounds,<br/>2. Get a list of RPS: total rewards of each round / total stake of each round<br/>3. Find the maximum of the list",
		561	| name: "RPS Volatility Score",
		562	| prop: "rpsScore",
		564	| tip: "The volatility of rewards. The less the volatility is, the rewards from this collator are relatively stable.<br/>1. Use data of latest 10 rounds,<br/>2. Get a list of RPS: total rewards of each round / total stake of each round<br/>3. Find the standard deviation of the list",
		573	| "RPS Volatility Score",
		583	| maxNominator: 50,
		584	| loading: false,
		585	| orderBys: [{ sort: "totalStake", order: "DESC" }],
		586	| collatorRewardDataMap: {},
		587	| top3DelegatorDataMap: {},
		588	| roundInfo: {
		589	| current: null,
		590	| first: null,
		591	| length: null,
		592	| totalIssuance: null,
		616	| this.initPage();
		618	| watch: {
		619	| "$store.state.global.currentChain"() {
		620	| this.initPage();
		622	| "$store.state.global.metamaskWallet"() {
		625	| "$store.state.global.polkadotWallet"() {
		629	| computed: {
		630	| startRoundIndex() {
		631	| return this.roundInfo.current - 11;
		633	| endRoundIndex() {
		634	| return this.roundInfo.current - 2;
		638	| getSumulatePercent(row) {
		639	| const rank = this.getSimulateRank(row);
		640	| const percent = BigNumber(this.maxNominator - rank)
		641	| .dividedBy(this.maxNominator)
		642	| .multipliedBy(100);
		643	| return percent.toFixed(2) + "%";
		645	| getSingleNominatorStakeByRank(row, rank) {
		646	| if (!row.allNominators[rank - 1]) {
		647	| return BigNumber(0);
		649	| const stake = row.allNominators[rank - 1].stake;
		650	| return this.$utils.roundNumber(stake);
		652	| getSimulateRank(row) {
		653	| if (!row.allNominators.length) {
		654	| return 1;
		656	| const index = row.allNominators.findIndex((v) => {
		657	| const result =
		658	| BigNumber(this.inputValue || 0).toNumber() >
		659	| BigNumber(v.stake).toNumber();
		660	| return result;
		662	| if (index == -1) {
		663	| return row.allNominators.length + 1;
		665	| return index + 1;
		667	| getBoundaryReward1(row) {
		668	| let topSum = BigNumber(0);
		669	| row.rpsHis.forEach((v) => {
		670	| topSum = topSum.plus(
		671	| BigNumber(v.rps).minus(row.avgRps).exponentiatedBy(2)
		674	| const standardDeviation = topSum.dividedBy(row.rpsHis.length).sqrt();
		675	| const min = BigNumber(this.inputValue || 0).multipliedBy(
		676	| new BigNumber(row.avgRps).minus(standardDeviation)
		678	| return min.toFormat(5);
		680	| getBoundaryReward2(row) {
		681	| let topSum = BigNumber(0);
		682	| row.rpsHis.forEach((v) => {
		683	| topSum = topSum.plus(
		684	| BigNumber(v.rps).minus(row.avgRps).exponentiatedBy(2)
		687	| const standardDeviation = topSum.dividedBy(row.rpsHis.length).sqrt();
		688	| const max = BigNumber(this.inputValue || 0).multipliedBy(
		689	| new BigNumber(row.avgRps).plus(standardDeviation)
		691	| return max.toFormat(5);
		693	| delegateSuccess() {
		695	| this.$emit("updateMyStakeList");
		697	| initPage() {
		698	| this.getMaxNominatorsPerCollator();
		699	| this.getRoundInfo();
		702	| getMaxNominatorsPerCollator() {
		703	| getMaxNominatorsPerCollator({
		706	| this.maxNominator = d;
		709	| tableSortChange({ prop, order }) {
		710	| if (!order) {
		711	| this.orderBys = [{ sort: "totalStake", order: "DESC" }];
		712	| } else {
		713	| this.orderBys = [
		714	| { sort: prop, order: order == "ascending" ? "ASC" : "DESC" },
		719	| figureStakePercent(sv, v) {
		720	| const result = new BigNumber(sv.stake)
		721	| .div(new BigNumber(v.delegatorStake))
		722	| .multipliedBy(100)
		723	| .toFormat(2);
		726	| getRowChartOption(row) {
		727	| const rewardHistoryList = this.collatorRewardDataMap[row.collator] || [];
		728	| const option = {
		734	| data: rewardHistoryList.map((v) => "Round " + v.roundIndex),
		747	| confine: true,
		751	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${
		752	| params.name
		753	| }</div>
		754	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${this.$utils.roundNumber(
		755	| params.value
		756	| )}</div>
		767	| data: rewardHistoryList.map((v) => v.reward.toNumber()),
		779	| data: rewardHistoryList.map((v) => v.reward.toNumber()),
		784	| return option;
		786	| handleExpand(row) {
		787	| this.getCollatorReward(row);
		788	| this.getTop3DelegatorStatistics(row);
		790	| getTop3DelegatorStatistics(row) {
		791	| delegatorStatistics({
		792	| pageSize: 3,
		794	| orderBys: [{ sort: "stake", order: "DESC" }],
		796	| collator: row.collator,
		798	| this.top3DelegatorDataMap[row.collator] = d.list;
		801	| getCollatorReward(row) {
		802	| getCollatorReward({
		804	| startRoundIndex: this.startRoundIndex,
		805	| endRoundIndex: this.endRoundIndex,
		806	| accounts: [row.collator],
		808	| const arr = [];
		809	| for (let i = this.startRoundIndex; i <= this.endRoundIndex; i++) {
		810	| const find = d.rewards.find(
		811	| (sv) =>
		812	| sv.account.toLowerCase() == row.collator.toLowerCase() &&
		813	| Number(sv.roundIndex) == i
		815	| if (find) {
		816	| arr.push({
		817	| roundIndex: i,
		818	| reward: BigNumber(find.reward),
		820	| } else {
		821	| arr.push({
		822	| roundIndex: i,
		823	| reward: BigNumber(0),
		827	| this.collatorRewardDataMap[row.collator] = arr;
		830	| getRoundInfo() {
		831	| getCurrentRoundInfo({
		834	| this.roundInfo = d;
		837	| goToCollatorDetail(address) {
		838	| localStorage.setItem("routeParamsAddress", address);
		839	| this.$router.push({
		840	| name: "collatorDetail",
		843	| goToDelegatorDetail(address) {
		844	| localStorage.setItem("routeParamsAddress", address);
		846	| name: "delegatorDetail",
		852	| myAccount: this.$store.getters.currentChainWalletAddress,
		855	| orderBys: this.orderBys,
		856	| needTotal: true,
		861	| this.totalCount = d.totalCount;
		865	| // 未登录或者钱包与网络不匹配
		866	| if (
		867	| !this.$store.getters.ifLogin ||
		868	| (this.$utils.ifSupportPolkadot(
		869	| this.$store.state.global.currentChain.network
		870	| ) &&
		871	| !this.$store.getters.polkadotWalletTransformAddress) ||
		872	| (!this.$utils.ifSupportPolkadot(
		873	| this.$store.state.global.currentChain.network
		874	| ) &&
		875	| !this.$store.state.global.metamaskWallet.address)
		876	| ) {
		877	| this.$eventBus.emit("goSignIn");
		878	| return;
		884	| this.$refs.DelegateDrawerRef.init(this.currentRow.collator);
		894	| this.inputValue = 0;
		895	| this.currentRow = {};
		896	| delegatorStatistics({
		897	| pageSize: 9999999999,
		899	| orderBys: [{ sort: "stake", order: "DESC" }],
		901	| collator: row.collator,
		903	| this.currentRow = { ...row, allNominators: d.list };
		999	| white-space: nowrap;
		1035	| .Risk {
		1038	| .Safe {
		1041	| .Pending {
		1042	| color: #10a7e4;
		1213	| .identity-icon {
		1262	| &.Risk {
		1264	| background: rgba(227, 26, 26, 0.1);
		1267	| &.Safe {
		1272	| &.Pending {
		1273	| color: #10a7e4;
		1274	| background: rgba(16, 167, 228, 0.1);
		1372	| min-height: 30px;
		1380	| .nowrap {
		1381	| white-space: nowrap;

	Unique lines in second:
		2	| <el-table :data="tableData" ref="table">
		4	| <template #default="props">
		5	| <!-- <p>State: {{ props.row.state }}</p> -->
		12	| <v-chart class="chart" :option="option" />
		17	| <span class="text">Top 3 Stake percent delegator</span>
		20	| <div v-for="(v, i) in 3" :key="i" class="item">
		22	| <img
		25	| alt=""
		26	| />
		39	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		41	| <div class="address">0xF97…acewaC</div>
		42	| <div class="percent">78.07%</div>
		52	| <span class="text" :class="'color' + (scope.$index + 1)">{{
		53	| getIndex(scope.$index + 1)
		58	| class="icon"
		65	| <div class="top">
		74	| <span class="safe" v-if="ifSafe(scope.row)">Safe</span>
		75	| <span v-else class="risk">Risk</span>
		76	| <span class="delegated">Delegated</span>
		88	| sortable
		95	| <span class="text">{{ scope.row[v.prop] }}%</span>
		103	| sortable
		109	| <a-tooltip :content="v.tip">
		121	| sortable
		221	| <div class="drawer-main">
		224	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		227	| <div class="value">Jetblue-125</div>
		232	| <div class="value">1790</div>
		235	| <div class="tag">Safe</div>
		236	| <div class="tag yellow">Delegated</div>
		262	| <div class="blue-line" :style="{ width: '20%' }"></div>
		263	| <div class="g-split" :style="{ left: '20%' }"></div>
		264	| <div class="popover" :style="{ left: '20%' }">
		267	| <div>Rank 28</div>
		268	| <div>Stake 10056464646</div>
		274	| <div class="rank">Rank 300</div>
		275	| <div class="stake">Stake 80</div>
		278	| <div class="rank">Rank 270</div>
		279	| <div class="stake">Stake 80</div>
		282	| <div class="rank">Rank 150</div>
		283	| <div class="stake">Stake 80</div>
		287	| <div class="stake">Stake 80</div>
		298	| <span class="num">0.0222222 </span>
		299	| <span class="unit">GLMR</span>
		306	| <span class="num">0.0222222 </span>
		307	| <span class="unit">GLMR</span>
		320	| <DelegateDrawer ref="DelegateDrawerRef" />
		325	| import { collatorStatistics } from "@/api/staking";
		331	| props: ["ifSafe"],
		347	| { name: "Delegator Stake", prop: "state", "min-width": "160" },
		348	| { name: "Self Stake", prop: "state", "min-width": "140" },
		351	| prop: "state",
		357	| prop: "state",
		363	| prop: "state",
		369	| { name: "Latest Rewards", prop: "totalReward", "min-width": "160" },
		371	| name: "Avg RPM",
		372	| prop: "state",
		374	| tip: "Average rewards per LIT for next round. It refers to rewards amount that you will get in the next round if you stake. This indicator is for delegators to find the average estimated rewards under the fixed token quantity.",
		377	| name: "Min RPM",
		378	| prop: "state",
		380	| tip: "Minimum rewards per LIT for next round. It refers to rewards amount that you will get in the next round if you stake. This indicator is for delegators to find the minimum estimated rewards under the fixed token quantity.",
		383	| name: "Max RPM",
		384	| prop: "state",
		386	| tip: "Maximum rewards per LIT for next round. It refers to rewards amount that you will get in the next round if you stake. This indicator is for delegators to find the maximum estimated rewards under the fixed token quantity.",
		389	| name: "RPM Volatility Score",
		390	| prop: "state",
		392	| tip: "The volatility of rewards. We use standard deviation to indicate the volatility of rewards. The less the volatility is, the rewards of nominating this collator are relatively stable(according to the latest 10 rounds)",
		401	| "RPM Volatility Score",
		430	| option: {
		436	| data: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
		452	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${params.name}</div>
		453	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${params.value}</div>
		464	| data: [140, 200, 150, 80, 70, 110, 130, 80, 70, 80],
		476	| data: [140, 200, 150, 80, 70, 110, 130, 80, 70, 80],
		493	| orderBys: [],
		498	| // this.totalCount = res.totalCount;
		499	| this.totalCount = 12;
		503	| this.currentRow = row;
		507	| this.$refs.DelegateDrawerRef.init(this.currentRow);
		647	| .risk {
		963	| height: 30px;


Partially similar files found. First length 25, Second length 19,  The files are 63% identicalThe files differ in 5 lines:
	./resources/european/service/src/viewModel/staking/portal/StatCollatorPageRequest.ts
	./resources/asia/service/src/viewModel/staking/portal/StatCollatorPageRequest.ts
	Unique lines in first:
		7	| default: false
		13	| description: 'used for search'
		19	| description: 'used for search'
		25	| description: 'if required myStake value, this field is compulsory'
		27	| myAccount: string

	Unique lines in second:
		12	| description: 'matched by LIKE %collator%'
		18	| description: 'matched by LIKE %delegator%'


Partially similar files found. First length 532, Second length 483,  The files are 62% identicalThe files differ in 98 lines:
	./resources/european/web/src/views/myStake/Timemachine/StakingTable.vue
	./resources/asia/ui/src/views/myStake/Timemachine/StakingTable.vue
	Unique lines in first:
		1	| <a-spin style="width: 100%" :loading="loading">
		3	| <el-table
		4	| :data="
		5	| formatTable.slice((pageIndex - 1) * pageSize, pageIndex * pageSize)
		6	| "
		7	| >
		11	| <IdentityWrap :address="scope.row.collator">
		12	| <template #default="{ identity }">
		13	| <IdentityIcon
		14	| class="hover-item"
		15	| @click="goToCollatorDetail(scope.row.collator)"
		16	| :identity="identity"
		17	| :address="scope.row.collator"
		18	| ></IdentityIcon>
		19	| <a-tooltip :content="scope.row.collator" placement="top">
		20	| <span
		21	| class="hover-primary"
		22	| style="margin-left: 8px"
		23	| @click="goToCollatorDetail(scope.row.collator)"
		24	| >{{
		25	| identity.display
		26	| ? identity.display
		27	| : $utils.shorterAddress(scope.row.collator)
		28	| }}</span
		29	| >
		30	| </a-tooltip>
		32	| </IdentityWrap>
		36	| <el-table-column
		37	| prop="roundindex"
		38	| label="Staked Round"
		39	| min-width="120"
		40	| />
		41	| <el-table-column
		42	| prop="actiontype"
		43	| label="Action Type"
		45	| />
		46	| <el-table-column label="Amount" min-width="120">
		48	| {{ $utils.roundNumber(scope.row.balancechange) }}
		51	| <el-table-column prop="blocknumber" label="Block" min-width="120" />
		52	| <el-table-column label="Timestamp" min-width="160">
		54	| {{ $moment(scope.row.timestamp).format("YYYY-MM-DD HH:mm:ss") }}
		58	| <div class="pagination-wrap">
		59	| <a-pagination
		60	| :total="formatTable.length"
		61	| v-model:current="pageIndex"
		62	| v-model:page-size="pageSize"
		63	| show-total
		64	| show-jumper
		65	| />
		68	| </a-spin>
		72	| import IdentityWrap from "@/components/IdentityWrap";
		73	| import IdentityIcon from "@/components/IdentityIcon";
		74	| import { timeMachineStakingHis } from "@/api/staking";
		77	| props: ["selectCollator", "selectRound"],
		78	| components: {
		79	| IdentityWrap,
		80	| IdentityIcon,
		84	| loading: false,
		85	| pageIndex: 1,
		86	| pageSize: 10,
		87	| totalCount: 0,
		98	| tableData: [],
		101	| created() {
		102	| this.initPage();
		104	| watch: {
		105	| "$store.state.global.currentChain"() {
		106	| this.initPage();
		108	| "$store.state.global.metamaskWallet"() {
		109	| this.initPage();
		111	| "$store.state.global.polkadotWallet"() {
		112	| this.initPage();
		115	| computed: {
		116	| formatTable() {
		117	| let arr = this.tableData;
		118	| if (this.selectCollator) {
		119	| arr = arr.filter((v) => v.collator == this.selectCollator);
		121	| if (this.selectRound) {
		122	| arr = arr.filter((v) => v.roundindex == this.selectRound);
		124	| return arr;
		127	| methods: {
		128	| initPage() {
		129	| this.getTableData();
		131	| getTableData() {
		132	| this.loading = true;
		133	| timeMachineStakingHis({
		134	| chainId: this.$store.state.global.currentChain.id,
		135	| delegator: this.$store.getters.currentChainWalletAddress,
		136	| }).then((d) => {
		137	| this.loading = false;
		138	| this.tableData = d;
		139	| });
		141	| goToCollatorDetail(address) {
		142	| localStorage.setItem("routeParamsAddress", address);
		143	| this.$router.push({
		144	| name: "collatorDetail",
		145	| });
		151	| .pagination-wrap {
		154	| justify-content: flex-end;

	Unique lines in second:
		2	| <el-table :data="tableData">
		6	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		7	| <span>binance account</span>
		11	| <el-table-column prop="state" label="Staked Round" min-width="120" />
		12	| <el-table-column prop="state" label="Action Type" min-width="120" />
		13	| <el-table-column prop="state" label="Amount" min-width="120" />
		14	| <el-table-column prop="state" label="Block" min-width="120" />
		15	| <el-table-column prop="state" label="Timestamp" min-width="120" />
		34	| tableData: [
		35	| {
		36	| date: "2016-05-03",
		37	| name: "Tom",
		38	| state: "California",
		39	| city: "Los Angeles",
		40	| address: "Los Angeles",
		41	| zip: "CA 90036",
		43	| {
		44	| date: "2016-05-03",
		45	| name: "Tom",
		46	| state: "California",
		47	| city: "Los Angeles",
		48	| address: "Los Angeles",
		49	| zip: "CA 90036",
		51	| {
		52	| date: "2016-05-03",
		53	| name: "Tom",
		54	| state: "California",
		55	| city: "Los Angeles",
		56	| address: "Los Angeles",
		57	| zip: "CA 90036",
		59	| {
		60	| date: "2016-05-03",
		61	| name: "Tom",
		62	| state: "California",
		63	| city: "Los Angeles",
		64	| address: "Los Angeles",
		65	| zip: "CA 90036",
		67	| {
		68	| date: "2016-05-03",
		69	| name: "Tom",
		70	| state: "California",
		71	| city: "Los Angeles",
		72	| address: "Los Angeles",
		73	| zip: "CA 90036",
		75	| {
		76	| date: "2016-05-03",
		77	| name: "Tom",
		78	| state: "California",
		79	| city: "Los Angeles",
		80	| address: "Los Angeles",
		81	| zip: "CA 90036",
		83	| {
		84	| date: "2016-05-03",
		85	| name: "Tom",
		86	| state: "California",
		87	| city: "Los Angeles",
		88	| address: "Los Angeles",
		89	| zip: "CA 90036",
		91	| {
		92	| date: "2016-05-03",
		93	| name: "Tom",
		94	| state: "California",
		95	| city: "Los Angeles",
		96	| address: "Los Angeles",
		97	| zip: "CA 90036",
		99	| ],
		102	| methods: {},
		135	| img {
		254	| img {


Partially similar files found. First length 19, Second length 21,  The files are 62% identicalThe files differ in 5 lines:
	./resources/european/service/src/parachain/staking/portal/service/home-service.ts
	./resources/asia/service/src/parachain/staking/portal/service/home-service.ts
	Unique lines in first:
		1	| import { StatNetwork } from "src/common/entity/StakingPortalStat/StatNetwork.entity";
		10	| constructor(private serviceManager: ServiceManager) {}
		19	| return DbManager.PORTAL.statNetworkRepository.findOne({ chainId });

	Unique lines in second:
		1	| import { StatNetwork } from "src/common/entity/StakingModule/StatNetwork.entity";
		10	| constructor(
		11	| private serviceManager: ServiceManager
		12	| ) {}
		21	| return DbManager.get(chainId).statNetworkRepository.findOne({});


Partially similar files found. First length 320, Second length 262,  The files are 61% identicalThe files differ in 72 lines:
	./resources/european/web/src/views/home/Table.vue
	./resources/asia/ui/src/views/home/Table.vue
	Unique lines in first:
		6	| @sort-change="tableSortChange"
		9	| <el-table-column class-name="first-col" label="Chain" width="180">
		19	| <el-table-column
		20	| class-name="collector-col"
		21	| label="Staked Collator"
		22	| min-width="180"
		29	| class="hover-item"
		30	| @click="goToCollatorDetail(scope.row)"
		31	| :network="scope.row.chainId"
		37	| <span
		38	| @click="goToCollatorDetail(scope.row)"
		39	| class="hover-primary"
		40	| style="margin-left: 8px"
		41	| >{{
		45	| }}</span
		56	| <span class="num">{{ $utils.roundNumber(scope.row.myStake) }}</span>
		61	| <el-table-column label="APR">
		66	| <el-table-column sortable="custom" prop="myRank" label="My Rank" />
		67	| <el-table-column
		68	| sortable="custom"
		69	| prop="latestReward"
		70	| label="Latest Rewards"
		75	| $utils.roundNumber(scope.row.latestReward, 4)
		81	| <el-table-column
		82	| sortable="custom"
		83	| prop="totalReward"
		84	| label="Total Rewards"
		100	| import { ChainUtils } from "@/utils/chain/chain.utils";
		113	| savedDefaultTableData: [],
		117	| this.getTableData();
		119	| watch: {
		120	| "$store.state.global.metamaskWallet"() {
		121	| this.getTableData();
		123	| "$store.state.global.polkadotWallet"() {
		124	| this.getTableData();
		144	| tableSortChange({ prop, order }) {
		145	| if (!order) {
		146	| this.tableData = JSON.parse(JSON.stringify(this.savedDefaultTableData));
		147	| return;
		149	| let chainMapData = {};
		150	| this.tableData.forEach((v) => {
		151	| v.rowSpan = undefined;
		152	| if (!chainMapData[v.chainId]) {
		153	| chainMapData[v.chainId] = [v];
		155	| chainMapData[v.chainId].push(v);
		158	| Object.keys(chainMapData).forEach((key) => {
		159	| chainMapData[key] = chainMapData[key].sort((a, b) =>
		160	| order == "ascending" ? a[prop] - b[prop] : b[prop] - a[prop]
		163	| let newArr = [];
		164	| Object.keys(chainMapData).forEach((key) => {
		165	| chainMapData[key][0].rowSpan = chainMapData[key].length;
		166	| newArr = [...newArr, ...chainMapData[key]];
		168	| console.log("111", newArr);
		169	| this.tableData = newArr;
		171	| getTableData() {
		172	| this.tableData = [];
		174	| let alreadyRequestCount = 0;
		176	| alreadyRequestCount++;
		177	| if (alreadyRequestCount == requestCount) {
		178	| this.savedDefaultTableData = JSON.parse(
		179	| JSON.stringify(this.tableData)
		191	| const transformAddress = ChainUtils.ss58transform_simple(
		192	| this.$store.state.global.polkadotWallet.address,
		193	| v.network
		197	| accountId: transformAddress,
		224	| goToCollatorDetail(row) {
		225	| const chain = this.$store.state.global.supportChainList.find(
		226	| (v) => v.id == row.chainId
		228	| this.$store.commit("changeCurrentChain", chain);
		229	| localStorage.setItem("routeParamsAddress", row.collator);
		230	| this.$router.push({
		231	| name: "collatorDetail",

	Unique lines in second:
		8	| <el-table-column class-name="first-col" label="Chain">
		18	| <el-table-column class-name="collector-col" label="Staked Collator">
		29	| <span style="margin-left: 8px">{{
		43	| <span class="num">{{
		44	| $utils.roundNumber(scope.row.stakedAmount)
		50	| <el-table-column label="apr">
		55	| <el-table-column sortable prop="rank" label="My Rank" />
		56	| <el-table-column sortable label="Latest Reward">
		60	| $utils.roundNumber(scope.row.latestReward)
		66	| <el-table-column sortable label="Total Rewards">
		93	| };
		96	| // this.tableData = [
		97	| //   ...this.tableData,
		98	| //   ...[
		99	| //     {
		100	| //       chainId: "litentry",
		101	| //       collator: "fGd1ED9fqVp4m2gLYK5oyVq2BY5s6xBBtedBQF6v6wMXfPC",
		102	| //       stakedAmount: 52.710000010001,
		103	| //       totalReward: 2073.3247550582455,
		104	| //       rank: 0,
		105	| //       apr: 0,
		106	| //       rowSpan: 2,
		107	| //     },
		108	| //     {
		109	| //       chainId: "litentry",
		110	| //       collator: "nnd1ED9fqVp4m2gLYK5oyVq2BY5s6xBBtedBQF6v6wMXfPC",
		111	| //       stakedAmount: 52.710000010001,
		112	| //       totalReward: 2073.3247550582455,
		113	| //       rank: 0,
		114	| //       apr: 0,
		115	| //     },
		116	| //   ],
		117	| // ];
		121	| if (requestCount == this.$store.state.global.supportChainList.length) {
		124	| };
		133	| accountId: this.$store.state.global.polkadotWallet.address,
		169	| };
		229	| img {


Partially similar files found. First length 230, Second length 181,  The files are 60% identicalThe files differ in 44 lines:
	./resources/european/web/src/views/myStake/index.vue
	./resources/asia/ui/src/views/myStake/index.vue
	Unique lines in first:
		17	| <span> {{ $utils.roundNumber(baseInfo.totalBond) }}</span>
		18	| <span class="unit">{{
		19	| $store.state.global.currentChain.symbols[0]
		20	| }}</span>
		42	| {{ $utils.roundNumber(baseInfo.stakedCollators, 0) }}
		62	| <span>{{ $utils.roundNumber(baseInfo.latestReward, 4) }}</span>
		64	| $store.state.global.currentChain.symbols[0]
		65	| }}</span>
		83	| <span> {{ $utils.roundNumber(baseInfo.totalReward) }} </span>
		85	| $store.state.global.currentChain.symbols[0]
		86	| }}</span>
		93	| <a-tab-pane :key="1" title="Staked Collators"></a-tab-pane>
		96	| <StakingCollators :refreshTopPage="initPage" v-if="tabKey == 1" />
		103	| import { delegatorInfo } from "@/api/staking";
		104	| import StakingCollators from "./StakingCollators";
		105	| import Timemachine from "./Timemachine";
		114	| baseInfo: {},
		117	| created() {
		118	| this.initPage();
		120	| watch: {
		121	| "$store.state.global.currentChain"() {
		122	| this.initPage();
		124	| "$store.state.global.metamaskWallet"() {
		125	| if (!this.$store.getters.currentChainWalletAddress) {
		126	| this.$router.push({
		127	| name: "home",
		128	| });
		129	| this.$eventBus.emit("goSignIn");
		130	| return;
		132	| this.initPage();
		134	| "$store.state.global.polkadotWallet"() {
		135	| if (!this.$store.getters.currentChainWalletAddress) {
		137	| name: "home",
		138	| });
		140	| return;
		142	| this.initPage();
		145	| methods: {
		146	| initPage() {
		147	| delegatorInfo({
		148	| chainId: this.$store.state.global.currentChain.id,
		149	| delegator: this.$store.getters.currentChainWalletAddress,
		150	| }).then((d) => {
		151	| this.baseInfo = d;
		152	| });

	Unique lines in second:
		9	| <img
		10	| class="icon"
		12	| alt=""
		13	| />
		17	| <span> 39,024,467 </span>
		18	| <span class="unit">GLMR</span>
		33	| class="icon"
		39	| <div class="value">39,024,467</div>
		51	| class="icon"
		58	| <span> 39,024,467 </span>
		59	| <span class="unit">GLMR</span>
		77	| <span> 39,024,467 </span>
		78	| <span class="unit">GLMR</span>
		85	| <a-tab-pane :key="1" title="Staking Collators"></a-tab-pane>
		88	| <StakingCollators v-if="tabKey == 1" />
		95	| import StakingCollators from "./StakingCollators/index.vue";
		96	| import Timemachine from "./Timemachine/index.vue";


Partially similar files found. First length 80, Second length 53,  The files are 59% identicalThe files differ in 23 lines:
	./resources/european/web/src/store/global.js
	./resources/asia/ui/src/store/global.js
	Unique lines in first:
		5	| import { ChainUtils } from "@/utils/chain/chain.utils";
		24	| ifHasCurrentChainWallet(state, getters) {
		25	| if (
		26	| !getters.ifLogin ||
		27	| (ifSupportPolkadot(
		28	| state.global.currentChain.network
		29	| ) &&
		30	| !getters.polkadotWalletTransformAddress) ||
		31	| (!ifSupportPolkadot(
		32	| state.global.currentChain.network
		33	| ) &&
		34	| !state.global.metamaskWallet.address)
		35	| ) {
		40	| polkadotWalletTransformAddress(state) {
		41	| if (state.currentChain.network) {
		42	| const transformAddress = ChainUtils.ss58transform_simple(
		43	| state.polkadotWallet.address,
		44	| state.currentChain.network
		45	| );
		46	| return transformAddress;
		48	| return state.polkadotWallet.address;
		50	| currentChainWalletAddress(state, getters) {
		52	| return getters.polkadotWalletTransformAddress

	Unique lines in second:
		22	| currentChainWalletAddress(state) {
		24	| return state.polkadotWallet.address


Partially similar files found. First length 20, Second length 12,  The files are 59% identicalThe files differ in 7 lines:
	./resources/european/service/src/viewModel/staking/DelegatorRewardHistory.ts
	./resources/asia/service/src/viewModel/staking/DelegatorRewardHistory.ts
	Unique lines in first:
		9	| @ApiProperty({
		10	| required: false
		11	| })
		12	| roundindex: number;
		14	| @ApiProperty({
		15	| required: false
		17	| collator: string;

	Unique lines in second:


Partially similar files found. First length 1333, Second length 979,  The files are 58% identicalThe files differ in 338 lines:
	./resources/european/web/src/views/myStake/StakingCollators/Table.vue
	./resources/asia/ui/src/views/myStake/StakingCollators/Table.vue
	Unique lines in first:
		1	| <a-spin style="width: 100%" :loading="loading">
		7	| <IdentityWrap :address="scope.row.collator">
		8	| <template #default="{ identity }">
		9	| <IdentityIcon
		10	| class="icon hover-item"
		11	| @click="goToCollatorDetail(scope.row.collator)"
		12	| :identity="identity"
		13	| :address="scope.row.collator"
		14	| :iconSize="32"
		15	| ></IdentityIcon>
		17	| <a-tooltip :content="scope.row.collator" placement="top">
		18	| <div
		19	| class="top hover-primary"
		20	| @click="goToCollatorDetail(scope.row.collator)"
		22	| {{
		23	| identity.display
		24	| ? identity.display
		25	| : $utils.shorterAddress(scope.row.collator)
		26	| }}
		28	| </a-tooltip>
		30	| <span :class="getSafeStatus(scope.row)">{{
		31	| getSafeStatus(scope.row)
		32	| }}</span>
		36	| </IdentityWrap>
		41	| <el-table-column
		49	| <span class="text" v-if="v.name == 'My Share'"
		50	| >{{ scope.row[v.prop] }}%</span
		53	| class="text"
		54	| v-else-if="v.name == 'Collator\'s Rank' || v.name == 'My Rank'"
		55	| >{{ scope.row[v.prop] }}</span
		57	| <span v-else class="text">{{
		58	| $utils.roundNumber(scope.row[v.prop])
		59	| }}</span>
		118	| v-if="scope.row.status == 'TO_REVOKE'"
		120	| @click="handleDelegate(scope.row)"
		124	| v-if="scope.row.status == 'TO_REVOKE'"
		131	| v-else-if="scope.row.status == 'TO_EXECUTE'"
		132	| class="common-table-option Exceute"
		134	| <span @click="handleExceute(scope.row)"> Exceute </span>
		151	| v-else
		161	| <span class="text" v-if="rowTimeFormatMap[scope.row.collator]">
		162	| <span class="num">{{
		163	| rowTimeFormatMap[scope.row.collator].days
		164	| }}</span>
		166	| <span class="num">{{
		167	| rowTimeFormatMap[scope.row.collator].hours
		168	| }}</span>
		170	| <span class="num">{{
		171	| rowTimeFormatMap[scope.row.collator].minutes
		172	| }}</span>
		181	| <span class="value">{{
		182	| scope.row.whenExecutableRoundIndex
		183	| }}</span>
		188	| class="value"
		189	| v-if="rowTimeFormatMap[scope.row.collator]"
		190	| >{{
		191	| rowTimeFormatMap[scope.row.collator].estimatedTime
		192	| }}</span
		198	| class="value"
		199	| v-if="rowTimeFormatMap[scope.row.collator]"
		200	| >{{ rowTimeFormatMap[scope.row.collator].timeLeft }}</span
		222	| <DelegateDrawer ref="DelegateDrawerRef" @success="delegateSuccess" />
		224	| </a-spin>
		228	| import aprUtlis from "@/utils/aprUtils";
		230	| import IdentityWrap from "@/components/IdentityWrap";
		231	| import IdentityIcon from "@/components/IdentityIcon";
		232	| import { homeMyStake, getSafeStateConfig } from "@/api/staking";
		235	| import { ChainUtils } from "@/utils/chain/chain.utils";
		239	| import { ethers } from "ethers";
		240	| import moonbeamContractAbi from "@/utils/moonbeamContractAbi";
		246	| IdentityWrap,
		247	| IdentityIcon,
		249	| props: ["roundInfo", "latestBlockNumber", "refreshTopPage"],
		254	| prop: "rank",
		255	| "min-width": "160",
		257	| { name: "Self Stake", prop: "selfStake", "min-width": "140" },
		258	| { name: "Delegator Stake", prop: "nominatorStake", "min-width": "160" },
		261	| prop: "totalStake",
		266	| prop: "myStake",
		271	| prop: "myRank",
		276	| prop: "myShare",
		286	| timerMap: {},
		287	| rowTimeFormatMap: {},
		288	| targetSecondsPerBlock: 12, //seconds
		289	| loading: false,
		290	| safeStateConfig: {},
		294	| tableData: [],
		306	| moonBeamContract: null,
		311	| this.initPage();
		313	| watch: {
		314	| "$store.state.global.currentChain"() {
		315	| this.initPage();
		317	| "$store.state.global.metamaskWallet"() {
		318	| this.getTableData();
		320	| "$store.state.global.polkadotWallet"() {
		321	| this.getTableData();
		324	| beforeUnmount() {
		325	| Object.keys(this.timerMap).forEach((v) => {
		326	| clearInterval(this.timerMap[v]);
		330	| delegateSuccess() {
		331	| this.getTableData();
		332	| this.refreshTopPage();
		334	| async getMoonBeamContract() {
		335	| if (this.moonBeamContract) {
		336	| return;
		338	| if (this.$store.state.global.currentChain.network == "moonbeam") {
		339	| await ethereum.request({
		340	| method: "wallet_addEthereumChain",
		341	| params: [
		343	| chainId: "0x504",
		344	| chainName: "Moonbeam",
		345	| rpcUrls: ["https://rpc.api.moonbeam.network"],
		346	| nativeCurrency: {
		347	| name: "GLMR",
		348	| symbol: "GLMR",
		349	| decimals: 18,
		351	| blockExplorerUrls: ["https://moonbeam.moonscan.io"],
		355	| } else if (this.$store.state.global.currentChain.network == "moonriver") {
		356	| await ethereum.request({
		357	| method: "wallet_addEthereumChain",
		358	| params: [
		360	| chainId: "0x505",
		361	| chainName: "Moonriver",
		362	| rpcUrls: ["https://rpc.api.moonriver.moonbeam.network"],
		363	| nativeCurrency: {
		364	| name: "MOVR",
		365	| symbol: "MOVR",
		366	| decimals: 18,
		368	| blockExplorerUrls: ["https://moonriver.moonscan.io"],
		373	| const provider = new ethers.providers.Web3Provider(window.ethereum);
		374	| await provider.send("eth_requestAccounts", []);
		375	| const signer = provider.getSigner();
		376	| console.log("Account:", await signer.getAddress());
		377	| const contract = new ethers.Contract(
		378	| "0x0000000000000000000000000000000000000800",
		379	| moonbeamContractAbi,
		380	| signer
		382	| this.moonBeamContract = contract;
		384	| async initPage() {
		385	| this.loading = true;
		386	| aprUtlis
		387	| .getBlockTargetSeconds(this.$store.state.global.currentChain.id)
		388	| .then((d) => {
		389	| this.targetSecondsPerBlock = d;
		398	| await this.getSafeStateConfig();
		399	| this.getTableData();
		403	| updateRowStatus(row, status) {
		404	| console.log("111", row, status);
		405	| const findIndex = this.tableData.findIndex(
		406	| (v) => v.collator == row.collator
		408	| if (findIndex !== -1) {
		409	| this.tableData[findIndex].status = status;
		412	| getTableData() {
		413	| if (!this.$store.getters.currentChainWalletAddress) {
		414	| return;
		417	| homeMyStake({
		418	| chainId: this.$store.state.global.currentChain.id,
		419	| accountId: this.$store.getters.currentChainWalletAddress,
		420	| }).then(async (d) => {
		421	| for (const v of d) {
		422	| await this.figureRevokeStatus(v);
		424	| this.tableData = d;
		425	| this.loading = false;
		428	| async figureRevokeStatus(row) {
		429	| let res = [];
		430	| try {
		431	| res = (
		432	| await this.apiPromise.query.parachainStaking.delegationScheduledRequests(
		433	| row.collator
		435	| ).toHuman();
		436	| } catch (e) {
		437	| console.warn("encountered errors while fetching the revoking status");
		439	| const matched = res.filter(
		440	| (it) =>
		441	| it.whenExecutable &&
		442	| it.delegator === this.$store.getters.currentChainWalletAddress
		444	| if (!matched.length) {
		445	| row.status = "TO_REVOKE";
		446	| return;
		448	| const whenExecutableRoundIndex = Number(
		449	| matched[0].whenExecutable.replace(/,/g, "")
		451	| row.whenExecutableRoundIndex = whenExecutableRoundIndex;
		452	| const blocksPerRound = this.roundInfo.length;
		453	| const currentRoundIndex = this.roundInfo.current;
		454	| const blocksFinishedInCurrentRound =
		455	| this.latestBlockNumber - this.roundInfo.first;
		457	| const estBlocksV1 =
		458	| (whenExecutableRoundIndex - currentRoundIndex) * blocksPerRound;
		459	| const estBlocksV2 = estBlocksV1 - blocksFinishedInCurrentRound;
		460	| const estSeconds = estBlocksV2 * this.targetSecondsPerBlock;
		461	| if (estSeconds > 0) {
		462	| // if (new Date().getSeconds() % 5 <= 2) {
		463	| this.doCountdown(row.collator, estSeconds);
		464	| row.status = "TO_WAIT";
		465	| } else {
		466	| this.cleanCountdown(row.collator);
		467	| row.status = "TO_EXECUTE";
		470	| doCountdown(collator, s, startTimestamp) {
		471	| startTimestamp = startTimestamp || new Date().getTime();
		472	| const remainingSeconds =
		473	| s - parseInt((new Date().getTime() - startTimestamp) / 1000);
		474	| const days = Math.floor(remainingSeconds / 86400);
		475	| const hours = Math.floor((remainingSeconds % 86400) / 3600);
		476	| const minutes = Math.ceil((remainingSeconds % 3600) / 60);
		477	| const seconds = remainingSeconds - minutes * 60;
		479	| if (hours < 1 && minutes < 1 && seconds < 2) {
		480	| this.cleanCountdown(collator);
		481	| const findIndex = this.tableData.findIndex(
		482	| (v) => v.collator == collator
		484	| const currentRow = this.tableData[findIndex];
		485	| this.figureRevokeStatus(currentRow);
		486	| } else {
		487	| this.rowTimeFormatMap[collator] = {
		488	| estimatedTime: this.$moment()
		489	| .add(s, "seconds")
		490	| .format("YYYY-MM-DD HH:mm"),
		491	| timeLeft: `${days}days ${hours}hours ${minutes}minutes`,
		492	| days,
		493	| hours,
		494	| minutes,
		496	| if (!this.timerMap[collator]) {
		497	| this.timerMap[collator] = setInterval(() => {
		498	| this.doCountdown(collator, s, startTimestamp);
		499	| }, 10000);
		503	| cleanCountdown(collator) {
		504	| if (this.timerMap[collator]) {
		505	| clearInterval(this.timerMap[collator]);
		506	| this.timerMap[collator] = undefined;
		509	| getSafeStateConfig() {
		510	| getSafeStateConfig({
		511	| chainId: this.$store.state.global.currentChain.id,
		512	| }).then((d) => {
		513	| this.safeStateConfig = d;
		516	| getSafeStatus(v) {
		517	| if (
		518	| v.rank <
		519	| this.safeStateConfig.max *
		520	| this.safeStateConfig.collatorSafeStateThreshold
		521	| ) {
		522	| return "Safe";
		523	| } else if (v.rank > this.safeStateConfig.max) {
		524	| return "Pending";
		525	| } else {
		526	| return "Risk";
		529	| goToCollatorDetail(address) {
		530	| localStorage.setItem("routeParamsAddress", address);
		531	| this.$router.push({
		532	| name: "collatorDetail",
		580	| async doMetamaskRevoke(successFn, failFn) {
		581	| await this.getMoonBeamContract();
		582	| let tx;
		583	| try {
		584	| tx = await this.moonBeamContract.schedule_revoke_delegation(
		585	| this.currentRow.collator
		587	| } catch (error) {
		588	| this.loading = false;
		590	| tx.wait().then((receipt) => {
		591	| if (receipt && receipt.status == 1) {
		592	| successFn();
		593	| } else {
		594	| failFn();
		598	| async doMetamaskExecuteRevoke(successFn, failFn) {
		599	| await this.getMoonBeamContract();
		600	| let tx;
		601	| try {
		602	| tx = await this.moonBeamContract.execute_delegation_request(
		604	| this.currentRow.collator
		606	| } catch (error) {
		607	| this.loading = false;
		609	| tx.wait().then((receipt) => {
		610	| if (receipt && receipt.status == 1) {
		611	| successFn();
		612	| } else {
		613	| failFn();
		617	| async doMetamaskCancelRevoke(successFn, failFn) {
		618	| await this.getMoonBeamContract();
		619	| let tx;
		620	| try {
		621	| tx = await this.moonBeamContract.cancel_delegation_request(
		622	| this.currentRow.collator
		624	| } catch (error) {
		625	| this.loading = false;
		627	| tx.wait().then((receipt) => {
		628	| if (receipt && receipt.status == 1) {
		629	| successFn();
		630	| } else {
		631	| failFn();
		637	| const successFn = () => {
		639	| const findIndex = this.tableData.findIndex(
		640	| (v) => v.collator == this.currentRow.collator
		642	| const currentRow = this.tableData[findIndex];
		643	| this.figureRevokeStatus(currentRow);
		644	| this.loading = false;
		646	| const failFn = () => {
		647	| this.loading = false;
		650	| if (
		651	| !this.$utils.ifSupportPolkadot(
		652	| this.$store.state.global.currentChain.network
		654	| ) {
		655	| this.doMetamaskRevoke(successFn, failFn);
		656	| return;
		659	| .scheduleRevokeDelegation(this.currentRow.collator)
		671	| successFn();
		673	| failFn();
		687	| const successFn = () => {
		689	| this.$eventBus.emit("updateSupportWalletFreeBalance");
		690	| this.getTableData();
		691	| this.refreshTopPage();
		693	| const failFn = () => {
		697	| if (
		698	| !this.$utils.ifSupportPolkadot(
		699	| this.$store.state.global.currentChain.network
		701	| ) {
		702	| this.doMetamaskExecuteRevoke(successFn, failFn);
		703	| return;
		708	| this.currentRow.collator
		721	| successFn();
		723	| failFn();
		737	| const successFn = () => {
		739	| const findIndex = this.tableData.findIndex(
		740	| (v) => v.collator == this.currentRow.collator
		742	| if (findIndex !== -1) {
		743	| this.tableData[findIndex].status = "TO_REVOKE";
		747	| const failFn = () => {
		752	| !this.$utils.ifSupportPolkadot(
		753	| this.$store.state.global.currentChain.network
		756	| this.doMetamaskCancelRevoke(successFn, failFn);
		757	| return;
		760	| .cancelDelegationRequest(this.currentRow.collator)
		770	| successFn();
		772	| failFn();
		786	| this.$refs.DelegateDrawerRef.init(this.currentRow.collator);
		788	| handleExceute(row) {
		946	| .Risk {
		949	| .Safe {
		952	| .Pending {
		953	| color: #10a7e4;
		962	| .Exceute {

	Unique lines in second:
		6	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		8	| <div class="top">jetblue-125</div>
		10	| <span class="safe">Safe</span>
		11	| <!-- <span class="risk">Risk</span> -->
		12	| <span class="delegated">Delegated</span>
		19	| <el-table-column :prop="v.prop" :label="v.name" :width="v.width" />
		75	| <span class="common-table-option" @click="handleDelegate(scope.row)"
		80	| v-if="scope.$index == 0"
		85	| <span v-if="scope.$index == 1" class="common-table-option excute">
		86	| <span @click="handleExcute(scope.row)"> Excute </span>
		103	| v-if="scope.$index == 2"
		109	| <img src="@/assets/images/home/keyboard_arrow_down.png" alt="" />
		110	| <span class="text">
		111	| <span class="num">12</span>
		113	| <span class="num">00</span>
		115	| <span class="num">08</span>
		124	| <span class="value">289</span>
		128	| <span class="value">2021-12-20 17:58</span>
		132	| <span class="value">20days 20hours 58minutes</span>
		153	| <DelegateDrawer ref="DelegateDrawerRef" />
		171	| {
		173	| prop: "state",
		176	| { name: "Self Stake", prop: "state", "min-width": "140" },
		177	| { name: "Delegator Stake", prop: "state", "min-width": "140" },
		178	| {
		180	| prop: "state",
		183	| {
		185	| prop: "state",
		190	| prop: "state",
		195	| prop: "state",
		208	| tableData: [
		210	| date: "2016-05-03",
		211	| name: "Tom",
		212	| state: "California",
		213	| city: "Los Angeles",
		214	| address: "Los Angeles",
		215	| zip: "CA 90036",
		218	| date: "2016-05-03",
		219	| name: "Tom",
		220	| state: "California",
		221	| city: "Los Angeles",
		222	| address: "Los Angeles",
		223	| zip: "CA 90036",
		226	| date: "2016-05-03",
		227	| name: "Tom",
		228	| state: "California",
		229	| city: "Los Angeles",
		230	| address: "Los Angeles",
		231	| zip: "CA 90036",
		234	| date: "2016-05-03",
		235	| name: "Tom",
		236	| state: "California",
		237	| city: "Los Angeles",
		238	| address: "Los Angeles",
		239	| zip: "CA 90036",
		242	| date: "2016-05-03",
		243	| name: "Tom",
		244	| state: "California",
		245	| city: "Los Angeles",
		246	| address: "Los Angeles",
		247	| zip: "CA 90036",
		250	| date: "2016-05-03",
		251	| name: "Tom",
		252	| state: "California",
		253	| city: "Los Angeles",
		254	| address: "Los Angeles",
		255	| zip: "CA 90036",
		258	| date: "2016-05-03",
		259	| name: "Tom",
		260	| state: "California",
		261	| city: "Los Angeles",
		262	| address: "Los Angeles",
		263	| zip: "CA 90036",
		266	| date: "2016-05-03",
		267	| name: "Tom",
		268	| state: "California",
		269	| city: "Los Angeles",
		270	| address: "Los Angeles",
		271	| zip: "CA 90036",
		301	| // this.currentRow = row;
		302	| this.currentRow = {
		303	| address: "67D6ecyNhnAzZqgRbxr3MdGnxB9Bw8VadMhjpLAYB3wf5Pq6",
		350	| .scheduleRevokeDelegation(this.currentRow.address)
		379	| this.currentRow.address
		407	| .cancelDelegationRequest(this.currentRow.address)
		432	| this.$refs.DelegateDrawerRef.init(this.currentRow);
		434	| handleExcute(row) {
		439	| // this.currentRow = row;
		440	| this.currentRow = {
		441	| address: "67D6ecyNhnAzZqgRbxr3MdGnxB9Bw8VadMhjpLAYB3wf5Pq6",
		520	| img {
		595	| .risk {
		605	| .excute {


Partially similar files found. First length 533, Second length 483,  The files are 58% identicalThe files differ in 101 lines:
	./resources/european/web/src/views/myStake/Timemachine/RewardTable.vue
	./resources/asia/ui/src/views/myStake/Timemachine/RewardTable.vue
	Unique lines in first:
		1	| <a-spin style="width: 100%" :loading="loading">
		7	| <IdentityWrap :address="scope.row.collator">
		8	| <template #default="{ identity }">
		9	| <IdentityIcon
		10	| class="hover-item"
		11	| @click="goToCollatorDetail(scope.row.collator)"
		12	| :identity="identity"
		13	| :address="scope.row.collator"
		14	| ></IdentityIcon>
		15	| <a-tooltip :content="scope.row.collator" placement="top">
		16	| <span
		17	| class="hover-primary"
		18	| style="margin-left: 8px"
		19	| @click="goToCollatorDetail(scope.row.collator)"
		20	| >{{
		21	| identity.display
		22	| ? identity.display
		23	| : $utils.shorterAddress(scope.row.collator)
		24	| }}</span
		25	| >
		26	| </a-tooltip>
		28	| </IdentityWrap>
		32	| <el-table-column
		33	| prop="realroundindex"
		34	| label="Staked Round"
		35	| min-width="120"
		36	| />
		37	| <el-table-column
		38	| prop="issueroundindex"
		39	| label="Issued Round"
		40	| min-width="120"
		41	| />
		42	| <el-table-column
		43	| prop="issueBlock"
		44	| label="Issued Block"
		45	| min-width="120"
		46	| />
		47	| <el-table-column label="Amount" min-width="120">
		49	| {{ $utils.roundNumber(scope.row.balance, 4) }}
		52	| <el-table-column label="Timestamp" min-width="160">
		54	| {{ $moment(scope.row.timestamp).format("YYYY-MM-DD HH:mm:ss") }}
		58	| <div class="pagination-wrap">
		59	| <a-pagination
		60	| @change="getTableData"
		61	| :total="totalCount"
		62	| v-model:current="pageIndex"
		63	| v-model:page-size="pageSize"
		64	| show-total
		65	| show-jumper
		66	| />
		69	| </a-spin>
		73	| import IdentityWrap from "@/components/IdentityWrap";
		74	| import IdentityIcon from "@/components/IdentityIcon";
		75	| import { getDelegatorRewardHistory } from "@/api/staking";
		78	| props: ["selectCollator", "selectRound"],
		79	| components: {
		80	| IdentityWrap,
		81	| IdentityIcon,
		85	| loading: false,
		86	| pageIndex: 1,
		87	| pageSize: 10,
		88	| totalCount: 0,
		99	| tableData: [],
		102	| created() {
		103	| this.initPage();
		105	| watch: {
		106	| selectCollator() {
		107	| this.getTableData();
		109	| selectRound() {
		110	| this.getTableData();
		112	| "$store.state.global.currentChain"() {
		113	| this.initPage();
		115	| "$store.state.global.metamaskWallet"() {
		116	| this.initPage();
		118	| "$store.state.global.polkadotWallet"() {
		119	| this.initPage();
		122	| methods: {
		123	| initPage() {
		124	| this.getTableData();
		126	| getTableData() {
		127	| this.loading = true;
		128	| getDelegatorRewardHistory({
		129	| pageSize: this.pageSize,
		130	| pageIndex: this.pageIndex,
		131	| orderBys: [],
		132	| chainId: this.$store.state.global.currentChain.id,
		133	| delegatorAccount: this.$store.getters.currentChainWalletAddress,
		134	| collator: this.selectCollator,
		135	| roundindex: this.selectRound,
		136	| }).then((d) => {
		137	| this.loading = false;
		138	| this.tableData = d.list;
		139	| this.totalCount = d.totalCount;
		140	| });
		142	| goToCollatorDetail(address) {
		143	| localStorage.setItem("routeParamsAddress", address);
		144	| this.$router.push({
		145	| name: "collatorDetail",
		146	| });
		163	| .pagination-wrap {
		166	| justify-content: flex-end;

	Unique lines in second:
		6	| <img src="@/assets/images/moonbeam/moonbeam.png" alt="" />
		7	| <span>binance account</span>
		11	| <el-table-column prop="state" label="Staked Round" min-width="120" />
		12	| <el-table-column prop="state" label="Issued Round" min-width="120" />
		13	| <el-table-column prop="state" label="Issued Block" min-width="120" />
		14	| <el-table-column prop="state" label="Amount" min-width="120" />
		15	| <el-table-column prop="state" label="Timestamp" min-width="120" />
		34	| tableData: [
		35	| {
		36	| date: "2016-05-03",
		37	| name: "Tom",
		38	| state: "California",
		39	| city: "Los Angeles",
		40	| address: "Los Angeles",
		41	| zip: "CA 90036",
		43	| {
		44	| date: "2016-05-03",
		45	| name: "Tom",
		46	| state: "California",
		47	| city: "Los Angeles",
		48	| address: "Los Angeles",
		49	| zip: "CA 90036",
		51	| {
		52	| date: "2016-05-03",
		53	| name: "Tom",
		54	| state: "California",
		55	| city: "Los Angeles",
		56	| address: "Los Angeles",
		57	| zip: "CA 90036",
		59	| {
		60	| date: "2016-05-03",
		61	| name: "Tom",
		62	| state: "California",
		63	| city: "Los Angeles",
		64	| address: "Los Angeles",
		65	| zip: "CA 90036",
		67	| {
		68	| date: "2016-05-03",
		69	| name: "Tom",
		70	| state: "California",
		71	| city: "Los Angeles",
		72	| address: "Los Angeles",
		73	| zip: "CA 90036",
		75	| {
		76	| date: "2016-05-03",
		77	| name: "Tom",
		78	| state: "California",
		79	| city: "Los Angeles",
		80	| address: "Los Angeles",
		81	| zip: "CA 90036",
		83	| {
		84	| date: "2016-05-03",
		85	| name: "Tom",
		86	| state: "California",
		87	| city: "Los Angeles",
		88	| address: "Los Angeles",
		89	| zip: "CA 90036",
		91	| {
		92	| date: "2016-05-03",
		93	| name: "Tom",
		94	| state: "California",
		95	| city: "Los Angeles",
		96	| address: "Los Angeles",
		97	| zip: "CA 90036",
		99	| ],
		102	| methods: {},
		135	| img {
		254	| img {


Partially similar files found. First length 15, Second length 13,  The files are 56% identicalThe files differ in 5 lines:
	./resources/european/service/src/parachain/staking/base/staking-base.module.ts
	./resources/asia/service/src/parachain/staking/base/staking-base.module.ts
	Unique lines in first:
		4	| import { MoonbeamStakingBaseService } from "./service/moonbeam-staking-base-service";
		5	| import { MoonriverStakingBaseService } from "./service/moonriver-staking-base-service";
		10	| max: 200
		13	| providers: [StakingBaseService, BifrostStakingBaseService, MoonbeamStakingBaseService, MoonriverStakingBaseService],
		14	| exports: [StakingBaseService, BifrostStakingBaseService, MoonbeamStakingBaseService, MoonriverStakingBaseService],

	Unique lines in second:
		8	| ttl: 15,
		11	| providers: [StakingBaseService, BifrostStakingBaseService],
		12	| exports: [StakingBaseService, BifrostStakingBaseService],


Partially similar files found. First length 448, Second length 329,  The files are 47% identicalThe files differ in 134 lines:
	./resources/european/web/src/views/myStake/Timemachine/index.vue
	./resources/asia/ui/src/views/myStake/Timemachine/index.vue
	Unique lines in first:
		7	| <a-spin style="width: 100%; height: 310px" :loading="loading">
		8	| <v-chart
		9	| v-if="chart1Arr.length"
		10	| class="chart"
		11	| :option="lineChartOption"
		13	| </a-spin>
		18	| <span class="text"> Rewards from My Delegated Collators </span>
		20	| <a-spin style="width: 100%; height: 310px" :loading="loading">
		21	| <v-chart
		22	| v-if="chart2Arr.length"
		23	| class="chart"
		24	| :option="barChartOption"
		34	| @click="changeTab(1)"
		41	| @click="changeTab(2)"
		47	| <a-select
		48	| v-model="selectCollator"
		49	| allow-clear
		50	| placeholder="Select Collator"
		52	| <a-option v-for="(v, i) in collatorList" :key="i" :value="v.value">{{
		53	| v.label
		54	| }}</a-option>
		56	| <a-select v-model="selectRound" allow-clear placeholder="Select Round">
		57	| <a-option v-for="(v, i) in roundList" :key="i" :value="v">{{
		58	| v
		59	| }}</a-option>
		63	| <StakingTable
		64	| :selectCollator="selectCollator"
		65	| :selectRound="selectRound"
		66	| v-if="currentTab == 1"
		68	| <RewardTable
		69	| :selectCollator="selectCollator"
		70	| :selectRound="selectRound"
		71	| v-if="currentTab == 2"
		77	| import {
		78	| timeMachineRewardsStat,
		79	| timeMachineActionSelect,
		80	| timeMachineRewardSelect,
		81	| } from "@/api/staking";
		82	| import StakingTable from "./StakingTable";
		83	| import RewardTable from "./RewardTable";
		91	| loading: false,
		92	| selectCollator: "",
		93	| selectRound: "",
		94	| collatorList: [],
		95	| roundList: [],
		96	| chart1Arr: [],
		97	| chart2Arr: [],
		101	| created() {
		102	| this.initPage();
		104	| watch: {
		105	| "$store.state.global.currentChain"() {
		106	| this.initPage();
		108	| "$store.state.global.metamaskWallet"() {
		109	| this.initPage();
		111	| "$store.state.global.polkadotWallet"() {
		112	| this.initPage();
		115	| computed: {
		116	| lineChartOption() {
		124	| data: this.chart1Arr.map((v) => "Round" + v.roundIndex),
		170	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${
		171	| params[0].name
		172	| }</div>
		173	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${this.$utils.roundNumber(
		174	| params[0].value,
		175	| 4
		176	| )}</div>
		208	| data: this.chart1Arr.map((v) => v.reward),
		213	| barChartOption() {
		231	| data: this.chart2Arr.map((v) => v.display),
		259	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${
		260	| params[0].name
		261	| }</div>
		262	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${this.$utils.roundNumber(
		263	| params[0].value,
		264	| 4
		265	| )}</div>
		275	| data: this.chart2Arr.map((v) => v.reward),
		281	| methods: {
		282	| changeTab(tabIndex) {
		283	| this.currentTab = tabIndex;
		284	| this.selectCollator = "";
		285	| this.selectRound = "";
		286	| this.getSelectData();
		288	| getSelectData() {
		289	| this.collatorList = [];
		290	| this.roundList = [];
		291	| let request;
		292	| if (this.currentTab == 1) {
		293	| request = timeMachineActionSelect;
		294	| } else {
		295	| request = timeMachineRewardSelect;
		297	| request({
		298	| chainId: this.$store.state.global.currentChain.id,
		299	| delegator: this.$store.getters.currentChainWalletAddress,
		300	| }).then(async (d) => {
		301	| const _collatorList = d.collators;
		302	| const collatorList = [];
		303	| for (const v of _collatorList) {
		304	| const { identity } = await this.$utils.loadAddressIdentityAsync(v);
		305	| const label = identity.display
		306	| ? identity.display
		307	| : this.$utils.shorterAddress(v);
		308	| collatorList.push({
		309	| value: v,
		310	| label,
		311	| });
		313	| this.collatorList = collatorList;
		314	| this.roundList = d.rounds;
		315	| });
		317	| getChartData() {
		318	| this.loading = true;
		319	| timeMachineRewardsStat({
		320	| chainId: this.$store.state.global.currentChain.id,
		321	| delegator: this.$store.getters.currentChainWalletAddress,
		322	| }).then(async (d) => {
		323	| this.chart1Arr = d.rewardByRoundIndex;
		324	| for (const v of d.rewardByCollator) {
		325	| const { identity } = await this.$utils.loadAddressIdentityAsync(
		326	| v.collator
		327	| );
		328	| v.display = identity.display
		330	| : this.$utils.shorterAddress(v.collator);
		332	| this.chart2Arr = d.rewardByCollator;
		333	| this.loading = false;
		334	| });
		336	| initPage() {
		337	| this.getChartData();
		338	| this.getSelectData();
		351	| :deep(.arco-spin-mask) {
		352	| background: transparent;
		355	| box-sizing: border-box;
		356	| min-height: 374px;
		383	| min-height: 374px;
		405	| height: 100%;

	Unique lines in second:
		6	| <a-tooltip content="This is tooltip content">
		8	| class="icon"
		9	| src="@/assets/images/moonbeam/Group_47.png"
		14	| <v-chart class="chart" :option="lineChartOption" />
		18	| <span class="text"> My Mostly-staking collators </span>
		19	| <a-tooltip content="This is tooltip content">
		21	| class="icon"
		27	| <v-chart class="chart" :option="barChartOption" />
		35	| @click="currentTab = 1"
		42	| @click="currentTab = 2"
		48	| <a-select allow-clear placeholder="Select Collator">
		49	| <a-option>Beijing</a-option>
		50	| <a-option>Shanghai</a-option>
		51	| <a-option>Guangzhou</a-option>
		53	| <a-select allow-clear placeholder="Select Round">
		54	| <a-option>Beijing</a-option>
		55	| <a-option>Shanghai</a-option>
		56	| <a-option>Guangzhou</a-option>
		60	| <StakingTable v-if="currentTab == 1" />
		61	| <RewardTable v-if="currentTab == 2" />
		66	| import StakingTable from "./StakingTable.vue";
		67	| import RewardTable from "./RewardTable.vue";
		76	| lineChartOption: {
		83	| data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
		129	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${params[0].name}</div>
		130	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${params[0].value}</div>
		146	| {
		150	| {
		162	| data: [120, 200, 150, 80, 70, 110, 130],
		166	| barChartOption: {
		183	| data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
		211	| <div style="font-weight: 500;font-size: 12px;line-height: 20px;letter-spacing: -0.02em;color: #A3AED0;">${params[0].name}</div>
		212	| <div style="font-weight: 500;font-size: 20px;line-height: 28px;color: #1B2559;margin-top:1px;">${params[0].value}</div>
		222	| data: [120, 200, 150, 80, 70, 110, 130],
		260	| height: 310px;


Partially similar files found. First length 482, Second length 351,  The files are 41% identicalThe files differ in 163 lines:
	./resources/european/service/src/parachain/staking/task/service/collator-service.ts
	./resources/asia/service/src/parachain/staking/task/service/collator-service.ts
	Unique lines in first:
		3	| import { StatCollator } from "src/common/entity/StakingPortalStat/StatCollator.entity";
		6	| import { BaseService } from "./base-service";
		9	| export class CollatorService extends BaseService {
		10	| constructor(private readonly httpService: HttpService) {
		11	| super();
		29	| let records = await DbManager.PORTAL.statDelegatorRepository.find({
		30	| where: { chainId, collator },
		39	| async getStatCollators(
		40	| chain: ChainConnector,
		44	| const { collatorData } = shareData;
		46	| this.doRank("totalStake", "totalStakeRank", collatorData);
		47	| await this.batchCalStake(chain, shareData);
		48	| await this.batchCalMinBond(chain, shareData);
		49	| await this.batchCalReward4Collators(shareData);
		50	| await this.injectRewards4RealtimeCollatorState(baseService, shareData);
		51	| await this.batchCalRps(baseService, shareData);
		52	| await this.batchCalBlock(baseService, chain, shareData);
		54	| this.doRank(
		55	| `avgBlockIn${roundSize}R`,
		56	| `avgBlockRankIn${roundSize}R`,
		57	| collatorData
		60	| await this.batchCalApr(baseService, chain, shareData);
		61	| this.doRank("apr", "aprRank", collatorData);
		63	| return collatorData;
		66	| // if the Top Delegator List has not been full yet (capacity of the list
		67	| // is an constant defined in parachain.constant.maxTopDelegationsPerCandidate),
		68	| // it would be higher than the last one on the list,
		69	| // or it would be the default value of each network’s.
		70	| private batchCalMinBond(chain: ChainConnector, shareData) {
		71	| const defaultMinBondValue = chain.defaultValues.minBond;
		73	| const maxTopDelegationsPerCandidate =
		74	| chain.api.consts.parachainStaking.maxTopDelegationsPerCandidate;
		77	| const row = collatorDataMap[collator];
		79	| row.minBond = defaultMinBondValue;
		81	| const tdr = shareData.topDelegators[i];
		82	| if (tdr.delegations < 1) continue;
		84	| const last = tdr.delegations[tdr.delegations.length - 1].amount;
		85	| if (tdr.delegations.length >= maxTopDelegationsPerCandidate) {
		86	| row.minBond = last + 1;
		88	| row.minBond = Math.max(defaultMinBondValue, last);
		93	| private async batchCalStake(chain: ChainConnector, shareData) {
		94	| const { collators, collatorDataMap, realtimeCollatorState } = shareData;
		95	| const selfStakeDataMap = {};
		96	| // rawData
		97	| //   .map((it) => it.toJSON())
		98	| realtimeCollatorState.forEach((it: any, i) => {
		99	| selfStakeDataMap[collators[i]] = chain
		100	| .formatWithDecimals(it.bond)
		104	| for (const collator of collators) {
		105	| collatorDataMap[collator].selfStake = selfStakeDataMap[collator] || 0;
		106	| collatorDataMap[collator].delegatorStake =
		107	| collatorDataMap[collator].totalStake -
		108	| collatorDataMap[collator].selfStake;
		112	| private async batchCalReward4Collators(shareData) {
		113	| const { chainId, collators, collatorDataMap, taskStartedAt } = shareData;
		116	| collatorDataMap[collator].latestReward = 0;
		117	| collatorDataMap[collator].totalReward = 0;
		120	| const existedStatCollators =
		121	| await DbManager.PORTAL.statCollatorRepository.find({
		122	| where: {
		124	| },
		126	| // //TODO TEST
		127	| // const existedStatCollators = [];
		128	| const startTime = existedStatCollators.length
		129	| ? existedStatCollators[0].timestamp
		130	| : null;
		131	| const endTime = taskStartedAt;
		133	| const newCollators = [];
		134	| const oldCollators = [];
		135	| // grouping and padding the previous reward
		137	| const matched = existedStatCollators.filter(
		138	| (it) => it.collator === collator
		139	| )[0];
		141	| row.totalReward = Number(row.totalReward) || 0;
		142	| if (matched) {
		143	| oldCollators.push(row);
		144	| row.totalReward = matched.totalReward - 0 || 0;
		145	| row.latestReward = matched.latestReward || 0;
		147	| newCollators.push(row);
		150	| const process = async (incre, data) => {
		151	| const rewards = await this.getReward4Collators({
		153	| collators: data.map((it) => it.collator),
		154	| startTime: incre ? startTime : null,
		155	| endTime,
		157	| rewards.forEach((reward) => {
		158	| const row = collatorDataMap[reward.collator];
		159	| row.totalReward = reward.reward + (incre ? row.totalReward : 0);
		160	| row.latestReward = reward.latestReward;
		163	| if (newCollators.length) {
		164	| await process(false, newCollators);
		166	| if (oldCollators.length) {
		167	| await process(true, oldCollators);
		171	| // MAYBE array_agg CAN BE OPTIMIZED FURTHUR BY SOME WINDOW FUNCTIONS LIKE FIRST_VAL, LAST_VAL, ETC.
		172	| // https://stackoverflow.com/questions/25170215/get-values-from-first-and-last-row-per-group
		173	| async getReward4Collators({ chainId, collators, startTime, endTime }) {
		174	| if (!collators.length) {
		175	| return [];
		177	| const startTs = this.getTsString(startTime);
		178	| const endTs = this.getTsString(endTime || new Date());
		180	| const query = `SELECT
		181	| account AS collator,
		183	| max(realroundindex) AS max_issueroundindex,
		184	| (array_agg(balance ORDER BY issueblock DESC))[1] AS latest_reward
		186	| collator_reward_histories
		187	| WHERE account in ( '${collators.toString().replace(/,/g, "','")}')
		190	| GROUP BY account`;
		191	| //   max(issueblock) AS latest_reward_block,
		199	| reward: row.reward - 0 || 0,
		200	| // latestRewardBlock: row.latest_reward_block - 0,
		201	| latestReward: row.latest_reward - 0,
		231	| let avg_blocks_per_round =
		232	| mapUser2Row[realtimeCollatorState[i].id].avgBlockIn10R;
		289	| async injectRewards4RealtimeCollatorState(
		293	| const { realtimeCollatorState } = shareData;
		417	| async batchCalBlock(
		435	| // current block
		436	| const findCurrent = blocks.find(
		438	| sv.account === collator && Number(sv.roundIndex) === round.current
		441	| collatorDataMap[collator].currentBlock = findCurrent
		442	| ? findCurrent.blocks_count - 0
		443	| : 0;
		445	| // avg block
		468	| async batchCalRps(baseService: StakingBaseService, shareData) {
		469	| const { chainId, collatorDataMap, realtimeCollatorState, round } =
		470	| shareData;
		471	| const startRoundIndex = round.current - 11 - 0;
		473	| const stakeRecords = (
		474	| await baseService.atStake({
		478	| collatorAccount: null,
		480	| ).stakes;
		481	| for (const v of realtimeCollatorState) {
		482	| const historyRps = [];
		484	| //debugger;
		485	| const findTop = v.historyNominatorTotalReward.find(
		486	| (sv) => Number(sv.roundIndex) == i
		488	| const findBottom = stakeRecords.find(
		489	| (sv) => Number(sv.roundIndex) == i
		492	| let rps = new BigNumber(0);
		493	| if (findTop && findBottom) {
		494	| const top = findTop.reward as BigNumber;
		495	| const bottom = findBottom.nominatorsStake as number;
		496	| if (bottom > 0 && top.comparedTo(0) > -1) {
		497	| rps = top.dividedBy(bottom);
		500	| historyRps.push({
		502	| rps,
		505	| const row = collatorDataMap[v.id] as StatCollator;
		506	| row.rpsHis = JSON.stringify(historyRps);
		507	| row.avgRps = historyRps
		508	| .map((i) => i.rps)
		509	| .reduce((i, ii) => i.plus(ii))
		510	| .dividedBy(historyRps.length)
		512	| // this.getAverageRPS(historyRps);
		513	| row.minRps = Math.min.apply(
		514	| null,
		515	| historyRps.map((sv) => sv.rps.toNumber())
		517	| row.maxRps = Math.max.apply(
		518	| null,
		519	| historyRps.map((sv) => sv.rps.toNumber())
		521	| // 标准差
		522	| let topSum = BigNumber(0);
		523	| historyRps.forEach((rps) => {
		524	| topSum = topSum.plus(rps.rps.minus(row.avgRps).exponentiatedBy(2));
		526	| row.rpsScore = topSum.dividedBy(10).sqrt().toNumber();

	Unique lines in second:
		7	| export class CollatorService {
		8	| constructor(private readonly httpService: HttpService) {}
		25	| let records = await DbManager.get(chainId).statDelegatorRepository.find({
		26	| where: { collator },
		28	| const dataMap = {};
		35	| async statDelegatorsReward({
		37	| collator,
		38	| delegators,
		39	| startTime,
		40	| endTime
		41	| }) {
		43	| const getTsString = (date) => {
		44	| return !date
		45	| ? null
		46	| : date.getFullYear() +
		47	| "-" +
		48	| String(date.getMonth() + 1).padStart(2, "0") +
		49	| "-" +
		50	| String(date.getDate()).padStart(2, "0") +
		51	| " " +
		52	| String(date.getHours()).padStart(2, "0") +
		53	| ":" +
		54	| String(date.getMinutes()).padStart(2, "0") +
		55	| ":" +
		56	| String(date.getSeconds()).padStart(2, "0");
		58	| const startTs = getTsString(startTime);
		59	| const endTs = getTsString(endTime || new Date());
		61	| let query = `SELECT
		62	| account,
		63	| collator,
		65	| max(realroundindex) AS latest_reward_block
		67	| nominator_reward_detail_histories
		68	| WHERE
		69	| collator = '${collator}'
		70	| AND account IN ( '${delegators.toString().replace(/,/g, "','")}' )
		73	| GROUP BY collator, account
		74	| ORDER BY collator, account`;
		82	| delegator: row.account,
		83	| reward: (row.reward - 0) || 0,
		84	| latestRewardBlock: row.latest_reward_block - 0,
		87	| for (const row of result) {
		88	| const data = await DbManager.get(chainId).rhRepository.query(
		89	| `SELECT balance AS reward FROM nominator_reward_detail_histories
		90	| WHERE collator = '${collator}' AND account = '${row.delegator}' AND realroundindex=${row.latestRewardBlock}
		91	| ORDER BY timestamp DESC LIMIT 1 `
		93	| row.latestReward = data[0].reward;
		100	| // private getStakeRank(row, collator) {
		101	| //   const findIndex = row.allNominators.findIndex(
		102	| //     (v) => v.pk === collator || v.owner === collator
		103	| //   );
		104	| //   return findIndex + 1;
		105	| // }
		107	| // async fillReward(baseService: StakingBaseService, shareData) {
		108	| //   const mapUser2Row = shareData.collatorDataMap;
		109	| //   const rs = await baseService.getCollatorTotalReward({
		110	| //     chainId: shareData.chainId,
		111	| //     collators: shareData.collators,
		112	| //   });
		113	| //   if (rs && rs.collators && rs.collators.length)
		114	| //     for (let i = 0; i < rs.collators.length; i++) {
		115	| //       const v = rs.collators[i];
		116	| //       mapUser2Row[v.account].totalReward = v.reward;
		117	| //       mapUser2Row[v.account].latestReward =
		118	| //         await this.getCollatorLatestReward({
		119	| //           collator: v.account,
		120	| //           chainId: shareData.chainId,
		121	| //         });
		122	| //     }
		126	| baseService: StakingBaseService,
		127	| cc: ChainConnector,
		128	| shareData
		147	| let avg_blocks_per_round = stake;
		148	| console.log(
		167	| await this.initRewards(
		168	| baseService,
		169	| accounts,
		170	| realtimeCollatorState,
		197	| // const multiCandidateInfos =
		198	| //   await cc.api.query.parachainStaking.candidateInfo.multi(
		199	| //     data.map((it) => it.collator)
		200	| //   );
		201	| //   // totalCounted
		203	| // return data;
		216	| private async initRewards(
		217	| baseService: StakingBaseService,
		218	| accounts,
		219	| realtimeCollatorState,
		227	| realtimeCollatorState.forEach((v) => {
		229	| for (let i = startRoundIndex; i <= endRoundIndex; i++) {
		236	| arr.push({
		237	| roundIndex: i,
		238	| reward: BigNumber(find.reward),
		241	| arr.push({
		243	| reward: BigNumber(0),
		257	| realtimeCollatorState.forEach((v) => {
		345	| async batchCalAvgBlock(


Partially similar files found. First length 299, Second length 460,  The files are 39% identicalThe files differ in 208 lines:
	./resources/european/service/src/parachain/staking/task/stat-data-sync-task.ts
	./resources/asia/service/src/parachain/staking/task/stat-data-sync-task.ts
	Unique lines in first:
		0	| import { Controller, Get, Injectable, Query } from "@nestjs/common";
		4	| import { StatCollator } from "src/common/entity/StakingPortalStat/StatCollator.entity";
		5	| import { StatDelegator } from "src/common/entity/StakingPortalStat/StatDelegator.entity";
		6	| import { StatNetwork } from "src/common/entity/StakingPortalStat/StatNetwork.entity";
		8	| import { StatNetworkRequest } from "src/viewModel/staking/portal/StatNetworkRequest";
		16	| import { StatDelegatorService } from "./service/delegator-service";
		27	| private collatorService: CollatorService,
		28	| private delegatorService: StatDelegatorService
		33	| getElapsedTimeInSec(date = this.taskStartedAt) {
		34	| if (!date) return -1;
		40	| async doCal(chainId: string, force=false) {
		41	| // skip cron task if running in my local env.
		43	| if (
		44	| !force &&
		45	| process.env.USER === "klaus" &&
		46	| process.env.TERM_PROGRAM === "vscode"
		50	| } catch (e) {}
		63	| if (chainId && network.info.id !== chainId) {
		64	| continue;
		66	| await this.doSyncByNetwork(network);
		80	| private async doSyncByNetwork(network: ParachainNetwork) {
		81	| const startTime = new Date();
		93	| const collators = await this.collatorService.getStatCollators(
		99	| const delegators = await this.delegatorService.getStatDelegator(
		100	| network,
		110	| `task stat-sync  for ${
		112	| } quited unexpectly, task consumed ${this.getElapsedTimeInSec()}s`,
		117	| `task stat-sync for ${
		119	| } done: cost ${this.getElapsedTimeInSec(startTime)}s`
		130	| const queryRunner = DbManager.PORTAL.dbConnect.createQueryRunner();
		132	| if (!data || data.length < 1) return;
		136	| // truncate enjoyed the high performance but also sacrifice the transaction
		137	| queryRunner.manager.query(
		138	| `delete from ${tableName} where chain_id='${network.info.id}'`
		148	| const pageSize = 2000;
		149	| if (data.length > pageSize) {
		150	| const paginate = (array, pageSize, pageNumber) => {
		151	| return array.slice(
		152	| (pageNumber - 1) * pageSize,
		153	| pageNumber * pageSize
		156	| let page = 1;
		157	| let realData = null;
		158	| while ((realData = paginate(data, pageSize, page++)).length) {
		159	| await queryRunner.manager.insert(entityClzRef, realData);
		161	| `saving data...${tableName} process: ${Math.min(
		162	| (page - 1) * pageSize,
		163	| data.length
		164	| )}/${data.length} network: ${network.info.id}`
		171	| `save finished: ${data.length} records network: ${
		209	| c.chainId = chainId;
		210	| c.collator = chain.formatAccountAddr(it.owner);
		222	| const round = (await baseService.getCurrentRoundInfo(chainId)) as {
		229	| // todo seems unused
		240	| taskStartedAt: this.taskStartedAt,
		286	| delegator.owner = chain.formatAccountAddr(delegator.owner);
		320	| async test(@Query() request: StatNetworkRequest) {
		321	| await this.cron.doCal(request.chainId, true);
		322	| return `task is running ${this.cron.getElapsedTimeInSec()}s ago`;

	Unique lines in second:
		0	| import { Controller, Get, Injectable } from "@nestjs/common";
		2	| import BigNumber from "bignumber.js";
		5	| import { ChainUtils } from "src/common/chain/chain-utils";
		6	| import { StatCollator } from "src/common/entity/StakingModule/StatCollator.entity";
		7	| import { StatDelegator } from "src/common/entity/StakingModule/StatDelegator.entity";
		8	| import { StatNetwork } from "src/common/entity/StakingModule/StatNetwork.entity";
		27	| private collatorService: CollatorService
		32	| private getElapsedTimeInSec(date = this.taskStartedAt) {
		33	| const now = new Date().getTime();
		38	| cal() {
		39	| //console.info("executed...");
		41	| this.doit();
		43	| // todo test code
		44	| // private
		45	| async doit() {
		67	| const collators = await this.getStatCollators(
		70	| shareData
		73	| const delegators = await this.getStatDelegator(network, shareData);
		93	| network: ParachainNetwork,
		98	| const queryRunner = DbManager.get(
		100	| ).dbConnect.createQueryRunner();
		105	| // truncate enjoyed the hight efficency but also sacrifice the transaction
		106	| // queryRunner.manager.query("truncate stat_network");
		107	| // queryRunner.manager.query("truncate stat_collator");
		108	| // queryRunner.manager.query("truncate stat_delegator");
		109	| //console.info('starting cleaning old data...');
		111	| // queryRunner.manager.query("delete from stat_network");
		112	| // queryRunner.manager.query("delete from stat_collator");
		113	| // queryRunner.manager.query("delete from stat_delegator");
		114	| queryRunner.manager.query(`delete from ${tableName}`);
		119	| //queryRunner.manager.query('truncate stat_delegator');
		124	| // let i = 0;
		125	| // for (const record of data) {
		126	| //   if (i++ % 100 === 0) {
		127	| //     this.logger.debug(
		128	| //       `saving process: ${i}/${data.length} network: ${
		129	| //         network.info.id
		130	| //       }, task elapsed ${this.getTaskElapsedTimeInSec()}s`
		131	| //     );
		133	| //   await queryRunner.manager.save(record);
		134	| // }
		137	| `save done: ${data.length} records network: ${
		161	| chain: ChainConnector,
		164	| const chainId = chain.network.id;
		175	| c.collator = ChainUtils.ss58transform_simple(it.owner, chain.network);
		187	| const round = (await chain.api.query.parachainStaking.round()).toJSON() as {
		194	| // const rewards = (
		195	| //   await baseService.getCollatorTotalReward({
		196	| //     chainId,
		197	| //     collators: collators,
		198	| //   })
		199	| // ).collators;
		202	| chainId,
		210	| chainId,
		223	| private async getStatCollators(
		225	| baseService: StakingBaseService,
		230	| const { collatorData } = shareData;
		232	| this.doRank("totalStake", "totalStakeRank", collatorData);
		233	| await this.batchCalStake(chain, shareData);
		234	| await this.batchCalMinBond(chain, shareData);
		235	| await this.batchCalReward(shareData);
		236	| await this.collatorService.batchCalApr(baseService, chain, shareData);
		237	| this.doRank("apr", "aprRank", collatorData);
		238	| await this.collatorService.batchCalAvgBlock(baseService, chain, shareData);
		239	| for (const roundSize of [1, 3, 4, 5, 8, 10]) {
		240	| this.doRank(
		241	| `avgBlockIn${roundSize}R`,
		242	| `avgBlockRankIn${roundSize}R`,
		243	| collatorData
		247	| // common datas
		248	| // for (const it of candidatePool) {
		249	| //   await this.calReward(baseService, chainId, it.owner);
		250	| //   it.minBond = 0;
		251	| //   //   collators.push(c);
		253	| return collatorData;
		275	| private async getStatDelegator(
		278	| ): Promise<StatDelegator[]> {
		279	| const { collators, topDelegators, bottomDelegators } = shareData;
		280	| const delegators = [] as StatDelegator[];
		281	| for (let i = 0; i < collators.length; i++) {
		282	| const collator = collators[i];
		283	| const tops = topDelegators[i].delegations;
		284	| const bottoms = bottomDelegators[i].delegations;
		285	| if (tops.length < 1) continue;
		287	| const existedRecords = await this.collatorService.getStatCollatorsHisBy({
		288	| chainId: network.info.id,
		289	| collator,
		292	| let rank = 1;
		293	| for (const groupData of [{ top: true, data: tops }, { data: bottoms }]) {
		294	| if (groupData.data.length < 1) continue;
		295	| const dataMap = {};
		296	| for (const d of groupData.data) {
		297	| const delegator = new StatDelegator();
		298	| delegator.collator = collator;
		299	| delegator.delegator = d.owner;
		300	| delegator.stake = d.amount;
		301	| delegator.rank = rank++;
		302	| delegator.isInTop = groupData.top ? 1 : 0;
		303	| delegator.reward = 0;
		304	| delegator.latestReward = 0;
		305	| delegator.latestRewardBlock = 0;
		306	| delegator.timestamp = this.taskStartedAt;
		307	| delegators.push(delegator);
		308	| dataMap[d.owner] = delegator;
		310	| // new records
		311	| await this.batchCalRewards4StatDelegators({
		312	| chainId: network.info.id,
		313	| dataMap,
		314	| collator,
		315	| existedRecords,
		316	| delegators: groupData.data
		317	| .filter((it) => !existedRecords[it.owner])
		318	| .map((it) => it.owner),
		319	| isIncre: false,
		321	| // increment
		322	| await this.batchCalRewards4StatDelegators({
		323	| chainId: network.info.id,
		324	| dataMap,
		325	| collator,
		326	| existedRecords,
		327	| delegators: groupData.data
		328	| .filter((it) => !!existedRecords[it.owner])
		329	| .map((it) => it.owner),
		330	| isIncre: true,
		334	| return delegators;
		337	| private async batchCalRewards4StatDelegators({
		339	| existedRecords,
		340	| dataMap,
		341	| collator,
		342	| delegators,
		343	| isIncre
		344	| }) {
		345	| if (!delegators || !delegators.length) {
		348	| let startTime = null;
		349	| let endTime = this.taskStartedAt;
		350	| if (isIncre) {
		351	| startTime = existedRecords[delegators[0]].timestamp as Date;
		352	| // no matter existed records has further updates, we needs to keep the legacy data
		353	| delegators.forEach(delegator => {
		354	| dataMap[delegator].reward = existedRecords[delegator].reward - 0;
		355	| dataMap[delegator].latestReward = existedRecords[delegator].latestReward;
		356	| dataMap[delegator].latestRewardBlock = existedRecords[delegator].latestRewardBlock;
		359	| let rewards = await this.collatorService.statDelegatorsReward({
		362	| delegators,
		363	| startTime,
		364	| endTime
		366	| rewards.forEach((reward) => {
		367	| dataMap[reward.delegator].reward =
		368	| reward.reward - 0 + (isIncre ? (dataMap[reward.delegator].reward - 0) : 0);
		369	| dataMap[reward.delegator].latestReward = reward.latestReward;
		370	| dataMap[reward.delegator].latestRewardBlock = reward.latestRewardBlock;
		386	| delegator.owner = ChainUtils.ss58transform_simple(
		387	| delegator.owner,
		388	| network
		416	| private async batchCalReward(shareData) {
		417	| const { collatorReward, collatorDataMap } = shareData;
		418	| //if (!rewards.length) return;
		419	| const max = {}; // {collator: [roundIndex, maxValue] }
		420	| for (const reward of collatorReward) {
		421	| const collator = reward.account;
		422	| collatorDataMap[collator].totalReward += reward.reward;
		423	| max[collator] = max[collator] || [0, 0];
		424	| if (max[collator][0] < reward.roundIndex) {
		425	| max[collator][1] = reward.reward;
		428	| for (const collator in max) {
		429	| collatorDataMap[collator].latestReward = max[collator][1];
		433	| private async batchCalStake(chain: ChainConnector, shareData) {
		434	| const { collators, collatorDataMap } = shareData;
		435	| const rawData = await chain.api.query.parachainStaking.candidateInfo.multi(
		436	| collators
		439	| const dataMap = {};
		440	| rawData
		441	| .map((it) => it.toJSON())
		442	| .forEach((it: any, i) => {
		443	| dataMap[collators[i]] = chain.formatWithDecimals(it.bond).toNumber();
		446	| for (const collator of collators) {
		447	| collatorDataMap[collator].selfStake = dataMap[collator] || 0;
		448	| collatorDataMap[collator].delegatorStake =
		449	| collatorDataMap[collator].totalStake -
		450	| collatorDataMap[collator].selfStake;
		454	| // if the Top Delegator List has not been full yet (capacity of the list
		455	| // is an constant defined in parachain.constant.maxTopDelegationsPerCandidate),
		456	| // it would be higher than the last one on the list,
		457	| // or it would be the default value of each network’s.
		458	| private batchCalMinBond(chain: ChainConnector, shareData) {
		459	| const defaultMinBondValue = chain.defaultValues.minBond;
		460	| const { collators, collatorDataMap } = shareData;
		461	| const maxTopDelegationsPerCandidate =
		462	| chain.api.consts.parachainStaking.maxTopDelegationsPerCandidate;
		463	| for (let i = 0; i < collators.length; i++) {
		464	| const collator = collators[i];
		465	| const row = collatorDataMap[collator];
		467	| row.minBond = defaultMinBondValue;
		469	| const tdr = shareData.topDelegators[i];
		470	| if (tdr.delegations < 1) continue;
		472	| const last = tdr.delegations[tdr.delegations.length - 1].amount;
		473	| if (tdr.delegations.length === maxTopDelegationsPerCandidate) {
		474	| row.minBond = last + 1;
		476	| row.minBond = Math.max(defaultMinBondValue, last);
		481	| private doRank(key: string, rankKey: string, data: Array<any>) {
		482	| const vs = [];
		483	| data.forEach((it) => vs.push(it[key]));
		484	| vs.sort();
		485	| data.forEach((it) => ((it as any)[rankKey] = vs.indexOf(it[key]) + 1));
		488	| private calByNetwork(network) {}
		497	| async test() {
		499	| await this.cron.doit();
		500	| return `task executed cost ${(new Date().getTime() - now) / 1000}s`;


Partially similar files found. First length 89, Second length 42,  The files are 36% identicalThe files differ in 46 lines:
	./resources/european/service/src/parachain/staking/portal/controller/stat-collator-controller.ts
	./resources/asia/service/src/parachain/staking/portal/controller/stat-collator-controller.ts
	Unique lines in first:
		10	| import { StatCollator } from "src/common/entity/StakingPortalStat/StatCollator.entity";
		14	| import { ChainConnectManager } from "../../core/chain/chain-connect-manager";
		21	| constructor(private collatorService: StatCollatorStatService) {}
		34	| // GET DATA
		36	| const result = {
		41	| // FORMATING THE RPS_HIS DATA
		42	| result.list &&
		43	| result.list.forEach((it: StatCollator) => {
		44	| if (it.rpsHis && it.rpsHis.length) {
		45	| try {
		46	| it.rpsHis = JSON.parse(it.rpsHis);
		47	| } catch (e) {
		48	| // mute exception for the text format error.
		51	| });
		53	| // EXTRA PROCEESDURES FOR MY-STAKE & ITS ORDERING
		54	| if (
		55	| result.list.length &&
		56	| request.myAccount &&
		57	| (request.myAccount = request.myAccount.trim()).length > 0
		58	| ) {
		59	| const chain = ChainConnectManager.get(request);
		60	| const myStakeChainData =
		61	| await chain.api.query.parachainStaking.delegatorState(
		62	| request.myAccount
		63	| );
		64	| if (!myStakeChainData || myStakeChainData.isEmpty) {
		65	| return result;
		67	| (myStakeChainData.toJSON() as any).delegations.forEach((stakeRecord) => {
		68	| let myStake = chain.formatWithDecimals(stakeRecord.amount).toNumber();
		69	| const collator = chain.formatAccountAddr(stakeRecord.owner);
		70	| result.list.forEach((row) => {
		71	| row.myStake = null;
		72	| if (row.collator === collator) {
		73	| row.myStake = myStake;
		75	| });
		76	| });
		77	| let sortMyStakeAsc = null;
		78	| request.orderBys.forEach((it) => {
		79	| if (it.sort === "myStake") {
		80	| sortMyStakeAsc = it.order === "DESC";
		82	| });
		83	| if (sortMyStakeAsc != null) {
		84	| result.list.sort(
		85	| (i, ii) =>
		86	| ((i.myStake || 0) - (ii.myStake || 0)) * (sortMyStakeAsc ? -1 : 1)
		87	| );

	Unique lines in second:
		12	| import { StatDelegatorPageRequest } from "src/viewModel/staking/portal/StatDelegatorPageRequest";
		15	| import { StatDelegatorService } from "../service/stat-delegator-service";
		21	| constructor(
		22	| private collatorService: StatCollatorStatService,
		23	| private delegatorService: StatDelegatorService
		24	| ) {}
		38	| return {
		44	| //


Partially similar files found. First length 83, Second length 32,  The files are 36% identicalThe files differ in 41 lines:
	./resources/european/service/src/parachain/staking/portal/controller/stat-delegator-controller.ts
	./resources/asia/service/src/parachain/staking/portal/controller/stat-delegator-controller.ts
	Unique lines in first:
		5	| Param,
		10	| import { ApiOperation, ApiTags } from "@nestjs/swagger";
		12	| import { DelegatorInfoRequest } from "src/viewModel/staking/portal/DelegatorInfoRequest";
		14	| import { ChainConnectManager } from "../../core/chain/chain-connect-manager";
		35	| @Get("info")
		37	| async showSummary(@Query() request: DelegatorInfoRequest): Promise<any> {
		38	| const data = await this.delegatorService.summaryDelegator(request);
		39	| return data;
		42	| @Get("timeMachine/rewards/stat")
		44	| async myRewardStat(@Query() request: DelegatorInfoRequest): Promise<any> {
		45	| // const data = await this.delegatorService.summaryDelegator(request);
		47	| const round = await ChainConnectManager.get(request).api.    query.parachainStaking.round();
		48	| let roundInfo: any = round.toJSON();
		49	| const allRewards = await this.delegatorService.listAllMyReward(request, roundInfo.current - 21, roundInfo.current - 2);
		50	| const aggregate = () => {
		51	| const rewardByCollator = [];
		52	| const rewardByRoundIndex = [];
		54	| const map1 = {};
		55	| const map2 = [];
		56	| allRewards.forEach(it => {
		57	| if (!map1[it.collator]) {
		58	| map1[it.collator] = {collator: it.collator, reward: 0};
		59	| rewardByCollator.push(map1[it.collator]);
		61	| map1[it.collator].reward += it.balance;
		63	| if (!map2[it.realroundindex]) {
		64	| map2[it.realroundindex] = {roundIndex: it.realroundindex, reward: 0};
		65	| rewardByRoundIndex.push(map2[it.realroundindex]);
		67	| map2[it.realroundindex].reward += it.balance;
		68	| });
		69	| rewardByCollator.sort((it, it2) => it.reward - it2.reward);
		70	| rewardByRoundIndex.sort((it, it2) => it.roundIndex - it2.roundIndex);
		72	| rewardByCollator,
		73	| rewardByRoundIndex,
		76	| return aggregate();
		80	| @Get("timeMachine/staking/his")
		82	| async myStakingHis(@Query() request: DelegatorInfoRequest): Promise<any> {
		83	| return await this.delegatorService.listAllMyStakingHis(request);
		88	| @Get("timeMachine/staking/:type/info")
		90	| @ApiOperation({ summary: 'type:[action, reward]. returning all Collators and Rounds of the corresponding data within a delegator\'s stakes' })
		91	| async listMyStakingsCollatorsAndRounds(@Query() request: DelegatorInfoRequest, @Param('type') type: string) {
		92	| return await this.delegatorService.listMyStakingsCollatorsAndRounds(request, type)

	Unique lines in second:
		9	| import { ApiTags } from "@nestjs/swagger";
		12	| import { StatCollatorStatService } from "../service/stat-collator-service";
		33	| //


Partially similar files found. First length 185, Second length 87,  The files are 33% identicalThe files differ in 72 lines:
	./resources/european/service/src/common/setting/appConfig.ts
	./resources/asia/service/src/parachain/staking/core/register/chain-network-register.ts
	Unique lines in first:
		0	| import { ParachainNetwork } from "../chain/chain-network";
		2	| //
		3	| export const PORTAL_DB_CONFIG = {
		5	| host: "",
		6	| password: "",
		11	| database: "dev-cumulon-protocol",
		12	| };
		14	| // CURRENT SUPPORTED CHAIN NETWORKS FOR the Go Staking Portal data acess from the network or the indexed database
		33	| collatorSafeStateThreshold: 0.9
		37	| host: "",
		39	| username: "",
		40	| password: "",
		43	| database: "prod-litentry-mainnet-staking",
		48	| id: "calamari",
		50	| displayName: "Calamari: Manta Canary Network",
		51	| network: "calamari",
		52	| prefix: 78,
		54	| symbols: ["KMA"],
		55	| website: "https://manta.network",
		56	| wssEndpoints: ["wss://ws.calamari.systems/"],
		59	| minBond: 5000,
		64	| host: "",
		66	| username: "",
		67	| password: "",
		70	| database: "prod-calamari-mainnet-staking",
		75	| id: "turing",
		76	| decimals: [10],
		77	| displayName: "Turing Network",
		78	| network: "turing",
		79	| prefix: 51,
		81	| symbols: ["TUR"],
		82	| website: "https://oak.tech/",
		83	| // wssEndpoints: ['wss://rpc.turing-staging.oak.tech'],
		84	| wssEndpoints: ["wss://rpc.turing.oak.tech"],
		92	| host: "",
		94	| username: "",
		95	| password: "",
		98	| database: "prod-oak-staking",
		120	| host: "",
		122	| username: "",
		123	| password: "",
		126	| database: "prod-bifrost-staking",
		132	| id: "moonbeam",
		133	| decimals: [18],
		134	| displayName: "Moonbeam",
		135	| network: "moonbeam",
		136	| prefix: 1284,
		137	| standardAccount: "secp256k1",
		138	| symbols: ["GLMR"],
		139	| website: "https://moonbeam.network",
		141	| {external: true, url: "ws://16.163.221.27:9944"},
		142	| "wss://wss.api.moonbeam.network"],
		145	| minBond: 5,
		150	| host: "",
		152	| username: "",
		153	| password: "",
		156	| database: "prod-moonbeam-staking",
		162	| id: "moonriver",
		163	| decimals: [18],
		164	| displayName: "Moonriver",
		165	| network: "moonriver",
		166	| prefix: 1285,
		167	| standardAccount: "secp256k1",
		168	| symbols: ["MOVR"],
		169	| website: "https://moonbeam.network",
		171	| {external: true, url: "ws://3.1.235.180:9944"},
		172	| "wss://wss.api.moonriver.moonbeam.network"],
		175	| minBond: 5,
		180	| host: "",
		182	| username: "",
		183	| password: "",
		186	| database: "prod-moonriver-staking",

	Unique lines in second:
		0	| import { ParachainNetwork } from "src/common/chain/chain-network";
		3	| {
		5	| id: "litentry-rococo",
		7	| displayName: "Litentry Rococo Network",
		8	| network: "Litentry-rococo",
		9	| prefix: 131,
		11	| symbols: ["LIT"],
		12	| website: "https://litentry.com/",
		13	| wssEndpoints: ["wss://rpc.rococo-parachain-sg.litentry.io"],
		16	| minBond: 50,
		22	| host: "16.163.5.216",
		23	| password: "Dev123!@#",
		27	| username: "postgres",
		28	| database: "dev-litentry-staking",
		31	| {
		52	| host: "16.163.5.216",
		55	| password: "Dev123!@#",
		58	| database: "dev-litentry-mainnet-staking",
		62	| {
		80	| host: "16.163.5.216",
		83	| password: "Dev123!@#",
		86	| database: "dev-bifrost-staking",


Partially similar files found. First length 93, Second length 213,  The files are 24% identicalThe files differ in 121 lines:
	./resources/european/service/src/parachain/staking/core/chain/connector/moonriver-chain-connector.ts
	./resources/asia/ui/src/utils/chain/chainConnector.ts
	Unique lines in first:
		0	| import { ChainConnector } from "src/common/chain/chain-connector";
		2	| export class MoonriverChainConnector extends ChainConnector {
		4	| protected BREAK_CHANGE_SPEC_VERSION = 1200;
		7	| protected NEED_CONVERT_ACCOUNT_ADDR = false;
		14	| let json = selectedCandidates.toJSON();
		15	| this.logger.debug(
		16	| "getSelectedCollators4CurrentRound:" + JSON.stringify(json)
		24	| let json = candidatePool.toJSON();
		25	| // this.logger.debug('getRealtimeCollatorCandidatePool:' + JSON.stringify(json));
		35	| const multiStates =
		36	| await this.api.query.parachainStaking.candidateState.multi(
		37	| collatorAccounts
		39	| multiStates.forEach((t) => {
		40	| let json = t.toJSON();
		41	| // console.log((json as any).id);
		42	| result.push(json);
		45	| //Break Changes:  https://github.com/PureStake/moonbeam/releases/tag/runtime-1200
		46	| this.logger.verbose(
		47	| "getRealtimeCollatorState found runtime specVersion >=" +
		48	| this.BREAK_CHANGE_SPEC_VERSION
		52	| collatorAccounts
		57	| collatorAccounts
		61	| collatorAccounts
		103	| this.logger.debug("maxTopDelegationsPerCandidate:" + JSON.stringify(json));

	Unique lines in second:
		0	| import { Inject, Injectable } from '@nestjs/common';
		1	| import { W3Logger } from 'src/common/log/logger.service';
		2	| import { ApiPromise, WsProvider } from '@polkadot/api';
		3	| import { FunctionExt } from 'src/common/utility/functionExt';
		4	| import BigNumber from 'bignumber.js';
		5	| import * as definitions from './interfaces/definitions';
		6	| import { AppConfig } from 'src/common/setting/appConfig';
		7	| import { ChainUtils } from './chain.utils';
		10	| @Injectable()
		11	| export class ChainConnector {
		13	| private BREAK_CHANGE_SPEC_VERSION = 0;
		15	| async atStake(roundIndex: number, collatorAccount: string): Promise<any> {
		16	| await this.checkReady();
		17	| const atStake = await this.api.query.parachainStaking.atStake(
		18	| roundIndex,
		19	| collatorAccount,
		21	| let json = atStake.toJSON();
		22	| this.logger.debug('atStake:' + JSON.stringify(json));
		25	| async getLatestBlockNumber(): Promise<number | PromiseLike<number>> {
		26	| await this.checkReady();
		27	| const number = await this.api.query.system.number();
		28	| let blocknumber = Number(number);
		29	| this.logger.debug('getLatestBlockNumber:' + blocknumber);
		30	| return blocknumber;
		32	| async getCurrentRoundInfo(): Promise<any> {
		33	| await this.checkReady();
		34	| const round = await this.api.query.parachainStaking.round();
		35	| let roundInfo = round.toJSON();
		37	| let data = (await this.api.query.balances.totalIssuance()) as unknown as any;
		38	| let formatSymbolDecimals = new BigNumber('1e' + AppConfig.ParaChainSymbolDecimals)
		39	| let value = new BigNumber(data.toString()).div(formatSymbolDecimals).toNumber();
		40	| roundInfo["totalIssuance"] = value;
		41	| this.logger.debug('getCurrentRoundInfo:' + JSON.stringify(roundInfo));
		43	| return roundInfo;
		46	| await this.checkReady();
		49	| let candidates = selectedCandidates.toJSON() as any;
		50	| if (candidates) {
		51	| for (let index = 0; index < candidates.length; index++) {
		52	| const c = candidates[index];
		53	| let convertedAddress = ChainUtils.ss58transform_simple(c, AppConfig.ParaChainName);
		54	| // this.logger.debug(`convertedAddress: ${c}=>${convertedAddress}`);
		55	| candidates[index] = convertedAddress;
		58	| this.logger.debug('getSelectedCollators4CurrentRound:' + JSON.stringify(candidates));
		59	| return candidates;
		63	| await this.checkReady();
		65	| let cps = candidatePool.toJSON() as any;
		67	| for (let index = 0; index < cps.length; index++) {
		68	| const cp = cps[index];
		69	| let convertedAddress = ChainUtils.ss58transform_simple(cp.owner, AppConfig.ParaChainName);
		70	| cps[index].owner = convertedAddress;
		72	| this.logger.debug('getRealtimeCollatorCandidatePool:' + JSON.stringify(cps));
		74	| return cps;
		81	| let collatorAccounts_publickey = [];
		82	| for (const a of collatorAccounts) {
		83	| let pk = ChainUtils.ss58transform_publickey(a);
		84	| collatorAccounts_publickey.push(pk);
		86	| this.logger.debug('collatorAccounts_publickey:' + JSON.stringify(collatorAccounts_publickey));
		90	| //
		94	| collatorAccounts_publickey,
		96	| this.logger.debug(`multiCandidateInfos ${JSON.stringify(multiCandidateInfos)}`);
		100	| collatorAccounts_publickey,
		102	| this.logger.debug(`multiTopDelegations ${JSON.stringify(multiTopDelegations)}`);
		106	| collatorAccounts_publickey,
		108	| this.logger.debug(`multiBottomDelegations ${JSON.stringify(multiBottomDelegations)}`);
		137	| async getScheduledExitQueue(): Promise<any> {
		139	| const exitQueue2 = await this.api.query.parachainStaking.exitQueue2();
		140	| let json = exitQueue2.toJSON();
		141	| this.logger.debug('getScheduledExitQueue:' + JSON.stringify(json));
		159	| this.logger.debug('maxTopDelegationsPerCandidate:' + JSON.stringify(json));
		165	| private wsProvider: WsProvider;
		166	| private api: ApiPromise;
		167	| private wssEndpoint: string;
		168	| private systemVersion: any;
		169	| private logger: W3Logger;
		170	| private modulePrefix: string;
		171	| constructor() {
		172	| this.logger = new W3Logger('ChainConnector');
		175	| async init(wssEndpoint: string, modulePrefix: string) {
		176	| this.wssEndpoint = wssEndpoint;
		177	| this.modulePrefix = modulePrefix;
		178	| this.logger.modulePrefix = modulePrefix;
		179	| this.logger.debug('init wssEndpoint:' + wssEndpoint);
		180	| const types = Object.values(definitions).reduce(
		181	| (res, { types }): object => ({ ...res, ...types }),
		182	| {},
		184	| this.wsProvider = new WsProvider(this.wssEndpoint);
		185	| this.api = await ApiPromise.create({
		186	| provider: this.wsProvider,
		187	| types: {
		188	| ...types,
		192	| this.wsProvider.on('connected', (val) => {
		193	| this.logger.debug('connected:' + val);
		195	| this.wsProvider.on('disconnected', (val) => {
		196	| this.logger.debug('disconnected:' + val);
		198	| this.wsProvider.on('error', (val) => {
		199	| this.logger.error('error:' + val);
		203	| this.logger.debug('chain genesisHash:' + this.api.genesisHash.toHex());
		207	| await this.getSystemVersion();
		210	| async checkReady() {
		211	| let isReady = this.wsProvider.isConnected;
		212	| let maxWait = 30;
		213	| while (!isReady && maxWait > 0) {
		214	| maxWait--;
		215	| await FunctionExt.sleep(1000);
		217	| if (isReady) {
		218	| this.logger.debug('checkReady pass, the connection is avaliable');
		220	| else {
		221	| this.logger.warn('checkReady failed , reInit the connection');
		222	| await this.init(this.wssEndpoint, this.modulePrefix);
		225	| async getSystemVersion() {
		226	| const version = await this.api.consts.system.version.toJSON();
		227	| if (version) {
		228	| this.logger.verbose(`getSystemVersion: ${JSON.stringify(version)}`);
		229	| this.systemVersion = version;
		231	| this.systemVersion = {};
		234	| getSpecVersion() {
		235	| let specVersion = 0;
		236	| if (this.systemVersion && this.systemVersion.specVersion) {
		237	| specVersion = Number(this.systemVersion.specVersion);
		239	| this.logger.verbose(`found runtime specVersion ${specVersion}`);
		240	| return specVersion;


Partially similar files found. First length 145, Second length 334,  The files are 17% identicalThe files differ in 199 lines:
	./resources/european/service/src/parachain/staking/portal/service/my-stake-list-service.ts
	./resources/asia/service/src/parachain/staking/portal/service/my-stake-list-service.ts
	Unique lines in first:
		1	| import { In } from "typeorm";
		33	| const myStakeChainData = await cc.api.query.parachainStaking.delegatorState(
		36	| if (!myStakeChainData || myStakeChainData.isEmpty) {
		41	| const result = (myStakeChainData.toJSON() as any).delegations.map((it) => {
		42	| let myStake = cc.formatWithDecimals(it.amount.toString()).toNumber();
		43	| const collator = cc.formatAccountAddr(it.owner);
		44	| return (mapUser2Row[collator] = {
		46	| collator,
		47	| myStake,
		52	| selfStake: 0,
		53	| nominatorStake: 0,
		54	| totalStake: 0,
		56	| myRank: 0,
		57	| myShare: 0,
		61	| const collators = result.map((it) => it.collator);
		65	| this.processStakeAndRank(
		67	| cc,
		68	| result,
		72	| const collatorStats = await DbManager.PORTAL.statCollatorRepository.find({
		73	| where: { chainId: request.chainId, collator: In(collators) },
		75	| const delegatorStats = await DbManager.PORTAL.statDelegatorRepository.find({
		76	| where: { chainId: request.chainId, collator: In(collators), delegator: request.accountId },
		78	| for (const it of collatorStats) {
		82	| row.rank = it.totalStakeRank;
		84	| const matched = delegatorStats.filter(delegator => delegator.collator === it.collator)[0];
		85	| if (matched) {
		86	| row.totalReward = matched.reward;
		87	| row.latestReward = matched.latestReward;
		89	| // row.totalReward = it.totalReward;
		90	| // row.latestReward = await this.getCollatorLatestReward({
		91	| //   collator: it.collator,
		92	| //   chainId: request.chainId,
		93	| // });
		96	| return result;
		99	| private async processStakeAndRank(
		101	| chain,
		102	| data,
		103	| delegator
		105	| const getRank = (delegationGroup, delegator) => {
		106	| let i = 0;
		107	| for (const group of delegationGroup) {
		108	| for (const delegations of group) {
		109	| i++;
		110	| if (delegations.owner === delegator) {
		111	| return i;
		115	| return null;
		118	| data.forEach((row) => {
		119	| for (let rank = 1; rank <= realtimeCollatorState.length; rank++) {
		120	| const matched = realtimeCollatorState[rank - 1];
		121	| if (matched.id !== row.collator) continue;
		122	| row.myRank = getRank(
		123	| [matched.topDelegations, matched.bottomDelegations],
		124	| delegator
		126	| //row.rank = rank;
		127	| row.selfStake = chain.formatWithDecimals(matched.bond).toNumber();
		128	| row.totalStake = chain
		129	| .formatWithDecimals(matched.totalCounted)
		130	| .toNumber();
		131	| row.nominatorStake = row.totalStake - row.selfStake;
		132	| const myShare: any = (
		133	| ((row.myStake / (row.nominatorStake || 1)) * 100) as number
		134	| ).toFixed(2);
		135	| row.myShare = myShare - 0 || 0;

	Unique lines in second:
		1	| import BigNumber from "bignumber.js";
		2	| import { request } from "express";
		3	| import { map } from "rxjs/operators";
		4	| import { ChainConnector } from "src/common/chain/chain-connector";
		5	| import { StakingRequest } from "src/viewModel/staking/StakingRequest";
		12	| // import { lastValueFrom } from 'rxjs';
		38	| const chainData = await cc.api.query.parachainStaking.delegatorState(
		41	| if (!chainData || chainData.isEmpty) {
		44	| // const maxTopDelegationsPerCandidate =
		45	| //   cc.api.consts.parachainStaking.maxTopDelegationsPerCandidate;
		47	| const data = (chainData.toJSON() as any).delegations.map((it) => {
		48	| let stakedAmount = cc.formatWithDecimals(it.amount.toString()).toNumber();
		49	| return (mapUser2Row[it.owner] = {
		50	| chainId: request.chainId,
		51	| collator: it.owner,
		52	| stakedAmount,
		59	| const baseService: StakingBaseService = this.serviceManager.getService(
		60	| request,
		61	| StakingBaseService.name
		64	| const collators = data.map((it) => it.collator);
		67	| // TODO TO OPTIMIZE THE RANK BY STAT-TASK
		69	| realtimeCollatorState &&
		70	| realtimeCollatorState.forEach((v) => {
		71	| v.allNominators = [...v.topDelegations, ...v.bottomDelegations];
		72	| mapUser2Row[v.id].rank = this.getStakeRank(v, request.accountId);
		75	| // becuase the data would be very small, get all directly
		76	| const stats = await DbManager.get(request).statCollatorRepository.find({});
		77	| for (const it of stats) {
		81	| row.totalReward = it.totalReward;
		82	| row.latestReward = await this.getCollatorLatestReward({
		83	| collator: it.collator,
		84	| chainId: request.chainId,
		89	| // await this.fillReward(request, baseService, collators, mapUser2Row);
		91	| // await this.fillApr(
		92	| //   request,
		93	| //   baseService,
		94	| //   collators,
		95	| //   cc,
		96	| //   mapUser2Row,
		97	| //   realtimeCollatorState,
		98	| //   divider
		100	| return data;
		103	| private getStakeRank(row, collator) {
		104	| const findIndex = row.allNominators.findIndex(
		105	| (v) => v.pk === collator || v.owner === collator
		107	| return findIndex + 1;
		111	| request: MyStakeRequest,
		112	| baseService: StakingBaseService,
		132	| async fillApr(
		133	| request: MyStakeRequest,
		134	| baseService: StakingBaseService,
		135	| accounts,
		136	| cc: ChainConnector,
		137	| mapUser2Row,
		138	| realtimeCollatorState,
		139	| divider
		141	| const round = (await cc.api.query.parachainStaking.round()).toJSON() as {
		142	| current;
		143	| first;
		144	| length;
		145	| totalIssuance;
		147	| const blockPerRound = round.length;
		150	| cc.network.network === "moonbeam" ||
		151	| cc.network.network === "moonriver"
		153	| let total_supply = Number(round.totalIssuance);
		155	| for (let i = 0; i < realtimeCollatorState.length; i++) {
		156	| let stake = this.formatWithDecimals(
		157	| realtimeCollatorState[i].totalCounted,
		158	| divider
		159	| ).toNumber();
		160	| let collator_counted_stake = Number(stake);
		161	| let avg_blocks_per_round = stake;
		163	| "total_supply:",
		164	| total_supply,
		165	| " collator_counted_stake:",
		166	| collator_counted_stake,
		167	| " avg_blocks_per_round:",
		168	| avg_blocks_per_round
		171	| mapUser2Row[realtimeCollatorState[i].id].apr =
		172	| ((0.00001388888888888889 * total_supply * avg_blocks_per_round) /
		173	| collator_counted_stake) *
		174	| 100;
		177	| const blockTargetSeconds = await this.getBlockTargetSeconds(
		178	| cc.network.network
		181	| await this.initRewards(
		182	| request,
		183	| baseService,
		184	| accounts,
		186	| round
		188	| for (let i = 0; i < realtimeCollatorState.length; i++) {
		189	| const rewardInRounds = this.getRewardInRounds(
		190	| realtimeCollatorState[i],
		191	| 10
		193	| // const filterNoRewardRoundWhenCalcAPR = false;
		194	| const rounds =
		195	| //   filterNoRewardRoundWhenCalcAPR === true
		196	| //     ? rewardInRounds.roundsHasReward :
		197	| rewardInRounds.rounds;
		199	| let roundPerYear = await this.getRoundPerYear(
		200	| blockTargetSeconds,
		201	| blockPerRound
		203	| let stake = this.formatWithDecimals(
		204	| realtimeCollatorState[i].totalCounted,
		205	| divider
		206	| ).toNumber();
		207	| let reward = rewardInRounds.collatorRewardInRounds;
		208	| //let rounds = params.rounds;
		209	| mapUser2Row[realtimeCollatorState[i].id].apr =
		210	| (reward / (rounds || 1) / (stake || 1)) * roundPerYear * 100;
		213	| // const multiCandidateInfos =
		214	| //   await cc.api.query.parachainStaking.candidateInfo.multi(
		215	| //     data.map((it) => it.collator)
		216	| //   );
		217	| //   // totalCounted
		219	| // return data;
		221	| formatWithDecimals(value, divider) {
		222	| return BigNumber(value).dividedBy(divider);
		225	| getStartRoundIndex(roundInfo) {
		226	| return roundInfo.current - 11 - 0;
		228	| getEndRoundIndex(roundInfo) {
		229	| return roundInfo.current - 2 - 0; //Reward延迟2round发放
		232	| private async initRewards(
		235	| accounts,
		237	| roundInfo
		239	| const startRoundIndex = this.getStartRoundIndex(roundInfo);
		240	| const endRoundIndex = this.getEndRoundIndex(roundInfo);
		241	| // 获取Collator的历史10次reward
		242	| const collector10Reward = await baseService.getCollatorReward({
		244	| startRoundIndex: startRoundIndex,
		245	| endRoundIndex: endRoundIndex,
		246	| accounts,
		249	| realtimeCollatorState.forEach((v) => {
		250	| const arr = [];
		251	| for (let i = startRoundIndex; i <= endRoundIndex; i++) {
		252	| const find = collector10Reward.rewards.find(
		253	| (sv) =>
		254	| sv.account.toLowerCase() == v.id.toLowerCase() &&
		255	| Number(sv.roundIndex) == i
		257	| if (find) {
		258	| arr.push({
		259	| roundIndex: i,
		260	| reward: BigNumber(find.reward),
		263	| arr.push({
		264	| roundIndex: i,
		265	| reward: BigNumber(0),
		269	| v.historyReward = arr;
		272	| const getNominatorReward = await baseService.getNominatorReward({
		274	| startRoundIndex,
		275	| endRoundIndex,
		278	| // 塞入10次NominatortotalReward (坑点：历史数据返回可能缺失某个roundIndex)
		279	| realtimeCollatorState.forEach((v) => {
		281	| for (let i = startRoundIndex; i <= endRoundIndex; i++) {
		282	| //按照collator分开reward数据
		283	| const find = getNominatorReward.rewards.find(
		285	| Number(sv.roundIndex) == i &&
		286	| sv.collator.toLowerCase() == v.id.toLowerCase()
		300	| v.historyNominatorTotalReward = arr;
		304	| getRewardInRounds(c, rounds) {
		305	| let roundsHasReward = 0;
		306	| let rewardInRounds = 0;
		307	| let startIndex = c.historyReward.length - rounds;
		308	| if (startIndex < 0) {
		309	| startIndex = 0;
		311	| for (let index = startIndex; index < c.historyReward.length; index++) {
		312	| const element = c.historyReward[index];
		313	| let reward = element.reward.toNumber();
		314	| if (reward > 0) {
		315	| roundsHasReward++;
		317	| rewardInRounds += reward;
		320	| startIndex = c.historyNominatorTotalReward.length - rounds;
		321	| if (startIndex < 0) {
		322	| startIndex = 0;
		324	| for (
		325	| let index = startIndex;
		326	| index < c.historyNominatorTotalReward.length;
		327	| index++
		329	| const element = c.historyNominatorTotalReward[index];
		330	| rewardInRounds += element.reward.toNumber();
		333	| return {
		334	| collatorRewardInRounds: rewardInRounds,
		335	| rounds,
		336	| roundsHasReward: roundsHasReward,
		340	| getRoundPerYear(blockTargetSeconds, blockPerRound) {
		341	| let roundPerYear = Math.ceil(
		342	| (365 * 24 * 3600) / (blockTargetSeconds * blockPerRound)
		344	| return roundPerYear;
		347	| async getBlockTargetSeconds(network) {
		348	| let key = "averageBlockTime" + network;
		349	| if (this[key]) {
		350	| return this[key];
		352	| if (network === "bifrost") {
		353	| let url = "https://api.bifrost.app/api/dapp/averageBlockTime";
		355	| let response: any = await this.httpService.get(url).toPromise();
		356	| // console.log("getBlockTargetSeconds response:", response);
		357	| if (response) {
		358	| let time = response.data.result.main;
		359	| this[key] = time;
		360	| return time;
		364	| return 12;


Partially similar files found. First length 137, Second length 25,  The files are 13% identicalThe files differ in 94 lines:
	./resources/european/service/src/parachain/staking/portal/service/stat-delegator-service.ts
	./resources/asia/service/src/parachain/staking/portal/service/stat-delegator-service.ts
	Unique lines in first:
		1	| import { NominatorActionHistory } from "src/common/entity/StakingModule/NominatorActionHistory.entity";
		2	| import { NominatorRewardDetailHistory } from "src/common/entity/StakingModule/NominatorRewardDetailHistory.entity";
		4	| import { DelegatorInfoRequest } from "src/viewModel/staking/portal/DelegatorInfoRequest";
		6	| import { Between, In } from "typeorm";
		7	| import { ChainConnectManager } from "../../core/chain/chain-connect-manager";
		14	| request.orderBys &&
		15	| request.orderBys.forEach((it) => {
		21	| const method = request.needTotal ? "findAndCount" : "find";
		22	| return await DbManager.PORTAL.statDelegatorRepository[method]({
		24	| chainId: request.chainId,
		25	| collator: request.collator,
		33	| async summaryDelegator(request: DelegatorInfoRequest) {
		34	| const result = {
		35	| latestReward: 0,
		36	| latestRewardBlock: "",
		37	| totalBond: 0,
		38	| totalReward: 0,
		39	| stakedCollators: 0,
		40	| };
		41	| const dbr = DbManager.PORTAL.statDelegatorRepository;
		43	| let raw = await dbr.query(
		44	| `SELECT latest_reward, latest_reward_block from stat_delegator WHERE chain_id='${request.chainId}' AND delegator='${request.delegator}' ORDER BY latest_reward_block DESC limit 1`
		45	| );
		46	| if (raw && raw.length) {
		47	| result.latestReward = raw[0].latest_reward;
		48	| result.latestRewardBlock = raw[0].latest_reward_block;
		49	| } else {
		50	| return result;
		53	| raw = await dbr.query(
		54	| `SELECT sum(stake) as total_bond, sum(reward) as total_reward from stat_delegator WHERE chain_id='${request.chainId}' AND delegator='${request.delegator}'`
		55	| );
		56	| if (raw && raw.length) {
		57	| // result.totalBond = raw[0].total_bond;
		58	| result.totalReward = raw[0].total_reward;
		59	| // result.stakedCollators = raw[0].stakedCollators; // , count(delegator) as staked_count
		62	| const chain = ChainConnectManager.get(request);
		63	| const myStakeChainData =
		64	| await chain.api.query.parachainStaking.delegatorState(request.delegator);
		65	| if (!myStakeChainData || myStakeChainData.isEmpty) {
		66	| return result;
		68	| (myStakeChainData.toJSON() as any).delegations.forEach((it) => {
		69	| result.totalBond += chain.formatWithDecimals(it.amount).toNumber();
		70	| result.stakedCollators++;
		76	| async listAllMyReward(
		77	| request: DelegatorInfoRequest,
		78	| startRound: number,
		79	| endRound: number,
		80	| ): Promise<NominatorRewardDetailHistory[]> {
		81	| return await DbManager.get(request).nrdhRepository.find({
		83	| account: request.delegator,
		84	| realroundindex: Between(startRound, endRound)
		86	| order: {
		87	| realroundindex: "DESC",
		92	| async listAllMyStakingHis(
		93	| request: DelegatorInfoRequest
		94	| ): Promise<NominatorActionHistory[]> {
		95	| return await DbManager.get(request).nahRepository.find({
		97	| account: request.delegator,
		98	| actiontype: In(["add", "increase", "left"]),
		100	| order: {
		101	| timestamp: "DESC",
		106	| async listMyStakingsCollatorsAndRounds(
		107	| request: DelegatorInfoRequest,
		108	| type: string
		109	| ): Promise<any> {
		110	| const isAction = type === "action";
		111	| const repository = isAction
		112	| ? DbManager.get(request).nahRepository
		113	| : DbManager.get(request).nrdhRepository;
		115	| const sql = `SELECT
		116	| DISTINCT collator,
		117	| ${isAction ? "roundindex" : "issueroundindex"} AS round_index
		118	| FROM
		119	| ${isAction ? "nominator_action_histories" : "nominator_reward_detail_histories"}
		120	| WHERE account = $1
		121	| ${isAction ? "AND actiontype in ('add', 'increase', 'left')" : ''}`;
		122	| const rawData = await repository.query(sql, [request.delegator]);
		123	| const collators = [];
		124	| const rounds = [];
		126	| if (rawData && rawData.length > 0) {
		127	| const map = {};  // because the round will never be conflict with the collator, we share a same map
		128	| rawData.forEach(it => {
		129	| const collator = it.collator;
		130	| const round = it.round_index;
		131	| if (!map[collator]) {
		132	| map[collator] = 1;
		133	| collators.push(collator);
		135	| if (!map[round]) {
		136	| map[round] = 1;
		137	| rounds.push(round);
		140	| rounds.sort();
		142	| return {
		143	| collators,
		144	| rounds,

	Unique lines in second:
		10	| request.orderBys && request.orderBys.forEach(it=> {
		15	| })
		16	| const method = request.needTotal? 'findAndCount' : 'find'
		17	| return await DbManager.get(request).statDelegatorRepository[method]({
		19	| collator: request.collator


